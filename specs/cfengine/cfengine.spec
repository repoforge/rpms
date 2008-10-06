# $Id$
# Authority: dag
# Upstream: Mark Burgess <Mark,Burgess$iu,hio,no>

%{?dtag: %{expand: %%define %dtag 1}}

%{?rh7:%define _without_db4 1}
%{?el2:%define _without_db4 1}
%{?rh6:%define _without_db4 1}

Summary: System administration tool for networks
Name: cfengine
Version: 2.2.6
Release: 1
License: GPL
Group: System Environment/Base
URL: http://www.cfengine.org/

Source: http://www.cfengine.org/downloads/cfengine-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: bison, flex, m4, openssl-devel, tetex, texinfo, ghostscript
BuildRequires: tetex-latex, tetex-dvips
%{!?_without_db4:BuildRequires: db4-devel}
%{?_without_db4:BuildRequires: db3-devel >= 3.2}

%description
Cfengine, or the configuration engine is an agent/software robot and a
very high level language for building expert systems to administrate
and configure large computer networks. Cfengine uses the idea of
classes and a primitive form of intelligence to define and automate
the configuration and maintenance of system state, for small to huge
configurations. Cfengine is designed to be a part of a computer immune
system.

%prep
%setup

%{__cat} <<EOF >default.sysconfig
# OPTIONS defines additional command line options to execute the program
# with.  Please see the output of --help for a brief description of the
# possible options availible.
#OPTIONS=""
EOF

%{__cat} <<'EOF' >cfenvd.sysv
#!/bin/bash
#
# Init file for the cfengine anomaly detection service
#
# chkconfig: 2345 98 20
# description: cfenvd is an optional anomaly detection service for cfengine.
#
# processname: cfenvd
# pidfile: %{_localstatedir}/run/cfengine

# Source function library.
source %{_initrddir}/functions

RETVAL=0
prog="cfenvd"
desc="cfengine anomaly detection service"

if [ -r /etc/sysconfig/$prog ]; then
    source %{_sysconfdir}/sysconfig/$prog
fi

start() {
    echo -n $"Starting $desc ($prog): "
    daemon $prog $OPTIONS
    RETVAL=$?
    echo
    [ $RETVAL -eq 0 ] && touch %{_localstatedir}/lock/subsys/$prog
    return $RETVAL
}

