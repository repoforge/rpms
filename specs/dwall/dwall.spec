# $Id$
# Authority: dag
# Upstream: Dag Wieers <dag$wieers,com>

Summary: All-purpose iptables firewall generator
Name: dwall
Version: 0.5.3
Release: 1.2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://dag.wieers.com/home-made/dwall/

Source: http://dag.wieers.com/home-made/dwall/dwall-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: iptables
Requires: iptables, iproute, bash
Obsoletes: quemo

%description
Dwall is a versatile firewall frontend to configure and manage iptables
firewalls. It generates an iptables firewall based on simple config
files. It allows you to give a simple overview of your whole network.

%prep
%setup

%{__cat} <<'EOF' >dwall.sysv
#!/bin/bash
#
# Init file for Dwall firewall
#
# Written by Dag Wieers <dag@wieers.com>.
#
# chkconfig: - 09 91
# description: Dwall firewall
#
# processname: dwall
# config: %{_sysconfdir}/dwall/dwall.conf
# pidfile: %{_localstatedir}/run/dwall

# source function library
source %{_initrddir}/functions

# Source networking configuration.
source %{_sysconfdir}/sysconfig/network

# Check that networking is up.
[ "${NETWORKING}" != "no" ] || exit 0

### Check if Dwall is installed correctly
[ -x "%{_bindir}/dwall" ] || exit 1
[ -r "%{_sysconfdir}/dwall/dwall.conf" ] || exit 1

source %{_sysconfdir}/dwall/dwall.conf

### Check if Dwall firewall exists
[ -x "$FIREWALL" ] || exit 0

### Check if iptables is installed
[ -x /sbin/iptables ] || exit 0


RETVAL=0
prog="dwall"
desc="Dwall iptables firewall"

KERNELMAJ="$(uname -r | sed                   -e 's,\..*,,')"
KERNELMIN="$(uname -r | sed -e 's,[^\.]*\.,,' -e 's,\..*,,')"

if [ "$KERNELMAJ" -lt 2 ] ; then
        exit 0
fi
if [ "$KERNELMAJ" -eq 2 -a "$KERNELMIN" -lt 3 ] ; then
        exit 0
fi
if  /sbin/lsmod 2>/dev/null |grep -q ipchains ; then
        # Don't do both
        exit 0
fi

### What does this do exactly ?
iftable() {
        if fgrep -qsx $1 /proc/net/ip_tables_names; then
                iptables -t "$@"
        fi
}

start() {
	echo -n $"Starting $desc ($prog): "
	daemon $FIREWALL
	RETVAL=$?
	echo
	[ $RETVAL -eq 0 ] && touch %{_localstatedir}/lock/subsys/$prog
	return $RETVAL
}

stop() {
	echo -n $"Shutting down $desc ($prog): "
        iptables -F
        iptables -X
	iptables -P INPUT ACCEPT
	iptables -P FORWARD DROP
	iptables -P OUTPUT ACCEPT
	success
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

%install
%{__rm} -rf %{buildroot}
%makeinstall

%post
/sbin/chkconfig --add dwall
if ! grep -q "%{_localstatedir}/log/dwall" /etc/syslog.conf; then
	echo -e "#kern.debug\t\t\t\t\t\t\t%{_localstatedir}/log/dwall" >>%{_sysconfdir}/syslog.conf
fi

%preun
if [ $1 -eq 0 ]; then
	/sbin/chkconfig --del dwall
fi

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog EXAMPLE README TODO chains-example/
%config(noreplace) %{_sysconfdir}/dwall/*.conf
%config(noreplace) %{_sysconfdir}/dwall/scripts/
%config %{_sysconfdir}/dwall/services/
%config %{_sysconfdir}/logrotate.d/*
%config %{_initrddir}/*
%dir %{_sysconfdir}/dwall/
%dir %{_sysconfdir}/dwall/backup/
%dir %{_sysconfdir}/dwall/tmp/
%{_bindir}/*
%{_libdir}/dwall/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.5.3-1.2
- Rebuild for Fedora Core 5.

* Mon Mar 22 2004 Dag Wieers <dag@wieers.com> - 0.5.3-1
- Updated to release 0.5.3.

* Fri Mar 19 2004 Dag Wieers <dag@wieers.com> - 0.5.2-1
- Updated to release 0.5.2.

* Sun Mar 14 2004 Dag Wieers <dag@wieers.com> - 0.5.1-1
- Updated to release 0.5.1.

* Wed Mar 10 2004 Dag Wieers <dag@wieers.com> - 0.5.0-0
- Updated to release 0.5.0.

* Fri Jul 25 2003 Dag Wieers <dag@wieers.com> - 0.4.1-0
- Updated to release 0.4.1.

* Fri Jun 06 2003 Dag Wieers <dag@wieers.com> - 0.4.0-0
- Initial package. (using DAR)
