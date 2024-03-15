#!/usr/bin/python3
import MySQLdb
import sys
"""
    lists all states from the
    database hbtn_0e_0_usa
    Usage:mysql username, mysql password
        and database name
"""
if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
            )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM `states` ORDER BY states.id ASC;")
    data = cursor.fetchall()
    for row in data:
        print(row)
