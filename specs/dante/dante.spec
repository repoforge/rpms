# $Id$
# Authority: dag

%define _libdir /%{_lib}

Summary: Free Socks v4/v5 client implementation
Name: dante
Version: 1.2.2
Release: 1%{?dist}
License: BSD-type
Group: Applications/Internet
URL: http://www.inet.no/dante/

Source: ftp://ftp.inet.no/pub/socks/dante-%{version}.tar.gz
Patch0: dante-1.2.0-private.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: bison
BuildRequires: flex
BuildRequires: miniupnpc-devel

%description
Dante is a free implementation of the proxy protocols socks version 4,
socks version 5 (rfc1928) and msproxy. It can be used as a firewall
between networks. It is being developed by Inferno Nettverk A/S, a
Norwegian consulting company. Commercial support is available.

This package contains the dynamic libraries required to "socksify"
existing applications to become socks clients.

%package server
Summary: free Socks v4/v5 server implementation
Group: System Environment/Daemons
Requires: %{name} = %{version}-%{release}

%description server
This package contains the socks proxy daemon and its documentation.
The sockd is the server part of the Dante socks proxy package and
allows socks clients to connect through it to the network.

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup
%patch0 -p0 -b .orig

### Example should use /var/log/sockd by default
%{__perl} -pi -e 's|/var/log/lotsoflogs|%{_localstatedir}/log/sockd|' example/sockd.conf

%{__cat} <<EOF >sockd.logrotate
%{_localstatedir}/log/sockd {
    missingok
    copytruncate
    notifempty
}
EOF

%{__cat} <<'EOF' >sockd.sysv
#!/bin/sh
#
# Init file for the Dante Socks server
#
# Written by Dag Wieers <dag@wieers.com>.
#
# chkconfig: 2345 65 35
# description: Dante Socks v4/v5 servers
#
# processname: sockd
# config: %{_sysconfdir}/sockd.conf
# pidfile: %{_localstatedir}/run/sockd

source %{_initrddir}/functions
source %{_sysconfdir}/sysconfig/network

# Check that networking is up.
[ ${NETWORKING} = "no" ] && exit 1

[ -x %{_sbindir}/sockd ] || exit 1
[ -r %{_sysconfdir}/sockd.conf ] || exit 1

RETVAL=0
prog="sockd"
desc="Dante Socks server"

