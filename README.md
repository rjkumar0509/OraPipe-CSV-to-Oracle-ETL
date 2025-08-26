# 📦 OraPipe-CSV-to-Oracle-ETL  

**OraPipe** is a lightweight, schema-aware ETL pipeline that transforms raw CSV files into structured Oracle database tables — automatically.  
It eliminates the manual overhead of table creation, enforces clean and consistent data, and streamlines multi-file imports with ease.  

---

## ✨ Features  

- 🚀 **Dynamic Table Creation** → Builds Oracle database tables automatically based on CSV headers.  
- 🧹 **Clean & Consistent Data** → Normalizes column names for Oracle compatibility and converts invalid numeric values to `NULL`.  
- 📂 **Batch File Support** → Import multiple CSV files from a folder in a single run.  
- 🎛 **Interactive Setup** → Prompts for DSN connection details and CSV folder path, ensuring flexible usage across environments.  

---

## 📦 Requirements  

- Python **3.8+**  
- [Oracle Client Libraries](https://python-oracledb.readthedocs.io/en/latest/user_guide/installation.html) (via `oracledb`)  
- [Pandas](https://pypi.org/project/pandas/)  
- [SQLAlchemy](https://pypi.org/project/SQLAlchemy/)  

---

## ⚙️ Installation  

1. Install **Python** (3.8 or later) from [python.org](https://www.python.org/downloads/).  
2. Install required dependencies:  
   ```bash
   pip install sqlalchemy oracledb pandas

## 🚀 Usage  

### Clone the repository:  
1. git clone https://github.com/yourusername/OraPipe-CSV-to-Oracle-ETL.git                     
2. cd OraPipe-CSV-to-Oracle-ETL
3. python orapipe_importer.py

When prompted, provide the following inputs:
- **DSN (Data Source Name): Host, port, and service name for your Oracle instance.
- **Folder Path: The path containing your CSV files.


✅ What OraPipe Does

- Creates a default Oracle table LOAD_CSV_DATA with columns as the csv headers and loads the csv data under the schema of your choice dynamically.
- Normalizes and cleans column names for compatibility
- Converts invalid numeric values to NULL
- Imports all CSV files from the specified folder into the database table

## 🛠 Roadmap  

- [ ] Add support for **JSON** and **Excel** imports  
- [ ] Implement **advanced data type inference** (dates, booleans)  
- [ ] Enable **config file support** for automation  

---

## 🤝 Contributing  

Contributions are welcome! 🎉  
If you’d like to improve **OraPipe**, please fork the repo, create a feature branch, and submit a pull request.  
