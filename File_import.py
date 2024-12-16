import pandas as pd
import sqlite3
import os

# Define the CSV file paths (update these paths as needed)
csv_files = {
    # Add CSV file's path as needed 
}

# Connect to SQLite database (this will create the database if it doesn't exist)
conn = sqlite3.connect("name_of_the_database.db")

for table_name, file_path in csv_files.items():
    # Load CSV file into DataFrame
    df = pd.read_csv(file_path)
    
    # Write the DataFrame to the SQLite database
    df.to_sql(table_name, conn, index=False, if_exists='replace')

print("CSV files loaded into the database successfully.")
conn.close()


