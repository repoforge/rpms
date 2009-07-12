#!/usr/bin/python

import sys, os, glob, sqlite, popen2, re
import hwsdb

sys.stdout = os.fdopen(1, 'w', 0)

con, cur = hwsdb.opendb()
hwsdb.createtb(cur, 'kmod')
hwsdb.createtb(cur, 'alias')
hwsdb.createtb(cur, 'parm')
hwsdb.createtb(cur, 'depends')
hwsdb.createtb(cur, 'pci')
hwsdb.createtb(cur, 'usb')

### First fill PCI and USB database
print 'Parsing pci.ids...'
pcirec = {}
for line in open('/usr/share/hwdata/pci.ids').readlines():
    l = line.split()
    if line.startswith('#'):
        continue
    elif len(l) == 0:
        continue
    elif line.startswith('\t\t'):
        pcirec['subvendor'] = l[0].lower()
        if len(l) > 2:
            pcirec['subdevice'] = l[1].lower()
        if len(l) > 3:
            pcirec['subsystem_name'] = ' '.join(l[2:])
    elif line.startswith('\t'):
        pcirec['device'] = l[0].lower()
        pcirec['device_name'] = ' '.join(l[1:])
        pcirec['subvendor'] = ''
        pcirec['subdevice'] = ''
        pcirec['subsystem_name'] = ''
    else:
        pcirec['vendor'] = l[0].lower()
        pcirec['vendor_name'] = ' '.join(l[1:])
        pcirec['device'] = ''
        pcirec['device_name'] = ''
        pcirec['subvendor'] = ''
        pcirec['subdevice'] = ''
        pcirec['subsystem_name'] = ''
    hwsdb.insertrec(cur, 'pci', pcirec)

print 'Parsing usb.ids...'
usbrec = {}
for line in open('/usr/share/hwdata/usb.ids').readlines():
    l = line.split()
    if line.startswith('#'):
        continue
    elif len(l) == 0:
        continue
    elif line.startswith('\t\t'):
        usbrec['interface'] = l[1]
        usbrec['interface_name'] = ''.join(l[2:])
    elif line.startswith('\t'):
        usbrec['device'] = l[1]
        usbrec['device_name'] = ''.join(l[2:])
        usbrec['interface'] = ''
        usbrec['interface_name'] = ''
    else:
        usbrec['vendor'] = l[0]
        usbrec['vendor_name'] = ''.join(l[1:])
        usbrec['device'] = ''
        usbrec['device_name'] = ''
        usbrec['interface'] = ''
        usbrec['interface_name'] = ''
    hwsdb.insertrec(cur, 'usb', usbrec)

def addfile((filelist, ), path, files):
    for file in files:
        if file.endswith('.ko'):
            filelist.add( os.path.join(path, file) )

filelist = set()
os.path.walk('/lib/modules/2.6.18-152.el5', addfile, (filelist,))

pcifilter = re.compile('^pci:v(0000)?(?P<vendor>.+)d(0000)?(?P<device>.+)sv(0000)?(?P<subvendor>.+)sd(0000)?(?P<subdevice>.+)bc(?P<bc>.+)sc(?P<sc>.+)i(?P<i>.+)\*?$')
usbfilter = re.compile('^usb:v(?P<vendor>.+)p(?P<p>.+)d(?P<device>.+)dc(?P<dc>.+)dsc(?P<dsc>.+)dp(?P<dp>.+)ic(?P<ic>.+)isc(?P<isc>.+)ip(?P<ip>.+)\*?$')

for file in filelist:
    print 'Parsing %s' % file
    (o, i) = popen2.popen4('/sbin/modinfo %s' % file)

    name = os.path.basename(file)
    kmodrec = { 'name': name }

    for line in o.readlines():
        l = line.split()
        if len(l) == 0:
            continue

        ### FIXME: Support pcmcia, serio and virtio
        elif line.startswith('alias:'):
            aliasrec = { 'filename': file, 'data': l[1] }
            if l[1].startswith('pci:'):
                aliasrec['type'] = 'pci'
                m = pcifilter.match(l[1])
                for key in m.groupdict().keys():
                    if m.group(key):
                        aliasrec[key] = m.group(key).lower()
            elif l[1].startswith('usb:'):
                aliasrec['type'] = 'usb'
                m = usbfilter.match(l[1])
                for key in m.groupdict().keys():
                    if m.group(key):
                        aliasrec[key] = m.group(key).lower()
            else:
                aliasrec['type'] = 'module'
            hwsdb.insertrec(cur, 'alias', aliasrec)

        elif line.startswith('parm:'):
            parmrec = { 'filename': file, 'option': l[1], 'description': ''.join(l[2:]) }
            hwsdb.insertrec(cur, 'parm', parmrec)

        elif line.startswith('depends:'):
            if len(l) > 2:
                for module in l[1].split(','):
                    dependsrec = { 'filename': file, 'module': module }
                    hwsdb.insertrec(cur, 'depends', dependsrec)

        else:
            key = l[0].split(':')[0]
            kmodrec[key] = ''.join(l[1:])
    hwsdb.insertrec(cur, 'kmod', kmodrec)

con.commit()
