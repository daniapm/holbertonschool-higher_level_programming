#!/usr/bin/python3
"""
script that takes in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa
"""
import MySQLdb
import sys

if __name__ == '__main__':

    miConexion = MySQLdb.connect(host='localhost', user=sys.argv[1],
                                 passwd=sys.argv[2], db=sys.argv[3])
    cur = miConexion.cursor()
    filter = "SELECT cities.name FROM cities\
    JOIN states ON cities.state_id = states.id\
    WHERE states.name = %s ORDER BY cities.id ASC"
    cur.execute(filter, (sys.argv[4], ))
    names = []
    for name in cur.fetchall():
        names.append(name[0])
    print(', '.join(names))
    cur.close()
    miConexion.close()
