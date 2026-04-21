import streamlit as st
import pandas as pd
import sqlite3
from logic import post_transaction
from database import init_db

# Initialize DB on startup
init_db()

st.set_page_config(page_title="Minimal Accounting", layout="wide")
st.title("Minimal Accounting App")

# --- SIDEBAR: DATA ENTRY ---
st.sidebar.header("Record an Event")
event_type = st.sidebar.selectbox("What happened?", [
    "Sales Invoice (I earned money but no cash yet)",
    "Payment Received (Customer paid me cash)",
    "Expense Bill (I bought something but haven't paid)",
    "Payment Sent (I paid the vendor)"
])

desc = st.sidebar.text_input("Description", placeholder="e.g., Monthly Consulting")
amt = st.sidebar.number_input("Amount ($)", min_value=0.0, step=10.0)
partner = st.sidebar.text_input("Partner Name", placeholder="e.g., Acme Corp")

if st.sidebar.button("Post Transaction"):
    if amt > 0 and desc and partner:
        if "Sales Invoice" in event_type:
            post_transaction(desc, 1100, 4000, amt, partner)  # Dr AR, Cr Revenue
        elif "Payment Received" in event_type:
            post_transaction(desc, 1000, 1100, amt, partner)  # Dr Cash, Cr AR
        elif "Expense Bill" in event_type:
            post_transaction(desc, 5000, 2000, amt, partner)  # Dr Expense, Cr AP
        elif "Payment Sent" in event_type:
            post_transaction(desc, 2000, 1000, amt, partner)  # Dr AP, Cr Cash
        st.sidebar.success("Success!")
    else:
        st.sidebar.error("Please fill all fields.")

# --- MAIN PAGE: REPORTS ---
col1, col2 = st.columns(2)

with col1:
    st.header("📊 Profit & Loss")
    conn = sqlite3.connect("accounting.db")

    #df = pd.read_sql_query("SELECT account_code, SUM(amount) as total FROM journal_entries GROUP BY account_code", conn)

    # Revenue is stored as negative credits, so we flip the sign back
    rev_row = pd.read_sql_query("SELECT SUM(amount) as total FROM journal_entries WHERE account_code == 4000", conn)
    rev_value = -rev_row['total'].fillna(0).iloc[0]
    rev = float(rev_value)

    exp_row = pd.read_sql_query("SELECT SUM(amount) as total FROM journal_entries WHERE account_code == 5000", conn)
    exp_value = exp_row['total'].fillna(0).iloc[0]
    exp = float(exp_value)

    profit = rev - exp

    st.metric("Net Profit", f"${profit:,.2f}", delta=f"${profit:,.2f}")
    st.write(f"Total Revenue (4000): **${rev:,.2f}**")
    st.write(f"Total Expenses (5000): **${exp:,.2f}**")

with col2:
    st.header("Partner Ledger")
    search_partner = st.text_input("Search Partner Name")
    if search_partner:

        query = "SELECT id, date, description, account_code, amount FROM journal_entries WHERE partner_name LIKE ?"

        search_term = f"%{search_partner}%"

        partner_df = pd.read_sql_query(
            query, conn, params=(search_term,)
        )

        if not partner_df.empty:
            # 1. Create a Header Row
            h_col1, h_col2, h_col3, h_col4, h_col5 = st.columns([2, 3, 1, 1, 2])
            h_col1.write("**Date**")
            h_col2.write("**Description**")
            h_col3.write("**Acc**")
            h_col4.write("**Amt**")
            h_col5.write("**Actions**")

        for index, row in partner_df.iterrows():
            c1, c2, c3, c4, c5 = st.columns([2, 3, 1, 1, 2])

            c1.text(row['date'])
            c2.text(row['description'])
            c3.markdown(f":yellow[{row['account_code']}]")


            amt = row['amount']
            if amt >= 0:
                c4.markdown(f":green[${amt:,.2f}]")
            else:
                c4.markdown(f":red[${amt:,.2f}]")

            # 3. Add buttons to the last column
            # We use a unique key for every button so Streamlit doesn't get confused
            if c5.button("🗑️ Delete", key=f"del_{row['id']}", use_container_width=True):
                with sqlite3.connect("accounting.db") as del_conn:
                    del_conn.execute(
                        "DELETE FROM journal_entries WHERE id = ?", (row['id'],)
                    )
                    del_conn.commit()

                st.success(f"Entry {row['id']} deleted")
                st.rerun()

    conn.close()

if st.button("Account code info"):
    with st.expander("❓ What do these Account Codes mean?"):
        st.write("""
        - **1000s:** Assets (Money in the bank)
        - **2000s:** Liabilities (Bills you haven't paid yet)
        - **4000s:** Revenue (Sales you made)
        - **5000s:** Expenses (Costs of doing business)
        """)
