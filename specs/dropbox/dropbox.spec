# $Id$
# Authority: shuff
# Upstream: Dropbox Support (https://www.dropbox.com/ticket)
# ExclusiveArch: i386 x86_64

Summary: Sync and backup files between computers
Name:    dropbox
Version: 0.7.110
Release: 3%{?dist}
License: Proprietary
Group:   Applications/Utilities
URL:     http://www.dropbox.com/

ExclusiveArch: %{ix86} x86_64
%ifarch %{ix86}
    %define dropbox_arch x86
%else
    %define dropbox_arch x86_64
%endif
Source: http://dl-web.dropbox.com/u/17/dropbox-lnx.%{dropbox_arch}-%{version}.tar.gz
Source1: https://dl.getdropbox.com/u/43645/dbcli.py
Source2: http://dl.dropbox.com/u/119154/permalink/dropboxdir.py
Patch0: %{name}_parentdir.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

# this contains binaries, don't autoprov
AutoReqProv: no

BuildRequires: dos2unix
BuildRequires: rpm-macros-rpmforge

Provides: %{name} = %{version}

# trim python2.5
%filter_from_requires /python2\.5/d
%filter_setup

# there are binaries in this package, don't mess with them
%define debug_package %{nil}
%define _enable_debug_packages %{nil}
%define __os_install_post %{nil}

%description
Dropbox is software that syncs your files online and across your computers.

Put your files into your Dropbox on one computer, and they'll be instantly
available on any of your other computers that you've installed Dropbox on
(Windows, Mac, and Linux too!) Because a copy of your files are stored on
Dropbox's secure servers, you can also access them from any computer or mobile
device using the Dropbox website.

%prep
%setup -n .dropbox-dist
cd %{_builddir}/.dropbox-dist
cp %{_sourcedir}/dbcli.py .
dos2unix -q dbcli.py
cp %{_sourcedir}/dropboxdir.py .
dos2unix -q dropboxdir.py
%patch0 -p0

%build

# generate init script
%{__cat} <<'EOFINIT' >dropbox-init
# chkconfig: 345 85 15
# description: Startup script for dropbox daemon
#
# processname: dropboxd
# pidfile: /var/run/dropbox.pid
# config: /etc/sysconfig/dropbox
#

### BEGIN INIT INFO
# Provides: dropboxd
# Required-Start: $local_fs $network $syslog
# Required-Stop: $local_fs $syslog
# Should-Start: $syslog
# Should-Stop: $network $syslog
# Default-Start: 2 3 4 5
# Default-Stop: 0 1 6
# Short-Description: Start up the Dropbox file syncing daemon
# Description:       Dropbox is a filesyncing sevice provided by dropbox.com
#                    This service starts up the dropbox daemon.
### END INIT INFO


# Source function library.
. /etc/rc.d/init.d/functions

DROPBOX_PATH=%{_libexecdir}/dropbox
[ -f %{_sysconfdir}/sysconfig/dropbox ] && . %{_sysconfdir}/sysconfig/dropbox

if [ -z $DROPBOX_GROUP ]; then
    DROPBOX_GROUP='dropbox'
fi

if [ -z $DROPBOX_USERS ]; then
    DROPBOX_USERS=$(lid -gn "$DROPBOX_GROUP")
fi

prog=dropboxd
lockfile=${LOCKFILE-/var/lock/subsys/$prog}
config=${CONFIG-%{_sysconfdir}/dropbox}
RETVAL=0

start() {
        echo -n $"Starting $prog"

        if [ -z $DROPBOX_USERS ] ; then
                echo -n ": unconfigured: $config"
                echo_failure
                echo
                rm -f ${lockfile} ${pidfile}
                RETURN=6
                return $RETVAL
        fi

        for dbuser in $DROPBOX_USERS; do
            daemon --user $dbuser /bin/sh -c "$DROPBOX_PATH/dropboxd&"
        done

        RETVAL=$?
        echo
        [ $RETVAL = 0 ] && touch ${lockfile}
        return $RETVAL
}

