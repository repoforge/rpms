# $Id$
# Authority: dag
# Upstream: <ebtables-devel$lists,sourceforge,net>

%define _sbindir /sbin

Summary: Ethernet Bridge frame table administration tool
Name: ebtables
Version: 2.0.6
Release: 2
License: GPL
Group: System Environment/Base
URL: http://ebtables.sourceforge.net/

Source: http://dl.sf.net/ebtables/ebtables-v%{version}.tar.gz
Patch0: ebtables-2.0.6-gcc34.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Ethernet bridge tables is a firewalling tool to transparantly filter network
traffic passing a bridge. The filtering possibilities are limited to link
layer filtering and some basic filtering on higher network layers.

The ebtables tool can be used together with the other Linux filtering tools,
like iptables. There are no incompatibility issues.

%prep
%setup -n ebtables-v%{version}
%patch0 -p1

%{__cat} <<'EOF' >ebtables.sysv
#!/bin/bash
#
# init script for the Ethernet Bridge filter tables
#
# Written by Dag Wieers <dag@wieers.com>.
#
# chkconfig: - 15 85
# description: Ethernet Bridge filtering tables
#
# config: /etc/sysconfig/ebtables.filter 
# config: /etc/sysconfig/ebtables.nat
# config: /etc/sysconfig/ebtables.route

source %{_initrddir}/functions
source %{_sysconfdir}/sysconfig/network

# Check that networking is up.
[ ${NETWORKING} = "no" ] && exit 0

[ -x %{_sbindir}/ebtables ] || exit 1

[ -r %{_sysconfdir}/sysconfig/etables.filter ] || exit 1
[ -r %{_sysconfdir}/sysconfig/etables.nat ] || exit 1
[ -r %{_sysconfdir}/sysconfig/etables.broute ] || exit 1

RETVAL=0
prog="ebtables"
desc="Ethernet bridge filtering"

start() {
	echo -n $"Starting $desc ($prog): "
	%{_sbindir}/ebtables -t filter --atomic-file %{_sysconfdir}/sysconfig/ebtables.filter --atomic-commit || RETVAL=1
	%{_sbindir}/ebtables -t nat --atomic-file %{_sysconfdir}/sysconfig/ebtables.nat --atomic-commit | RETVAL=1
	%{_sbindir}/ebtables -t broute --atomic-file %{_sysconfdir}/sysconfig/ebtables.broute --atomic-commit || RETVAL=1

	if [ $RETVAL -eq 0 ]; then
		success "$prog startup"
		rm -f %{_localstatedir}/lock/subsys/$prog
	else
		failure "$prog startup"
	fi

	echo
	return $RETVAL
}

stop() {
	echo -n $"Starting $desc ($prog): "
	%{_sbindir}/ebtables -t filter --init-table || RETVAL=1
	%{_sbindir}/ebtables -t nat --init-table || RETVAL=1
	%{_sbindir}/ebtables -t broute --init-table || RETVAL=1

	for mod in $(grep -E '^(ebt|ebtable)_' /proc/modules | cut -f1 -d' ') ebtables; do
		rmmod $mod || RETVAL=1
	done

	if [ $RETVAL -eq 0 ]; then
		success "$prog shutdown"
		rm -f %{_localstatedir}/lock/subsys/$prog
	else
		failure "$prog shutdown"
	fi

	echo
	return $RETVAL
}

restart() {
	stop
	start
}

save() {
	echo -n $"Saving $desc ($prog): "
	%{_sbindir}/ebtables -t filter --atomic-file %{_sysconfdir}/sysconfig/ebtables.filter --atomic-save || RETVAL=1
	%{_sbindir}/ebtables -t nat --atomic-file %{_sysconfdir}/sysconfig/ebtables.nat --atomic-save || RETVAL=1
	%{_sbindir}/ebtables -t broute --atomic-file %{_sysconfdir}/sysconfig/ebtables.broute --atomic-save || RETVAL=1

	if [ $RETVAL -eq 0 ]; then
		success "$prog saved"
	else
		failure "$prog saved"
	fi
	echo
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
  save)
	save
	;;
  status)
	status $prog
	RETVAL=$?
	;;
  *)
	echo $"Usage $0 {start|stop|restart|condrestart|save|status}"
	RETVAL=1
esac

exit $RETVAL
EOF

%build
%{__make} %{?_smp_mflags} \
	CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__install} -D -m0755 ebtables %{buildroot}%{_sbindir}/ebtables
%{__install} -D -m0755 ebtables.sysv %{buildroot}%{_initrddir}/ebtables
%{__install} -D -m0644 ethertypes %{buildroot}%{_sysconfdir}/ethertypes
%{__install} -D -m0644 ebtables.8 %{buildroot}%{_mandir}/man8/ebtables.8

%clean
%{__rm} -rf %{buildroot}

%post
/sbin/chkconfig --add ebtables

%preun
if [ $1 -eq 0 ]; then
	/sbin/service ebtables stop &>/dev/null || :
	/sbin/chkconfig --del ebtables
fi

%postun
/sbin/service ebtables condrestart &>/dev/null || :

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING INSTALL THANKS
%doc %{_mandir}/man8/ebtables.8*
%config %{_sysconfdir}/ethertypes
%config %{_initrddir}/ebtables
%{_sbindir}/ebtables

%changelog
* Thu Dec 02 2004 Dag Wieers <dag@wieers.com> - 2.0.6-2
- Added patch for gcc 3.4. (Nigel Smith)

* Tue Apr 27 2004 Dag Wieers <dag@wieers.com> - 2.0.6-2
- Cosmetic changes.

* Tue Apr 27 2004 Dag Wieers <dag@wieers.com> - 2.0.6-1
- Initial package. (using DAR)
