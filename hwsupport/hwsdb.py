import os, sqlite, types

dbase = 'hwsdb.sqlite'

headers = {
    'kmod': ('filename', 'name', 'license', 'author', 'version', 'description', 'firmware', 'srcversion', 'depends', 'vermagic', 'module_sig'),
    'alias': ('filename', 'data', 'type', 'vendor', 'device', 'subvendor', 'subdevice'),
    'parm': ('filename', 'option', 'description', 'type'),
    'depends': ('filename', 'module'),
    'pci': ('vendor', 'device', 'subvendor', 'subdevice', 'vendor_name', 'device_name', 'subsystem_name'),
    'usb': ('vendor', 'device', 'interface', 'vendor_name', 'device_name', 'interface_name'),
}

dataopts = {
    'kmod': { 'filename': 'unique primary key' },
#    'alias': { 'filename': 'unique primary key', 'data': 'unique' },
#    'parm': { 'filename': 'unique primary key', 'option': 'unique' },
#    'pci': { 'vendor': 'unique primary key' },
#    'usb': { 'vendor': 'unique primary key' },
}


### Build insert strings for each database
insertstr = { }
for name in headers.keys():
    insertstr[name] = 'insert into %s ( ' % name
    for key in headers[name]: insertstr[name] += '%s, ' % key
    insertstr[name] = insertstr[name].rstrip(', ') + ' ) values ( ' + '%s, ' * len(headers[name])
    insertstr[name] = insertstr[name].rstrip(', ') + ' )'

def sqlcreate(name):
    'Return a database create SQL statement'
    str = 'create table %s ( ' % name
    for key in headers[name]:
        if dataopts.has_key(name) and dataopts[name].has_key(key):
            str += '%s %s,' % (key, dataopts[name][key])
        else:
            str += '%s varchar(10),' % key
    return str.rstrip(', ') + ' )'

#def sqlinsert(name):
#   'Return a database insert SQL statement'
#   str = 'insert into %s ( ' % name
#   for key in headers[name]: str += '%s, ' % key
#   str = str.rstrip(', ') + ' ) values ( '
#   for key in headers[name]: str += '"%%(%s)s", ' % key
#   return str.rstrip(', ') + ' )'

def opendb():
    'Open a database and return references'
    con = sqlite.connect(dbase)
    cur = con.cursor()
    return con, cur

def createtb(cur, name, create=False):
    try:
        cur.execute('drop table "%s"' % name)
    except Exception, e: 
#       print e
        pass
    cur.execute(sqlcreate(name))

def insertrec(cur, name, rec):
    'Insert a record in a database'
    global insertstr

    values = []
    for key in headers[name]:
        ### Convert to UTF-8
        if key not in rec.keys():
            rec[key] = ''
        if isinstance(rec[key], types.UnicodeType):
            rec[key] = rec[key].encode('utf-8')
        values.append(rec[key])
#   print insertstr[name]
#   print values
    cur.execute(insertstr[name], values)
