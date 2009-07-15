# $Id$
# Authority: dag

%define logmsg logger -t %{name}/rpm

Summary: Universal Plug'nPlay (uPNP) Media Server
Name: ushare
Version: 1.1a
Release: 3
License: GPL
Group: Applications/Multimedia
URL: http://ushare.geexbox.org/

Source: http://ushare.geexbox.org/releases/ushare-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: pkgconfig >= 0.9.0, libupnp-devel, libdlna-devel
Requires(post): /sbin/chkconfig
Requires(preun): /sbin/service, /sbin/chkconfig
Requires(postun): /sbin/service

%description
uShare is a UPnP (TM) A/V Media Server. It implements the server 
component that provides UPnP media devices with information on 
available multimedia files. uShare uses the built-in http server 
of libupnp to stream the files to clients.

%prep
%setup

%{__cat} <<'EOF' >ushare.sysv
#!/bin/bash
#
# Init file for uShare UPnP Media Server
#
# Written by Dag Wieers <dag@wieers.com>
#
# chkconfig: - 54 46
# description: uShare UPnP Media Server
#
# processname: ushare
# config: %{_sysconfdir}/ushare.conf
# pidfile: %{_localstatedir}/run/ushare

source %{_initrddir}/functions

OPTIONS=""

[ -x %{_bindir}/ushare ] || exit 1
[ -r "%{_sysconfdir}/ushare.conf" ] && source %{_sysconfdir}/ushare.conf
[ -z "$USHARE_DIR" ] && exit 0

RETVAL=0
prog="ushare"
desc="UPnP Media Server"

start() {
    echo -n $"Starting $desc ($prog): "
    daemon --user ushare $prog -D $OPTIONS
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
./configure \
    --prefix="%{_prefix}" \
    --sysconfdir="%{_sysconfdir}" \
    --enable-dlna
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

%{__install} -Dp -m0755 ushare.sysv %{buildroot}%{_initrddir}/ushare
%{__install} -Dp -m0644 src/ushare.1 %{buildroot}%{_mandir}/man1/ushare.1
%{__install} -d -m0755 %{buildroot}%{_localstatedir}/lib/ushare/

%pre
if ! /usr/bin/id ushare &>/dev/null; then
    /usr/sbin/useradd -r -M -d %{_localstatedir}/lib/ushare -s /sbin/nologin -c "ushare service accoung" ushare || \
        %logmsg "Unexpected error adding user \"ushare\". Aborting installation."
fi

%post
/sbin/chkconfig --add ushare

%preun
if [ $1 -eq 0 ]; then
    /sbin/service ushare stop &>/dev/null || :
    /sbin/chkconfig --del ushare
fi

%postun
if [ $1 -eq 0 ]; then 
    /usr/sbin/userdel ushare || %logmsg "User \"ushare\" could not be deleted."
    /usr/sbin/groupdel ushare || %logmsg "Group \"ushare\" could not be deleted."
fi
if [ $1 -ge 1 ]; then
    /sbin/service ushare condrestart &>/dev/null || :
fi

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README
%doc %{_mandir}/man1/ushare.1*
%config(noreplace) %{_sysconfdir}/ushare.conf
%config %{_initrddir}/ushare
%{_bindir}/ushare

%defattr(-, ushare, ushare, 0770)
%{_localstatedir}/lib/ushare/

%exclude %{_sysconfdir}/init.d/ushare

%changelog
* Tue Jul 14 2009 Dag Wieers <dag@wieers.com> - 1.1a-3
- Rebuild against ffmpeg-0.5.

* Mon Dec 17 2007 Dag Wieers <dag@wieers.com> - 1.1a-2
- Rebuild against libupnp 1.6.x.

* Tue Dec 11 2007 Dag Wieers <dag@wieers.com> - 1.1a-1
- Updated to release 1.1a.

* Fri Nov 23 2007 Dag Wieers <dag@wieers.com> - 1.1-1
- Updated to release 1.1.

* Fri Jul 06 2007 Dag Wieers <dag@wieers.com> - 1.0-1
- Updated to release 1.0.

* Thu Mar 01 2007 Dag Wieers <dag@wieers.com> - 0.9.10-1
- Updated to release 0.9.10.

* Wed Feb 21 2007 Dag Wieers <dag@wieers.com> - 0.9.8-1
- Initial package. (using DAR)
