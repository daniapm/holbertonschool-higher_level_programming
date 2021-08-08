#!/usr/bin/python3
"""
script that takes in arguments and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument. But this time,
write one that is safe from MySQL injections!
"""
import MySQLdb
import sys

if __name__ == '__main__':

    miConexion = MySQLdb.connect(host='localhost', user=sys.argv[1],
                                 passwd=sys.argv[2], db=sys.argv[3])
    cur = miConexion.cursor()
    filter = "SELECT * FROM states\
    WHERE states.name = %s ORDER BY states.id ASC"
    cur.execute(filter, (sys.argv[4], ))
    for name, id in cur.fetchall():
        print((name, (id)))
    cur.close()
    miConexion.close()
