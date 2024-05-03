#!/usr/bin/python3
"""
This module llists all states with a name starting with N (upper N)
from the database
"""

import sys
import MySQLdb

if __name__ == "__main__":

    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = connection.cursor()

    query = "SELECT * FROM states \
            WHERE name LIKE BINARY 'N%' \
            ORDER BY states.id ASC;"

    cursor.execute(query)
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    connection.close()
