OraPipe is a lightweight, schema-aware ETL pipeline that transforms raw CSV files into structured Oracle database tables — automatically.
It eliminates the manual overhead of schema creation, enforces clean and consistent data, and streamlines multi-file imports with ease.

✨ Features

Dynamic Table Creation → Automatically builds Oracle database tables based on CSV headers. No manual schema setup required.
Clean & Consistent Data → Normalizes column names for Oracle compatibility and converts invalid numeric values to NULL for data integrity.
Batch File Support → Import multiple CSV files from a specified folder in one execution.
Interactive Setup → Prompts for DSN connection details and CSV folder path, ensuring flexible use across environments.

📦 Requirements

Python 3.8+
Oracle Client Libraries
 (via oracledb)
Pandas
SQLAlchemy

⚙️ Installation

Install Python (3.8 or later) from python.org/downloads
Install dependencies:
pip install sqlalchemy oracledb pandas


🚀 Usage

Clone the repository:

git clone https://github.com/yourusername/OraPipe-CSV-to-Oracle-ETL.git
cd OraPipe-CSV-to-Oracle-ETL


Run the script:

python orapipe.py

Provide the required inputs when prompted:
DSN (Data Source Name): Host, port, and service name for your Oracle instance.
Folder Path: The path containing your CSV files.

OraPipe will:
Create Oracle tables dynamically from the CSV headers.
Normalize and clean the data.
Import all CSV files from the folder into the database.

📖 Example DSN Configuration
import oracledb

dsn = oracledb.makedsn(
    host="your_host",
    port=1521,
    service_name="ODSD"
)

🛠 Roadmap

 Add support for JSON and Excel imports
 Advanced data type inference (dates, booleans)
 Config file support for automation
  


