# $Id$
# Authority: dag
# Upstream: <monitgroup$tildeslash,com>

%define logmsg logger -t %{name}/rpm

Summary: Process monitor and restart utility
Name: monit
Version: 4.8.1
Release: 3
License: GPL
Group: Applications/Internet
URL: http://www.tildeslash.com/monit/

Source: http://www.tildeslash.com/monit/dist/monit-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: flex, openssl-devel, byacc

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
# config: %{_sysconfdir}/monit.conf
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

%{__perl} -pi.orig -e 's|\bmonitrc\b|monit.conf|' monitor.h

%build
%configure \
	--with-ssl-lib-dir="%{_libdir}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall \
	BINDIR="%{buildroot}%{_bindir}" \
	MANDIR="%{buildroot}%{_mandir}/man1/"

%{__install} -Dp -m0755 monit.sysv %{buildroot}%{_initrddir}/monit
%{__install} -Dp -m0600 monitrc %{buildroot}%{_sysconfdir}/monit.conf

%{__install} -d -m0755 %{buildroot}%{_sysconfdir}/monit.d/
%{__install} -d -m0755 %{buildroot}%{_localstatedir}/lib/monit/

%pre
if ! /usr/bin/id monit &>/dev/null; then
	/usr/sbin/useradd -M -r -d %{_localstatedir}/lib/monit -s /bin/sh -c "monit daemon" monit || \
                %logmsg "Unexpected error adding user \"monit\". Aborting installation."
fi

%post
/sbin/chkconfig --add monit

%preun
if [ $1 -eq 0 ]; then
	service monit start &>/dev/null || :
	/sbin/chkconfig --del monit
fi

%postun
/sbin/service monit condrestart &>/dev/null || :
if [ $1 -eq 0 ]; then
	/usr/sbin/userdel monit || %logmsg "User \"monit\" could not be deleted."
fi

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES.txt CONTRIBUTORS COPYING FAQ.txt LICENSE PACKAGES README* STATUS UPGRADE.txt
%doc %{_mandir}/man1/monit.1*
%config(noreplace) %{_sysconfdir}/monit.conf
%config %{_initrddir}/monit
%config %{_sysconfdir}/monit.d/
%{_bindir}/monit

%defattr(-, monit, monit, 0755)
%{_localstatedir}/lib/monit/

%changelog
* Mon May 29 2006 Dag Wieers <dag@wieers.com> - 4.8.1-3
- Fixed reference to monitrc from monitor.h. (Tim Jackson)

* Thu May 18 2006 Dag Wieers <dag@wieers.com> - 4.8.1-2
- Fixed the nagios references in the monit user creation. (Tim Jackson)
- Removed the -o option to useradd. (Tim Jackson)

* Wed May 17 2006 Dag Wieers <dag@wieers.com> - 4.8.1-1
- Updated to release 4.8.1.
- Added %{_sysconfdir}/monit.d/ and %{_localstatedir}/lib/monit/. (Michael C. Hoffman)
- Creation/removal of user monit. (Michael C. Hoffman)

* Mon May 08 2006 Dag Wieers <dag@wieers.com> - 4.8-1
- Updated to release 4.8.

* Thu Jan 12 2006 Dag Wieers <dag@wieers.com> - 4.7-1
- Updated to release 4.7.

* Fri Sep 24 2004 Dag Wieers <dag@wieers.com> - 4.4-1
- Updated to release 4.4.

* Thu May 13 2004 Dag Wieers <dag@wieers.com> - 4.3-1
- Updated to release 4.3.

* Mon Apr 05 2004 Dag Wieers <dag@wieers.com> - 4.2.1-1
- Updated to release 4.2.1.

* Fri Mar 26 2004 Dag Wieers <dag@wieers.com> - 4.2.0-0
- Updated to release 4.2.0.

* Sun Nov 23 2003 Dag Wieers <dag@wieers.com> - 4.1.1-0
- Updated to release 4.1.1.

* Mon Oct 13 2003 Dag Wieers <dag@wieers.com> - 4.0-0
- Initial package. (using DAR)
