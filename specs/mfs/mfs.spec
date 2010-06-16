# $Id$
# Authority: shuff
# Upstream: <moosefs-users@lists.sourceforge.net>

Summary: Fault tolerant, network distributed file system
Name: mfs
Version: 1.6.15
Release: 3%{?dist}
License: GPL
Group: System Environment/Daemons
URL: http://www.moosefs.org/

Source: http://moosefs.org/tl_files/mfscode/mfs-%{version}.tar.gz
Patch0: mfs-1.6.15_cgi.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: autoconf, automake
BuildRequires: binutils
BuildRequires: fuse-devel >= 2.6
BuildRequires: gcc-c++
BuildRequires: glibc-devel
BuildRequires: make
BuildRequires: pkgconfig >= 0.9.0
BuildRequires: python
BuildRequires: zlib-devel

Requires: chkconfig
Requires: python

%description
MooseFS is a fault tolerant, network distributed file system. It spreads data
over several physical servers which are visible to the user as one resource.
For standard file operations MooseFS acts as other Unix-alike file systems. It
has a hierarchical structure (directory tree), stores file attributes
(permissions, last access and modification times) as well as makes it possible
to create special files (block and character devices, pipes and sockets),
symbolic links (file names pointing to target files, not necessarily on
MooseFS) and hard links (different names of files which refer to the same data
on MooseFS). Access to the file system can be limited based on IP address
and/or password.

Distinctive features of MooseFS are:

* higher reliability (data can be stored in several copies on separate
  computers)
* dynamically expanding disk space by attaching new computers/disks
* possibility of storing deleted files for a defined period of time ("trash
  bin" service on a file system level)
* possibility of creating snapshots of files, which means coherent copies of
  the whole file, even while the file is being written/accessed.

Install this package to run a MooseFS master server, metalogger server, or chunk server.  MooseFS clients require only the %{name}-client package; however, you may want to install %{name}-client on your servers as well, for administrative reasons.

%package client
Summary: Client tools for MooseFS
Group: System Environment/Utilities

%description client
Install this package to run a MooseFS client.  This package contains administrative utilities for MooseFS in addition to basic client tools.

%package cgi
Summary: Status CGI for MooseFS
Group: System Environment/Utilities
Requires: httpd

%description cgi
Install this package to display MooseFS status via Apache-hosted CGI.  The CGI attempts to connect to localhost by default; if running on a host that is not the MooseFS master server, modify index.html accordingly. 

If you just want to run the status CGI using the bundled CGI server, not Apache, it is not necessary to install this package.

%prep
%setup

%build
%configure \
    --disable-dependency-tracking \
    --disable-static \
    --sysconfdir=%{_sysconfdir}/mfs \
    --with-mfscgi-dir=%{_datadir}/mfscgi \
    --with-default-user=daemon \
    --with-default-group=daemon
%{__make} %{?_smp_mflags}

%install
rm -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}

# yes, really apply the patch here rather than during %setup
%{__patch} -p1 < %{_sourcedir}/mfs-1.6.15_cgi.patch

# copy the CGI stuff into the right place for Apache
%{__install} -m0755 -d %{buildroot}%{_localstatedir}/www/cgi-bin/mfs
%{__install} -m0755 mfscgi/mfs.cgi %{buildroot}%{_localstatedir}/www/cgi-bin/mfs
%{__install} -m0755 mfscgi/chart.cgi %{buildroot}%{_localstatedir}/www/cgi-bin/mfs
%{__install} -m0755 -d %{buildroot}%{_localstatedir}/www/html/mfs
%{__install} -m0644 mfscgi/index.html %{buildroot}%{_localstatedir}/www/html/mfs
%{__install} -m0644 mfscgi/mfs.css %{buildroot}%{_localstatedir}/www/html/mfs
%{__install} -m0644 mfscgi/err.gif %{buildroot}%{_localstatedir}/www/html/mfs
%{__install} -m0644 mfscgi/logomini.png %{buildroot}%{_localstatedir}/www/html/mfs