status() {
    for dbuser in $DROPBOX_USERS; do
        dbpid=`pgrep -u $dbuser dropbox`
        if [ -z $dbpid ] ; then
            echo "dropboxd for USER $dbuser: not running."
        else
            echo "dropboxd for USER $dbuser: running (pid $dbpid)"
        fi
    done
}

stop() {
        echo -n $"Stopping $prog"
    for dbuser in $DROPBOX_USERS; do
        pkill -u $dbuser -f -x "$DROPBOX_PATH/dropbox"
    done
        RETVAL=$?
        echo
        [ $RETVAL = 0 ] && rm -f ${lockfile} ${pidfile}
}

# See how we were called.
case "$1" in
  start)
        start
        ;;
  status)
        status
        ;;
  stop)
        stop
        ;;
  restart)
        stop
        start
        ;;
  *)
        echo $"Usage: $prog {start|status|stop|restart}"
        RETVAL=3
esac

exit $RETVAL
EOFINIT

# generate the sysconfig
%{__cat} <<'EOFSYSCONFIG' >dropbox-sysconfig 
# By default, a dropbox daemon will be started for all users in the dropbox 
# group.  You can override the group name here, or define the users any other
# way you like.
#
#DROPBOX_GROUP=dropbox
#DROPBOX_USERS=foo bar baz
EOFSYSCONFIG

# generate the launcher
%{__cat} <<'EOFBIN' >dropbox-bin 
#!/bin/sh
#
# Simple wrapper script for %{_libexecdir}/dropbox/dropboxd.
cd %{_libexecdir}/dropbox
exec ./dropboxd "$@"
EOFBIN

%install
%{__rm} -rf %{buildroot}

# first install the init script
%{__install} -m0755 -d %{buildroot}%{_sysconfdir}/init.d
%{__install} -m0755 dropbox-init %{buildroot}%{_sysconfdir}/init.d/dropbox
%{__rm} -f dropbox-init

# then install the sysconfig
%{__install} -m0755 -d %{buildroot}%{_sysconfdir}/sysconfig
%{__install} -m0644 dropbox-sysconfig %{buildroot}%{_sysconfdir}/sysconfig/dropbox
%{__rm} -f dropbox-sysconfig

# and now the helper scripts
%{__install} -m0755 -d %{buildroot}%{_bindir}
%{__install} -m0755 dropbox-bin %{buildroot}%{_bindir}/dropbox
%{__rm} -f dropbox-bin
%{__install} -m0755 dbcli.py %{buildroot}%{_bindir}/dbcli
%{__rm} -f dbcli.py
%{__install} -m0755 dropboxdir.py %{buildroot}%{_bindir}/dropboxdir
%{__rm} -f dropboxdir.py

# finally, install everything else
%{__install} -d %{buildroot}%{_libexecdir}/dropbox
%{__cp} -a ./* %{buildroot}%{_libexecdir}/dropbox

%clean
%{__rm} -rf %{buildroot}

%post
if [ $1 -lt 2 ]; then
    /sbin/chkconfig --add dropbox 2>&1 >/dev/null
fi
/usr/bin/chcon -u system_u -t initrc_exec_t /etc/init.d/dropbox
/usr/bin/chcon -u system_u -t etc_t /etc/sysconfig/dropbox


%preun
if [ $1 -eq 0 ]; then
    /sbin/chkconfig --del dropbox 2>&1 >/dev/null
fi

%files
%defattr(-, root, root, 0755)
%doc ACKNOWLEDGEMENTS VERSION
%{_bindir}/*
%{_libexecdir}/dropbox
%config(noreplace) %{_sysconfdir}/init.d/*
%config(noreplace) %{_sysconfdir}/sysconfig/*

%changelog
* Fri Sep 03 2010 Yury V. Zaytsev <yury@shurup.com> - 0.7.110-3
- Changed ExclusiveArch to include all ix86 flavors.

* Mon May 10 2010 Steve Huff <shuff@vecna.org> - 0.7.110-2
- Disabled AutoReqProv (thanks to Robin Bowes) to eliminate bogus Provides: entries.

* Wed Mar 24 2010 Steve Huff <shuff@vecna.org> - 0.7.110-1
- Initial package.
- Just a repackaging of the binary install; needs testing.
