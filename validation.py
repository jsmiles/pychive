import sqlite3
from datetime import date

# Connect to the db
conn = sqlite3.connect('example.db')
c = conn.cursor()

# List my tables
c.execute("SELECT name from sqlite_master where type = 'table' ")
print("Table List")
print(c.fetchall())

# All possible tables on day of dev
table_list = ['transactions', 'purchases', 'labour',
              'transactions_Archive_20190816', 'purchases_Archive_20190816',
              'labour_Archive_20190816']

print("TABLE DATA LOOP")
for table in table_list:
    query = f"SELECT * FROM {table}"
    try:
        print(f"THIS TABLE: {table}")
        for row in c.execute(query):
            print(row)
    except:
        print(f"Table {table} does not exist")

# List all tables - useful if while testing you need to drop tables
c.execute("SELECT name from sqlite_master where type = 'table' ")
print("Table List")
print(c.fetchall())

conn.commit()
conn.close()
