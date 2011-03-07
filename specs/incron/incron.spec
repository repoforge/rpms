# $Id$
# Authority: dag

Summary: Inotify cron system
Name: incron
Version: 0.5.9
Release: 2%{?dist}
License: GPL
Group: System Environment/Base
URL: http://inotify.aiken.cz/

Source: http://inotify.aiken.cz/download/incron/incron-%{version}.tar.bz2
Patch0: incron-gcc44.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Requires(post):  /sbin/chkconfig
Requires(preun): /sbin/chkconfig, /sbin/service

%description
incron is an "inotify cron" system. incron consists of a daemon and a table
manipulator. One can use it a similar way as the regular cron, but the
difference is that the inotify cron handles filesystem events rather than
time periods.

%prep
%setup
%patch0 -p1 -b .cstdlib

%{__cat} <<'EOF' >incrond.sysv
#!/bin/bash
#
# Init file for incrond daemon
#
# Written by Dag Wieers <dag@wieers.com>
#
# chkconfig: - 97 03
# description: Filesystem event daemon, works like cron, but handles filesystem events
#              instead of time periods and can send notifications via mail, dbus
#              or syslog.
#
# processname: incrond
# config: %{_sysconfdir}/incrond.conf
# pidfile: %{_localstatedir}/run/incrond.pid

source %{_initrddir}/functions

RETVAL=0
prog="incrond"
desc="Filesystem event daemon"

start() {
    echo -n $"Starting $desc ($prog): "
    daemon $prog
    RETVAL=$?
    echo
    [ $RETVAL -eq 0 ] && touch %{_localstatedir}/lock/subsys/$prog
}

stop() {
    echo -n $"Shutting down $desc ($prog): "
    killproc $prog
    echo
    [ $RETVAL -eq 0 ] && rm -f %{_localstatedir}/lock/subsys/$prog
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
  restart|force-reload|reload)
    restart
    ;;
  condrestart)
    [ -f /var/lock/subsys/incrond ] && restart
    ;;
  status)
    status incrond
    RETVAL=$?
    ;;
  *)
    echo $"Usage: $0 {start|stop|status|restart|reload|force-reload|condrestart}"
    exit 1
esac

exit $RETVAL
EOF

%build
%{__make} %{?_smp_mflags} CXXFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}

#%{__make} install DESTDIR="%{buildroot}"

#install files manually since source Makefile tries to do it as root
%{__install} -Dp -m0755 incrond %{buildroot}%{_sbindir}/incrond
%{__install} -Dp -m4755 incrontab %{buildroot}%{_bindir}/incrontab
%{__install} -Dp -m0755 incrond.sysv %{buildroot}%{_initrddir}/incrond
%{__install} -Dp -m0644 incron.conf.example %{buildroot}%{_sysconfdir}/incron.conf
%{__install} -d %{buildroot}%{_sysconfdir}/incron.d/
%{__install} -d %{buildroot}%{_localstatedir}/spool/incron/

# install manpages
make install-man MANPATH="%{buildroot}%{_mandir}" INSTALL="install -D -p"

%post
if [ $1 -eq 1 ]; then
    /sbin/chkconfig --add incrond
fi

%preun
if [ $1 -eq 0 ]; then
    /sbin/service incrond stop &>/dev/null || :
    /sbin/chkconfig --del incrond
fi

%postun
if [ $1 -ge 1 ]; then
    /sbin/service incrond condrestart &>/dev/null || :
fi

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGELOG COPYING LICENSE-* README TODO incron.conf.example
%doc %{_mandir}/man1/incrontab.1*
%doc %{_mandir}/man5/incrontab.5*
%doc %{_mandir}/man5/incron.conf.5*
%doc %{_mandir}/man8/incrond.8*
%config(noreplace) %{_sysconfdir}/incron.conf
%config %{_initrddir}/incrond
%{_sbindir}/incrond
%dir %{_localstatedir}/spool/incron/
%dir %{_sysconfdir}/incron.d/

%defattr(4755, root, root, 0755)
%{_bindir}/incrontab

%changelog
* Mon Mar 07 2011 Yury V. Zaytsev <yury@shurup.com> - 0.5.9-2
- Fixed build failure on EL6 (thanks to Paul Evans!)

* Wed Jun 24 2009 Dag Wieers <dag@wieers.com> - 0.5.9-1
- Updated to release 0.5.9.

* Tue Jan 06 2009 Dag Wieers <dag@wieers.com> - 0.5.8-1
- Updated to release 0.5.8.

* Fri Mar 28 2008 Dag Wieers <dag@wieers.com> - 0.5.7-2
- Fixed typo in initscript.

* Thu Mar 27 2008 Dag Wieers <dag@wieers.com> - 0.5.7-1
- Initial package. (using DAR)
