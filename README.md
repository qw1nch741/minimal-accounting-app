Minimal Accounting App 📊
A pragmatic, event-driven accounting system built with Python and Streamlit. This app implements the fundamental principles of double-entry bookkeeping to help users track profit, loss, and partner balances with mathematical precision.

🚀 Overview
This project was developed as a lightweight solution for managing business finances. By focusing on "Event-Types" rather than complex accounting jargon, it allows users to record transactions like sales and bills while the backend automatically handles the balancing of debits and credits.

🛠️ Technologies Used
Python 3.11: The core programming language.

Streamlit: Used for the interactive web interface and real-time data visualization.

SQLite3: A serverless SQL database engine used for robust data storage.

Pandas: For efficient data manipulation and generating financial reports.

Docker: For containerization, ensuring the app runs perfectly in any environment.

📖 Key Concepts: Account Codes
The app uses a standard numbering system to categorize financial data:

1000s (Assets): What the business owns (e.g., Cash, Accounts Receivable).

2000s (Liabilities): What the business owes (e.g., Unpaid vendor bills).

4000s (Revenue): Income earned from sales or services.

5000s (Expenses): Costs incurred to operate (e.g., Rent, Utilities).

📥 Installation
Prerequisites
Python 3.11+

Docker (Optional, for containerized deployment)

Local Setup
Clone the repository.

Install dependencies:

Bash
pip install -r requirements.txt
Run the application:

Bash
streamlit run app.py
Using Docker
Build the image:

Bash
docker build -t minimal-accounting .
Run the container:

Bash
docker run -p 8501:8501 minimal-accounting
📂 Project Structure
app.py: The main entry point and UI logic.

logic.py: Contains the post_transaction function and business rules.

database.py: Handles database initialization and schema creation.

Dockerfile: Configuration for building the Docker container.

.gitignore: Specifies files to be ignored by Git (including the local database).