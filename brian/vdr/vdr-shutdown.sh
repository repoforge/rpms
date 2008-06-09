#!/bin/sh

# To enable this script, pass it to vdr with the -s option, eg.
# "-s vdr-shutdown.sh" (sans quotes) in VDR_OPTIONS in /etc/sysconfig/vdr.
# See also below for additional required sudo configuration, and
# README.package for information how to get the time written to ACPI and
# thus getting the system to wake up at the correct time.

# How many minutes before the next timer event should the system wake up,
# ie. how long does it take to boot until VDR is running?
delay=3

file=/var/lib/vdr/acpi-wakeup
rm -f $file

if [ ${1:-0} -gt 0 -a -e /proc/acpi/alarm ] ; then
    date -d "1970-01-01 UTC $1 sec -$delay min" +"%Y-%m-%d %H:%M:%S" > $file
fi

# In order to make this work, the vdr user needs to be allowed to run
# /sbin/shutdown -h now with sudo as root, without giving a password and
# without a tty.  Example sudoers(5) configuration to accomplish that:
#     Defaults:vdr    !requiretty
#     vdr             ALL = (root) NOPASSWD: /sbin/shutdown -h now

exec sudo /sbin/shutdown -h now
