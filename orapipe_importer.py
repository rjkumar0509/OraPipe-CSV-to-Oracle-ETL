# -*- coding: utf-8 -*-
"""
Created on Mon Aug 25 16:50:58 2025

@author: rpandi
"""

import time
import os
import shutil
import glob
import oracledb
import pandas as pd
from sqlalchemy import create_engine, MetaData, Column, Integer, Float, String, Table, inspect
from sqlalchemy.dialects import oracle


#Input folder path C:\\Users\\raj\\Downloads\\folder_containing_csv
folder_path = input("Enter the full path to your CSV folder: ").strip()

if not os.path.isdir(folder_path):
    print(f"❌ Folder not found: {folder_path}")
    exit(1)


# Get all CSV files in the folder
csv_files = glob.glob(os.path.join(folder_path, "*.csv"))

# Find the most recently modified CSV file
#latest_csv = max(csv_files, key=os.path.getmtime)
#df = pd.read_csv(latest_csv)
# Print headers (optional)
#print("CSV Headers:", df.columns.tolist())
#df.columns = [col.strip().replace(" ", "_") for col in df.columns]

# Get all CSV files
csv_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.csv')]

# List to hold individual DataFrames
dataframes = []
# Loop through each CSV file
for csv_file in csv_files:
    print(f"\n📄 Processing file: {csv_file}")
    # Read the CSV
    df = pd.read_csv(csv_file)
    # Print headers (optional)
    print("CSV Headers:", df.columns.tolist())
    # Clean column names
    df.columns = [col.strip().replace(" ", "_") for col in df.columns]
    # Append to list
    dataframes.append(df)

# Merge all DataFrames
df = pd.concat(dataframes, ignore_index=True)

# ✅ Final output
print(f"\n✅ Combined {len(csv_files)} files. Total rows: {len(df)}")


df = df.apply(lambda col: col.astype(str) if not pd.api.types.is_numeric_dtype(col) else col)


float_columns = df.select_dtypes(include='float').columns.tolist()
print("Columns with float64 dtype:", float_columns)

# --- Step 2: Connect to Oracle using SQLAlchemy ---
# Replace the placeholders with your Oracle DB credentials
# === Prompt user for Oracle connection details ===
host = input("Enter Oracle host (e.g., testdb.unm.edu): ").strip()
port = input("Enter Oracle port (e.g., 1678): ").strip()
service_name = input("Enter Oracle service name (e.g., ODS): ").strip()

# === Build DSN dynamically ===
dsn = oracledb.makedsn(host, int(port), service_name=service_name)

username = input("Enter Oracle username: ").strip()
password = input("Enter Oracle password: ").strip()

# SQLAlchemy engine using Oracle dialect
engine = create_engine(
    f"oracle+oracledb://{username}:{password}@{dsn}",
    connect_args={"mode": oracledb.DEFAULT_AUTH}
)


# SQLAlchemy engine using Oracle dialect
engine = create_engine(
    f"oracle+oracledb://{username}:{password}@{dsn}",
    connect_args={"mode": oracledb.DEFAULT_AUTH}
)

table_name = "LOAD_CSV_DATA"
# --- Step 3: Write DataFrame to Oracle (auto-create table) ---
inspector = inspect(engine)
existing_tables = inspector.get_table_names()
table_exists = table_name.lower() in [t.lower() for t in existing_tables]

# === STEP 4: Define Table Schema (Only if First Run) ===
if not table_exists:
    print(f"🚧 Table '{table_name}' does not exist — creating it...")
  
    columns = []

    for col in df.columns:
        normalized_col = col.strip().replace(" ", "_")  # Remove spaces and replace with underscore
        dtype = df[col].dtype
        if pd.api.types.is_integer_dtype(dtype):
            columns.append(Column(normalized_col, Integer))
        elif pd.api.types.is_float_dtype(dtype):
            columns.append(Column(
                normalized_col,
                Float(precision=53).with_variant(oracle.FLOAT(binary_precision=126), 'oracle')
            ))
        else:
            max_len = df[col].astype(str).str.len().max()
            col_length = int(min(max_len + 10, 4000)) if pd.api.types.is_string_dtype(dtype) else 4000
            columns.append(Column(normalized_col, String(col_length)))
            
    metadata = MetaData()
    table = Table(table_name, metadata, *columns)
    metadata.create_all(engine)
    print(f"✅ Created table '{table_name}' successfully.")
else:
    print(f"✅ Table '{table_name}' already exists — reusing it.")
    
df.to_sql(table_name, con=engine, if_exists="append", index=False)
print("✅ Data uploaded successfully.")