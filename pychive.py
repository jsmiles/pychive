import sqlite3
import pandas as pd
from datetime import date

# Static parameters
today = date.today()
today = today.strftime("%Y%m%d")

# Connect to the db
conn = sqlite3.connect('example.db')
c = conn.cursor()

######################
# Define my functions
######################

# Generates all queries required for pychive
def query_gen(tbl, date):
    prod_select = f"SELECT * FROM {tbl} WHERE date <= '{date}'"
    prod_count = f"SELECT COUNT(*) FROM {tbl} WHERE date <= '{date}'"
    prod_del = f"DELETE FROM {tbl} WHERE date <= '{date}'"
    arch_count = f"SELECT COUNT(*) from {tbl}_ARCHIVE_{today}"
    arch_create = f"CREATE TABLE {tbl}_ARCHIVE_{today} as SELECT * FROM {tbl} WHERE date <= '{date}'"
    return prod_select, prod_count, prod_del, arch_count, arch_create

# Will query the database and return the result
def query_return(query):
    res = []
    for row in c.execute(query):
        res.append(row)
    return res

# Function to create the archive db tables
def create_table(query):
    try:
        c.execute(query)
    except:
        print("Failed at create table step")

# Function to delete the archived data from the production tables
# Note: split
def del_data(query):
    try:
        c.execute(query)
    except:
        print("Failed at table delete step")

# Data validation check. Ensure the number of records in the
# archive table matches the select statement in the production
# table
def data_check(prod_query, arch_query):
    prod_record_count = query_return(prod_query)
    arch_record_count = query_return(arch_query)
    if prod_record_count == arch_record_count:
        return True
    else:
        return "Data validation failed!"

# Main function, pulls everything together
def main_logic(tbl, date):
    ps, pc, pd, ac, acr = query_gen(tbl, date)
    create_table(acr)
    checksum = data_check(pc, ac)
    if checksum == True:
        del_data(pd)
    else:
        print("Failed at data check stage")


######################
# Read the data
######################
arch_list = pd.read_csv('archiveList.txt', sep=',')
print(arch_list)

######################
# Call functions on the data
######################
for index, row in arch_list.iterrows():
    table = row[0]
    arch_date = row[1]
    try:
        main_logic(table, arch_date)
    except:
        print(f"failed on this table {table} and this date {arch_date}")

# Save changes and close connection
conn.commit()
conn.close()
