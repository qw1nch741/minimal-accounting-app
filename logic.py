import sqlite3
from datetime import datetime

def post_transaction(description: str, debit_acc: int, credit_acc: int, amount: int, partner: str, db_path="accounting.db"):
    conn = sqlite3.connect(db_path)

    try:
        with conn:
            cursor = conn.cursor()
            date_str = datetime.now().strftime("%Y-%m-%d")

            cursor.execute(
                """
                INSERT INTO journal_entries (date, description, account_code, amount, partner_name)
                VALUES (?, ?, ?, ?, ?)
                """, (date_str, description, debit_acc, amount, partner)
            )

            cursor.execute(
                """
                INSERT INTO journal_entries (date, description, account_code, amount, partner_name)
                VALUES (?, ?, ?, ?, ?)
                """, (date_str, description, credit_acc, -amount, partner)
            )

    except Exception as e:
        print(f"Transaction failed. No changes were made. Error: {e}")
    finally:
        conn.close()
