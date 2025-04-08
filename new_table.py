#Description: This python script assumes that you already have
# a database.db file at the root of your workspace.
# This python script will CREATE a table called students 
# in the database.db using SQLite3 which will be used
# to store the data collected by the forms in this app
# Execute this python script before testing or editing this app code. 
# Open a python terminal and execute this scripts with below:
# python new_table.py  then
# python app.py

import sqlite3

conn = sqlite3.connect('database.db')
print("Database is connected successfully")

conn.execute('CREATE TABLE products (name TEXT, barcode TEXT, price TEXT, quantity TEXT)')


print("Created table successfully!")

conn.close()

