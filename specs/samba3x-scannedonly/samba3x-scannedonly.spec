# $Id$
# Authority: dag
# Upstream: Olivier Sessink <oli4$users,sourceforge,net>

# ExclusiveDist: el5

%define vfsdir %{_libdir}/samba/vfs

%define real_name scannedonly
%define samba_version 3.3.8

Summary: Scannedonly scalable samba anti-virus daemon
Name: samba3x-scannedonly
Version: 0.20
Release: 2%{?dist}
License: GPL
Group: Applications/File
URL: http://olivier.sessink.nl/scannedonly/

Source0: http://olivier.sessink.nl/scannedonly/scannedonly-%{version}.tar.bz2
Source1: http://www.samba.org/samba/ftp/stable/samba-%{samba_version}.tar.gz
Patch0: scannedonly-0.20-ctime.patch
Patch1: scannedonly-0.20-zerofile.patch
Patch2: scannedonly-0.20-isqueued.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: clamav-devel
BuildRequires: libtalloc-devel

Requires: samba3x = %{samba_version}

%description
Scannedonly is a samba VFS module and a scanning daemon that ensure that only
files that have been scanned for viruses are visible and accessible to the end
user.

Scannedonly was developed because of scalability problems with samba-vscan:
high server loads when (the same) files were requested often, and timeouts
when large zip files were requested. Scannedonly doesn't have these problems,
but it does introduce some other issues. Choose the product that suits you best.

%package -n scannedonly
Summary: Scannedonly scalable samba anti-virus VFS module
Group: Applications/File

%description -n scannedonly
Scannedonly is a samba VFS module and a scanning daemon that ensure that only
files that have been scanned for viruses are visible and accessible to the end
user.

Scannedonly was developed because of scalability problems with samba-vscan:
high server loads when (the same) files were requested often, and timeouts
when large zip files were requested. Scannedonly doesn't have these problems,
but it does introduce some other issues. Choose the product that suits you best.

%prep
%setup -n %{real_name}-%{version} -a1
%patch0 -p0
%patch1 -p0
%patch2 -p0

%{__cat} <<EOF >scannedonlyd.sysconfig
### The UDP port to listen on. Default: 2020 (but by default a domain
### socket is used)
#PORTNUM=2020

### The unix domain socket name to listen on. The directory needs to
### exist! Default: /var/lib/scannedonly/scan
#SOCKET=/var/lib/scannedonly/scan

### The total number of scanning threads. Maximum one thread (see option
### maxlargethreads) will be scanning large files. Maximum one thread
### might be updating the clam database. So use at least 3 threads if
### you want to guarantee that there is always a thread for small files
### available. Default: 4 threads
#MAXTHREADS=4

### The maximum number of scanning threads that may scan large files.
### Default: 1 thread
#MAXLARGETHREADS=1

### The log level from 0 (little logging) to 3 (verbose logging). Default: 1
#LOGLEVEL=1

### Which size files are treated as big. Default: 5 Mb (and higher)
#BIG=5

### The interval for status messages in the logs. Default: 10 minutes
#TIME=10

### The base directory for which requests for scanning are accepted.
### Requests to scan files outside this directory are ignored. Using thisxi
###  option is very much advised! Default: / (all files are accepted by default)
#SCANROOT=/

### Exclude scanning of files that match this (regular expression) pattern.
### For example '/home/[^/]+/Maildir/.*'. You might want to use the option
### veto files in your Samba configuration to exclude these files in samba
### as well, otherwise samba will keep telling that these files need
### scanning. Default: none
#EXCLUDE=

### By default a file is renamed into .virus:file. If you want all viruses
### in a central location specify a quarantainedir. If a virus is found it
### will be moved to this directory. Default: none
#QUARANTAINEDIR=

### The maximum request queue length. If the maximum number of requests are
### on the queue, new requests are ignored. Default: 5000 requests
#QUEUELEN=5000

### Additional options can be found in the documentation and can be provided
### here.
#OPTIONS=
EOF

%{__cat} <<'EOF' >scannedonlyd.init
#!/bin/bash
#
# Init file for Scannedonly samba antivirus daemon
#
# Written by Dag Wieers <dag@wieers.com>
#
# chkconfig: - 90 36
# description: Scannedonlyd samba antivirus daemon
#
# processname: scannedonlyd_clamav
# pidfile: %{_localstatedir}/run/scannedonlyd_clamav

# Source function library.
source /etc/rc.d/init.d/functions

# Source networking configuration.
source /etc/sysconfig/network

