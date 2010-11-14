# $Id$
# Authority: dag

### FIXME: Too heavily integrated with Novell's product.
# Tag: rft

Summary: Network switching and control applet.
Name: netapplet
Version: 1.0.0
Release: 1.2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://primates.ximian.com/~rml/netapplet/

Source: http://primates.ximian.com/~rml/netapplet/netapplet-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk2-devel >= 2.4.0, glib2-devel >= 2.4.0
BuildRequires: wireless-tools, gnome-keyring-devel
BuildRequires: perl(XML::Parser), intltool
BuildRequires: libgnomeui-devel
Requires: wireless-tools

%description
Network switching and control applet.

%prep
%setup

%{__cat} <<'EOF' >netdaemon.sysv
#!/bin/bash
#
# Init file for netdaemon.
#
# Written by Dag Wieers <dag@wieers.com>.
#
# chkconfig: 345 54 46
# description: Network control and switching daemon
#
# processname: netdaemon
# pidfile: %{_localstatedir}/run/netdaemon

source %{_initrddir}/functions

[ -x %{_bindir}/netdaemon ] || exit 1

RETVAL=0
prog="netdaemon"
desc="Network control and switching daemon"

start() {
	echo -n $"Starting $desc ($prog): "
	daemon %{_bindir}/$prog
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
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%{__install} -Dp -m0755 netdaemon.sysv %{buildroot}%{_initrddir}/netdaemon

%post
/sbin/chkconfig --add netdaemon
/sbin/service netdaemon restart &>/dev/null

%preun
if [ $1 -eq 0 ]; then
	/sbin/service netdaemon stop &>/dev/null
	/sbin/chkconfig --del netdaemon
fi

%postun
if [ $1 -ne 0 ]; then
	/sbin/service netdaemon restart &>/dev/null
fi

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%exclude %{_sysconfdir}/init.d/netdaemon
%config %{_initrddir}/netdaemon
%{_bindir}/netapplet
%{_bindir}/netdaemon
%{_datadir}/applications/netapplet.desktop
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/icons/hicolor/*/stock/data/*.png
%{_datadir}/netapplet/
%{_datadir}/pixmaps/netapplet.png

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.0.0-1.2
- Rebuild for Fedora Core 5.

* Tue Dec 07 2004 Dag Wieers <dag@wieers.com> - 1.0.0-1
- Updated to release 1.0.0.

* Sun Aug 28 2004 Dag Wieers <dag@wieers.com> - 0.98.0-1
- Initial package. (using DAR)
