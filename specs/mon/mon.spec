# $Id$
# Authority: dag
# Upstream: Jim Trocki <trockij$linux,kernel,org>

%define moncgi_version 1.52

Summary: General-purpose resource monitoring system
Name: mon
Version: 1.2.0
Release: 2
License: GPL
Group: Applications/Internet
URL: http://www.kernel.org/software/mon/

Source0: ftp://ftp.kernel.org/pub/software/admin/mon/mon-%{version}.tar.bz2
Source1: ftp://ftp.kernel.org/pub/software/admin/mon/contrib/cgi-bin/mon.cgi/mon.cgi-%{moncgi_version}.tar.bz2
Source2: ftp://ftp.kernel.org/pub/software/admin/mon/contrib/all-alerts.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Requires: perl
Requires: perl(Authen::PAM)

%description
Mon is a general-purpose resource monitoring system.  It can be used
to monitor network service availability, server problems,
environmental conditions (i.e., the temperature in a room) or other
things. Mon can be used to test the condition and/or to trigger an
action upon failure of the condition.  Mon keeps the testing and
action-taking tasks as separate, stand-alone programs.

Mon is very extensible.  Monitors and alerts are not a part of mon, but
the distribution comes with a handful of them to get you started. This
means that if a new service needs monitoring, or if a new alert is
required, the mon server will not need to be changed.

%prep
%setup -a 1 -a 2

### FIXME: Change to real perl. (Please fix upstream)
%{__perl} -pi -e 's|^#!/.*bin/perl|#!%{__perl}|i' mon.cgi-%{moncgi_version}/util/moncgi-appsecret.pl alerts/hpov/*.alert mon.d/*.monitor

### FIXME: get rid of chgrp. (Please fix upstream)
%{__perl} -pi.orig -e 's|-g uucp ||' mon.d/Makefile

%{__cat} <<EOF >userfile
# user: passwd
EOF

%{__cat} <<'EOF' >mon.cf
### Extremely basic mon.cf file

### global options
cfbasedir   = %{_sysconfdir}/mon
pidfile     = %{_localstatedir}/run/mon.pid
statedir    = %{_localstatedir}/lib/mon/state.d
logdir      = %{_localstatedir}/lib/mon/log.d
dtlogfile   = %{_localstatedir}/lib/mon/log.d/downtime.log
alertdir    = %{_libdir}/mon/alert.d
mondir      = %{_libdir}/mon/mon.d
maxprocs    = 20
histlength  = 100
randstart   = 60s
authtype    = pam
userfile    = %{_sysconfdir}/mon/userfile

### group definitions (hostnames or IP addresses)
hostgroup servers localhost

watch servers
    service ping
    interval 5m
    monitor ping.monitor
    period wd {Mon-Fri} hr {7am-10pm}
        alert mail.alert root@localhost
        alertevery 1h
    period wd {Sat-Sun}
        alert mail.alert root@localhost
    service telnet
    interval 10m
    monitor telnet.monitor
    period wd {Mon-Fri} hr {7am-10pm}
        alertevery 1h
        alertafter 2 30m
        alert mail.alert root@localhost
   service http
        interval 4m
        monitor http.monitor
        allow_empty_group
        period wd {Sun-Sat}
            upalert mail.alert -S "web server is back up" mis
            alertevery 45m
    service smtp
        interval 10m
        monitor smtp.monitor
        period wd {Mon-Fri} hr {7am-10pm}
            alertevery 1h
            alertafter 2 30m
            alert qpage.alert mis-pagers@domain.com

### See /usr/doc for the original example...
EOF

%{__cat} <<'EOF' >mon.sysv
#!/bin/bash
#
# Init file for Mon System Monitoring daemon
#
# Written by Dag Wieers <dag@wieers.com>.
#
# chkconfig: 2345 99 10
# description: Mon System Monitoring daemon
#
# processname: mon
# config: %{_sysconfdir}/mon/mon.conf
# config: %{_sysconfdir}/mon/auth.conf
# pidfile: %{_localstatedir}/run/mon.pid

source %{_initrddir}/functions

[ -x %{_bindir}/mon ] || exit 1
[ -r %{_sysconfdir}/mon/mon.cf ] || exit 1
[ -r %{_sysconfdir}/mon/auth.cf ] || exit 1

RETVAL=0
prog="mon"
desc="System Monitoring daemon"

start() {
    echo -n $"Starting $desc ($prog): "
    daemon $prog -f -c %{_sysconfdir}/mon/mon.cf
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
%{__make} %{?_smp_mflags} -C mon.d \
    RPM_OPT_FLAGS="%{optflags} -DUSE_VENDOR_CF_PATH=1"

%install
%{__rm} -rf %{buildroot}
%makeinstall -C mon.d MONPATH="%{buildroot}%{_libdir}/mon"

#%{__install} -p -m0755 mon.d/*.monitor %{buildroot}%{_libdir}/mon/mon.d/
#%{__install} -p -m0555 mon.d/dialin.monitor.wrap %{buildroot}%{_libdir}/mon/mon.d/

%{__install} -Dp -m0755 mon %{buildroot}%{_bindir}/mon
%{__install} -Dp -m0755 clients/moncmd %{buildroot}%{_bindir}/moncmd
%{__install} -Dp -m0755 clients/monshow %{buildroot}%{_bindir}/monshow
%{__install} -Dp -m0755 clients/skymon/skymon %{buildroot}%{_bindir}/skymon

%{__install} -d -m0755 %{buildroot}%{_mandir}/man{1,8}/
%{__install} -p -m0644 doc/*.1 %{buildroot}%{_mandir}/man1/
%{__install} -p -m0644 doc/*.8 %{buildroot}%{_mandir}/man8/

%{__install} -d -m0755 %{buildroot}%{_libdir}/mon/{alert.d,mon.d}/
%{__install} -p -m0755 alert.d/* %{buildroot}%{_libdir}/mon/alert.d/
%{__install} -p -m0755 alerts/*/*.alert %{buildroot}%{_libdir}/mon/alert.d/

