#!/usr/bin/python3
'''
Script that takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument
'''

import MySQLdb
from sys import argv

if __name__ == "__main__":
    connect = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3])
    current = connect.cursor()
    current.execute(
        """SELECT * from states WHERE BINARY name='{}' ORDER by id ASC"""
        .format(sys.argv[4])
    )
    query_rows = current.fetchall()
    for row in query_rows:
        print(row)
    current.close()
    connect.close()
