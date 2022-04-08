#!/usr/bin/python3

"""
Script that lists all cities from the database hbtn_0e_4_usa
"""

import sys
import MySQLdb

if __name__ == "__main__":
    """4 arguments: mysql username, mysql password, database name
    and state name searched
    """
    server = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                                  passwd=sys.argv[2], database=sys.argv[3])

    curs = server.cursor()

    curs.execute("SELECT c.id, c.name, s.name FROM cities c LEFT JOIN states s ON \
			c.state_id = s.id ")

    column = curs.fetchall()

    for row in column:
        print(row)

    curs.close()
    server.close()
