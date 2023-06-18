#!/usr/bin/python3
import MySQLdb
import sys

# Retrieve command-line arguments
mysql_user = sys.argv[1]
mysql_password = sys.argv[2]
database_name = sys.argv[3]

# Connect to the MySQL server
db = MySQLdb.connect(user=mysql_user, passwd=mysql_password, host="localhost", port=3306)
cursor = db.cursor()

# Create the database if it doesn't exist
create_db_query = f"CREATE DATABASE IF NOT EXISTS mysql"
cursor.execute(create_db_query)

# Switch to the specified database
use_db_query = f"USE mysql"
cursor.execute(use_db_query)

# Create the states table if it doesn't exist
create_table_query = """
    CREATE TABLE IF NOT EXISTS states (
        id INT(11) NOT NULL AUTO_INCREMENT,
        name VARCHAR(255) NOT NULL,
        PRIMARY KEY (id)
    )
"""
cursor.execute(create_table_query)

# Insert states into the table
insert_query = """
    INSERT INTO states (name)
    VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada")
"""
cursor.execute(insert_query)
db.commit()

# Execute the SQL query to retrieve states
query = "SELECT * FROM states ORDER BY id ASC"
cursor.execute(query)

# Fetch all the rows from the result set
rows = cursor.fetchall()

# Display the results
for row in rows:
    print(row)

# Close the database connection
cursor.close()
db.close()
