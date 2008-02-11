# $Id$
# Authority: dag

%{?dtag: %{expand: %%define %dtag 1}}

Summary: Virtual tunnel over TCP/IP networks
Name: vtun
Version: 3.0.2
Release: 1
License: GPL
Group: Applications/Internet
URL: http://vtun.sourceforge.net/

Source: http://dl.sf.net/vtun/vtun-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: flex, bison, cyrus-sasl-devel, openssl-devel, lzo-devel
%{?el5:BuildRequires: glibc-kernheaders}
%{?fc6:BuildRequires: glibc-kernheaders}
%{?fc5:BuildRequires: glibc-kernheaders}
%{?fc4:BuildRequires: glibc-kernheaders}
%{?el4:BuildRequires: glibc-kernheaders}
%{?fc3:BuildRequires: glibc-kernheaders}
%{?fc2:BuildRequires: glibc-kernheaders}
%{?fc1:BuildRequires: glibc-kernheaders}
%{?el3:BuildRequires: glibc-kernheaders}
%{?rh9:BuildRequires: glibc-kernheaders}
%{?rh8:BuildRequires: glibc-kernheaders}
%{?rh7:BuildRequires: glibc-kernheaders}
Obsoletes: vppp

%description
VTun provides the method for creating Virtual Tunnels over TCP/IP networks
and allows to shape, compress, encrypt traffic in that tunnels.
Supported type of tunnels are: PPP, IP, Ethernet and most of other serial
protocols and programs.

VTun is easily and highly configurable, it can be used for various network
tasks like VPN, Mobil IP, Shaped Internet access, IP address saving, etc.
It is completely user space implementation and does not require modification
to any kernel parts.

%prep
%setup

%{__cat} <<'EOF' >vtund.sysv
#!/bin/sh
#
# Init script for starting and stoping vtund.
#
# Writen by Dag Wieers <dag@wieers.com>.
#
# chkconfig: - 55 45
# description: Virtual Tunnel Daemon. (vtund)
#    VTun provides the method for creating Virtual Tunnels over TCP/IP networks
#    and allows to shape, compress, encrypt traffic in that tunnels.
#
# processname: vtund
# config: %{_sysconfdir}/vtund.conf
# pidfile: %{_localstatedir}/run/vtund

source %{_initrddir}/functions

[ -x %{_sbindir}/vtund ] || exit 1
[ -r %{_sysconfdir}/vtund.conf ] || exit 1

RETVAL=0
prog="vtund"
desc="Virtual Tunnel daemon"

start() {
	echo -n $"Starting $desc ($prog): "
	daemon $prog -s
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
	killproc $proc -HUP
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

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall SBIN_DIR="%{buildroot}%{_sbindir}" \
        MAN_DIR="%{buildroot}%{_mandir}" \
        ETC_DIR="%{buildroot}%{_sysconfdir}" \
        VAR_DIR="%{buildroot}%{_localstatedir}" \
    INSTALL_OWNER=

%{__install} -Dp -m0755 vtund.sysv %{buildroot}%{_initrddir}/vtund
#%{__install} -Dp -m0755 scripts/vtund.rc.red_hat %{buildroot}%{_initrddir}/vtund

%pre
if [ ! -e /dev/net/tun ]; then
    if [ ! -d /dev/net/ ]; then
        %{__install} -d -m0755 /dev/net
    fi
    mknod -m0600 /dev/net/tun c 10 200
fi

%post
/sbin/chkconfig --add vtund

%preun
if [ $1 -eq 0 ]; then
    /sbin/service vtund stop &>/dev/null || :
    /sbin/chkconfig --del vtund
fi

%postun
/sbin/service vtund condrestart &>/dev/null || :

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog Credits FAQ README* TODO vtund.conf
%doc %{_mandir}/man5/vtund.conf.5*
%doc %{_mandir}/man8/vtun.8*
%doc %{_mandir}/man8/vtund.8*
%attr(600, root, root) %config(noreplace) %{_sysconfdir}/vtund.conf
%config %{_initrddir}/vtund
%{_sbindir}/vtund
%{_localstatedir}/lock/vtund/
%{_localstatedir}/log/vtund/

%changelog
* Sun Feb 10 2008 Dag Wieers <dag@wieers.com> - 3.0.2-1
- Updated to release 3.0.2.

* Sun Jun 17 2007 Dries Verachtert <dries@ulyssis.org> - 3.0.1-1
- Updated to release 3.0.1.

* Sun Dec 15 2006 Dries Verachtert <dries@ulyssis.org> - 3.0.0-1
- Updated to release 3.0.0.

* Mon May 26 2003 Dag Wieers <dag@wieers.com> - 2.6-0
- Updated to release 2.6.
- Embedded improved sysv script.

* Sat Dec 28 2002 Dag Wieers <dag@wieers.com> - 2.5-0
- Made use of more macros
- Cleaned up SPEC file
- Added /dev/net/tun for RH 7 (RH 8 has it already)

* Mon May 29 2000 Michael Tokarev <mjt@tls.msk.ru>
- Allow to build as non-root (using new INSTALL_OWNER option)
- Added vtund.conf.5 manpage
- Allow compressed manpages
- Added cleanup of old $RPM_BUILD_ROOT at beginning of %%install stage

* Sat Mar 04 2000 Dag Wieers <dag@wieers.com>
- Added USE_SOCKS compile option.
- Added Prefix-header

* Sat Jan 29 2000 Dag Wieers <dag@wieers.com>
- Replaced SSLeay-dependency by openssl-dependency
- Replaced README.Config by README.Setup
- Added TODO

* Tue Nov 23 1999 Dag Wieers <dag@wieers.com>
- Added Url and Obsoletes-headers
- Added ChangeLog ;)
- Changed summary
