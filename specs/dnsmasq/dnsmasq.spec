# $Id$

# Authority: dag
# Upstream: Simon Kelley <simon@thekelleys.org.uk>

# Tag: test

Summary: Lightweight caching nameserver
Name: dnsmasq
Version: 2.6
Release: 0.pre1
License: GPL
Group: System Environment/Daemons
URL: http://www.thekelleys.org.uk/dnsmasq/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.thekelleys.org.uk/dnsmasq/dnsmasq-%{version}test1.tar.gz
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

%{__cat} <<'EOF' >%{name}.sysv
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

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_localstatedir}/lib/misc/
%{__install} -D -m0755 src/dnsmasq %{buildroot}%{_sbindir}/dnsmasq
%{__install} -D -m0644 dnsmasq.conf.example %{buildroot}%{_sysconfdir}/dnsmasq.conf
%{__install} -D -m0755 dnsmasq.sysv %{buildroot}%{_initrddir}/dnsmasq
%{__install} -D -m0644 dnsmasq.8 %{buildroot}%{_mandir}/man8/

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
%doc CHANGELOG COPYING FAQ doc.html setup.html UPGRADING_to_2.0 dnsmasq.conf.example
%doc %{_mandir}/man?/*
%config(noreplace) %{_sysconfdir}/*.conf
%config %{_initrddir}/*
%{_sbindir}/*
%{_localstatedir}/lib/misc/

%changelog
* Mon Mar 22 2004 Dag Wieers <dag@wieers.com> - 2.6-0.pre1
- Updated to release 2.6test1.

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
