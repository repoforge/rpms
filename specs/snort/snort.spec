# $Id$

# Authority: dag
# Upstream: Marty Roesch <roesch@sourcefire.com>

%define mysql 1
%define pgsql 1
%define odbc 1
%define bloat 1
%{?rhel3:%undefine pgsql}
%{?rhel3:%undefine odbc}

Summary: Open Source network intrusion detection system.
Name: snort
Version: 2.1.1
Release: 0
License: GPL
Group: Applications/Internet
URL: http://www.snort.org/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.snort.org/releases/snort-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: libpcap >= 0.4, mysql-devel, openssl-devel, libnet = 1.0.2
BuildRequires: pcre-devel, perl
%{?rhfc1:BuildRequires: net-snmp-devel, postgresql-devel, unixODBC-devel}
%{?rhel3:BuildRequires: net-snmp-devel}
%{?rh90:BuildRequires: net-snmp-devel, postgresql-devel, unixODBC-devel}
%{?rh80:BuildRequires: net-snmp-devel, postgresql-devel, unixODBC-devel}
%{?rh73:BuildRequires: ucd-snmp-devel, postgresql-devel, unixODBC-devel}
%{?rhel21:BuildRequires: ucd-snmp-devel, postgresql-devel, unixODBC-devel}

%description
Snort is a libpcap-based packet sniffer/logger which 
can be used as a lightweight network intrusion detection system. 
It features rules based logging and can perform protocol analysis, 
content searching/matching and can be used to detect a variety of 
attacks and probes, such as buffer overflows, stealth port scans, 
CGI attacks, SMB probes, OS fingerprinting attempts, and much more. 

Snort has a real-time alerting capabilty, with alerts being sent to syslog, 
a seperate "alert" file, or as a WinPopup message via Samba's smbclient

This package has no database support.

%package mysql
Summary: Snort with MySQL support.
Group: Applications/Internet
Requires: snort = %{version}-%{release}
Obsoletes: snort-postgresql, snort-odbc, snort-bloat

%description mysql
Snort compiled with mysql support.

%package postgresql
Summary: Snort with PostgreSQL support.
Group: Applications/Internet
Requires: snort = %{version}-%{release}
Obsoletes: snort-mysql, snort-odbc, snort-bloat

%description postgresql
Snort compiled with PostgreSQL support. 

%package odbc
Summary: Snort with ODBC support.
Group: Applications/Internet
Requires: snort = %{version}-%{release}
Obsoletes: snort-mysql, snort-postgresql, snort-bloat

%description odbc
Snort compiled with ODBC support. 

%package bloat
Summary: Snort with MySQL, PostgreSQL and ODBC support.
Group: Applications/Internet
Requires: snort = %{version}-%{release}
Obsoletes: snort-mysql, snort-postgresql, snort-odbc

%description bloat
Snort compiled with MySQL, PostgreSQL and ODBC support.
Requires snort libnet rpm.

%prep
%setup

%{__cat} <<EOF >snort.sysconf
### Specify your network interface here
INTERFACE="eth0"

### Add extra options here
#OPTIONS="-s -d"
EOF

%{__cat} <<'EOF' >snortd.sysv
#!/bin/sh
#
# Init file for Snort - An Open Source network intrusion detection system.
#
# Written by Dag Wieers <dag@wieers.com>.
#
# chkconfig: 2345 40 60
# description:  snort is a lightweight network intrusion detection system \
#               that currently detects more than 1100 host and network \
#		vulnerabilities, portscans, backdoors, and more.
#
# processname: snort
# config: %{_sysconfdir}/sysconfig/snort
# config: %{_sysconfdir}/snort/snort.conf
# pidfile: %{_localstatedir}/lock/subsys/snort.pid

source %{_initrddir}/functions
source %{_sysconfdir}/sysconfig/network

### Check that networking is up.
[ "${NETWORKING}" == "no" ] && exit 0

[ -x %{_sbindir}/snort ] || exit 1
[ -r %{_sysconfdir}/snort/snort.conf ] || exit 1

### Default variables
SYSCONFIG="%{_sysconfdir}/sysconfig/snort"
OPTIONS="-s -d"
INTERFACE="eth0"
USER="snort"