%{__install} -Dp -m0644 etc/auth.cf %{buildroot}%{_sysconfdir}/mon/auth.cf
%{__install} -Dp -m0644 mon.cf %{buildroot}%{_sysconfdir}/mon/mon.cf
%{__install} -Dp -m0600 userfile %{buildroot}%{_sysconfdir}/mon/userfile
%{__install} -Dp -m0755 mon.sysv %{buildroot}%{_initrddir}/mon

%{__install} -Dp -m0755 mon.cgi-%{moncgi_version}/mon.cgi %{buildroot}%{_localstatedir}/www/cgi-bin/mon.cgi

%{__install} -d -m0755 %{buildroot}%{_localstatedir}/lib/mon/{log.d,state.d}/

%clean
%{__rm} -rf %{buildroot}

%post
/sbin/chkconfig --add mon

%preun
if [ $1 -eq 0 ]; then
    /sbin/service mon stop &>/dev/null || :
    /sbin/chkconfig --del mon
fi

%postun
/sbin/service mon condrestart &>/dev/null || :

%files
%defattr(-, root, root, 0755)
%doc CHANGES COPYING COPYRIGHT CREDITS KNOWN-PROBLEMS README TODO VERSION
%doc alerts/*/*.README doc/README.* mon.cgi-1.52/ utils/
%doc clients/{skymon,batch-example} etc/*.cf etc/example.m4 etc/example.monshowrc
%doc %{_mandir}/man1/moncmd.1*
%doc %{_mandir}/man1/monshow.1*
%doc %{_mandir}/man8/mon.8*
%config(noreplace) %{_sysconfdir}/mon/
%config %{_initrddir}/mon
%{_bindir}/mon
%{_bindir}/moncmd
%{_bindir}/monshow
%{_bindir}/skymon
%{_libdir}/mon/
%{_localstatedir}/lib/mon/
%{_localstatedir}/www/cgi-bin/mon.cgi

%defattr(2555, root, uucp)
%{_libdir}/mon/mon.d/dialin.monitor.wrap

%changelog
* Wed Dec 17 2008 Dag Wieers <dag@wieers.com> - 1.2.0-2
- Added missing perl(Authen::PAM) requirement.

* Wed Jun 27 2007 Dag Wieers <dag@wieers.com> - 1.2.0-1
- Updated to release 1.2.0.

* Tue Mar 06 2004 Dag Wieers <dag@wieers.com> - 0.99.2-1
- Fixed problems with perl-modules.

* Fri Jan 09 2004 Dag Wieers <dag@wieers.com> - 0.99.2-0
- Initial package. (using DAR)
