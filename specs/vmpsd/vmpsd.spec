# $Id$
# Authority: dag
# Upstream: <dori.seliskar@select-tech.si>

Summary: VLAN Management Policy Server
Name: vmpsd
Version: 1.3
Release: 1.2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://vmps.sourceforge.net/

Source: http://dl.sf.net/vmps/vmpsd-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
VMPS (VLAN Management Policy Server) is a way of assigning switch ports
to specific VLANs based on MAC address of connecting device. OpenVMPS
is a GPL implementation of VMPS.

%prep
%setup -n %{name}

%{__cat} <<'EOF' >vmpsd.sysconfig
### See man vmpsd(1) for details.
#
#CONFIGFILE="/etc/vmps.db"
#OPTIONS="-a 10.0.0.1 -l 0xf07"
#USER=nobody
EOF

%{__cat} <<'EOF' >vmpsd.sysv
#!/bin/bash
#
# Init script for VLAN Management Policy Server.
#
# Written by Dag Wieers <dag@wieers.com>.
#
# chkconfig: - 79 31
# description: VLAN Management Policy Server.
#
# processname: vmpsd
# config: %{_sysconfdir}/vmps.db
# pidfile: %{_localstatedir}/run/vmpsd.pid

source %{_initrddir}/functions

[ -x %{_bindir}/vmpsd ] || exit 1

### Default variables
CONFIGFILE="/etc/vmps.db"
OPTIONS=""
SYSCONFIG="%{_sysconfdir}/sysconfig/vmpsd"
USER=nobody

### Read configuration
[ -r "$SYSCONFIG" ] && source "$SYSCONFIG"

[ -r "$CONFIGFILE" ] || exit 1

RETVAL=0
prog="vmpsd"
desc="VLAN Management Policy Server"

start() {
	echo -n $"Starting $desc ($prog): "
	daemon --user $USER $prog -f $CONFIGFILE
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
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%{__install} -Dp -m0755 vmpsd.sysv %{buildroot}%{_initrddir}/vmpsd
%{__install} -Dp -m0644 vmpsd.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/vmpsd

#find . -name CVS -type d -exec rm -rf {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING* INSTALL NEWS README vlan.db
%doc contrib/ doc/ tools/
%doc %{_mandir}/man1/vmpsd.1*
%config(noreplace) %{_sysconfdir}/vlan.db
%config(noreplace) %{_sysconfdir}/sysconfig/vmpsd
%config %{_initrddir}/vmpsd
%{_bindir}/vmpsd

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.3-1.2
- Rebuild for Fedora Core 5.

* Mon Nov 15 2004 Dag Wieers <dag@wieers.com> - 1.3-1
- Updated to release 1.3.

* Tue Aug 24 2004 Dag Wieers <dag@wieers.com> - 1.2-1
- Initial package. (using DAR)
