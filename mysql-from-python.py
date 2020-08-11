import os
import datetime
import pymysql

# Get username from Cloud9 workspace
# (modify this variable if running on another environment)
username = os.getenv('C9_USER')

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user=username,
                             password='',
                             db='Chinook')

try:
    # Run a query
    with connection.cursor() as cursor:
        rows = [("Bob", 21, "1990-02-06 22:00:45"),
                ("Jim", 56, "1955-05-09 13:45:21"),
                ("Fred", 100, "1911-09-12 01:01:15")]
        cursor.executemany("INSERT INTO Friends VALUES (%s, %s, %s);", rows)
        connection.commit()
finally:
    # Close the connection, regardless of whether or not 
    # the above was successful
    connection.close()