### Read configuration
[ -r "$SYSCONFIG" ] && source "$SYSCONFIG"

RETVAL=0
prog="snort"
desc="Intrusion Detection System"

start() {
	echo -n $"Starting $desc ($prog): "
	cd %{_localstatedir}/log/snort
	daemon $prog -u $USER -g $USER -D -i $INTERFACE -l %{_localstatedir}/log/snort -c %{_sysconfdir}/snort/snort.conf $OPTIONS
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

dump() {
	echo -n $"Dumping $prog database to syslog: "
	killproc $prog -USR1
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
  dump)
	dump
	;;
  *)
	echo $"Usage: $0 {start|stop|restart|reload|condrestart|status|dump}"
	RETVAL=1
esac

exit $RETVAL
EOF

%build
#touch -r . *
### Ugly workaround
#%{__perl} -pi.orig -e 's|^DIST_SOURCES|#DIST_SOURCES|' doc/Makefile.am
#%{__aclocal}
#%{__automake} --add-missing
#%{__rm} -rf building && mkdir -p building && cd building

export AM_CFLAGS="%{optflags}"
SNORT_BASE_CONFIG="
	--prefix=%{_prefix}
	--bindir=%{_sbindir}
	--sysconfdir=%{_sysconfdir}/snort
	--enable-flexresp2
	--with-openssl
	--with-libpcap-includes=%{_includedir}/pcap
	--without-oracle
"
#	--with-snmp="%{_includedir}/ucd-snmp"

mkdir plain; cd plain
../configure $SNORT_BASE_CONFIG \
	--without-mysql \
	--without-postgresql \
	--without-odbc
%{__make} %{?_smp_mflags}
%{__mv} -f src/snort ../snort-plain
cd -

%if %{?mysql:1}%{!?mysql:0}
mkdir mysql; cd mysql
../configure $SNORT_BASE_CONFIG \
	--with-mysql \
	--without-postgresql \
	--without-odbc
%{__make} %{?_smp_mflags}
%{__mv} src/snort ../snort-mysql
cd -
%endif

%if %{?pgsql:1}%{!?pgsql:0}
mkdir pgsql; cd pgsql
../configure $SNORT_BASE_CONFIG \
	--without-mysql \
	--with-postgresql \
	--without-odbc
%{__make} %{?_smp_mflags}
%{__mv} -f src/snort ../snort-pgsql
cd -
%endif

%if %{?odbc:1}%{!?odbc:0}
mkdir odbc; cd odbc
../configure $SNORT_BASE_CONFIG \
	--without-mysql \
	--without-postgresql \
	--with-odbc
%{__make} %{?_smp_mflags}
%{__mv} -f src/snort ../snort-odbc
cd -
%endif

mkdir bloat; cd bloat
../configure $SNORT_BASE_CONFIG \
%{?mysql:	--with-mysql} \
%{?pgsql:	--with-postgresql} \
%{?odbc:	--with-odbc}
%{__make} %{?_smp_mflags}
%{__mv} -f src/snort ../snort-bloat
cd -

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_sysconfdir}/snort \
			%{buildroot}%{_sysconfdir}/sysconfig/ \
			%{buildroot}%{_localstatedir}/log/snort \
			%{buildroot}%{_sbindir} \
			%{buildroot}%{_initrddir} \
			%{buildroot}%{_mandir}/man8

%{__install} -m0755 snort-* %{buildroot}%{_sbindir}

