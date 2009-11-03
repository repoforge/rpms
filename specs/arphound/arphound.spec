# $Id$
# Authority: dag
# Upstream: Matthieu Nottale <matthieu@nottale.net>


%{!?dtag:%define _with_libpcapdevel 1}
%{?el5:%define _with_libpcapdevel 1}
%{?fc6:%define _with_libpcapdevel 1}

Summary: ARP traffic monitoring/logging tool
Name: arphound
Version: 1.3.2
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://www.nottale.net/index.php?project=arphound

Source: http://www.nottale.net/arphound/download/arphound-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc-c++, libpcap
%{?_with_libpcapdevel:BuildRequires:libpcap-devel}

%description
Arphound is a tool that listens to all traffic on an ethernet network
interface. It reports IP/MAC address pairs as well as events such as
IP conflicts, IP changes, IP addresses with no RDNS, various ARP
spoofing, and packets not using the expected gateway. Reporting is
done to stdout, to a specified file, or to syslog in a format that
can be easily parsed by scripts.

%prep
%setup

%{__cat} <<'EOF' >arphound.sysv
#!/bin/bash
#
# Init file for Arphound ARP monitor
#
# Written by Dag Wieers <dag@wieers.com>.
#
# chkconfig: - 54 46
# description: Arphound ARP monitor
#
# processname: arphound
# config: %{_sysconfdir}/arphound.conf
# pidfile: %{_localstatedir}/run/arphound

source %{_initrddir}/functions

[ -x %{_sbindir}/arphound ] || exit 1
[ -r %{_sysconfdir}/arphound.conf ] || exit 1

RETVAL=0
prog="arphound"
desc="ARP monitor"

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
EOF

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 arphound %{buildroot}%{_sbindir}/arphound
%{__install} -Dp -m0644 docs/arphound.8 %{buildroot}%{_mandir}/man8/arphound.8
%{__install} -Dp -m0644 docs/arphound.conf.5 %{buildroot}%{_mandir}/man5/arphound.conf.5
%{__install} -Dp -m0644 arphound.conf.sample %{buildroot}%{_sysconfdir}/arphound.conf
%{__install} -Dp -m0755 arphound.sysv %{buildroot}%{_initrddir}/arphound

%post
/sbin/chkconfig --add arphound

%preun
if [ $1 -eq 0 ]; then
	/sbin/service arphound stop &>/dev/null || :
	/sbin/chkconfig --del arphound
fi

%postun
/sbin/service arphound condrestart &>/dev/null || :

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGELOG* COPYING INSTALL README TODO arphound.conf.sample
%doc %{_mandir}/man?/arphound.*
%config(noreplace) %{_sysconfdir}/arphound.conf
%config %{_initrddir}/arphound
%{_sbindir}/arphound

%changelog
* Fri Nov 24 2006 Dries Verachtert <dries@ulyssis.org> - 1.3.2-1
- Updated to release 1.3.2.

* Wed Apr 19 2006 Dries Verachtert <dries@ulyssis.org> - 1.3.1-1
- Updated to release 1.3.1.

* Thu Jul 22 2004 Dag Wieers <dag@wieers.com> - 1.3-1
- Initial package. (using DAR)
