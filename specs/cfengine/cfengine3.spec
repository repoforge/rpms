# $Id: cfengine.spec 6647 2009-01-14 17:05:42Z cmr $
# Authority: dag
# Upstream: Mark Burgess <Mark,Burgess$iu,hio,no>
# Tag: test


%{?rh7:%define _without_db4 1}
%{?el2:%define _without_db4 1}
%{?rh6:%define _without_db4 1}
%{?el4:%define _without_texinfotex 1}

Summary: System administration tool for networks
Name: cfengine
Version: 3.0.2
Release: 1%{?dist}
License: GPL
Group: System Environment/Base
URL: http://www.cfengine.org/

Source: http://www.cfengine.org/tarballs/cfengine-%{version}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: bison, flex, m4, openssl-devel 
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

%package docs
Summary: System administration tool for networks (documentation pack)
Group: System Environment/Base
BuildRequires: tetex-latex, tetex-dvips, texinfo
%{!?_without_texinfotex:BuildRequires: texinfo-tex}

%description docs
Full documentation for cfengine

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
prog="cf-serverd"
desc="cfengine server daemon"

if [ -r /etc/sysconfig/$prog ]; then
    source %{_sysconfdir}/sysconfig/$prog
fi

start() {
    echo -n $"Starting $desc ($prog): "
    if [ ! -f %{_localstatedir}/cfengine/ppkeys/localhost.priv ]; then
        %{_sbindir}/cfkey
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
    --program-prefix="%{?_program_prefix}" \
     --docdir=%{_defaultdocdir}/%{name}-%{version}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_sbindir}
%{__install} -d -m0755 %{buildroot}%{_datadir}/cfengine/
%{__install} -d -m0755 %{buildroot}%{_localstatedir}/cfengine/{bin,inputs}/
%{__make} install DESTDIR="%{buildroot}" 
%{__install} -Dp -m0755 cfenvd.sysv %{buildroot}%{_initrddir}/cfenvd
%{__install} -Dp -m0755 cfexecd.sysv %{buildroot}%{_initrddir}/cfexecd
%{__install} -Dp -m0755 cfservd.sysv %{buildroot}%{_initrddir}/cfservd
%{__install} -Dp -m0644 default.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/cfenvd
%{__install} -Dp -m0644 default.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/cfexecd
%{__install} -Dp -m0644 default.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/cfservd
%{__ln_s} -f %{_sbindir}/cfagent %{buildroot}%{_localstatedir}/cfengine/bin/

### Clean up buildroot
%{__rm} -f %{buildroot}%{_infodir}/dir

%post
%{_sbindir}/cfkey &>/dev/null || :
/sbin/install-info %{_infodir}/cfengine-Reference.info.gz %{_infodir}/dir
/sbin/install-info %{_infodir}/cfengine-Tutorial.info.gz %{_infodir}/dir

if [ $1 -eq 1 ]; then
    chkconfig --add cfenvd
    chkconfig --add cfexecd
    chkconfig --add cfservd
fi

%preun
/sbin/install-info --delete %{_infodir}/cfengine-Reference.info.gz %{_infodir}/dir
/sbin/install-info --delete %{_infodir}/cfengine-Tutorial.info.gz %{_infodir}/dir

if [ $1 -eq 0 ]; then
    chkconfig --del cfenvd
    chkconfig --del cfexecd
    chkconfig --del cfservd
fi

%clean
%{__rm} -rf %{buildroot}

%files docs
%doc docs/cf3-Reference.pdf


%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%doc %{_mandir}/man8/cf-agent.8*
%doc %{_mandir}/man8/cf-execd.8*
%doc %{_mandir}/man8/cf-key.8*
%doc %{_mandir}/man8/cf-know.8*
%doc %{_mandir}/man8/cf-monitord.8*
%doc %{_mandir}/man8/cf-promises.8*
%doc %{_mandir}/man8/cf-report.8*
%doc %{_mandir}/man8/cf-runagent.8*
%doc %{_mandir}/man8/cf-serverd.8*
%config(noreplace) %{_sysconfdir}/sysconfig/cfexecd
%config(noreplace) %{_sysconfdir}/sysconfig/cfenvd
%config(noreplace) %{_sysconfdir}/sysconfig/cfservd
%config %{_initrddir}/cfenvd
%config %{_initrddir}/cfexecd
%config %{_initrddir}/cfservd
%{_sbindir}/cf-agent
%{_sbindir}/cf-execd
%{_sbindir}/cf-key
%{_sbindir}/cf-know
%{_sbindir}/cf-monitord
%{_sbindir}/cf-promises
%{_sbindir}/cf-report
%{_sbindir}/cf-runagent
%{_sbindir}/cf-serverd
%{_localstatedir}/cfengine/
%{_libdir}/libpromises.a
%{_libdir}/libpromises.la
%exclude %{_datadir}/cfengine/

%changelog
* Mon Aug 24 2009 Chritsoph Maser <cmr@financial.com> - 3.0.2
- Update to version 3.0.2.

* Tue May 12 2009 Chritsoph Maser <cmr@financial.com> - 3.0.1
- Bump version: 3.0.1

* Wed Apr 15 2009 Chritsoph Maser <cmr@financial.com> - 3.0.1b6-1
- Bump version: 3.0.1b6

* Mon Mar 30 2009 Chritsoph Maser <cmr@financial.com> - 3.0.1b5-1
- update to version 3.0.1b5

* Thu Mar 05 2009 Chritsoph Maser <cmr@financial.com> - 3.0.1b4-1
- initial cfengine 3 build

* Wed Jan 14 2009 Christoph Maser <cmr@financial.com> - 2.2.9-1
- Updated to release 2.2.9.
- Use --with-docs on configure
- subpackage for ps/pdf/html docs

* Wed Oct 08 2008 Dag Wieers <dag@wieers.com> - 2.2.8-1
- Updated to release 2.2.8.

* Mon Oct 06 2008 Dag Wieers <dag@wieers.com> - 2.2.6-2
- Rebuild without info-page commands.

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