DAEMON="%{_sbindir}/scannedonlyd_clamav"
SYSCONFIG="%{_sysconfdir}/sysconfig/scannedonlyd"
PORTNUM=
SOCKET=
MAXTHREADS=
MAXLARGETHREADS=
LOGLEVEL=
BIG=
TIME=
SCANROOT=
QUARANTAINEDIR=
QUEUELEN=
PIDFILE="/var/run/scannedonlyd_clamav"
EXCLUDE=
OPTIONS=

if [ -r "$SYSCONFIG" ]; then
    source "$SYSCONFIG"
fi

[ -x "$DAEMON" ] || exit 1

RETVAL=0
prog="scannedonlyd_clamav"
desc="Scannedonly Daemon"

OPTIONS="$OPTIONS --pidfile=$PIDFILE
        ${PORTNUM:+--portnum=$PORTNUM}
        ${SOCKET:+--socket=$SOCKET}
        ${MAXTHREADS:+--maxthreads=$MAXTHREADS}
        ${MAXLARGETHREADS:+--maxlargethreads=$MAXLARGETHREADS}
        ${LOGLEVEL:+--loglevel=$LOGLEVEL}
        ${BIG:+--big=$BIG}
        ${TIME:+--time=$TIME}
        ${SCANROOT:+--scanroot=$SCANROOT}
        ${QUARANTAINEDIR:+--quarantainedir=$QUARANTAINEDIR}
        ${QUEUELEN:+--queuelen=$QUEUELEN}
        ${EXCLUDE:+--exclude=$EXCLUDE}
    "

start() {
    echo -n $"Starting $desc ($prog): "
    daemon --pidfile=$PIDFILE $prog $OPTIONS
    RETVAL=$?
    echo
    [ $RETVAL -eq 0 ] && touch %{_localstatedir}/lock/subsys/$prog
    return $RETVAL
}

stop() {
    echo -n $"Shutting down $desc ($prog): "
    killproc $prog
    RETVAL=$?
    echo
    [ $RETVAL -eq 0 ] && rm -f %{_localstatedir}/lock/subsys/$prog
    return $RETVAL
}

restart() {
    stop
    start
}

reload() {
    echo -n $"Reloading $desc ($prog): "
    killproc $prog -HUP
    RETVAL=$?
    echo
    return $RETVAL
}

case "$1" in
  start)
    start
    ;;
  stop)
    stop
    ;;
  restart)
    restart
    ;;
  reload)
    reload
    ;;
  condrestart)
    [ -e %{_localstatedir}/lock/subsys/$prog ] && restart
    RETVAL=$?
    ;;
  status)
    status $prog
    RETVAL=$?
    ;;
  *)
    echo $"Usage: $0 {start|stop|restart|reload|condrestart|status}"
    RETVAL=1
esac

exit $RETVAL
EOF

%build
### Prepare Samba
cd samba-%{samba_version}/source
./autogen.sh || :
./configure
make proto
cd -

%configure \
    --with-samba-source="$PWD/samba-%{samba_version}/source" \
    --with-samba-vfs-dir="%{vfsdir}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%{__install} -Dp -m0755 scannedonlyd.init %{buildroot}%{_initrddir}/scannedonlyd
%{__install} -Dp -m0644 scannedonlyd.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/scannedonlyd
%{__install} -d -m0755 %{buildroot}%{_localstatedir}/lib/scannedonly/

%post
/sbin/chkconfig --add scannedonlyd

%preun
if [ $1 -eq 0 ]; then
        /sbin/service scannedonlyd stop &> /dev/null || :
        /sbin/chkconfig --del scannedonlyd
fi

%postun
/sbin/service scannedonlyd condrestart &> /dev/null || :

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING INSTALL
%{_sbindir}/scannedonlyd_clamav
%dir %{_localstatedir}/lib/scannedonly/

%files -n scannedonly
%defattr(-, root, root, 0755)
%dir %{vfsdir}
%{vfsdir}/scannedonly.so
%doc COPYING INSTALL
%doc %{_mandir}/man8/scannedonlyd_clamav.8*
%doc %{_mandir}/man8/scannedonly_prescan.8*
%config(noreplace) %{_sysconfdir}/sysconfig/scannedonlyd
%config %{_initrddir}/scannedonlyd
%{_bindir}/scannedonly_prescan

%changelog
* Thu Oct 14 2010 Dag Wieers <dag@wieers.com> - 0.20-2
- Added a patch to skip already queued files.

* Mon Oct 11 2010 Dag Wieers <dag@wieers.com> - 0.20-1
- Initial package. (using DAR)
