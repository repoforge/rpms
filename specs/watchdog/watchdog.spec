# $Id$
# Authority: dag

%{?dtag: %{expand: %%define %dtag 1}}

Summary: Software watchdog
Name: watchdog
Version: 5.3.1
Release: 1%{?dist}
License: GPL
Group: System Environment/Daemons
#URL: http://oss.digirati.com.br/watchcatd/watchdog.html
URL: http://sourceforge.net/projects/watchdog/

#Source: http://ftp.debian.org/debian/pool/main/w/watchdog/watchdog_%{version}.orig.tar.gz
#Source: http://www.ibiblio.org/pub/Linux/system/daemons/watchdog/watchdog-%{version}.tar.gz
Source: http://dl.sf.net/watchdog/watchdog_%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
watchdog is a software watchdog.

%prep
%setup

### FIXME: Make it compile on RH80, RH9, RHEL3 and RHFC1. (Fix upstream please)
%{?fc1:%{__perl} -pi.orig -e 's| __GNUC__ == 2 && __GNUC_MINOR__ >= 5| __GNUC__ >= 2|' include/sundries.h}
%{?el3:%{__perl} -pi.orig -e 's| __GNUC__ == 2 && __GNUC_MINOR__ >= 5| __GNUC__ >= 2|' include/sundries.h}
%{?rh9:%{__perl} -pi.orig -e 's| __GNUC__ == 2 && __GNUC_MINOR__ >= 5| __GNUC__ >= 2|' include/sundries.h}
%{?rh8:%{__perl} -pi.orig -e 's| __GNUC__ == 2 && __GNUC_MINOR__ >= 5| __GNUC__ >= 2|' include/sundries.h}

### FIXME: Fix the errno problem on RH9. (Fix upsteam please)
%{?rh9: %{__perl} -pi.orig -e 's|^(#include <linux/unistd.h>)$|$1\n#include <errno.h>|' src/quotactl.c}

%{__cat} <<EOF >%{name}.sysconfig
### Controls the behaviour of the watchdog
###
### -v		verbose mode
### -s		sync filesystem
### -b		softboot
### -f		force internal defaults
### -q		test-run, no action taken

#OPTIONS="-v"
EOF

%{__cat} <<'EOF' >%{name}.sysv
#!/bin/bash
#
# Init file for Software Watchdog daemon.
#
# Written by Dag Wieers <dag@wieers.com>.
#
# chkconfig: 2345 02 98
# description: Software Watchdog Daemon
#
# processname: watchdog
# config: %{_sysconfdir}/watchdog.conf
# pidfile: %{_localstatedir}/run/watchdog

source %{_initrddir}/functions

[ -x %{_sbindir}/watchdog ] || exit 1
[ -r %{_sysconfdir}/watchdog.conf ] || exit 1

### Default variables
SYSCONFIG="%{_sysconfdir}/sysconfig/watchdog"
OPTIONS="-v"

### Read configuration
[ -r "$SYSCONFIG" ] && source "$SYSCONFIG"

RETVAL=0
prog="watchdog"
desc="Software Watchdog daemon"

start() {
	echo -n $"Starting $desc ($prog): "

	### For some people it is a module, for others not. We force it because
	### for kernels < 2.1, we need kerneld, and it's not running yet.
	modprobe softdog &>/dev/null
	modprobe pcwd &>/dev/null
	modprobe acquirewdt &>/dev/null

	daemon $prog $OPTIONS
	RETVAL=$?
	echo
	[ $RETVAL -eq 0 ] && touch %{_localstatedir}/lock/subsys/$prog
	return $RETVAL
}

stop() {
	echo -n $"Shutting down $desc ($prog): "
	killproc $prog

	### If you compiled your kernel with CONFIG_WATCHDOG_NOWAYOUT, you may
	### not want  to remove the module  as sometimes /etc/rc.d/init.d/halt
	### will hang on umounting some remote nfs partition or for some other
	### reason, and you may then want the kernel to reboot by itself.
	### However, this means that if you stop watchdog, your system has one
	### minute to reboot cleanly, or it will be rebooted by the kernel. If
	### this behavior  isn't what you  want, just uncomment  the following
	### lines
	#rmmod softdog &>/dev/null
	#rmmod pcwd &>/dev/null
	#rmmod acquirewdt &>/dev/null

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
	;;
esac

exit $RETVAL
EOF

%build
%configure

### FIXME: Fix to use standard autotool directories. (Fix upstream please)
%{__perl} -pi.orig -e 's| /etc/| \$(sysconfdir)/|' Makefile

%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_sysconfdir}
%makeinstall
%{__install} -Dp -m0644 %{name}.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/watchdog
%{__install} -Dp -m0755 %{name}.sysv %{buildroot}%{_initrddir}/watchdog

%post
/sbin/chkconfig --add watchdog

%preun
if [ $1 -eq 0 ]; then
        /sbin/service watchdog stop &>/dev/null || :
        /sbin/chkconfig --del watchdog
fi

%postun
/sbin/service watchdog condrestart &>/dev/null || :

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING examples/ IAFA-PACKAGE NEWS README TODO watchdog.lsm
%doc %{_mandir}/man5/watchdog.conf.5*
%doc %{_mandir}/man8/watchdog.8*
%config(noreplace) %{_sysconfdir}/watchdog.conf
%config(noreplace) %{_sysconfdir}/sysconfig/watchdog
%config %{_initrddir}/watchdog
%{_sbindir}/watchdog
%{_sbindir}/wd_keepalive

%changelog
* Thu Feb 22 2007 Dag Wieers <dag@wieers.com> - 5.3.1-1
- Updated to release 5.3.1.

* Mon Apr 24 2006 Dag Wieers <dag@wieers.com> - 5.2.5-1
- Updated to release 5.2.5.

* Mon Mar 29 2004 Dag Wieers <dag@wieers.com> - 5.2-7
- Fixed missing statement in %preun. (Matthew Lenz)

* Wed Jan 28 2004 Dag Wieers <dag@wieers.com> - 5.2-6
- Register sysv script with chkconfig.

* Tue Sep 09 2003 Dag Wieers <dag@wieers.com> - 5.2-5
- Embedded sysconfig and sysv script.
- Fixes for building on RH9.

* Tue Dec 31 2002 Dag Wieers <dag@wieers.com> - 5.2-4
- Init script should be a config file.

* Sun Aug 26 2001 Dag Wieers <dag@wieers.com> - 5.2-0
- Initial package.
