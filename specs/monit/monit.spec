# $Id$
# Authority: dag
# Upstream: <monitgroup@tildeslash.com>

Summary: Process monitor and restart utility
Name: monit
Version: 4.2.1
Release: 1
License: GPL
Group: Applications/Internet
URL: http://www.tildeslash.com/monit/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.tildeslash.com/monit/dist/monit-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Monit is an utility for monitoring daemons or similar programs running on
a Unix system. It will start specified programs if they are not running
and restart programs not responding. 

%prep
%setup

%{__cat} <<'EOF' >monit.sysv
#!/bin/bash
#
# Init file for Monit process monitor.
#
# Written by Dag Wieers <dag@wieers.com>.
#
# chkconfig: - 98 02
# description: Monit Process Monitor
#
# processname: monit
# config: %{_sysconfdir}/monitrc
# pidfile: %{_localstatedir}/run/monit

source %{_initrddir}/functions

### Default variables
CONFIG="%{_sysconfdir}/monit.conf"

[ -x %{_bindir}/monit ] || exit 1
[ -r "$CONFIG" ] || exit 1

RETVAL=0
prog="monit"
desc="Process Monitor"

start() {
	echo -n $"Starting $desc ($prog): "
	daemon $prog -c "$CONFIG"
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
	monit -c "$CONFIG" reload
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
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall \
	BINDIR="%{buildroot}%{_bindir}" \
	MANDIR="%{buildroot}%{_mandir}/man1/"

%{__install} -D -m0755 monit.sysv %{buildroot}%{_initrddir}/monit
%{__install} -D -m0600 monitrc %{buildroot}%{_sysconfdir}/monit.conf

%post
/sbin/chkconfig --add monit

%preun
if [ $1 -eq 0 ]; then
	service monit start &>/dev/null || :
	/sbin/chkconfig --del monit
fi

%postun
/sbin/service monit condrestart &>/dev/null || :

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES.txt CONTRIBUTORS COPYING FAQ.txt LICENSE README README.SSL STATUS
%doc %{_mandir}/man?/*
%config(noreplace) %{_sysconfdir}/monit.conf
%config %{_initrddir}/*
%{_bindir}/*

%changelog
* Mon Apr 05 2004 Dag Wieers <dag@wieers.com> - 4.2.1-1
- Updated to release 4.2.1.

* Fri Mar 26 2004 Dag Wieers <dag@wieers.com> - 4.2.0-0
- Updated to release 4.2.0.

* Sun Nov 23 2003 Dag Wieers <dag@wieers.com> - 4.1.1-0
- Updated to release 4.1.1.

* Mon Oct 13 2003 Dag Wieers <dag@wieers.com> - 4.0-0
- Initial package. (using DAR)
