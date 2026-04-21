Full conversation available: https://gemini.google.com/share/f47f5c6d73f4


📜 Detailed AI Prompt History: Minimal Accounting App
This document serves as a full log of the collaborative development process between the developer and the AI assistant, as required by the Jito assessment constraints.

Phase 1: Domain Research & Core Architecture
Prompt 1: "I am building a minimal accounting app for a job assessment. I need to understand the 'Two-Hand Rule'. Can you explain how a single business event like a 'Sale' translates into a Debit and a Credit in a database?"

Prompt 2: "Help me design a post_transaction function in Python using sqlite3. It should take a description, two account codes, and an amount, and it must use a SQL transaction (commit/rollback) so that either both entries are saved or none are."

Prompt 3: "I need a fixed chart of accounts: 1000 (Cash), 1100 (AR), 2000 (AP), 4000 (Revenue), 5000 (Expense). How should I structure my init_db function to create this table if it doesn't exist?"

Phase 2: UI Development (Streamlit)
Prompt 4: "I'm using Streamlit. How do I create a sidebar dropdown where a user selects 'Sales Invoice' and it automatically knows to use account 1100 for Debit and 4000 for Credit?"

Prompt 5: "In the main dashboard, I want to show a 'Net Profit' metric. Since Revenue is stored as a negative number in my database, how do I write the Pandas code to flip the sign and subtract expenses?"

Prompt 6: "How can I use st.columns to create a ledger view that looks like a table, but allows me to put a 'Delete' button next to every row?"

Phase 3: Technical Deep-Dive & Debugging
Prompt 7: "In what form does pd.read_sql_query return information? Is it a list or a DataFrame? How do I check if it's empty before trying to display it?"

Prompt 8: "I'm getting a TypeError: Query must be a string unless using sqlalchemy when I try to run my search query. I think my parentheses or commas are wrong. Can you help me fix this line: query = (f'SELECT...', conn)?"

Prompt 9: "My SQL query for the partner search isn't working with the variable. How do I properly use the params argument in pd.read_sql_query to prevent SQL injection?"

Phase 4: Unit Testing (Pytest)
Prompt 10: "How can I use pytest here and what can I test to prove the accounting logic works?"

Prompt 11: "My tests are failing with 6 != 1. It seems the accounting.db file is keeping data from my manual tests. How do I write a @pytest.fixture that drops the table and recreates it before every test?"

Prompt 12: "I want to separate my test data from my real data. How do I modify logic.py so the database path isn't hardcoded, allowing me to pass test_accounting.db during tests?"

Prompt 13: "I'm stuck on a test for multiple transactions. I want to post a sale and an expense and assert that the profit is exactly 800. My test is returning 0. Help me check the logic."

Phase 5: Containerization & Final Polish
Prompt 14: "Write a Dockerfile for this project. It needs to install pandas and streamlit. Make sure it exposes port 8501."

Prompt 15: "Why does test_accounting.db stay in my file explorer after the tests finish? Is there a way to make it disappear or should I just ignore it?"

Prompt 16: "Review my README.md. I want to make sure the Jito recruiters understand my technical decisions regarding 'Separation of Concerns' and 'Pragmatic UX'."




