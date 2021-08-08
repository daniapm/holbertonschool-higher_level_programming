#!/usr/bin/python3

"""
script that lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

if __name__ == '__main__':

    miConexion = MySQLdb.connect(host='localhost', user=sys.argv[1],
                                 passwd=sys.argv[2], db=sys.argv[3])
cur = miConexion.cursor()
cur.execute("SELECT * FROM states ORDER BY states.id ASC")
for name, id in cur.fetchall():
    print((name, (id)))
cur.close()
miConexion.close()
