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

    curs.execute("SELECT * FROM cities JOIN states\
                        ON cities.state_id = states.id ORDER BY cities.id")

    [print(", ".join([c[2] for c in curs.fetchall() if c[4] == sys.argv[4]]))]

    curs.close()
    server.close()