# create the mfsmaster init script
%{__install} -m0755 -d %{buildroot}%{_initrddir}
%{__cat} > %{buildroot}%{_initrddir}/mfsmaster <<'MFSMASTER'
#!/bin/bash
#
# Init file for the MooseFS master service
#
# chkconfig: - 92 84
#
# description: MooseFS master
#
# processname: mfsmaster
# config: %{_sysconfdir}/mfs/mfsmaster.cfg

# Source function library.
. %{_initrddir}/functions

# Source networking configuration.
. %{_sysconfdir}/sysconfig/network

# Source initialization configuration.
[ -r "%{_sysconfdir}/sysconfig/mfsmaster" ] && . %{_sysconfdir}/sysconfig/mfsmaster

# Check that networking is up.
[ "${NETWORKING}" == "no" ] && exit 0
[ -x "%{_sbindir}/mfsmaster" ] || exit 1
[ -r "%{_sysconfdir}/mfs/mfsmaster.cfg" ] || exit 1
[ -r "%{_sysconfdir}/mfs/mfsexports.cfg" ] || exit 1

RETVAL=0
prog="mfsmaster"

start () {
    echo -n $"Starting $prog: "
    daemon $prog >/dev/null 2>&1
    RETVAL=$?
    echo
    [ $RETVAL -eq 0 ] && touch %{_localstatedir}/lock/subsys/\$prog
    return $RETVAL
}

stop () {
    echo -n $"Stopping $prog: "
    $prog stop >/dev/null 2>&1 || killproc $prog >/dev/null 2>&1
    RETVAL=$?
    echo
    [ $RETVAL -eq 0 ] && rm -f %{_localstatedir}/lock/subsys/$prog
    return $RETVAL
}

restart () {
    stop
    start
}

case "$1" in
  start)
    start
    ;;
  stop)
    stop
    ;;
  restart|reload)
    restart
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
    echo $"Usage: $0 {start|stop|restart|condrestart|status}"
    RETVAL=1
esac

exit $RETVAL
MFSMASTER

# create the mfsmetalogger init script
%{__cat} > %{buildroot}%{_initrddir}/mfsmetalogger <<'MFSMETALOGGER'
#!/bin/bash
#
# Init file for the MooseFS metalogger service
#
# chkconfig: - 92 84
#
# description: MooseFS metalogger
#
# processname: mfsmetalogger
# config: %{_sysconfdir}/mfs/mfsmetalogger.cfg

# Source function library.
. %{_initrddir}/functions

# Source networking configuration.
. %{_sysconfdir}/sysconfig/network

# Source initialization configuration.
[ -r "%{_sysconfdir}/sysconfig/mfsmetalogger" ] && . %{_sysconfdir}/sysconfig/mfsmetalogger

# Check that networking is up.
[ "${NETWORKING}" == "no" ] && exit 0
[ -x "%{_sbindir}/mfsmetalogger" ] || exit 1
[ -r "%{_sysconfdir}/mfs/mfsmetalogger.cfg" ] || exit 1

RETVAL=0
prog="mfsmetalogger"

start () {
    echo -n $"Starting $prog: "
    daemon $prog >/dev/null 2>&1
    RETVAL=$?
    echo
    [ $RETVAL -eq 0 ] && touch %{_localstatedir}/lock/subsys/\$prog
    return $RETVAL
}

stop () {
    echo -n $"Stopping $prog: "
    $prog stop >/dev/null 2>&1 || killproc $prog >/dev/null 2>&1
    RETVAL=$?
    echo
    [ $RETVAL -eq 0 ] && rm -f %{_localstatedir}/lock/subsys/$prog
    return $RETVAL
}

restart () {
    stop
    start
}

case "$1" in
  start)
    start
    ;;
  stop)
    stop
    ;;
  restart|reload)
    restart
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
    echo $"Usage: $0 {start|stop|restart|condrestart|status}"
    RETVAL=1
esac

exit $RETVAL
MFSMETALOGGER

