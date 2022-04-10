#!/usr/bin/python3

"""
script that takes in the name of a state as an argument and lists all cities
of that state, using the database hbtn_0e_4_usa
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

    curs.execute("SELECT c.name, s.name c.id FROM cities AS c\
                        JOIN states AS s\
                        ON c.state_id=s.id ORDER BY s.id")

    column = curs.fetchall()

    for row in column:
        print(row)

    curs.close()
    server.close()
