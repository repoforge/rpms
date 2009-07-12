#!/usr/bin/python

import sys, os, sqlite, string
import hwsdb

sys.stdout = os.fdopen(1, 'w', 0)
con, cur = hwsdb.opendb()

query = string.join(sys.argv[1:], ' ')
if not query:
    print >>sys.stderr, 'syntax: hwsdb-sql \'sql statement\''
    print >>sys.stderr, 'error: You did not provide a SQL command as argument.'
    sys.exit(1)

try:
    cur.execute(query)
except sqlite.DatabaseError, m:
    print >>sys.stderr, 'error: Syntax error in SQL statement, %s' % m
    sys.exit(2)

for rec in cur.fetchall():
    for col in rec:
        print '%s\t' % col,
    print
