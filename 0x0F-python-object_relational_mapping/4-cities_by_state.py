#!/usr/bin/python3
"""
     displays all values in the states table of
     hbtn_0e_0_usa where name matches the argument.
"""
if __name__ == '__main__':

    import MySQLdb
    import sys

    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
            )

    cur = db.cursor()
    query = """
                SELECT cities.id,cities.name,states.name
                FROM cities INNER JOIN states
                ON cities.state_id = states.id
                ORDER BY cities.id;"""
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
