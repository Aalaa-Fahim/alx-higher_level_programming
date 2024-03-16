#!/usr/bin/python3
"""Module that lists all states from mySQL database"""
import sys
import MySQLdb


def list_states(username, password, database):
    """ lists all states sorted by states.id """
    conn = MySQLdb.connect(host='localhost',
                           port=3306,
                           user=username,
                           passwd=password,
                           db=database)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()


if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    list_states(username, password, database)
