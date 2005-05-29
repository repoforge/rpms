#!/bin/sh

/usr/lib/rpm/find-requires $* | grep -v 'perl(GD)' | grep -v 'perl(MRP::BaseClass)' | grep -v 'perl(Net::Netmask)' | grep -v 'perl(Net::Telnet)'
