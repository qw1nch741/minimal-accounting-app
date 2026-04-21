import sqlite3
import pandas as pd
import pytest
from logic import post_transaction


@pytest.fixture
def test_db():
    conn = sqlite3.connect("test_accounting.db")
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS journal_entries")
    cursor.execute("""
            CREATE TABLE journal_entries (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT,
                description TEXT,
                account_code INTEGER,
                amount REAL,
                partner_name TEXT
            )
    """)
    conn.commit()
    conn.close()
    yield

def test_post_transaction(test_db):
    description, dr, cr, amt, partner = "test_sale", 1100, 4000, 100.0, "test_partner"

    post_transaction(description, dr, cr, amt, partner, db_path="test_accounting.db")

    conn = sqlite3.connect("test_accounting.db")

    query = (f"""SELECT * FROM journal_entries 
                                WHERE account_code == 4000 
                                AND description == '{description}' 
                                AND amount == -100.0
                                AND partner_name == '{partner}'""")
    result_df = pd.read_sql_query(query, conn)
    conn.close()

    assert len(result_df) == 1
    assert result_df.iloc[0]['amount'] == -100.0


def test_multiple_transactions(test_db):
    db = "test_accounting.db"
    post_transaction("sale", 1100, 4000, 1000, "John", db_path=db)
    post_transaction("expense", 5000, 2000, 500, "Bob", db_path=db)
    post_transaction("sale2", 1100, 4000, 300, "Jack", db_path=db)

    conn = sqlite3.connect(db)

    rev_row = pd.read_sql_query("SELECT SUM(amount) as total FROM journal_entries WHERE account_code == 4000", conn)
    rev_value = -rev_row['total'].fillna(0).iloc[0]
    rev = float(rev_value)

    exp_row = pd.read_sql_query("SELECT SUM(amount) as total FROM journal_entries WHERE account_code == 5000", conn)
    exp_value = exp_row['total'].fillna(0).iloc[0]
    exp = float(exp_value)

    profit = rev - exp

    assert profit == 800

    conn.close()

