#!/usr/bin/env python2
import sys
import commands
import xml.dom.minidom
from xml.dom import Node

class Connection:
    name = '???'
    def __repr__(self):
        return '<Connection %s>' % self.name

class Setting:
    name = '???'
    def __repr__(self):
        return '<Setting %s>' % self.name

class Worker:
    pass

class SqualeParser:
    SETTINGS_PROPERTIES = ['name', 'value']
    CONNECTION_PROPERTIES = ['name', 'backend', 'max-pending-warn-level',
                             'tnsname', 'user', 'dbname', 'host', 'port', 'passwd']
    WORKER_PROPERTIES = ['tnsname', 'user', 'passwd', 'host', 'port', 'dbname']
    def __init__(self, filename):
        self.settings = []
        self.connections = []
        self.doc = xml.dom.minidom.parse(filename)

        assert len(self.doc.childNodes) == 1
        root = self.doc.childNodes[0]
        assert root.nodeType == Node.ELEMENT_NODE
        assert root.nodeName == 'squale'

        self.parseRoot(root)

    def parseRoot(self, node):
        for child in node.childNodes:
            if child.nodeType == Node.TEXT_NODE:
                continue
            assert child.nodeType == Node.ELEMENT_NODE

            if child.nodeName == 'settings':
                self.parseSettings(child)
            elif child.nodeName == 'connections':
                self.parseConnections(child)
            else:
                raise AssertionErro

    def parseSettings(self, node):
        for child in node.childNodes:
            if child.nodeType == Node.TEXT_NODE:
                continue
            assert child.nodeType == Node.ELEMENT_NODE
            assert child.nodeName == 'setting'

            self.settings.append(self.parseSetting(child))

    def parseSetting(self, node):
        setting = Setting()

        for prop in self.SETTINGS_PROPERTIES:
            if node.hasAttribute(prop):
                value = node.getAttribute(prop)
            else:
                value = None
            setattr(setting, prop, value)
        return setting

    def parseConnections(self, node):
        for child in node.childNodes:
            if child.nodeType == Node.TEXT_NODE:
                continue
            assert child.nodeType == Node.ELEMENT_NODE
            assert child.nodeName == 'connection'

            self.connections.append(self.parseConnection(child))

    def parseConnection(self, node):
        connection = Connection()
        connection.workers = []

        for prop in self.CONNECTION_PROPERTIES:
            if node.hasAttribute(prop):
                value = node.getAttribute(prop)
            else:
                value = None
            setattr(connection, prop, value)

        for child in node.childNodes:
            if child.nodeType == Node.TEXT_NODE:
                continue
            assert child.nodeType == Node.ELEMENT_NODE
            assert child.nodeName == 'worker'
            connection.workers.append(self.parseWorker(child))

        return connection

    def parseWorker(self, node):
        worker = Worker()

        for prop in self.WORKER_PROPERTIES:
            if node.hasAttribute(prop):
                value = node.getAttribute(prop)
            else:
                value = None
            setattr(worker, prop, value)
        return worker

def main(args):
    if not len(args) == 2:
        print 'Usage: squale_check.py squale_config_file.xml'
        return 1
    filename = args[1]
    exitstatus = 0

    parser = SqualeParser(filename)

    for setting in parser.settings:
        if setting.name == 'socket_name':
            socket_name = setting.value

    squaleruncmd = 'squale-run -s %s -c foo -t 60 -q squale_global_stats' % socket_name
    (status, output) = commands.getstatusoutput(squaleruncmd)
    print output
    if status:
        print 'Status : %s' % status
        return 1

    for connection in parser.connections:
        squalerunstats = 'squale-run -s %s -c %s -t 60 -q squale_local_stats' % (socket_name, connection.name)
        if connection.backend == 'oracle':
            sqlquery = 'select sysdate from dual'
            squalerunquery = 'squale-run -s %s -c %s -t 60 -q "%s"' % (socket_name, connection.name, sqlquery)
        (unused, local_stats_output) = commands.getstatusoutput(squalerunstats)
        (status, unused) = commands.getstatusoutput(squalerunquery)
        if status:
            # Spool non-zero exit status
            exitstatus = 1
            print 'Query "%s" on connection "%s" exited abnormally, please check!' % (sqlquery, connection.name)
        print 'SQuaLe stats for "%s" :' % connection.name
        print local_stats_output

    return exitstatus

if __name__ == '__main__':
    sys.exit(main(sys.argv))

