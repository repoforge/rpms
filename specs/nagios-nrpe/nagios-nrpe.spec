# $Id$
# Authority: dag
# Upstream: Ethan Galstad <nagios$nagios,org>

%define logmsg logger -t %{name}/rpm

%define real_name nrpe

Summary: Nagios Remote Plug-ins Execution daemon
Name: nagios-nrpe
Version: 2.12
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://www.nagios.org/

Source: http://dl.sf.net/nagios/nrpe-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: openssl-devel, krb5-devel
Provides: nrpe
Obsoletes: nrpe, netsaint-nrpe
Requires: bash, grep, nagios-plugins
#Conflicts: nagios

%description
The nagios-nrpe packages contains the Nagios Remote Plug-ins Executor
-- daemon which can execute predefined commands on the remote host.
Execution request is send via check_nrpe Nagios plug-in. Allowed
monitoring commands are described in the daemon configuration file.

Install the nagios-nrpe package if you want accept and process requests
from check_nrpe on this hosts.

%package -n nagios-plugins-nrpe
Summary: Nagios plug-in for NRPE
Group: Applications/Internet
Requires: nagios, nagios-plugins
Obsoletes: nrpe-plugins

%description -n nagios-plugins-nrpe
Plug-in for Nagios monitoring system. With this plug-in you can send check
request to remote host, with installed NRPE, and process result of execution
as host or service state.

%prep
%setup -n %{real_name}-%{version}

%{__cat} <<EOF >nrpe.xinetd.dag
# default: off
# description: NRPE (Nagios Remote Plugin Executor)
service nrpe
{
        flags           = REUSE
	type		= UNLISTED
	port		= 5666
        socket_type     = stream
        wait            = no
        user            = nagios
        group           = nagios
        server          = %{_sbindir}/nrpe
        server_args     = -c %{_sysconfdir}/nagios/nrpe.cfg --inetd
        log_on_failure  += USERID
        disable         = yes
        only_from       = 127.0.0.1
}
EOF

%{__cat} <<'EOF' >nrpe.sysv
#!/bin/bash
#
# Init file for Nagios NRPE
#
# Written by Dag Wieers <dag@wieers.com>.
#
# chkconfig: - 80 20
# description: Nagios NRPE daemon
#
# processname: nrpe
# config: %{_sysconfdir}/nagios/nrpe.cfg
# pidfile: %{_localstatedir}/run/nrpe

source %{_initrddir}/functions

### Default variables
CONFIG="%{_sysconfdir}/nagios/nrpe.cfg"

[ -x %{_sbindir}/nrpe ] || exit 1
[ -r "$CONFIG" ] || exit 1

RETVAL=0
prog="nrpe"
desc="Nagios NRPE daemon"

start() {
	echo -n $"Starting $desc ($prog): "
	daemon $prog -c "$CONFIG" -d
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
%configure \
	--datadir="%{_datadir}/nagios" \
	--libexecdir="%{_libdir}/nagios/plugins" \
	--localstatedir="%{_localstatedir}/log/nagios" \
	--sbindir="%{_libdir}/nagios/cgi" \
	--sysconfdir="%{_sysconfdir}/nagios" \
	--enable-command-args \
	--with-init-dir="%{_initrddir}" \
	--with-nrpe-user="nagios" \
	--with-nrpe-group="nagios" \
	--with-nrpe-port="5666"
%{__make} %{?_smp_mflags} all

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0711 src/nrpe %{buildroot}%{_sbindir}/nrpe
%{__install} -Dp -m0711 src/check_nrpe %{buildroot}%{_libdir}/nagios/plugins/check_nrpe
%{__install} -Dp -m0644 sample-config/nrpe.cfg %{buildroot}%{_sysconfdir}/nagios/nrpe.cfg
%{__install} -Dp -m0755 nrpe.sysv %{buildroot}%{_initrddir}/nrpe
#%{__install} -Dp -m0755 init-script %{buildroot}%{_initrddir}/nrpe
%{__install} -Dp -m0644 nrpe.xinetd.dag %{buildroot}%{_sysconfdir}/xinetd.d/nrpe

%pre
if ! /usr/bin/id nagios &>/dev/null; then
	/usr/sbin/useradd -r -d %{_localstatedir}/log/nagios -s /bin/sh -c "nagios" nagios || \
		%logmsg "Unexpected error adding user \"nagios\". Aborting installation."
fi

%post
/sbin/chkconfig --add nrpe

%preun
if [ $1 -eq 0 ]; then
	/sbin/service nrpe stop &>/dev/null || :
	/sbin/chkconfig --del nrpe
fi

%postun
if [ $1 -eq 0 ]; then
	/usr/sbin/userdel nagios || %logmsg "User \"nagios\" could not be deleted."
	/usr/sbin/groupdel nagios || %logmsg "Group \"nagios\" could not be deleted."
fi
/sbin/service nrpe condrestart &>/dev/null || :

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changelog LEGAL README
%config(noreplace) %{_sysconfdir}/nagios/
%config(noreplace) %{_sysconfdir}/xinetd.d/nrpe
%config %{_initrddir}/nrpe
%{_sbindir}/nrpe
%dir %{_libdir}/nagios/
%dir %{_libdir}/nagios/plugins/

%files -n nagios-plugins-nrpe
%defattr(-, root, root, 0755)
%doc Changelog LEGAL README
%dir %{_libdir}/nagios/
%{_libdir}/nagios/plugins/

%changelog
* Tue Mar  3 2009 Ville Mattila <vmattila@csc.fi> - 2.12-1
- Updated to release 2.12.

* Mon Dec 11 2006 Dag Wieers <dag@wieers.com> - 2.5.2-1
- Updated to release 2.5.2.

* Mon May 29 2006 Dag Wieers <dag@wieers.com> - 2.5.1-1
- Updated to release 2.5.1.

* Wed Feb 08 2006 Dag Wieers <dag@wieers.com> - 2.3-2
- Fixed wrong -s option and sysv problem on some dists. (Rick Johnson)

* Wed Feb 08 2006 Dag Wieers <dag@wieers.com> - 2.3-1
- Updated to release 2.3.

* Sat Aug 06 2005 Dag Wieers <dag@wieers.com> - 2.0-4
- Added nagios user-creation. (Jamie Wilkinson)
- Conflicts nagios-nrpe with nagios. (Jesse Keating)

* Mon Apr 26 2004 Dag Wieers <dag@wieers.com> - 2.0-3
- Added nagios-plugins requirement. (Jamie Wilkinson)

* Tue Nov 06 2003 Dag Wieers <dag@wieers.com> - 2.0-2
- Removed the nagios dependency. (Johan Krisar)

* Mon Oct 27 2003 Dag Wieers <dag@wieers.com> - 2.0-1
- Fixed default port, xinetd file and --enable-command-args. (Shad L. Lords)

* Mon Oct 06 2003 Dag Wieers <dag@wieers.com> - 2.0-0
- Initial package. (using DAR)
