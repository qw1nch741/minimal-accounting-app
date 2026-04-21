import sqlite3


def init_db():
    conn = sqlite3.connect("accounting.db")
    cursor = conn.cursor()

    # The 'Journal' is the master list of every 'hand movement'
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS journal_entries
                   (
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


if __name__ == "__main__":
    init_db()