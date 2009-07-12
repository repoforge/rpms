#!/usr/bin/python

import sys, os, glob, sqlite
import hwsdb

sys.stdout = os.fdopen(1, 'w', 0)

con, cur = hwsdb.opendb()

os.makedirs('HardwareSupport')

print 'Make PCI index...'
os.makedirs('HardwareSupport/PCI')
cur.execute('select * from alias where type == "pci" order by vendor')
kmodlist = cur.fetchall()
fd = open('HardwareSupport/PCI/index.html', 'w')
for data in kmodlist:
#    print >>fd, data
    print data

print 'Make USB index...'
os.makedirs('HardwareSupport/USB')
cur.execute('select * from alias where type == "usb" order by vendor')
kmodlist = cur.fetchall()
for data in kmodlist:
    print data

print 'Make KernelModule index...'
os.makedirs('HardwareSupport/KernelModule')
cur.execute('select * from kmod order by name')
kmodlist = cur.fetchall()

print 'Make Vendor index...'
os.makedirs('HardwareSupport/Vendor')
#cur.execute('select vendor_name,vendor from vendor order by vendor')
#kmodlist = cur.fetchall()
#count = {}
#for adv, in advlist:
#    if not count.has_key(adv): count[adv] = 0
#    count[adv] += 1
#print '  ',·
#for key in ('critical', 'important', 'moderate', 'low', 'unknown', 'error'):
#    if key in count.keys():
#        print '%s: %s  ' % (key, count[key]),
#print
#print



con.commit()
