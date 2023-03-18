#!/usr/bin/python3
'''
Script that lists all states with a name starting with N (upper N) from the
database hbtn_0e_0_usa:
'''

import MySQLdb
from sys import argv

if __name__ == "__main__":

    connect = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )
    current = connect.cursor()
    current.execute("""SELECT * from states WHERE name LIKE BINARY 'N%'
    ORDER BY id ASC""")

    query_rows = current.fetchall()
    for row in query_rows:
        print(row)
    current.close()
    connect.close()
