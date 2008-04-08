# $Id$
# Authority: dag

%{?dtag: %{expand: %%define %dtag 1}}

%{!?dtag:%define _with_libpcapdevel 1}
%{?el5:%define _with_libpcapdevel 1}
%{?fc6:%define _with_libpcapdevel 1}

Summary: Monitor ethernet networks
Name: arpalert
Version: 2.0.10
Release: 1
License: GPL
Group: Applications/Internet
URL: http://www.arpalert.org/

Source: http://www.arpalert.org/src/arpalert-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%{?_with_libpcapdevel:BuildRequires:libpcap-devel}

%description
arpalert listens on a network interface (without using 'promiscuous' mode)
and catches all conversations of MAC address to IP request.

It then compares the mac addresses it detected with a pre-configured list
of authorized MAC addresses. If the MAC is not in list, arpalert launches
a pre-defined user script with the MAC address and IP address as parameters.
This software can run in daemon mode; it's very fast (low CPU and memory
consumption).

%prep
%setup

%{__cat} <<'EOF' >arpalert.sysv
#!/bin/bash
#
# Init file for arpalert.
#
# Written by Dag Wieers <dag@wieers.com>
#
# chkconfig: 2345 55 46
# description: Arpalert daemon to monitor ethernet networks.
#
# processname: arpalert
# config: %{_sysconfdir}/arpalert/arpalert.conf
# pidfile: %{_localstatedir}/run/arpalert

source %{_initrddir}/functions

[ -x %{_sbindir}/arpalert ] || exit 1
[ -r %{_sysconfdir}/arpalert/arpalert.conf ] || exit 1

RETVAL=0
prog="arpalert"
desc="Arpalert daemon"

start() {
    echo -n $"Starting $desc ($prog): "
    daemon $prog -d
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
    ;;
esac
exit $RETVAL
EOF

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%{__install} -d -m0755 %{buildroot}%{_localstatedir}/lib/arpalert/
%{__install} -Dp -m0755 arpalert.sysv %{buildroot}%{_initrddir}/arpalert

%clean
%{__rm} -rf %{buildroot}

%pre
if ! /usr/bin/id arpalert &>/dev/null; then
    /usr/sbin/useradd -r -d %{_localstatedir}/log/arpalert -s /sbin/login -c "arpalert" arpalert &>/dev/null || \
        %logmsg "Unexpected error adding user \"dovecot\". Aborting installation."
fi
/usr/sbin/usermod -s /sbin/nologin arpalert &>/dev/null || :

%post
/sbin/chkconfig --add arpalert

%preun
if [ $1 -eq 0 ]; then
    /sbin/service arpalert stop &>/dev/null || :
    /sbin/chkconfig --del arpalert
fi

%postun
/sbin/service arpalert condrestart &>/dev/null || :

%files
%defattr(-, root, root, 0755)
%doc CHANGES COPYING README
%doc %{_mandir}/man8/arpalert.8*
%config %{_initrddir}/arpalert
%{_includedir}/arpalert.h
%config(noreplace) %{_sysconfdir}/arpalert/
%{_sbindir}/arpalert

%defattr(-, arpalert, arpalert, 0755)
%{_localstatedir}/lib/arpalert/

%changelog
* Sun Mar 30 2008 Dag Wieers <dag@wieers.com> - 2.0.10-1
- Updated to release 2.0.10.

* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 2.0.9-1
- Updated to release 2.0.9.

* Sat Aug 04 2007 Dag Wieers <dag@wieers.com> - 2.0.7-1
- Updated to release 2.0.7.

* Thu Jun 07 2007 Dag Wieers <dag@wieers.com> - 2.0.6-1
- Initial package. (using DAR)
