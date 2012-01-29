# $Id$
# Authority: dag
# Upstream: Simon Kelley <simon$thekelleys,org,uk>

### EL6 ships with dnsmasq-2.48-4.el6
%{?el6:# Tag: rfx}
### EL5 ships with dnsmasq-2.45-1.1.el5_3
%{?el5:# Tag: rfx}

Summary: Lightweight caching nameserver with integrated DHCP server
Name: dnsmasq
Version: 2.59
Release: 1%{?dist}
License: GPL
Group: System Environment/Daemons
URL: http://www.thekelleys.org.uk/dnsmasq/

Source: http://www.thekelleys.org.uk/dnsmasq/dnsmasq-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Requires: chkconfig

%description
Dnsmasq is lightweight, easy to configure DNS forwarder and DHCP server.
It is designed to provide DNS (domain name) and, optionally, DHCP
services to a small network. It can serve the names of local machines
which are not in the global DNS. The DHCP server integrates with the DNS
server and allows machines with DHCP-allocated address to appear in the
DNS with names configured either in each host or in a central
configuration file. Dnsmasq supports static and dynamic DHCP leases and
BOOTP for network booting of diskless machines.

%prep
%setup

%{__cat} <<'EOF' >dnsmasq.sysv
#!/bin/bash
#
# Startup script for the DNS caching server
#
# Written by Dag Wieers <dag@wieers.com>
#
# chkconfig: - 55 45
# description: This script starts your DNS caching server
#
# processname: dnsmasq
# config: %{_sysconfdir}/dnsmasq.conf
# pidfile: %{_localstatedir}/run/dnsmasq.pid

source %{_initrddir}/functions
source %{_sysconfdir}/sysconfig/network

# Check that networking is up.
[ ${NETWORKING} = "no" ] && exit 0

[ -x %{_sbindir}/dnsmasq ] || exit 1
[ -r %{_sysconfdir}/dnsmasq.conf ] || exit 1

RETVAL=0
prog="dnsmasq"
desc="Lightweight caching nameserver"

start() {
    echo -n $"Starting $desc ($prog): "
    daemon $prog
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

reload() {
    echo -n $"Reloading $desc ($prog): "
    killproc $prog -HUP
    RETVAL=$?
    echo
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
    echo $"Usage $0 {start|stop|restart|reload|condrestart|status}"
    RETVAL=1
esac

exit $RETVAL
EOF

%build
%{__make} %{?_smp_mflags} \
    CFLAGS="%{optflags}"
#   CFLAGS="%{optflags} -DHAVE_DBUS -I%{_libdir}/dbus-1.0/include/ -I%{_includedir}/dbus-1.0/"

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}" PREFIX="%{_prefix}"
%{__install} -Dp -m0644 dnsmasq.conf.example %{buildroot}%{_sysconfdir}/dnsmasq.conf
%{__install} -Dp -m0755 dnsmasq.sysv %{buildroot}%{_initrddir}/dnsmasq

%{__install} -d -m0755 %{buildroot}%{_localstatedir}/lib/misc/

### Disable contrib stuff from being considered for dependencies
find contrib -type f -exec chmod 0644 {} \;

%post
/sbin/chkconfig --add dnsmasq

%preun
if [ $1 -eq 0 ]; then
    /sbin/service dnsmasq stop &>/dev/null || :
    /sbin/chkconfig --del dnsmasq
fi

%postun
/sbin/service dnsmasq condrestart &>/dev/null || :

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGELOG contrib/* COPYING dnsmasq.conf.example FAQ *.html dbus/
%doc %{_mandir}/man8/dnsmasq.8*
%config(noreplace) %{_sysconfdir}/dnsmasq.conf
%config %{_initrddir}/dnsmasq
%{_localstatedir}/lib/misc/
%{_sbindir}/dnsmasq

%changelog
* Mon Oct 24 2011 Dag Wieers <dag@wieers.com> - 2.59-1
- Updated to release 2.59.

* Mon Sep 05 2011 Dag Wieers <dag@wieers.com> - 2.58-1
- Updated to release 2.58.

* Sat Feb 19 2011 Dag Wieers <dag@wieers.com> - 2.57-1
- Updated to release 2.57.

* Tue Jun 08 2010 Dag Wieers <dag@wieers.com> - 2.55-1
- Updated to release 2.55.

* Fri Jun 04 2010 Dag Wieers <dag@wieers.com> - 2.53-1
- Updated to release 2.53.

* Thu Oct 22 2009 Dag Wieers <dag@wieers.com> - 2.51-1
- Updated to release 2.51.

* Thu Sep 10 2009 Dag Wieers <dag@wieers.com> - 2.50-1
- Updated to release 2.50.

* Thu Jun 18 2009 Dag Wieers <dag@wieers.com> - 2.49-1
- Updated to release 2.49.

* Sat Jun 06 2009 Dag Wieers <dag@wieers.com> - 2.48-1
- Updated to release 2.48.

* Sun Feb 08 2009 Dag Wieers <dag@wieers.com> - 2.47-1
- Updated to release 2.47.

* Mon Nov 17 2008 Dag Wieers <dag@wieers.com> - 2.46-1
- Updated to release 2.46.

* Sat Jul 26 2008 Dag Wieers <dag@wieers.com> - 2.45-1
- Updated to release 2.45.

* Sat Jul 12 2008 Dag Wieers <dag@wieers.com> - 2.43-1
- Updated to release 2.43.

* Tue Jun 03 2008 Dag Wieers <dag@wieers.com> - 2.42-1
- Updated to release 2.42.

* Wed Feb 13 2008 Dag Wieers <dag@wieers.com> - 2.41-1
- Updated to release 2.41.

* Thu Aug 30 2007 Dag Wieers <dag@wieers.com> - 2.40-1
- Updated to release 2.40.

* Mon Apr 30 2007 Dag Wieers <dag@wieers.com> - 2.39-1
- Updated to release 2.39.

* Tue Feb 13 2007 Dag Wieers <dag@wieers.com> - 2.38-1
- Updated to release 2.38.

* Mon Jan 22 2007 Dag Wieers <dag@wieers.com> - 2.37-1
- Updated to release 2.37.

* Mon Jan 22 2007 Dag Wieers <dag@wieers.com> - 2.36-1
- Updated to release 2.36.

* Sun Oct 29 2006 Dag Wieers <dag@wieers.com> - 2.35-1
- Updated to release 2.35.

* Mon Oct 16 2006 Dag Wieers <dag@wieers.com> - 2.34-1
- Updated to release 2.34.

* Sun Aug 06 2006 Dag Wieers <dag@wieers.com> - 2.33-1
- Updated to release 2.33.

* Sat Jun 10 2006 Dag Wieers <dag@wieers.com> - 2.32-1
- Updated to release 2.32.

* Mon May 08 2006 Dag Wieers <dag@wieers.com> - 2.31-1
- Updated to release 2.31.

* Mon Apr 24 2006 Dag Wieers <dag@wieers.com> - 2.30-1
- Updated to release 2.30.
- Disabled dbus support because of compile issues.

* Thu Jan 26 2006 Dag Wieers <dag@wieers.com> - 2.27-1
- Updated to release 2.27.

* Thu Jan 26 2006 Dag Wieers <dag@wieers.com> - 2.26-2
- Enable dbus support.

* Thu Jan 26 2006 Dag Wieers <dag@wieers.com> - 2.26-1
- Updated to release 2.26.

* Mon Jan 16 2006 Dag Wieers <dag@wieers.com> - 2.25-1
- Updated to release 2.25.

* Sun Nov 27 2005 Dag Wieers <dag@wieers.com> - 2.24-1
- Updated to release 2.24.

* Sat Sep 03 2005 Dag Wieers <dag@wieers.com> - 2.23-1
- Updated to release 2.23.

* Fri Apr 01 2005 Dag Wieers <dag@wieers.com> - 2.22-1
- Updated to release 2.22.

* Thu Mar 24 2005 Dag Wieers <dag@wieers.com> - 2.21-1
- Updated to release 2.21.

* Mon Jan 24 2005 Dag Wieers <dag@wieers.com> - 2.20-1
- Updated to release 2.20.

* Tue Dec 21 2004 Dag Wieers <dag@wieers.com> - 2.19-1
- Updated to release 2.19.

* Tue Nov 23 2004 Dag Wieers <dag@wieers.com> - 2.18-1
- Updated to release 2.18.

* Sun Nov 14 2004 Dag Wieers <dag@wieers.com> - 2.17-1
- Updated to release 2.17.

* Mon Nov 01 2004 Dag Wieers <dag@wieers.com> - 2.16-1
- Updated to release 2.16.

* Wed Sep 22 2004 Dag Wieers <dag@wieers.com> - 2.15-1
- Updated to release 2.15.

* Sat Aug 14 2004 Dag Wieers <dag@wieers.com> - 2.13-1
- Updated to release 2.13.

* Thu Aug 12 2004 Dag Wieers <dag@wieers.com> - 2.12-1
- Updated to release 2.12.

* Mon Aug 02 2004 Dag Wieers <dag@wieers.com> - 2.11-1
- Updated to release 2.11.

* Fri Jul 30 2004 Dag Wieers <dag@wieers.com> - 2.10-1
- Updated to release 2.10.

* Thu Jun 24 2004 Dag Wieers <dag@wieers.com> - 2.9-1
- Updated to release 2.9.

* Fri May 14 2004 Dag Wieers <dag@wieers.com> - 2.8-1
- Updated to release 2.8.

* Sat Apr 24 2004 Dag Wieers <dag@wieers.com> - 2.7-1
- Updated to release 2.7.

* Fri Apr 09 2004 Dag Wieers <dag@wieers.com> - 2.6-2
- Use 2.6 tarball, not 2.6test1. (Bert de Bruijn)

* Sun Apr 04 2004 Dag Wieers <dag@wieers.com> - 2.6-1
- Updated to release 2.6.

* Tue Mar 16 2004 Dag Wieers <dag@wieers.com> - 2.5-1
- Updated to release 2.5.

* Fri Mar 12 2004 Dag Wieers <dag@wieers.com> - 2.4-1
- Updated to release 2.4.

* Thu Mar 11 2004 Dag Wieers <dag@wieers.com> - 2.3-0
- Updated to release 2.3.

* Sat Jan 31 2004 Dag Wieers <dag@wieers.com> - 2.2-0
- Updated to release 2.2.

* Fri Jan 30 2004 Dag Wieers <dag@wieers.com> - 2.1-1
- Updated to release 2.1.

* Tue Jan 27 2004 Dag Wieers <dag@wieers.com> - 2.1-0.pre
- Updated to release 2.1-pre.

* Fri Jan 23 2004 Dag Wieers <dag@wieers.com> - 2.0-0
- Updated to release 2.0.

* Wed Dec 03 2003 Dag Wieers <dag@wieers.com> - 1.18-1
- Fixed the start priorities to 55/45. (C.Lee Taylor)

* Mon Nov 17 2003 Dag Wieers <dag@wieers.com> - 1.18-0
- Updated to release 1.18.

* Sun Oct 12 2003 Dag Wieers <dag@wieers.com> - 1.17-0
- Updated to release 1.17.
- Removed sysconfig, use dnsmasq.conf instead.
- Added reload to sysv service.

* Sun Sep 21 2003 Dag Wieers <dag@wieers.com> - 1.16-0
- Updated to release 1.16.

* Wed Sep 17 2003 Dag Wieers <dag@wieers.com> - 1.15-0
- Updated to release 1.15.

* Mon Sep 15 2003 Dag Wieers <dag@wieers.com> - 1.14-0
- Initial package. (using DAR)
