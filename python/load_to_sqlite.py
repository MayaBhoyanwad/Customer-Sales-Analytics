import pandas as pd
import sqlite3

# Load cleaned data
df = pd.read_csv("data/processed/orders_cleaned.csv")

# Connect to SQLite database
conn = sqlite3.connect("data/analytics.db")

# Load dataframe into SQL table
df.to_sql("orders", conn, if_exists="replace", index=False)

print("Data loaded into SQLite successfully!")

# Check number of records
cursor = conn.cursor()
cursor.execute("SELECT COUNT(*) FROM orders")

count = cursor.fetchone()[0]

print("Total records in orders table:", count)

conn.close()