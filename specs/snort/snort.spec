# $Id$
# Authority: dag
# Upstream: Marty Roesch <roesch$sourcefire,com>


%{!?dtag:%define _with_libpcapdevel 1}
%{?el5:%define _with_libpcapdevel 1}
%{?fc6:%define _with_libpcapdevel 1}

#{?el3:#define _without_odbc 1}

%{?rh7:%define _without_net_snmp 1}
%{?el2:%define _without_net_snmp 1}
%{?rh6:%define _without_net_snmp 1}

Summary: Open Source network intrusion detection system (NIDS)
Name: snort
Version: 2.4.3
Release: 1.2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://www.snort.org/

Source: http://www.snort.org/dl/current/snort-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libpcap >= 0.4, openssl-devel, libnet
BuildRequires: pcre-devel, perl
%{!?_without_net_snmp:BuildRequires: net-snmp-devel}
%{?_without_net_snmp:BuildRequires: ucd-snmp-devel}
%{!?_without_odbc:BuildRequires: unixODBC-devel}
%{!?_without_postgresql:BuildRequires: postgresql-devel}
%{!?_without_mysql:BuildRequires: mysql-devel}
%{?_with_libpcapdevel:BuildRequires:libpcap-devel}

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
Summary: Snort with MySQL support
Group: Applications/Internet
Requires: snort = %{version}-%{release}
Conflicts: snort-postgresql, snort-odbc, snort-bloat

%description mysql
Snort compiled with mysql support.

%package postgresql
Summary: Snort with PostgreSQL support
Group: Applications/Internet
Requires: snort = %{version}-%{release}
Conflicts: snort-mysql, snort-odbc, snort-bloat

%description postgresql
Snort compiled with PostgreSQL support.

%package odbc
Summary: Snort with ODBC support
Group: Applications/Internet
Requires: snort = %{version}-%{release}
Conflicts: snort-mysql, snort-postgresql, snort-bloat

%description odbc
Snort compiled with ODBC support.

%package bloat
Summary: Snort with MySQL, PostgreSQL and ODBC support
Group: Applications/Internet
Requires: snort = %{version}-%{release}
Conflicts: snort-mysql, snort-postgresql, snort-odbc

%description bloat
Snort compiled with MySQL, PostgreSQL and ODBC support.
Requires snort libnet rpm.

%prep
%setup

%{__perl} -pi.orig -e '
		s|lib lib/|%{_lib} %{_lib}/|;
		s|(\$ODBC_DIR)/lib|$1/%{_lib}|;
	' configure

%build
export CFLAGS="%{optflags}"
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

%if %{!?_without_mysql:1}0
mkdir mysql; cd mysql
../configure $SNORT_BASE_CONFIG \
	--with-mysql \
	--without-postgresql \
	--without-odbc
%{__make} %{?_smp_mflags}
%{__mv} src/snort ../snort-mysql
cd -
%endif

%if %{!?_without_postgresql:1}0
mkdir pgsql; cd pgsql
../configure $SNORT_BASE_CONFIG \
	--without-mysql \
	--with-postgresql \
	--without-odbc
%{__make} %{?_smp_mflags}
%{__mv} -f src/snort ../snort-pgsql
cd -
%endif

%if %{!?_without_odbc:1}0
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
%{!?_without_mysql:	--with-mysql} \
%{!?_without_pgsql:	--with-postgresql} \
%{!?_without_odbc:	--with-odbc}
%{__make} %{?_smp_mflags}
%{__mv} -f src/snort ../snort-bloat
cd -

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_sbindir}
%{__install} -p -m0755 snort-* %{buildroot}%{_sbindir}

%{__install} -Dp -m0644 snort.8 %{buildroot}%{_mandir}/man8/snort.8

%{__install} -d -m0755 %{buildroot}%{_sysconfdir}/snort
%{__install} -p -m0644 etc/*.config etc/*.conf etc/*.map rules/*.rules %{buildroot}%{_sysconfdir}/snort/

#%{__install} -Dp -m0755 snortd.sysv %{buildroot}%{_initrddir}/snortd
#%{__install} -Dp -m0644 snort.sysconf %{buildroot}%{_sysconfdir}/sysconfig/snort
%{__install} -Dp -m0755 rpm/snortd %{buildroot}%{_initrddir}/snortd
%{__install} -Dp -m0644 rpm/snort.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/snort
%{__install} -Dp -m0644 rpm/snort.logrotate %{buildroot}%{_sysconfdir}/logrotate.d/snort

%{__install} -d -m0755 %{buildroot}%{_localstatedir}/log/snort/

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
%doc ChangeLog contrib/ COPYING LICENSE RELEASE.NOTES
%doc doc/AUTHORS doc/BUGS doc/CREDITS doc/NEWS doc/PROBLEMS
%doc doc/README* doc/RULES.todo doc/TODO doc/USAGE doc/WISHLIST
%doc doc/*.pdf doc/signatures/ rpm/CHANGES.rpms rpm/README* rpm/RPM-TODO
%doc %{_mandir}/man?/*
%config(noreplace) %{_sysconfdir}/sysconfig/*
%config(noreplace) %{_sysconfdir}/logrotate.d/snort
%config %{_initrddir}/snortd
%{_sbindir}/snort-plain

%defattr(-, snort, snort, 0755)
%config(noreplace) %{_sysconfdir}/snort/
%{_localstatedir}/log/snort/

%if %{!?_without_mysql:1}0
%files mysql
%defattr(-, root, root, 0755)
%{_sbindir}/snort-mysql
%endif

%if %{!?_without_postgresql:1}0
%files postgresql
%defattr(-, root, root, 0755)
%{_sbindir}/snort-pgsql
%endif

%if %{!?_without_odbc:1}0
%files odbc
%defattr(-, root, root, 0755)
%{_sbindir}/snort-odbc
%endif

%files bloat
%defattr(-, root, root, 0755)
%{_sbindir}/snort-bloat

%changelog
* Fri Nov 11 2005 Dries Verachtert <dries@ulyssis.org> - 2.4.3-1
- Updated to release 2.4.3.

* Tue May 17 2005 Dag Wieers <dag@wieers.com> - 2.3.3-1
- Updated to release 2.3.3.

* Tue Feb 22 2005 Dag Wieers <dag@wieers.com> - 2.3.0-1
- Replaced own sysv logic by provided one.
- Updated to release 2.3.0.

* Thu Aug 12 2004 Dag Wieers <dag@wieers.com> - 2.2.0-1
- Replaced Obsoletes by Conflicts.

* Fri Jun 25 2004 Dag Wieers <dag@wieers.com> - 2.1.3-1
- Updated to release 2.1.3.

* Tue Apr 13 2004 Dag Wieers <dag@wieers.com> - 2.1.2-2
- Added rh-postgresql-devel for RHEL3.
- Build against libnet 1.2.2.1.

* Thu Apr 08 2004 Dag Wieers <dag@wieers.com> - 2.1.2-1
- Updated to release 2.1.2.

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
