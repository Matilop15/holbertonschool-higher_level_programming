#!/usr/bin/python3
"""
Lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    """
    Results must be sorted in ascending order by states.id
    """
    server = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                                  passwd=sys.argv[2], database=sys.argv[3])

    """cursor sirve para ejecutar codigo SQL"""
    curs = server.cursor()
    curs.execute("SELECT * FROM states WHERE (name LIKE 'N%') ORDER BY id ASC")

    column = curs.fetchall()

    for row in column:
        print(row)

    curs.close()
    server.close()
