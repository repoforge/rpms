# Authority: dag

%define rname nrpe

Summary: Nagios Remote Plug-ins Execution daemon.
Name: nagios-nrpe
Version: 2.0
Release: 1
License: GPL
Group: Applications/Internet
URL: http://www.nagios.org/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/nagios/%{rname}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: openssl-devel, krb5-devel
Provides: nrpe
Obsoletes: nrpe, netsaint-nrpe

%description
The nagios-nrpe packages contains the Nagios Remote Plug-ins Executor
-- daemon which can execute predefined commands on the remote host.
Execution request is send via check_nrpe Nagios plug-in. Allowed
monitoring commands are described in the daemon configuration file.

Install the nagios-nrpe package if you want accept and process requests
from check_nrpe on this hosts.

%package -n nagios-plugins-nrpe
Summary: Nagios plug-in for NRPE.
Group: Applications/Internet
Requires: nagios

%description -n nagios-plugins-nrpe
Plug-in for Nagios monitoring system. With this plug-in you can send check
request to remote host, with installed NRPE, and process result of execution
as host or service state.

%prep
%setup -n %{rname}-%{version}

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
	--libexecdir="%{_libdir}/nagios/plugins" \
	--enable-command-args \
	--with-nrpe-user="nagios" \
	--with-nrpe-grp="nagios" \
	--with-nrpe-port="5666"
%{__make} %{?_smp_mflags}

%install
%{__install} -d -m0755 %{buildroot}%{_sysconfdir}/nagios/ \
			%{buildroot}%{_sbindir} \
			%{buildroot}%{_libdir}/nagios/plugins/ \
			%{buildroot}%{_initrddir} \
			%{buildroot}%{_sysconfdir}/xinetd.d/
%{__install} -m0711 src/nrpe %{buildroot}%{_sbindir}
%{__install} -m0711 src/check_nrpe %{buildroot}%{_libdir}/nagios/plugins/
%{__install} -m0644 nrpe.cfg %{buildroot}%{_sysconfdir}/nagios/
%{__install} -m0755 nrpe.sysv %{buildroot}%{_initrddir}/nrpe
%{__install} -m0644 nrpe.xinetd.dag %{buildroot}%{_sysconfdir}/xinetd.d/nrpe

%post
/sbin/chkconfig --add nrpe

%preun
if [ $1 -eq 0 ]; then
        /sbin/service nrpe stop &>/dev/null || :
        /sbin/chkconfig --del nrpe
fi

%postun
/sbin/service nrpe condrestart &>/dev/null || :

%files
%defattr(-, root, root, 0755)
%doc Changelog LEGAL README
%config(noreplace) %{_sysconfdir}/nagios/
%config(noreplace) %{_sysconfdir}/xinetd.d/nrpe
%config %{_initrddir}/nrpe
%{_sbindir}/*

%files -n nagios-plugins-nrpe
%defattr(-, root, root, 0755)
%doc Changelog LEGAL README
%{_libdir}/nagios/plugins/

%changelog
* Tue Nov 06 2003 Dag Wieers <dag@wieers.com> - 2.0-2
- Removed the nagios dependency. (Johan Krisar)

* Mon Oct 27 2003 Dag Wieers <dag@wieers.com> - 2.0-1
- Fixed default port, xinetd file and --enable-command-args. (Shad L. Lords)

* Mon Oct 06 2003 Dag Wieers <dag@wieers.com> - 2.0-0
- Initial package. (using DAR)
