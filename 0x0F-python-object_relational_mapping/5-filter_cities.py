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
                SELECT cities.name
                FROM cities INNER JOIN states
                ON cities.state_id = states.id
                WHERE states.name = %s
                ORDER BY cities.id;"""
    cur.execute(query, (sys.argv[4], ))
    rows = cur.fetchall()
    c_names = [row[0] for row in rows]
    print(", ".join(c_names))
