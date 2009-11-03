# $Id$

# Authority: dag
# Upstream: Daniel Grobe Sachs <sachs$uiuc,edu>

Summary: IBM Trackpoint scroll-wheel emulation
Name: tp-scroll
Version: 1.0
Release: 1.2%{?dist}
License: BSD
Group: Applications/System
URL: http://rsim.cs.uiuc.edu/~sachs/tp-scroll/

Source: http://rsim.cs.uiuc.edu/~sachs/tp-scroll/%{name}-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


%description
This package provides scroll-wheel emulation for IBM Trackpoints.

%prep
%setup

%{__cat} <<'EOF' >tp-scroll.sysv
#!/bin/bash
#
# Init file for tp-scroll, IBM Trackpoint emulation
#
# Written by Dag Wieers <dag@wieers.com>.
#
# chkconfig: - 90 10
# description: IBM Trackpoint Emulation
#
# processname: tp-scroll
# config: %{_sysconfdir}/sysconfig/tp-scroll
# pidfile: %{_localstatedir}/run/tp-scroll

# source function library
. %{_initrddir}/functions

[ -x %{_sbindir}/tp-scroll ] || exit 1
[ -r %{_sysconfdir}/sysconfig/tp-scroll ] || exit 1

RETVAL=0
prog="tp-scroll"
desc="IBM Trackpoint emulation"

# Read configuration
if [ -r %{_sysconfdir}/sysconfig/tp-scroll ]; then
	. %{_sysconfdir}/sysconfig/tp-scroll
fi

start () {
	echo -n $"Starting $desc ($prog): "
	daemon $prog -i $INPUT_DEVICE -o $OUTPUT_DEVICE -x $XY_ACCEL_EXP -z $Z_ACCEL_EXP -m $Z_ACCEL_MULT &
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

restart(){
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
%{__install} -Dp -m0755 tp-scroll %{buildroot}%{_sbindir}/tp-scroll
%{__install} -Dp -m0755 tp-scroll.sysv %{buildroot}%{_initrddir}/tp-scroll
#%{__install} -Dp -m0644 tp-scroll.rc %{buildroot}%{_initrddir}/tp-scroll
%{__install} -Dp -m0644 tp-scroll.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/tp-scroll

touch %{buildroot}/dev/imouse

%post
[ -e /dev/imouse ] || mkfifo /dev/imouse
/sbin/chkconfig --add tp-scroll

%preun
if [ $1 -eq 0 ]; then
	/sbin/chkconfig --del tp-scroll
fi

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%{_sbindir}/*
%{_sysconfdir}/sysconfig/*
%{_initrddir}/*
%ghost /dev/imouse

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.0-1.2
- Rebuild for Fedora Core 5.

* Tue Jun 03 2003 Dag Wieers <dag@wieers.com> - 1.0-1
- Embedded my own sysv script.

* Fri Apr 11 2003 Dag Wieers <dag@wieers.com> - 1.0-0
- Initial package. (using DAR)