stop() {
    echo -n $"Stopping $desc ($prog): "
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
EOF

%{__cat} <<'EOF' >cfexecd.sysv
#!/bin/bash
#
# Init file for the cfengine client daemon
#
# chkconfig: 2345 98 20
# description: cfexecd is scheduler and reporter in cfengine client hosts.
#
# processname: cfexecd
# config: %{_localstatedir}/cfengine/inputs
# pidfile: %{_localstatedir}/run/cfengine

# Source function library.
source %{_initrddir}/functions

RETVAL=0
prog="cfexecd"
desc="cfengine client daemon"

if [ -r /etc/sysconfig/$prog ]; then
    source %{_sysconfdir}/sysconfig/$prog
fi

start() {
    echo -n $"Starting $desc ($prog): "
    daemon $prog $OPTIONS
    RETVAL=$?
    echo
    [ $RETVAL -eq 0 ] && touch %{_localstatedir}/lock/subsys/$prog
    return $RETVAL
}

stop() {
    echo -n $"Stopping $desc ($prog): "
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
EOF

%{__cat} <<'EOF' >cfservd.sysv
#!/bin/bash
#
# Init file for the cfengine server daemon
#
# chkconfig: 2345 96 20
# description: cfservd is responsible for giving out configuration files to
#              those cfengine clients, who wish to update their configs.
#
# processname: cfservd
# config: %{_localstatedir}/cfengine/masterfiles
# pidfile: %{_localstatedir}/run/cfengine

# Source function library.
source %{_initrddir}/functions

RETVAL=0
prog="cfservd"
desc="cfengine server daemon"

if [ -r /etc/sysconfig/$prog ]; then
    source %{_sysconfdir}/sysconfig/$prog
fi

start() {
    echo -n $"Starting $desc ($prog): "
    if [ ! -f %{_localstatedir}/cfengine/ppkeys/localhost.priv ]; then
        /usr/sbin/cfkey
    fi
    daemon $prog $OPTIONS
    RETVAL=$?
    echo
    [ $RETVAL -eq 0 ] && touch %{_localstatedir}/lock/subsys/$prog
    return $RETVAL
}

stop() {
    echo -n $"Stopping $desc ($prog): "
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
EOF

%build
%configure BERKELEY_DB_LIB="-ldb" \
    --program-prefix="%{?_program_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_sbindir}
%{__install} -d -m0755 %{buildroot}%{_datadir}/cfengine/
%{__install} -d -m0755 %{buildroot}%{_localstatedir}/cfengine/{bin,inputs}/
%{__make} install DESTDIR="%{buildroot}"
%{__make} install DESTDIR="%{buildroot}" -C doc
%{__install} -Dp -m0755 cfenvd.sysv %{buildroot}%{_initrddir}/cfenvd
%{__install} -Dp -m0755 cfexecd.sysv %{buildroot}%{_initrddir}/cfexecd
%{__install} -Dp -m0755 cfservd.sysv %{buildroot}%{_initrddir}/cfservd
%{__install} -Dp -m0644 default.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/cfenvd
%{__install} -Dp -m0644 default.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/cfexecd
%{__install} -Dp -m0644 default.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/cfservd
%{__ln_s} -f %{_sbindir}/cfagent %{buildroot}%{_localstatedir}/cfengine/bin/

%post
%{_sbindir}/cfkey &>/dev/null || :
if [ $1 -eq 1 ]; then
    chkconfig --add cfenvd
    chkconfig --add cfexecd
    chkconfig --add cfservd
fi

%preun
if [ $1 -eq 0 ]; then
    chkconfig --del cfenvd
    chkconfig --del cfexecd
    chkconfig --del cfservd
fi

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%doc contrib/cfengine.el inputs/*
%doc %{_mandir}/man?/*
%config %{_initrddir}/*
%config(noreplace) %{_sysconfdir}/sysconfig/cfexecd
%config(noreplace) %{_sysconfdir}/sysconfig/cfenvd
%config(noreplace) %{_sysconfdir}/sysconfig/cfservd
%{_sbindir}/*
%{_localstatedir}/cfengine/
%exclude %{_datadir}/cfengine/
%exclude %{_libdir}/libcfengine.a
%exclude %{_libdir}/libcfengine.la

%changelog
* Mon Oct 06 2008 Dag Wieers <dag@wieers.com> - 2.2.6-1
- Updated to release 2.2.6.

* Fri Dec 28 2007 Dag Wieers <dag@wieers.com> - 2.2.3-1
- Updated to release 2.2.3.

* Tue Oct 02 2007 Dag Wieers <dag@wieers.com> - 2.2.2-1
- Updated to release 2.2.2.

* Sat Jun 02 2007 Dag Wieers <dag@wieers.com> - 2.2.1-1
- Updated to release 2.2.1.

* Wed May 02 2007 Dag Wieers <dag@wieers.com> - 2.2.0-1
- Updated to release 2.2.0.

* Wed Jan 31 2007 Dag Wieers <dag@wieers.com> - 2.1.22-1
- Updated to release 2.1.22.

* Mon Dec 18 2006 Dag Wieers <dag@wieers.com> - 2.1.21-1
- Updated to release 2.1.21.

* Fri Apr 21 2006 Dries Verachtert <dries@ulyssis.org> - 2.1.20-1
- Updated to release 2.1.20.

* Tue Jan 03 2006 Dag Wieers <dag@wieers.com> - 2.1.18-1
- Updated to release 2.1.18.

* Tue Nov 15 2005 Dries Verachtert <dries@ulyssis.org> - 2.1.17-1
- Updated to release 2.1.17.

* Mon Jul 11 2005 Dag Wieers <dag@wieers.com> - 2.1.15-1
- Updated to release 2.1.15.

* Sat Apr 09 2005 Dag Wieers <dag@wieers.com> - 2.1.14-1
- Added sysconfig files for sysv scripts. (Nathan R. Hruby)
- Updated to release 2.1.14.

* Wed Mar 30 2005 Dag Wieers <dag@wieers.com> - 2.1.13-1
- Updated to release 2.1.13.

* Mon Nov 01 2004 Dag Wieers <dag@wieers.com> - 2.1.11-1
- Updated to release 2.1.11.

* Thu Sep 02 2004 Dag Wieers <dag@wieers.com> - 2.1.10-1
- Updated to release 2.1.10.

* Wed Aug 11 2004 Dag Wieers <dag@wieers.com> - 2.1.9-1
- Updated to release 2.1.9.

* Sun Aug 08 2004 Dag Wieers <dag@wieers.com> - 2.1.8-1
- Updated to release 2.1.8.

* Tue Jun 15 2004 Dag Wieers <dag@wieers.com> - 2.1.6-1
- Updated to release 2.1.6.

* Wed Apr 28 2004 Dag Wieers <dag@wieers.com> - 2.1.5-2
- Removed the %%{_infodir}/dir from the buildroot. (Shawn Ashlee)

* Mon Apr 26 2004 Dag Wieers <dag@wieers.com> - 2.1.5-1
- Updated to release 2.1.5.
- Fixed problem with info-files and added cfenvd sysv script. (James Wilkinson)

* Sat Jan 31 2004 Dag Wieers <dag@wieers.com> - 2.1.1-0
- Updated to release 2.1.1.

* Wed Sep 03 2003 Dag Wieers <dag@wieers.com> - 2.0.6-3
- Added --program-prefix for RH73. (Soren Roug)

* Thu Jun 12 2003 Dag Wieers <dag@wieers.com> - 2.0.6-2
- Fix install-info and moved documentation. (Terje Rosten)

* Fri Apr 25 2003 Dag Wieers <dag@wieers.com> - 2.0.6-0
- Initial package. (using DAR)
