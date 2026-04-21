import sqlite3
from datetime import datetime

def post_transaction(description, debit_acc, credit_acc, amount, partner):
    conn = sqlite3.connect("accounting.db")

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
