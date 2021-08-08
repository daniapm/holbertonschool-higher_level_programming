#!/usr/bin/python3
"""
script that takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
import sys

if __name__ == '__main__':

    miConexion = MySQLdb.connect(host='localhost', user=sys.argv[1],
                                 passwd=sys.argv[2], db=sys.argv[3])
    cur = miConexion.cursor()
    filter = "SELECT * FROM states WHERE\
    states.name LIKE BINARY '{}' ORDER BY states.id ASC".format(sys.argv[4])
    cur.execute(filter)
    for name, id in cur.fetchall():
        print((name, (id)))
    cur.close()
    miConexion.close()