start() {
    echo -n $"Starting $desc ($prog): "
    daemon $prog -D
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

%{__cat} <<'EOF' >dsocksify
#!/bin/sh -

# Socksify any dynamically linked program by issuing:
#
#   dsocksify <program> <arguments>

LIBRARY="${SOCKS_LIBRARY-%{_libdir}/libdsocks.so}"
LD_PRELOAD="${LD_PRELOAD} ${LIBRARY}"
export LD_PRELOAD

exec "$@"
EOF

%{__cat} <<'EOF' >dsocksify.sysv
#!/bin/bash
#
# Startup script to transparantly socksify your system using Dante.
#
# chkconfig: - 89 11
# description: Dsocksify is a means to socksify your system transparantly \
#   (using Dante) on start-up after the network is up and running.
#
# processname: dsocksify
#
# config: %{_sysconfdir}/socks.conf
# config: /etc/ld.so.preload

# Source function library.
source %{_initrddir}/functions

disable() {
    echo $"Warning: your installation is faulty."
    stop
    exit 1
}

[ -r %{_sysconfdir}/socks.conf ] || disable
[ -x %{_libdir}/libdsocks.so ] || disable

start() {
    echo -n $"Socksifying system: "
    grep "%{_libdir}/libdsocks.so" /etc/ld.so.preload &>/dev/null
    ret=$?
    if [ ! -f /etc/ld.so.preload -o $ret -ne 0 ]; then
        echo $"%{_libdir}/libdsocks.so" >>/etc/ld.so.preload
        success $"dsocksify startup"
    elif [ $ret -eq 0 ]; then
        passed $"dsocksify startup"
    else
        failure $"dsocksify startup"
    fi
    echo
}

stop() {
    echo -n $"Unsocksifying system: "
    grep "%{_libdir}/libdsocks.so" /etc/ld.so.preload &>/dev/null
    if [ $? -eq 0 ]; then
        cat /etc/ld.so.preload | grep -v "%{_libdir}/libdsocks.so" >/etc/ld.so.preload.cache
        mv -f /etc/ld.so.preload.cache /etc/ld.so.preload
        success $"dsocksify shutdown"
    else
        failure $"dsocksify shutdown"
    fi
    if [ ! -s /etc/ld.so.preload ]; then
        rm -f /etc/ld.so.preload
    fi
    echo
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
  *)
    echo $"Usage: $0 {start|stop|restart}"
    RETVAL=1
esac

exit $RETVAL
EOF

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%{__install} -Dp -m0644 example/socks-simple.conf %{buildroot}%{_sysconfdir}/socks.conf
%{__install} -Dp -m0644 example/sockd.conf %{buildroot}%{_sysconfdir}/sockd.conf

%{__install} -Dp -m0755 sockd.sysv %{buildroot}%{_initrddir}/sockd
%{__install} -Dp -m0644 sockd.logrotate %{buildroot}%{_sysconfdir}/logrotate.d/sockd
%{__install} -Dp -m0755 dsocksify.sysv %{buildroot}%{_initrddir}/dsocksify
%{__install} -Dp -m0755 dsocksify %{buildroot}%{_bindir}/dsocksify
%{__ln_s} -f dsocksify %{buildroot}%{_bindir}/socksify

#%{__mv} -f %{buildroot}%{_includedir}/socks.h.in %{buildroot}%{_includedir}/socks.h

### FIXME: Set library as executable - prevent ldd from complaining
%{__chmod} +x %{buildroot}%{_libdir}/*.so*

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post server
/sbin/chkconfig --add sockd

%preun server
if [ $1 -eq 0 ]; then
    /sbin/service sockd stop &>/dev/null || :
    /sbin/chkconfig --del sockd
fi

%postun server
/sbin/service sockd condrestart &>/dev/null || :

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc BUGS CREDITS INSTALL LICENSE NEWS README* SUPPORT TODO
%doc doc/*.txt doc/README*
%doc example/socks*.conf
%doc %{_mandir}/man1/socksify.1*
%doc %{_mandir}/man5/socks.conf.5*
%config %{_sysconfdir}/socks.conf
%config %{_initrddir}/dsocksify
### Required for dsocksify script
%{_libdir}/libdsocks.so
%{_libdir}/libsocks.so.*
%{_bindir}/dsocksify
%{_bindir}/socksify

%files server
%defattr(-, root, root, 0755)
%doc example/sockd*.conf
%doc %{_mandir}/man5/sockd.conf.5*
%doc %{_mandir}/man8/sockd.8*
%config(noreplace) %{_sysconfdir}/sockd.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/sockd
%config %{_initrddir}/sockd
%{_sbindir}/sockd

%files devel
%defattr(-, root, root, 0755)
%doc doc/rfc* doc/SOCKS4.protocol INSTALL
%{_includedir}/socks.h
#%{_includedir}/socks_glibc.h
%{_libdir}/libsocks.so
%exclude %{_libdir}/libdsocks.a
%exclude %{_libdir}/libdsocks.la
%exclude %{_libdir}/libsocks.a
%exclude %{_libdir}/libsocks.la

%changelog
* Thu Sep 23 2010 Dag Wieers <dag@wieers.com> - 1.2.2-1
- Updated to release 1.2.2.

* Fri May 28 2010 Dag Wieers <dag@wieers.com> - 1.2.1-1
- Updated to release 1.2.1.

* Tue Jan 12 2010 Dag Wieers <dag@wieers.com> - 1.2.0-2
- Backported GLIBC_PRIVATE related patch.

* Thu Oct 29 2009 Dag Wieers <dag@wieers.com> - 1.2.0-1
- Updated to release 1.2.0.

* Tue Apr  7 2009 Dries Verachtert <dries@ulyssis.org> - 1.1.19-3
- Applied a fix by Thomas M Steenholdt for the dsocksify sysv init script.

* Wed Jun 11 2008 Dag Wieers <dag@wieers.com> - 1.1.19-2
- Get rid of GLIBC_PRIVATE caused by using __libc_enable_secure.

* Sat Apr 29 2006 Dag Wieers <dag@wieers.com> - 1.1.19-1
- Updated to release 1.1.19.

* Fri Sep 09 2005 Dag Wieers <dag@wieers.com> - 1.1.18-1
- Updated to release 1.1.18.

* Thu Jul 14 2005 Dag Wieers <dag@wieers.com> - 1.1.17-1
- Updated to release 1.1.17.

* Mon Jul 11 2005 Dag Wieers <dag@wieers.com> - 1.1.16-1
- Updated to release 1.1.16.

* Sun Feb 06 2005 Dag Wieers <dag@wieers.com> - 1.1.15-1
- Updated to release 1.1.15.

* Wed Feb 25 2004 Dag Wieers <dag@wieers.com> - 1.1.14-2
- Fixed no-replacing config files.
- Documentation clean-up.

* Tue Feb 24 2004 Dag Wieers <dag@wieers.com> - 1.1.14-1
- Added logrotate config. (Matthias Saou)

* Mon Jul 28 2003 Dag Wieers <dag@wieers.com> - 1.1.14-0
- Updated to release 1.1.14.

* Tue Apr 08 2003 Dag Wieers <dag@wieers.com> - 1.1.13-2
- Incorporated the official bswap32 patch.

* Tue Dec 31 2002 Dag Wieers <dag@wieers.com> - 1.1.13-1
- Added dsocksify init script
- Put libraries in /lib
- Moved *.so from dante-devel to dante
- Added pam-devel to BuildRequires (to provide PAM support)

* Mon Dec 30 2002 Dag Wieers <dag@wieers.com> - 1.1.13-0
- Updated to 1.1.13
- Cleaned up SPEC file
- Made more use of macros

* Thu Oct 12 2000 Karl-Andre' Skevik <karls@inet.no>
- Use of macros for directory locations/paths
- Explicitly name documentation files
- Run chkconfig --del before files are deleted on uninstall

* Wed Mar 10 1999 Karl-Andre' Skevik <karls@inet.no>
- Integrated into CVS
- socksify patch no longer needed

* Thu Mar 04 1999 Oren Tirosh <oren@hishome.net>
- configurable %{prefix}, fixed daemon init script
- added /lib/libdl.so to socksify

* Wed Mar 03 1999 Oren Tirosh <oren@hishome.net>
- First spec file for Dante
