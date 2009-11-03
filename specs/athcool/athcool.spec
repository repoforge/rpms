# $Id$
# Authority: dag

Summary: Enabling/disabling Powersaving mode for AMD processors
Name: athcool
Version: 0.3.11
Release: 1%{?dist}
License: GPL
Group: System Environment/Base
URL: http://members.jcom.home.ne.jp/jacobi/linux/softwares.html

Source:	http://members.jcom.home.ne.jp/jacobi/linux/files/athcool-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Buildrequires: pciutils-devel
Requires: /sbin/chkconfig

ExclusiveArch: %{ix86} x86_64

%description
Athcool is a small utility, enabling/disabling Powersaving mode
for AMD Athlon/Duron processors.

Since enabling Powersaving mode, you can save power consumption,
lower CPU temprature when CPU is idle.

Powersaving works if your kernel support ACPI (APM not work),
because athcool only set/unset "Disconnect enable when STPGNT detected"
bits in the Northbridge of Chipset.
To really save power, someone has to send the STPGNT signal when idle.
This is done by the ACPI subsystem when C2 state entered.

!!!WARNING!!!
Depending on your motherboard and/or hardware components,
enabling powersaving mode may cause that:

 * noisy or distorted sound playback
 * a slowdown in harddisk performance
 * system locks or instability

If you met those problems, you should not use athcool.
Please use athcool AT YOUR OWN RISK.

%prep
%setup

%{__cat} <<'EOF' >athcool.sysv
#!/bin/bash
#
# Init file for Athlon powersaving mode.
#
# Written by Dag Wieers <dag@wieers.com>.
#
# chkconfig: 2345 10 90
# description: Athlon powersaving mode
#
# processname: athcool
# pidfile: %{_localstatedir}/run/athcool

source %{_initrddir}/functions

[ -x %{_sbindir}/athcool ] || exit 1

RETVAL=0
prog="athcool"
desc="Athlon powersaving mode"

start() {
	echo -n $"Starting $desc ($prog): "
	$prog on &>/dev/null
	RETVAL=$?
	if [ $RETVAL -eq 0 ]; then
		success
	else
		failure
	fi
	echo
	[ $RETVAL -eq 0 ] && touch %{_localstatedir}/lock/subsys/$prog
	return $RETVAL
}

stop() {
	echo -n $"Shutting down $desc ($prog): "
	$prog off &>/dev/null
	RETVAL=$?
	if [ $RETVAL -eq 0 ]; then
		success
	else
		failure
	fi
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
	killproc $prog -HUP
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
	$prog stat
	RETVAL=$?
	;;
  *)
	echo $"Usage: $0 {start|stop|restart|reload|condrestart|status}"
	RETVAL=1
esac

exit $RETVAL
EOF

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%{__install} -Dp -m0755 athcool.sysv %{buildroot}%{_initrddir}/athcool

%post
/sbin/chkconfig --add athcool

%preun
if [ $1 -eq 0 ]; then
	/sbin/service athcool stop &>/dev/null || :
	/sbin/chkconfig --del athcool
fi

%postun
/sbin/service athcool condrestart &>/dev/null || :

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING README
%doc %{_mandir}/man8/athcool.8*
%{_initrddir}/athcool
%{_sbindir}/athcool

%changelog
* Wed Apr 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.3.11-1
- Updated to release 0.3.11.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.3.7-1.2
- Rebuild for Fedora Core 5.

* Mon Aug 02 2004 Dag Wieers <dag@wieers.com> - 0.3.7-1
- Initial package. (using DAR)
