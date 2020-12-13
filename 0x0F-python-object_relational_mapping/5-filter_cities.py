#!/usr/bin/python3
"""  Write a script that takes in the name of a
state as an argument and lists all cities of that
state, using the database hbtn_0e_4_usa
"""
import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    getQueryCursor = db.cursor()
    getQueryCursor.execute("SELECT cities.name FROM cities WHERE " +
                           "cities.state_id=(SELECT id FROM states " +
                           "WHERE name='{}')".format(sys.argv[4]))
    newlist = []
    for query in getQueryCursor.fetchall():
        for x in query:
            newlist.append(x)
    for newquery in range(len(newlist) - 1):
        print(newlist[newquery], end=', ')
    if len(newlist) >= 1:
        print(newlist[len(newlist) - 1])
    else:
        print()
    getQueryCursor.close()
    db.close()