%{__install} -m0644 snort.8 %{buildroot}%{_mandir}/man8
%{__install} -m0644 etc/*.config etc/*.conf etc/*.map rules/*.rules %{buildroot}%{_sysconfdir}/snort
%{__install} -m0755 snortd.sysv %{buildroot}%{_initrddir}/snortd
%{__install} -m0644 snort.sysconf %{buildroot}%{_sysconfdir}/sysconfig/snort

%{__perl} -pi -e 's|^var RULE_PATH ../rules|var RULE_PATH %{_sysconfdir}/snort|'  %{buildroot}%{_sysconfdir}/snort/snort.conf

%pre
/usr/sbin/useradd -M -s /sbin/nologin -r snort -d %{_localstatedir}/log/snort -c "Snort" &>/dev/null || :
/usr/sbin/usermod -s /sbin/nologin snort &>/dev/null || :

%post
%{__ln_s} -f %{_sbindir}/snort-plain %{_sbindir}/snort
/sbin/chkconfig --add snortd

%preun
if [ $1 -eq 0 ] ; then
	/sbin/service snortd stop &>/dev/null || :
	/sbin/chkconfig --del snortd
	%{__rm} -f %{_sbindir}/snort
fi

%postun
/sbin/service snortd condrestart &>/dev/null || :

%post mysql
%{__ln_s} -f %{_sbindir}/snort-mysql %{_sbindir}/snort

%postun mysql
%{__ln_s} -f %{_sbindir}/snort-plain %{_sbindir}/snort

%post postgresql
%{__ln_s} -f %{_sbindir}/snort-pgsql %{_sbindir}/snort

%postun postgresql
%{__ln_s} -f %{_sbindir}/snort-plain %{_sbindir}/snort

%post odbc
%{__ln_s} -f %{_sbindir}/snort-odbc %{_sbindir}/snort

%postun odbc
%{__ln_s} -f %{_sbindir}/snort-plain %{_sbindir}/snort

%post bloat
%{__ln_s} -f %{_sbindir}/snort-bloat %{_sbindir}/snort

%postun bloat
%{__ln_s} -f %{_sbindir}/snort-plain %{_sbindir}/snort

%clean
%{__rm} -rf %{buildroot}
						
%files
%defattr(-, root, root, 0755)
%doc ChangeLog contrib doc/AUTHORS doc/BUGS doc/CREDITS doc/FAQ doc/NEWS
%doc doc/README* doc/TODO doc/USAGE doc/snort_manual.* doc/signatures/
%doc %{_mandir}/man?/*
%config(noreplace) %{_sysconfdir}/sysconfig/*
%config %{_initrddir}/snortd
%{_sbindir}/snort-plain

%defattr(-, snort, snort, 0755)
%config(noreplace) %{_sysconfdir}/snort/
%{_localstatedir}/log/snort/

%if %{?mysql:1}%{!?mysql:0}
%files mysql
%defattr(-, root, root, 0755)
%{_sbindir}/snort-mysql
%endif

%if %{?pgsql:1}%{!?pgsql:0}
%files postgresql
%defattr(-, root, root, 0755)
%{_sbindir}/snort-pgsql
%endif

%if %{?odbc:1}%{!?odbc:0}
%files odbc
%defattr(-, root, root, 0755)
%{_sbindir}/snort-odbc
%endif

%files bloat
%defattr(-, root, root, 0755)
%{_sbindir}/snort-bloat

%changelog
* Sat Feb 28 2004 Dag Wieers <dag@wieers.com> - 2.1.1-0
- Updated to release 2.1.1.
- Added %%postun scripts for each build.
- Added obsoletes between optional packages.

* Wed Feb 11 2004 Dag Wieers <dag@wieers.com> - 2.1.0-1
- Fixed a couple of config-files.

* Sun Dec 21 2003 Dag Wieers <dag@wieers.com> - 2.1.0-0
- Updated to release 2.1.0.

* Fri Nov 21 2003 Dag Wieers <dag@wieers.com> - 2.0.5-0
- Updated to release 2.0.5.

* Tue Sep 23 2003 Dag Wieers <dag@wieers.com> - 2.0.2-0
- Updated to release 2.0.2.

* Sat Aug 16 2003 Dag Wieers <dag@wieers.com> - 2.0.1-0
- Updated to release 2.0.1.

* Tue Apr 29 2003 Dag Wieers <dag@wieers.com> - 2.0.0-1
- Made sysv script executable. (Dries Verachtert)

* Fri Apr 18 2003 Dag Wieers <dag@wieers.com> - 2.0.0-0
- Updated to release 2.0.0.

* Mon Mar 10 2003 Dag Wieers <dag@wieers.com> - 1.9.1-0
- Updated to release 1.9.1.

* Wed Feb 19 2003 Dag Wieers <dag@wieers.com> - 1.9.0-1
- Fixed a problem with the post-script.

* Fri Feb 14 2003 Dag Wieers <dag@wieers.com> - 1.9.0-0
- Initial package. (using DAR)
