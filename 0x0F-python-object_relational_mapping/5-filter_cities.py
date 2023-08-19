#!/usr/bin/python3
"""
return all table values (table 'states')
parameters given to script: username, password, database
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=argv[1],
                           passwd=argv[2],
                           db=argv[3])
    cur = conn.cursor()
    query = """SELECT name
                 FROM cities
                 WHERE state_id IN (
                 SELECT id,
                 FROM states
                 WHERE name = %s
                 )"""
    cur.execute(query, (argv[4], ))
    for row in cur.fetchall():
        print(','.join(row))
    cur.close()
    conn.close()
