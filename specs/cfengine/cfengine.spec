# $Id$

# Authority: dag
# Upstream: Mark Burgess <Mark.Burgess@iu.hio.no>

### FIXME: configure has problems finding flex output using soapbox on RHEL3
# Soapbox: 0

Summary: System administration tool for networks
Name: cfengine
Version: 2.1.1
Release: 0
License: GPL
Group: System Environment/Base
URL: http://www.cfengine.org/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: ftp://ftp.iu.hio.no/pub/cfengine/cfengine-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: bison, flex, m4, openssl-devel, tetex
%{?rhfc1:BuildRequires: db4-devel}
%{?rhel3:BuildRequires: db4-devel}
%{?rh90:BuildRequires: db4-devel}
%{?rh80:BuildRequires: db4-devel}
%{?rh73:BuildRequires: db3-devel}
%{?rhel21:BuildRequires: db3-devel}
%{?rh62:BuildRequires: db3-devel}

%description
Cfengine, or the configuration engine is an agent/software robot and a
very high level language for building expert systems to administrate
and configure large computer networks. Cfengine uses the idea of
classes and a primitive form of intelligence to define and automate
the configuration and maintenance of system state, for small to huge
configurations. Cfengine is designed to be a part of a computer immune
system.

%prep
%setup

%{__cat} <<'EOF' >cfexecd.sysv
#!/bin/bash
#
# Init file for the cfengine client daemon
#
# chkconfig: 2345 98 20
# description: cfexecd is scheduler and reporter in cfengine client hosts.
#
# processname: cfexecd
# config: %{_localstatedir}/cfengine/inputs
# pidfile: %{_localstatedir}/run/cfengine

# Source function library.
. %{_initrddir}/functions

RETVAL=0
prog="cfexecd"
desc="cfengine client daemon"

start() {
	echo -n $"Starting $desc ($prog): "
	daemon $prog
	RETVAL=$?
	echo
	[ $RETVAL -eq 0 ] && touch %{_localstatedir}/lock/subsys/$prog
	return $RETVAL
}

stop() {
	echo -n $"Stopping $desc ($prog): "
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
  restart)
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

%{__cat} <<'EOF' >cfservd.sysv
#!/bin/bash
#
# Init file for the cfengine server daemon
#
# chkconfig: 2345 96 20
# description: cfservd is responsible for giving out configuration files to
#              those cfengine clients, who wish to update their configs.
#
# processname: cfservd
# config: %{_localstatedir}/cfengine/masterfiles
# pidfile: %{_localstatedir}/run/cfengine

# Source function library.
. %{_initrddir}/functions

RETVAL=0
prog="cfservd"
desc="cfengine server daemon"

start() {
	echo -n $"Starting $desc ($prog): "
	if [ ! -f %{_localstatedir}/cfengine/ppkeys/localhost.priv ]; then
	    /usr/sbin/cfkey
	fi
	daemon $prog
	RETVAL=$?
	echo
	[ $RETVAL -eq 0 ] && touch %{_localstatedir}/lock/subsys/$prog
	return $RETVAL
}

stop() {
	echo -n $"Stopping $desc ($prog): "
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
  restart)
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
%configure BERKELEY_DB_LIB="-ldb" \
	--program-prefix="%{?_program_prefix}" \
	--disable-dependency-tracking
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_sbindir} \
			%{buildroot}%{_datadir}/cfengine \
			%{buildroot}%{_localstatedir}/cfengine/inputs \
			%{buildroot}%{_localstatedir}/cfengine/bin \
			%{buildroot}%{_initrddir}
%makeinstall
%{__install} -m0755 cfexecd.sysv %{buildroot}%{_initrddir}/cfexecd
%{__install} -m0755 cfservd.sysv %{buildroot}%{_initrddir}/cfservd
%{__ln_s} -f %{_sbindir}/cfagent %{buildroot}%{_localstatedir}/cfengine/bin/

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_datadir}/cfengine/
%{__rm} -f %{buildroot}%{_infodir}/dir

%post
%{_sbindir}/cfkey &>/dev/null || :
/sbin/install-info %{_infodir}/cfengine*.info.gz %{_infodir}/dir

if [ "$1" = "1" ]; then
	chkconfig --add cfenvd
	chkconfig --add cfexecd
	chkconfig --add cfservd
fi

%preun
/sbin/install-info --delete %{_infodir}/cfengine*.info.gz %{_infodir}/dir

if [ "$1" = "0" ]; then
	chkconfig --del cfenvd
	chkconfig --del cfexecd
	chkconfig --del cfservd
fi

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING DOCUMENTATION NEWS README TODO
%doc contrib/cfengine.el doc/*.html inputs/*
%doc %{_mandir}/man?/*
%doc %{_infodir}/*
%config %{_initrddir}/*
%{_sbindir}/*
%{_localstatedir}/cfengine/

%changelog
* Sat Jan 31 2004 Dag Wieers <dag@wieers.com> - 2.1.1-0
- Updated to release 2.1.1.

* Wed Sep 03 2003 Dag Wieers <dag@wieers.com> - 2.0.6-3
- Added --program-prefix for RH73. (Soren Roug)

* Thu Jun 12 2003 Dag Wieers <dag@wieers.com> - 2.0.6-2
- Fix install-info and moved documentation. (Terje Rosten)

* Fri Apr 25 2003 Dag Wieers <dag@wieers.com> - 2.0.6-0
- Initial package. (using DAR)