# create the mfschunkserver init script
%{__cat} > %{buildroot}%{_initrddir}/mfschunkserver <<'MFSCHUNKSERVER'
#!/bin/bash
#
# Init file for the MooseFS chunkserver service
#
# chkconfig: - 93 83
#
# description: MooseFS chunkserver
#
# processname: mfschunkserver
# config: %{_sysconfdir}/mfs/mfschunkserver.cfg

# Source function library.
. %{_initrddir}/functions

# Source networking configuration.
. %{_sysconfdir}/sysconfig/network

# Source initialization configuration.
[ -r "%{_sysconfdir}/sysconfig/mfschunkserver" ] && . %{_sysconfdir}/sysconfig/mfschunkserver

# Check that networking is up.
[ "${NETWORKING}" == "no" ] && exit 0
[ -x "%{_sbindir}/mfschunkserver" ] || exit 1
[ -r "%{_sysconfdir}/mfs/mfschunkserver.cfg" ] || exit 1
[ -r "%{_sysconfdir}/mfs/mfshdd.cfg" ] || exit 1

RETVAL=0
prog="mfschunkserver"

start () {
    echo -n $"Starting $prog: "
    daemon $prog >/dev/null 2>&1
    RETVAL=$?
    echo
    [ $RETVAL -eq 0 ] && touch %{_localstatedir}/lock/subsys/\$prog
    return $RETVAL
}

stop () {
    echo -n $"Stopping $prog: "
    $prog stop >/dev/null 2>&1 || killproc $prog >/dev/null 2>&1
    RETVAL=$?
    echo
    [ $RETVAL -eq 0 ] && rm -f %{_localstatedir}/lock/subsys/$prog
    return $RETVAL
}

restart () {
    stop
    start
}

case "$1" in
  start)
    start
    ;;
  stop)
    stop
    ;;
  restart|reload)
    restart
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
    echo $"Usage: $0 {start|stop|restart|condrestart|status}"
    RETVAL=1
esac

exit $RETVAL
MFSCHUNKSERVER

%post
/sbin/chkconfig --add mfsmaster >/dev/null 2>&1
/sbin/chkconfig --add mfsmetalogger >/dev/null 2>&1
/sbin/chkconfig --add mfschunkserver >/dev/null 2>&1

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,0755)
%doc COPYING INSTALL NEWS README UPGRADE
%doc %{_mandir}/man?/*
%exclude %doc %{_mandir}/man1/*
%{_sbindir}/*
%{_sysconfdir}/mfs/
%dir %{_initrddir}
%attr(0755,root,root) %{_initrddir}/*
%{_datadir}/mfscgi/
%attr(-,daemon,daemon) %{_localstatedir}/mfs/

%files client
%doc %{_mandir}/man1/*
%{_bindir}/*

%files cgi
%defattr(-,apache,apache,0755)
%dir %{_localstatedir}/www/cgi-bin/mfs
%config %{_localstatedir}/www/cgi-bin/mfs/mfs.cgi
%config %{_localstatedir}/www/cgi-bin/mfs/chart.cgi
%dir %{_localstatedir}/www/html/mfs
%config %{_localstatedir}/www/html/mfs/index.html
%config %{_localstatedir}/www/html/mfs/mfs.css
%config %{_localstatedir}/www/html/mfs/err.gif
%config %{_localstatedir}/www/html/mfs/logomini.png

%changelog
* Fri Jun 11 2010 Steve Huff <shuff@vecna.org> - 1.6.15-3
- Ported to RPMforge.
- Split out client into a separate package.
- Split out cgi into a separate package.

* Fri Jun 11 2010 Laurent Wandrebeck <lw@hygeos.com> - 1.6.15-2
- Put config files in /etc/mfs instead of /etc.

* Mon May 31 2010 Laurent Wandrebeck <lw@hygeos.com> - 1.6.15-1
- Update to 1.6.15

* Mon Mar 08 2010 Kirby Zhou - 1.6.13-1
- initial rpm spec
