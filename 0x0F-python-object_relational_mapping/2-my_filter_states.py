#!/usr/bin/python3
"""  Write a script that takes in an argument and displays
all values in the states table of hbtn_0e_0_usa where name matches the argument
"""
import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    getQueryCursor = db.cursor()
    getQueryCursor.execute("SELECT * FROM states WHERE " +
                           "name='{}' ORDER BY id".format(sys.argv[4]))
    for state in getQueryCursor.fetchall():
        print(state)
    getQueryCursor.close()
    db.close()
