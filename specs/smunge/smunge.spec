# $Id$

# Authority: dag

# Upstream: Joshua Reich <josh@i2pi.com>

%define rversion 1.3.6

Summary: A funneling POP proxy
Name: smunge
Version: 1.3.6
Release: 0
License: GPL
Group: System Environment/Daemons
URL: http://www.i2pi.com/smunge/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.i2pi.com/smunge/%{name}-%{rversion}.tar.gz
Patch: smunge-hostent.patch
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: openldap-devel

%description
Smunge is a stand alone POP3 funneling proxy server, designed to allow
clients to attach to multiple pop servers as if they were one. Smunge can
be used to join together multiple mailboxes, or to present different users
with different mailboxes (depending on username). This allows for
administrators of pop servers to set up either load balancing or redundant
clusters for pop services.

It was initially designed to smooth over the transition of pop services
from one machine to another, without users losing mail (by keeping the
old server active whilst the new one was being installed). 

It also supports DRAC for pop-before-smtp authentication. Also featured is
support for LDAP based authentication and lookups for mapping users to sets
of pop servers.

%prep
%setup -n %{name}
%patch -p0

%{__cat} <<EOF >smunged.sysconfig
OPTIONS="-p 110 +localhost:2110"
SERVERS="+localhost:2110 +pop1.server,\"[a-k]*\" +pop2.server,\"[l-z]*\""
EOF

%{__cat} <<'EOF' >smunged.sysv
#!/bin/bash
#
# Startup script for smunge, a funneling POP proxy server.
#
# Written by Dag Wieers <dag@wieers.com>.
#
# chkconfig: - 80 20
# description: Smunge is a stand alone funneling POP proxy server, designed \
#	 to allow clients to attach to multiple pop servers as if they were one.
#
# processname: smunged
# config: %{_sysconfdir}/sysconfig/smunged
# pidfile: %{_localstatedir}/run/smunged

source %{_initrddir}/functions

### Default variables
OPTIONS=""
SERVERS=""

[ -x %{_sbindir}/smunged ] || exit 1
[ -r %{_sysconfdir}/sysconfig/smunged ] || exit 1
source %{_sysconfdir}/sysconfig/smunged

RETVAL=0
prog="smunged"
desc="POP proxy server"

start() {
	echo -n $"Starting $desc ($prog): "
	daemon $prog $SERVERS $OPTIONS
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

case "$1" in
  start)
	start
	;;
  stop)
	stop
	;;
  restart|reload)
	restart
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
	echo $"Usage: $0 {start|stop|restart|condrestart|status}"
	RETVAL=1
esac

exit $RETVAL
EOF

%build
#%{__make} CFLAGS="%{optflags} -DLINUX -DUSE_DRAC -DUSE_LDAP" LDFLAGS="-ldrac -llber -lldap"
%{__make} %{?_smp_mflags} \
	CFLAGS="%{optflags} -DLINUX -DUSE_LDAP" \
	LDFLAGS="-llber -lldap"

%install
%{__rm} -rf %{buildroot}
#makeinstall
%{__install} -d -m0755 %{buildroot}%{_sbindir} \
		%{buildroot}%{_sysconfdir}/sysconfig \
		%{buildroot}%{_initrddir}
%{__install} -m0755 smunged %{buildroot}%{_sbindir}
%{__install} -m0755 smunged.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/smunged
%{__install} -m0755 smunged.sysv %{buildroot}%{_initrddir}/smunged

%post
/sbin/chkconfig --add smunged

%preun
if [ $1 -eq 0 ]; then
	/sbin/service smunged stop &>/dev/null || :
	/sbin/chkconfig --del smunged
fi

%postun 
/sbin/service smunged condrestart &>/dev/null || :

%clean
%{__rm} -rf %{buildroot} 

%files
%defattr(-, root, root, 0755)
%doc LICENSE README rfc1734.txt rfc1939.txt
%config(noreplace) %{_sysconfdir}/sysconfig/smunged
%config %{_initrddir}/smunged
%{_sbindir}/*

%changelog
* Mon Dec 01 2003 Dag Wieers <dag@wieers.com> - 1.3.6.0-0
- Updated to release 1.3.6.

* Sun Feb 16 2003 Dag Wieers <dag@wieers.com> - 1.3.6a-0
- SPEC file cleanup.
- Added LDAP support.

* Thu Feb  1 2001 Bert de Bruijn <bert@debruijn.be> - 1.3.5-1
- main.c patch (malloc size + 1)

* Sat Nov 18 2000 Dag Wieers <dag@wieers.com> - 1.3.5-0
- Initial package.
- Built for Red Hat 6.x and 7.0
