#!/usr/bin/python3
""" Script  that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument preventing SQL
injection.
"""
if __name__ == "__main__":
    import sys
    import MySQLdb

    server = MySQLdb.connect(host="localhost",  port=3306, user=sys.argv[1],
                                  password=sys.argv[2], database=sys.argv[3])

    curs = server.cursor()
    curs.execute("SELECT * FROM states WHERE name=%s ORDER BY id ASC", (
        sys.argv[4],))
    rows = curs.fetchall()
    for row in rows:
        if row[1] == sys.argv[4]:
            print(row)
    curs.close()
    server.close()
