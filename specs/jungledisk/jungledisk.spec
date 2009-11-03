# $Id$
# Authority: dag

%{?dtag: %{expand: %%define %dtag 1}}

%{?el5:%define _with_junglediskmonitor 1}
%{?el4:%define _with_junglediskmonitor 1}

Summary: Store files and backup data securely to Amazon.com's S3 Storage Service
Name: jungledisk
Version: 1.46
Release: 2%{?dist}
License: GPL
Group: System Environment/Daemons
URL: http://jungledisk.com/

Source: http://downloads.jungledisk.com/jungledisk/jungledisk.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

ExclusiveArch: i386

%description
Jungle Disk is an application that lets you store files and backup
data securely to Amazon.com's S3 Storage Service.

 * Store an unlimited amount of data for only 15¢ per gigabyte
 * No monthly subscription fee, no startup fee, no commitment
 * Your data is fully encrypted at all times
 * Data is stored at multiple Amazon.com datacenters around the country
   for high availability
 * Access files directly from Windows Explorer, Mac OSX Finder, and Linux
 * Automatically backup your important files quickly and easily

%package -n junglediskmonitor
Summary: Store files and backup data securely to Amazon.com's S3 Storage Service
Group: Applications/Archiving

%description -n junglediskmonitor
Jungle Disk is an application that lets you store files and backup
data securely to Amazon.com's S3 Storage Service.

 * Store an unlimited amount of data for only 15¢ per gigabyte
 * No monthly subscription fee, no startup fee, no commitment
 * Your data is fully encrypted at all times
 * Data is stored at multiple Amazon.com datacenters around the country
   for high availability
 * Access files directly from Windows Explorer, Mac OSX Finder, and Linux
 * Automatically backup your important files quickly and easily

%prep
%setup -n %{name}

%{__cat} <<EOF >jungledisk-settings.ini
### Sample config file for jungledisk
LoginUsername=
LoginPassword=
AccessKeyID=
SecretKey=
Bucket=default
CacheDirectory=%{_localstatedir}/jungledisk
ListenPort=2667
CacheCheckInterval=120
AsyncOperations=1
Encrypt=1
ProxyServer=
EncryptionKey=PROTECTED:
DecryptionKeys=PROTECTED:
MaxCacheSize=1000
MapDrive=
UseSSL=0
RetryCount=10
FastCopy=1
WebAccess=0
LogDuration=30
License=
EOF

%{__cat} <<EOF >jungledisk.logrotate
%{_localstatedir}/log/jungledisk.log {
    missingok
    copytruncate
    notifempty
}
EOF

%{__cat} <<'EOF' >jungledisk.sysv
#!/bin/bash
#
# Init file for Jungledisk backup daemon
#
# Written by Dag Wieers <dag@wieers.com>
#
# chkconfig: - 54 46
# description: Jungledisk backup
#
# processname: jungledisk
# config: %{_sysconfdir}/jungledisk-settings.ini
# pidfile: %{_localstatedir}/run/jungledisk

source %{_initrddir}/functions

[ -x %{_bindir}/jungledisk ] || exit 1
[ -r %{_sysconfdir}/jungledisk-settings.ini ] || exit 1

RETVAL=0
prog="jungledisk"
desc="Jungledisk daemon"

start() {
    echo -n $"Starting $desc ($prog): "
    daemon $prog -c %{_sysconfdir}/jungledisk-settings.ini
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

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 jungledisk %{buildroot}%{_bindir}/jungledisk

%{__install} -Dp -m0600 jungledisk-settings.ini %{buildroot}%{_sysconfdir}/jungledisk-settings.ini
%{__install} -Dp -m0755 jungledisk.sysv %{buildroot}%{_initrddir}/jungledisk
%{__install} -Dp -m0755 jungledisk.logrotate %{buildroot}%{_sysconfdir}/logrotate.d/jungledisk

%{__install} -d -m0700 %{buildroot}%{_localstatedir}/cache/jungledisk/

%{?_with_junglediskmonitor:%{__install} -Dp -m0755 junglediskmonitor %{buildroot}%{_bindir}/junglediskmonitor}

%post
/sbin/chkconfig --add jungledisk

%preun
if [ $1 -eq 0 ]; then
    /sbin/service jungledisk stop &>/dev/null || :
    /sbin/chkconfig --del jungledisk
fi

%postun
/sbin/service jungledisk condrestart &>/dev/null || :
%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc INSTALL jungledisk-settings.ini
%config(noreplace) %{_sysconfdir}/jungledisk-settings.ini
%config(noreplace) %{_sysconfdir}/logrotate.d/jungledisk
%config %{_initrddir}/jungledisk
%{_bindir}/jungledisk
%dir %{_localstatedir}/cache/jungledisk/

%if %{?_with_junglediskmonitor:1}0
%files -n junglediskmonitor
%defattr(-, root, root, 0755)
%doc INSTALL jungledisk-settings.ini
%{_bindir}/junglediskmonitor
%endif

%changelog
* Sun Nov 11 2007 Dag Wieers <dag@wieers.com> - 1.46-2
- Fix group tag.

* Sat Nov 10 2007 Dag Wieers <dag@wieers.com> - 1.46-1
- Initial package. (using DAR)
