# $Id$

# Authority: dag

### FIXME: usermod -G nagios apache removes other groups.

%define rname nsca

Summary: Nagios Service Check Acceptor
Name: nagios-nsca
Version: 2.4
Release: 2
License: GPL
Group: Applications/Internet
URL: http://www.nagios.org/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/nagios/nsca-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


%{?!rh62:BuildRequires: libmcrypt-devel}
Provides: nsca
Obsoletes: nsca, netsaint-nsca

%description
The purpose of this addon is to allow you to execute NetSaint/Nagios
plugins on a remote host in as transparent a manner as possible.

%prep
%setup -n %{rname}-%{version} 

%{__perl} -pi.orig -e '
		s|^(command_file)=\@localstatedir\@/rw/nagios.cmd|$1=%{_localstatedir}/spool/nagios/nagios.cmd|;
		s|^(alternate_dump_file)=\@localstatedir\@/rw/nsca.dump|$1=%{_localstatedir}/spool/nagios/nsca.dump|;
	' nsca.cfg.in

%{__cat} <<EOF >nsca.xinetd.dag
# default: off
# description: NSCA (Nagios Service Check Acceptor)
service nsca
{
        flags           = REUSE
	type		= UNLISTED
	port		= 5667
        socket_type     = stream
        wait            = no
        user            = nagios
        group           = nagios
        server          = %{_sbindir}/nsca
        server_args     = -c %{_sysconfdir}/nagios/nsca.cfg --inetd
        log_on_failure  += USERID
        disable         = yes
        only_from       = 127.0.0.1
}
EOF

%{__cat} <<'EOF' >nsca.sysv
#!/bin/bash
#
# Init file for Nagios NRPE
#
# Written by Dag Wieers <dag@wieers.com>.
#
# chkconfig: - 80 20
# description: Nagios NSCA daemon
#
# processname: nsca
# config: %{_sysconfdir}/nagios/nsca.cfg
# pidfile: %{_localstatedir}/run/nsca

source %{_initrddir}/functions

### Default variables
CONFIG="%{_sysconfdir}/nagios/nsca.cfg"

[ -x %{_sbindir}/nsca ] || exit 1
[ -r "$CONFIG" ] || exit 1

RETVAL=0
prog="nsca"
desc="Nagios NSCA daemon"

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
	--with-nsca-user="nagios" \
        --with-nsca-grp="nagios" \
        --with-nsca-port="5667"

%{__make} %{?_smp_mflags} all

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_sbindir} \
			%{buildroot}%{_sysconfdir}/nagios/ \
			%{buildroot}%{_initrddir} \
			%{buildroot}%{_sysconfdir}/xinetd.d/ \
			%{buildroot}%{_localstatedir}/spool/nagios/
%{__install} -m0755 src/nsca %{buildroot}%{_sbindir}
%{__install} -m0755 src/send_nsca %{buildroot}%{_sbindir}
%{__install} -m0644 nsca.cfg %{buildroot}%{_sysconfdir}/nagios/
%{__install} -m0644 send_nsca.cfg %{buildroot}%{_sysconfdir}/nagios/
%{__install} -m0755 nsca.sysv %{buildroot}%{_initrddir}/nsca
%{__install} -m0644 nsca.xinetd.dag %{buildroot}%{_sysconfdir}/xinetd.d/nsca

%post
/sbin/chkconfig --add nsca

%preun
if [ $1 -eq 0 ]; then
        /sbin/service nsca stop &>/dev/null || :
        /sbin/chkconfig --del nsca
fi

%postun
/sbin/service nsca condrestart &>/dev/null || :

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changelog LEGAL README SECURITY
%config(noreplace) %{_sysconfdir}/nagios/
%config(noreplace) %{_sysconfdir}/xinetd.d/nsca
%config %{_initrddir}/nsca
%dir %{_localstatedir}/spool/nagios/
%{_sbindir}/*

%changelog
* Tue Nov 11 2003 Dag Wieers <dag@wieers.com> - 2.4-2
- Fixed command_file and alternate_dump_file in nsca.cfg. (Johan Krisar)
- Removed the nagios dependency. (Johan Krisar)
- Added %%{_localstatedir}/spool/nagios/ as directoriy to filelist.

* Mon Oct 27 2003 Dag Wieers <dag@wieers.com> - 2.4-1
- Fixed default port and xinetd file. (Shad L. Lords)

* Mon Oct 06 2003 Dag Wieers <dag@wieers.com> - 2.4-0
- Initial package. (using DAR)
