#!/usr/bin/python3
"""
script that lists all states with a name starting
with N (upper N) from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == '__main__':

    miConexion = MySQLdb.connect(host='localhost', user=sys.argv[1],
                                 passwd=sys.argv[2], db=sys.argv[3])
    cur = miConexion.cursor()
    filter = "SELECT * FROM states \
            WHERE states.name LIKE BINARY 'N%' ORDER BY states.id ASC"
    cur.execute(filter)
    for name, id in cur.fetchall():
        print((name, (id)))
    cur.close()
    miConexion.close()
