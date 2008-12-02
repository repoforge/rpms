# $Id$
# Authority: dag

# Tag: test

Summary: Utility to collect Linux performance data
Name: collectl
Version: 3.1.1
Release: 1
License: Artistic/GPL
Group: Applications/System
URL: http://collectl.sourceforge.net/

Source: http://dl.sf.net/collectl/collectl-%{version}.src.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
Requires: chkconfig
Requires: initscripts
Requires: perl(Compress::Zlib)
Requires: perl(Sys::Syslog)
Requires: perl(Time::HiRes)

%description
collectl is a utility to collect Linux performance data.

%prep
%setup

%{__cat} <<EOF >collectl.init
#!/bin/sh
# Startup script for collectl
#
# chkconfig: - 99 01
# description: Run data collection for a number of subsystems
#    see /etc/collectl.conf for startup options
# config: /etc/collectl.conf

# BEGIN INIT INFO
# Provides:          collectl
# Required-Start:    $syslog
# Required-Stop:     $syslog
# Default-Start:
# Default-Stop:      0 1 2 3 4 5 6
# Short-Description: Run data collection for a number of subsystems
# Description:       Run data collection for a number of subsystems
# END INIT INFO

source %{_initrddir}/functions

exec=/usr/bin/collectl
prog=collectl

[ -e /etc/sysconfig/$prog ]  && . /etc/sysconfig/$prog

lockfile=/var/lock/subsys/$prog

start() {
    [ -x $exec ]  || exit 5
    [ -f $config ]  || exit 6
    echo -n $"Starting $prog: "
    daemon $exec $OPTS
    retval=$?
    echo
    [ $retval -eq 0 ]  && touch $lockfile
    return $retval
}

stop() {
    echo -n $"Stopping $prog: "
    killproc $prog
    retval=$?
    echo
    [ $retval -eq 0 ]  && rm -f $lockfile
    return $retval
}

restart() {
    stop
    start
}

reload() {
    restart
}

force_reload() {
    restart
}

rh_status() {
    status $prog
}

rh_status_q() {
    rh_status >/dev/null 2>&1
}


case "$1" in
    start)
        rh_status_q && exit 0
        $1
        ;;
    stop)
        rh_status_q || exit 0
        $1
        ;;
    restart)
        $1
        ;;
    reload)
        rh_status_q || exit 7
        $1
        ;;
    force-reload)
        force_reload
        ;;
    status)
        rh_status
        ;;
    condrestart|try-restart)
        rh_status_q || exit 0
        restart
        ;;
    *)
        echo $"Usage: $0 {start|stop|status|restart|condrestart|try-restart|reload|force-reload}"
        exit 2
esac
exit $?
EOF

%{__cat} <<EOF >collectl.sysconfig
### For list of available options see man page or %{_sysconfig}/collectd.conf
OPTIONS="-D"
EOF

%{__cat} <<EOF >collectl.logrotate
%{_localstatedir}/log/collectl/*.log {
    copytruncate
    missingok
    notifempty
}
EOF

%{__cat} <<'EOF' >collectl
#!/bin/sh
cd %{_libexecdir}/collectl/
exec %{__perl} collectl.pl $@
EOF

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 collectl %{buildroot}%{_bindir}/collectl
%{__install} -Dp -m0755 readS %{buildroot}%{_bindir}/readS
%{__install} -Dp -m0755 collectl.pl %{buildroot}%{_libexecdir}/collectl/collectl.pl
%{__install} -Dp -m0644 formatit.ph %{buildroot}%{_libexecdir}/collectl/formatit.ph
%{__install} -Dp -m0644 lexpr.ph %{buildroot}%{_libexecdir}/collectl/lexpr.ph
%{__install} -Dp -m0644 sexpr.ph %{buildroot}%{_libexecdir}/collectl/sexpr.ph
%{__install} -Dp -m0644 vmstat.ph %{buildroot}%{_libexecdir}/collectl/vmstat.ph
%{__install} -Dp -m0644 man1/collectl.1 %{buildroot}%{_mandir}/man1/collectl.1
%{__install} -Dp -m0644 collectl.conf %{buildroot}%{_sysconfdir}/collectl.conf
%{__install} -Dp -m0755 collectl.init %{buildroot}%{_initrddir}/collectl
%{__install} -Dp -m0644 collectl.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/collectl
%{__install} -Dp -m0644 collectl.logrotate %{buildroot}%{_sysconfdir}/logrotate.d/collectl
%{__install} -d -m0755 %{buildroot}%{_localstatedir}/log/collectl/

%post
/sbin/chkconfig --add collectl

%postun
if [ $1 -ge 1 ]; then
    /sbin/service collectl condrestart &>/dev/null || :
fi

%preun
if [ $1 -eq 0 ]; then
    /sbin/service collectl stop &>/dev/null || :
    /sbin/chkconfig --del collectl
fi

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ARTISTIC COPYING GPL RELEASE-collectl docs/
%doc %{_mandir}/man1/collectl.1*
%config(noreplace) %{_sysconfdir}/collectl.conf
%config %{_initrddir}/collectl
%config(noreplace) %{_sysconfdir}/sysconfig/collectl
%config(noreplace) %{_sysconfdir}/logrotate.d/collectl
%{_bindir}/collectl
%{_bindir}/readS
%{_libexecdir}/collectl/
%{_localstatedir}/log/collectl/

%changelog
* Mon Dec 01 2008 Dag Wieers <dag@wieers.com> - 3.1.1-1
- Updated to release 3.1.1.

* Wed Sep 17 2008 Dag Wieers <dag@wieers.com> - 3.1.0-1
- Initial package based on Fedora.
