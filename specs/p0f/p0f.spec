# $Id$
# Authority: dag
# Upstream: Michal Zalewski <lcamtuf$coredump,cx>
# Upstream: William Stearns <wstearns$pobox,com>

%{?dist: %{expand: %%define %dist 1}}

Summary: Passive OS fingerprinting tool
Name: p0f
Version: 2.0.5
Release: 1
License: LGPL
Group: Applications/Internet
URL: http://lcamtuf.coredump.cx/p0f.shtml

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://lcamtuf.coredump.cx/p0f/p0f-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libpcap
Prereq: /sbin/chkconfig

%description
p0f performs passive OS fingerprinting technique bases on information coming
from a remote host when it establishes a connection to our system. Captured
packets contains enough information to determine OS - and, unlike
active scanners (nmap, queSO) - it is done without sending anything to 
this host.

%prep
%setup -n %{name}

%{?el4:%{__perl} -pi.orig -e 's|net/bpf.h|pcap-bpf.h|' *.c *.h}
%{?fc3:%{__perl} -pi.orig -e 's|net/bpf.h|pcap-bpf.h|' *.c *.h}
%{?fc2:%{__perl} -pi.orig -e 's|net/bpf.h|pcap-bpf.h|' *.c *.h}

%{__cat} <<EOF >p0f.sysconfig
### Uncomment and change this if you want to change the default p0f options.
### See manual p0f(1) for details.

#BPFFILTER="tcp"
#OPTIONS="-p -t -M -i eth0"

#OPTIONS="-p -t -M -m "%{_sysconfdir}/p0f-mysql.conf"
EOF

%{__cat} <<'EOF' >p0f.sysv
#!/bin/bash
#
# Init file for p0f - Passive OS fingerprinting tool
#
# Written by Dag Wieers <dag@wieers.com>.
#
# chkconfig: 345 52 48
# description: Passive OS fingerprinting tool
#
# processname: p0f
# pidfile: %{_localstatedir}/run/p0f.pid

source %{_initrddir}/functions

### Default variables
BPFFILTER="tcp"
OPTIONS="-p -t -M -u pcap"
SYSCONFIG="%{_sysconfdir}/sysconfig/p0f"

### Read configuration
[ -r "$SYSCONFIG" ] && source "$SYSCONFIG"

RETVAL=0
prog="p0f"
desc="Passive OS fingerprinting"

start() {
	echo -n $"Starting $desc ($prog): "

	for ip in $(/sbin/ifconfig 2>/dev/null | grep 'inet addr' | sed -e 's|.*addr:||' -e 's| .*||'); do
		BPFFILTER="$BPFFILTER and not src host $ip"
	done

	daemon p0f -d -o %{_localstatedir}/log/p0f -q $OPTIONS "$BPFFILTER"
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
%{__make} %{?_smp_mflags} all p0fq tools

%install
%{__rm} -rf %{buildroot}

%{__install} -D -m0755 p0f %{buildroot}%{_sbindir}/p0f

%{__install} -d -m0755 %{buildroot}%{_bindir}
%{__install} -m0755 p0frep test/p0fq test/sendack test/sendack2 test/sendsyn %{buildroot}%{_bindir}

%{__install} -d -m0755 %{buildroot}%{_sysconfdir}/p0f/
%{__install} -m0644 *.fp %{buildroot}%{_sysconfdir}/p0f/

%{__install} -D -m0644 p0f.1 %{buildroot}%{_mandir}/man1/p0f.1

%{__install} -D -m0644 p0f.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/p0f
%{__install} -D -m0755 p0f.sysv %{buildroot}%{_initrddir}/p0f

%{__install} -d -m0755 %{buildroot}%{_localstatedir}/arpwatch/
						
%clean
%{__rm} -rf %{buildroot}

%post
if [ ! -f "%{_localstatedir}"/log/p0f ]; then
	touch %{_localstatedir}/log/p0f
	chown root.root %{_localstatedir}/log/p0f
	chmod 600 %{_localstatedir}/log/p0f
fi
/sbin/chkconfig --add p0f

%preun
if [ $1 -eq 0 ]; then
	/sbin/service p0f stop &>/dev/null || :
	/sbin/chkconfig --del p0f
fi

%postun
/sbin/service p0f condrestart &>/dev/null || :

%files
%defattr(-, root, root, 0755)
%doc doc/ChangeLog doc/COPYING doc/CREDITS doc/KNOWN_BUGS doc/README doc/TODO
%doc %{_mandir}/man?/*
%config(noreplace) %{_sysconfdir}/sysconfig/p0f
%config %{_sysconfdir}/p0f/
%config %{_initrddir}/p0f
%{_bindir}/*
%{_sbindir}/*

%defattr(-, pcap, pcap, 0755)
%{_localstatedir}/arpwatch/

%changelog
* Wed Sep 22 2004 Dag Wieers <dag@wieers.com> - 2.0.5-1
- Updated to release 2.0.5.

* Sun Jul 11 2004 Dag Wieers <dag@wieers.com> - 2.0.4-1
- Updated to release 2.0.4.
- Added /var/arpwatch to package. (Juha Sahakangas)

* Tue May 18 2004 Dag Wieers <dag@wieers.com> - 2.0.3-2
- Fixed sysconfig location.

* Thu Apr 15 2004 Dag Wieers <dag@wieers.com> - 2.0.3-1
- Initial package. (using DAR)
