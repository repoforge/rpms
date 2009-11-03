# $Id$
# Authority: dag
# Upstream: Ricardo Galli <gallir$uib,es>

Summary: Control the speed and power consumption of your computer
Name: cpudyn
Version: 1.0.1
Release: 1.2%{?dist}
License: GPL
Group: System Environment/Base
URL: http://mnm.uib.es/~gallir/cpudyn/

Source: http://mnm.uib.es/~gallir/cpudyn/download/cpudyn-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
cpudyn controls the speed in Intel SpeedStep, Pentium 4 Mobile and
PowerPC machines with the cpufreq compiled in the kernel (check if
/proc/cpufreq exist).

Tested with 2.4, Pentium 3 Speedstep Laptop (Dell Latitude),
Pentium 4 Mobile Laptop (Dell Inspiron), Apple iBook, IBM Thinkpad.

%prep
%setup -n %{name}

### FIXME: Make Makefile use autotool directory standard. (Please fix upstream)
%{__perl} -pi.orig -e '
		s| /usr/sbin| \$(sbindir)|g;
		s| /etc/init.d| \$(sysconfdir)/rc.d/init.d|g;
		s| /etc/sysconfig| \$(sysconfdir)/sysconfig|g;
		s| /usr/share/man| \$(mandir)|g;
	' Makefile

%{__cat} <<EOF >cpudynd.sysconfig
### See manual cpudynd(8) for more information about the different options

#OPTIONS="-i 1 -p 0.5 0.90 -t 120 -h /dev/hda"
EOF

%{__cat} <<'EOF' >cpudynd.sysv
#!/bin/bash
#
# Init file for cpudyn daemon.
#
# Written by Dag Wieers <dag@wieers.com>.
#
# chkconfig: 2345 05 95
# description: CPU frequency and power consumption control daemon.
#
# processname: cpudynd
# config: %{_sysconfdir}/sysconfig/cpudynd
# pidfile: %{_localstatedir}/run/cpudynd.pid

source %{_initrddir}/functions

### Default variables
SYSCONFIG="%{_sysconfdir}/sysconfig/cpudynd"
OPTIONS="-i 1 -p 0.5 0.90"

### Read configuration
[ -x %{_sbindir}/cpudynd ] || exit 1
[ -r "$SYSCONFIG" ] && source "$SYSCONFIG"

RETVAL=0
prog="cpudynd"
desc="CPU power consumption control"

start() {
	echo -n $"Starting $desc ($prog): "
	daemon $prog -d $OPTIONS
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
%{__make} %{?_smp_mflags} \
	CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}

### FIXME: Disables make install as it starts services
#makeinstall

%{__install} -Dp -m0755 cpudynd %{buildroot}%{_sbindir}/cpudynd
%{__install} -Dp -m0644 cpudynd.8.gz %{buildroot}%{_mandir}/man8/cpudynd.8.gz

%{__install} -Dp -m0755 cpudynd.sysv %{buildroot}%{_initrddir}/cpudynd
%{__install} -Dp -m0644 cpudynd.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/cpudynd

%post
/sbin/chkconfig --add cpudynd

%preun
if [ $1 -eq 0 ]; then
        /sbin/service cpudynd stop &>/dev/null || :
        /sbin/chkconfig --del cpudynd
fi

%postun
/sbin/service cpudynd condrestart &>/dev/null || :

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc changelog COPYING faq.html README
%doc %{_mandir}/man?/*
%config(noreplace) %{_sysconfdir}/sysconfig/*
%config %{_initrddir}/*
%{_sbindir}/*

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.0.1-1.2
- Rebuild for Fedora Core 5.

* Sun Mar 20 2005 Dag Wieers <dag@wieers.com> - 1.0.1-1
- Updated to release 1.0.1.

* Mon May 31 2004 Dag Wieers <dag@wieers.com> - 1.0-1
- Updated to release 1.0.

* Mon Feb 16 2004 Dag Wieers <dag@wieers.com> - 0.99.0-0
- Updated to release 0.99.0.

* Thu Jan 15 2004 Dag Wieers <dag@wieers.com> - 0.6.1-0
- Updated to release 0.6.1.

* Sun Jan 11 2004 Dag Wieers <dag@wieers.com> - 0.6.0-0
- Updated to release 0.6.0.

* Mon Dec 29 2003 Dag Wieers <dag@wieers.com> - 0.5.0-0
- Updated to release 0.5.0.

* Sun Oct 19 2003 Dag Wieers <dag@wieers.com> - 0.4.7-0
- Updated to release 0.4.7.

* Fri Oct 10 2003 Dag Wieers <dag@wieers.com> - 0.4.6-0
- Updated to release 0.4.6.

* Sun Sep 28 2003 Dag Wieers <dag@wieers.com> - 0.4.5-0
- Updated to release 0.4.5.

* Thu Aug 28 2003 Dag Wieers <dag@wieers.com> - 0.4.4-0
- Updated to release 0.4.4.

* Fri Aug 01 2003 Dag Wieers <dag@wieers.com> - 0.4.2-0
- Updated to release 0.4.2.

* Thu Jul 17 2003 Dag Wieers <dag@wieers.com> - 0.4.0-0
- Initial package. (using DAR)
