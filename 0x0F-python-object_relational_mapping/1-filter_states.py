#!/usr/bin/python3
"""Lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Check if all required arguments are provided
    if len(sys.argv) != 4:
        print("Usage: ./script.py <mysql username> <mysql password> <database name>")
        sys.exit(1)
    
    # Retrieve command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL server
    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )
        c = db.cursor()
    except MySQLdb.Error as e:
        print("Error connecting to MySQL:", e)
        sys.exit(1)

    # Execute the query to select states starting with N
    try:
        c.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
        results = c.fetchall()
        for state in results:
            print(state)
    except MySQLdb.Error as e:
        print("Error executing MySQL query:", e)
        sys.exit(1)

    # Close the database connection
    db.close()
