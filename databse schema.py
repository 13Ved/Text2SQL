import sqlite3

# Connect to the SQLite database
db_name = 'Sakila.db'  # Change this to your database name for the Sakila database
connection = sqlite3.connect(db_name)
cursor = connection.cursor()

# Step 1: Retrieve and print table names
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print("Tables in the Sakila database:")
for table in tables:
    print(f"- {table[0]}")

# Step 2: Retrieve and print column information for each table
for table in tables:
    table_name = table[0]
    print(f"\nColumn information for table: {table_name}")
    
    cursor.execute(f"PRAGMA table_info({table_name});")
    columns = cursor.fetchall()
    
    for column in columns:
        column_id = column[0]
        column_name = column[1]
        column_type = column[2]
        is_not_null = column[3]
        default_value = column[4]
        is_primary_key = column[5]
        
        print(f"Column ID: {column_id}, Name: {column_name}, Type: {column_type}, "
              f"Not Null: {bool(is_not_null)}, Default: {default_value}, "
              f"Primary Key: {bool(is_primary_key)}")

# Close the connection
connection.close()
