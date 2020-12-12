#!/usr/bin/python3
"""  Write a script that lists all states with a name
starting with N (upper N) from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    getQueryCursor = db.cursor()
    getQueryCursor.execute("SELECT * FROM states WHERE " +
                           "name RLIKE '^N' ORDER BY id")
    for state in getQueryCursor.fetchall():
        print(state)
    getQueryCursor.close()
    db.close()
