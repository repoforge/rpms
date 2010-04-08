# $Id$
# Authority: cmr
# Upstream:  

Summary: Network backup solution
Name: bacula
Version: 5.0.1
Release: 1%{?dist}
License: GPL
Group: System Environment/Daemons
URL: http://www.bacula.org/

Source: %{name}-%{version}.tar.bz2
Patch0: bacula-mtx-changer-mailslot.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: atk-devel
BuildRequires: libstdc++-devel
BuildRequires: libxml2-devel
BuildRequires: mysql-devel
BuildRequires: ncurses-deveui
BuildRequires: pango-devel
BuildRequires: readline-devel
BuildRequires: zlib-devel
Requires: atk 
Requires: libstdc++
Requires: libxml2
Requires: ncurses
Requires: pango
Requires: perl
Requires: readline
Requires: zlib


%description
Bacula - It comes by night and sucks the vital essence from your computers.

Bacula is a set of computer programs that permit you (or the system
administrator) to manage backup, recovery, and verification of computer
data across a network of computers of different kinds. In technical terms,
it is a network client/server based backup program. Bacula is relatively
easy to use and efficient, while offering many advanced storage management
features that make it easy to find and recover lost or damaged files.
Bacula source code has been released under the GPL version 2 license.

%prep
%setup
%patch0 -p1

%build
%configure \
    --sysconfdir=%{_sysconfdir}/%{name} \
    --with-mysql
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%{__mkdir} %{buildroot}/%{_libdir}/%{name}/
%{__cp} -r updatedb %{buildroot}/%{_libdir}/%{name}/


%clean
%{__rm} -rf %{buildroot}

%files 
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL LICENSE README 
%{_sysconfdir}/bacula/bacula
%{_sysconfdir}/bacula/bacula-ctl-dir
%{_sysconfdir}/bacula/bacula-ctl-fd
%{_sysconfdir}/bacula/bacula-ctl-sd
%{_sysconfdir}/bacula/bacula-dir.conf
%{_sysconfdir}/bacula/bacula-fd.conf
%{_sysconfdir}/bacula/bacula-sd.conf
%{_sysconfdir}/bacula/bacula_config
%{_sysconfdir}/bacula/bconsole
%{_sysconfdir}/bacula/bconsole.conf
%{_sysconfdir}/bacula/btraceback.dbx
%{_sysconfdir}/bacula/btraceback.gdb
%{_sysconfdir}/bacula/create_bacula_database
%{_sysconfdir}/bacula/create_mysql_database
%{_sysconfdir}/bacula/delete_catalog_backup
%{_sysconfdir}/bacula/disk-changer
%{_sysconfdir}/bacula/drop_bacula_database
%{_sysconfdir}/bacula/drop_bacula_tables
%{_sysconfdir}/bacula/drop_mysql_database
%{_sysconfdir}/bacula/drop_mysql_tables
%{_sysconfdir}/bacula/dvd-handler
%{_sysconfdir}/bacula/grant_bacula_privileges
%{_sysconfdir}/bacula/grant_mysql_privileges
%{_sysconfdir}/bacula/make_bacula_tables
%{_sysconfdir}/bacula/make_catalog_backup
%{_sysconfdir}/bacula/make_catalog_backup.pl
%{_sysconfdir}/bacula/make_mysql_tables
%{_sysconfdir}/bacula/mtx-changer
%{_sysconfdir}/bacula/mtx-changer.conf
%{_sysconfdir}/bacula/query.sql
%{_sysconfdir}/bacula/startmysql
%{_sysconfdir}/bacula/stopmysql
%{_sysconfdir}/bacula/update_bacula_tables
%{_sysconfdir}/bacula/update_mysql_tables
%{_libdir}/%{name}/updatedb
%{_libdir}/bpipe-fd.so
%{_libdir}/libbac-5.0.1.so
%{_libdir}/libbac.la
%{_libdir}/libbac.so
%{_libdir}/libbaccfg-5.0.1.so
%{_libdir}/libbaccfg.la
%{_libdir}/libbaccfg.so
%{_libdir}/libbacfind-5.0.1.so
%{_libdir}/libbacfind.la
%{_libdir}/libbacfind.so
%{_libdir}/libbacpy-5.0.1.so
%{_libdir}/libbacpy.la
%{_libdir}/libbacpy.so
%{_libdir}/libbacsql-5.0.1.so
%{_libdir}/libbacsql.la
%{_libdir}/libbacsql.so
%{_sbindir}/bacula
%{_sbindir}/bacula-dir
%{_sbindir}/bacula-fd
%{_sbindir}/bacula-sd
%{_sbindir}/bconsole
%{_sbindir}/bcopy
%{_sbindir}/bextract
%{_sbindir}/bls
%{_sbindir}/bregex
%{_sbindir}/bscan
%{_sbindir}/bsmtp
%{_sbindir}/btape
%{_sbindir}/btraceback
%{_sbindir}/bwild
%{_sbindir}/dbcheck
%{_defaultdocdir}/bacula/ChangeLog
%{_defaultdocdir}/bacula/INSTALL
%{_defaultdocdir}/bacula/LICENSE
%{_defaultdocdir}/bacula/README
%{_defaultdocdir}/bacula/ReleaseNotes
%{_defaultdocdir}/bacula/VERIFYING
%{_defaultdocdir}/bacula/technotes
%{_mandir}/man1/bacula-bwxconsole.1.gz
%{_mandir}/man1/bacula-tray-monitor.1.gz
%{_mandir}/man1/bat.1.gz
%{_mandir}/man1/bsmtp.1.gz
%{_mandir}/man8/bacula-dir.8.gz
%{_mandir}/man8/bacula-fd.8.gz
%{_mandir}/man8/bacula-sd.8.gz
%{_mandir}/man8/bacula.8.gz
%{_mandir}/man8/bconsole.8.gz
%{_mandir}/man8/bcopy.8.gz
%{_mandir}/man8/bextract.8.gz
%{_mandir}/man8/bls.8.gz
%{_mandir}/man8/bscan.8.gz
%{_mandir}/man8/btape.8.gz
%{_mandir}/man8/btraceback.8.gz
%{_mandir}/man8/dbcheck.8.gz


%changelog
* Wed Apr 08 2010 Christoph Maser <cmr@financial.com>
- Initial package.
