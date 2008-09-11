# $Id$
# Authority: dag
# Upstream: Eddy Vervest <eddy$clevervest,com>

Summary: HTTP based time synchronization tool
Name: htpdate
Version: 1.0.3
Release: 1
License: GPL
Group: Applications/Internet
URL: http://www.clevervest.com/htp/

Source: http://www.clevervest.com/htp/archive/c/htpdate-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Requires: /sbin/chkconfig

%description
The HTTP Time Protocol (HTP) is used to synchronize a computer's time with
web servers as reference time source. Htpdate will synchronize your computer's
time by extracting timestamps from HTTP headers found in web servers responses.
Htpdate can be used as a daemon, to keep your computer synchronized.

Accuracy of htpdate is usually better than 0.5 seconds (even better with
multiple servers). If this is not good enough for you, try the ntpd package.

%prep
%setup

%{__cat} <<EOF >htpdate.sysconfig
### Uncomment and change this if you want to change the default htpdate options.
### See manual htpdate(8) for details.

#OPTIONS="-a -l -s"
#SERVERS="www.linux.org www.freebsd.org"
EOF

%{__cat} <<'EOF' >htpdate.sysv
#!/bin/bash
#
# Init file for HTTP Time Protocol (HTP) daemon
#
# Written by Dag Wieers <dag@wieers.com>
#
# chkconfig: - 58 74
# description: HTTP Time Protocol daemon
#
# processname: htpdate
# config: %{_sysconfdir}/sysconfig/htpdate
# pidfile: %{_localstatedir}/run/htpdate

source %{_initrddir}/functions

[ -x %{_bindir}/htpdate ] || exit 1

### Default variables
OPTIONS="-a -l -s"
PIDFILE="%{_localstatedir}/run/htpdate.pid"
SERVERS="www.linux.org www.freebsd.org"
SYSCONFIG="%{_sysconfdir}/sysconfig/htpdate"

### Read configuration
[ -r "$SYSCONFIG" ] && source "$SYSCONFIG"

RETVAL=0
prog="htpdate"
desc="HTTP Time Protocol daemon"

start() {
    echo -n $"Starting $desc ($prog): "
    daemon $prog -D $OPTIONS -i $PIDFILE $SERVERS
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
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -D -m0755 htpdate %{buildroot}%{_bindir}/htpdate
%{__install} -D -m0644 htpdate.8.gz %{buildroot}%{_mandir}/man8/htpdate.8.gz
#%{__install} -D -m0755 scripts/htpdate.init %{buildroot}%{_initrddir}/htpdate
%{__install} -D -m0755 htpdate.sysv %{buildroot}%{_initrddir}/htpdate
%{__install} -D -m0644 htpdate.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/htpdate

%post
/sbin/chkconfig --add htpdate

%preun
if [ $1 -eq 0 ]; then
    /sbin/service htpdate stop &>/dev/null || :
    /sbin/chkconfig --del htpdate
fi

%postun
/sbin/service htpdate condrestart &>/dev/null || :

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changelog README
%doc %{_mandir}/man8/htpdate.8*
%config(noreplace) %{_sysconfdir}/sysconfig/htpdate
%config %{_initrddir}/htpdate
%{_bindir}/htpdate

%changelog
* Wed Sep 03 2008 Dag Wieers <dag@wieers.com> - 1.0.3-1
- Updated to release 1.0.3.

* Tue Sep 02 2008 Dag Wieers <dag@wieers.com> - 1.0.2-1
- Updated to release 1.0.2.

* Tue Apr 29 2008 Dag Wieers <dag@wieers.com> - 1.0.1-1
- Updated to release 1.0.1.

* Sun Mar 04 2007 Dag Wieers <dag@wieers.com> - 1.0.0-1
- Updated to release 1.0.0.

* Tue Nov 07 2006 Dag Wieers <dag@wieers.com> - 0.9.3-1
- Updated to release 0.9.3.

* Sun Feb 12 2006 Dag Wieers <dag@wieers.com> - 0.9.1-2
- Fixed sysv script. (Alain Rykaert)

* Tue Feb 07 2006 Dag Wieers <dag@wieers.com> - 0.9.1-1
- Initial package. (using DAR)
