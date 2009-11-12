# $Id$
# Authority: yury
# Upstream: <libopendbx-devel$lists,sourceforge,net>

#
#  OpenDBX rpm spec file
#
#  By default OpenDBX is build with this backends:
#  - mysql
#  - pgsql
#  - odbc
#  - sqlite3
#  to disable use --without [module-name]
#
#  Optional supported backends are:
#  - firebird
#  - mssql
#  - sqlite
#  - oracle
#  - sybase
#  to enable use --with [module-name]
#

%define _without_sqlite		1
%define _without_firebird	1

# We have freetds in RPMForge
#%define _without_mssql		1
#%define _without_sybase	1

# Why not?
#%define _without_oracle	1

Name:		opendbx
Version:	1.4.4
Release:	15.2%{?dist}
Summary:	Unified database layer with a clean and lightweight interface

Group:		Development/Libraries
License:	LGPL
URL:		http://www.linuxnetworks.de/opendbx/download/
Source0:	http://linuxnetworks.de/opendbx/download/%{name}-%{version}.tar.gz

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:	gcc-c++, gettext

%description
OpenDBX provides a clean and lightweight API for interfacing native relational
database APIs in a consistent way. By using the OpenDBX API you don't have to
adapt your program to the different database APIs by yourself.

%package utils
Summary:	Utility application for manipulating database content
Group:		Applications/Databases
Requires:	%{name} >= %{version}
Requires:	readline, ncurses

BuildRequires:	gcc-c++, gettext, readline, readline-devel, ncurses, ncurses-devel

%description utils
Utility application for manipulating database content either interactively by
the user or in batch mode.

%package devel
Summary:	OpenDBX development headers
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	pkgconfig

BuildRequires:	doxygen

%description devel
Header files for the OpenDBX database abstraction library

%if %{!?_without_mysql:1}%{?_without_mysql:0}

%package mysql
Summary:	MySQL backend for OpenDBX
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	mysql
BuildRequires:	mysql-devel

%description mysql
MySQL backend for the OpenDBX database abstraction library

%endif


%if %{!?_without_pgsql:1}%{?_without_pgsql:0}

%package pgsql
Summary:	PostgreSQL backend for OpenDBX
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	postgresql
BuildRequires:	postgresql-devel

%description pgsql
PostgreSQL backend for the OpenDBX database abstraction library

%endif


%if %{!?_without_sqlite3:1}%{?_without_sqlite3:0}

%package sqlite3
Summary:	SQLite3 backend for OpenDBX
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	sqlite >= 3.0
BuildRequires:	sqlite-devel >= 3.0

%description sqlite3
SQLite3 backend for the OpenDBX database abstraction library

%endif

%if %{?_with_sqlite:1}%{!?_with_sqlite:0}

%package sqlite
Summary:	SQLite backend for OpenDBX
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	sqlite < 3.0
BuildRequires:	sqlite-devel < 3.0

%description sqlite
SQLite backend for the OpenDBX database abstraction library

%endif

%if %{?_with_firebird:1}%{!?_with_firebird:0}

%package firebird
Summary:	Firebird/Interbase backend for OpenDBX
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	firebird
BuildRequires:	firebird-devel

%description firebird
Firebird/Interbase backend for the OpenDBX database abstraction library

%endif

%if %{?_with_mssql:1}%{!?_with_mssql:0}

%package mssql
Summary:	MS SQL Server backend for OpenDBX
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	freetds
BuildRequires:	freetds-devel

%description mssql
MS SQL Server backend for the OpenDBX database abstraction library

%endif

%if %{?_with_oracle:1}%{!?_with_oracle:0}

%package oracle
Summary:	Oracle backend for OpenDBX
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description oracle
Oracle ctlib backend for the OpenDBX database abstraction library

%endif


%if %{?_with_sybase:1}%{!?_with_sybase:0}

%package sybase
Summary:	Sybase backend for OpenDBX
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	freetds
BuildRequires:	freetds-devel

%description sybase
Sybase ctlib backend for the OpenDBX database abstraction library

%endif


%if %{!?_without_odbc:1}%{?_without_odbc:0}

%package odbc
Summary:	ODBC backend for OpenDBX
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	unixODBC
BuildRequires:	unixODBC-devel

%description odbc
ODBC backend for the OpenDBX database abstraction library

%endif

%debug_package

%prep

%setup -q

%build
CPPFLAGS="%{!?_without_mysql:-I/usr/include/mysql} %{!?_without_pgsql:-I/usr/include/pgsql}"; export CPPFLAGS;
LDFLAGS="-L/%{_lib} %{!?_without_mysql:-L/usr/lib/mysql -L/usr/%{_lib}/mysql}"; export LDFLAGS;
%configure \
    --disable-rpath \
    --disable-static \
    --with-backends="\
%{?_with_firebird:firebird }\
%{?_with_mssql:mssql }\
%{!?_without_mysql:mysql }\
%{!?_without_odbc:odbc }\
%{?_with_oracle:oracle }\
%{!?_without_pgsql:pgsql }\
%{?_with_sqlite:sqlite }\
%{!?_without_sqlite3:sqlite3 }\
%{?_with_sybase:sybase }\
" || cat config.log

%{__make} %{?_smp_mflags}

%install
%{__make} DESTDIR=%{buildroot} install
rm %{buildroot}%{_libdir}/lib*.*a
rm %{buildroot}%{_libdir}/opendbx/lib*.*a
%find_lang %{name}
%find_lang %{name}-utils

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(-,root,root,-)
%{_libdir}/libopendbx.so.*
%{_libdir}/libopendbxplus.so.*
%dir %{_libdir}/opendbx
%doc AUTHORS COPYING ChangeLog NEWS README TODO

%files utils -f %{name}-utils.lang
%defattr(-,root,root,-)
%{_bindir}/odbx-sql
%{_datadir}/%{name}
%{_datadir}/%{name}/keywords
#%{_mandir}/man1/*

%files devel
%defattr(-,root,root,-)
%{_includedir}/odbx.h
%{_includedir}/opendbx
%{_includedir}/opendbx/api*
%{_libdir}/libopendbx.so
%{_libdir}/libopendbxplus.so
%{_libdir}/pkgconfig/opendbx.pc
%{_libdir}/pkgconfig/opendbxplus.pc
#%{_mandir}/man3/*

%if %{!?_without_mysql:1}%{?_without_mysql:0}
%files mysql
%defattr(-,root,root,-)
%{_libdir}/opendbx/libmysqlbackend.so*
%endif

%if %{!?_without_pgsql:1}%{?_without_pgsql:0}
%files pgsql
%defattr(-,root,root,-)
%{_libdir}/opendbx/libpgsqlbackend.so*
%endif

%if %{!?_without_sqlite3:1}%{?_without_sqlite3:0}
%files sqlite3
%defattr(-,root,root,-)
%{_libdir}/opendbx/libsqlite3backend.so*
%endif

%if %{?_with_sqlite:1}%{!?_with_sqlite:0}
%files sqlite
%defattr(-,root,root,-)
%{_libdir}/opendbx/libsqlitebackend.so*
%endif

%if %{?_with_firebird:1}%{!?_with_firebird:0}
%files firebird
%defattr(-,root,root,-)
%{_libdir}/opendbx/libfirebirdbackend.so*
%endif

%if %{?_with_mssql:1}%{!?_with_mssql:0}
%files mssql
%defattr(-,root,root,-)
%{_libdir}/opendbx/libmssqlbackend.so*
%endif

%if %{?_with_oracle:1}%{!?_with_oracle:0}
%files oracle
%defattr(-,root,root,-)
%{_libdir}/opendbx/liboraclebackend.so*
%endif

%if %{?_with_sybase:1}%{!?_with_sybase:0}
%files sybase
%defattr(-,root,root,-)
%{_libdir}/opendbx/libsybasebackend.so*
%endif

%if %{!?_without_odbc:1}%{?_without_odbc:0}
%files odbc
%defattr(-,root,root,-)
%{_libdir}/opendbx/libodbcbackend.so*
%endif

%changelog
* Thu Nov 12 2009 Yury V. Zaytsev <yury@shurup.com> - 1.4.4-15.2
- Minor updates to port to RPMForge.

* Wed Sep 30 2009 Norbert Sendetzky <norbert@linuxnetworks.de> 1.4.4-1
- Fixed included backends in main package
- Fixed odbx package
- Fixed builds on x86_64 platforms
- Compatible with OpenSUSE build service
- Added workarounds for RHEL, CentOS and Mandriva regarding readline

* Sun Apr 19 2009 Norbert Sendetzky <norbert@linuxnetworks.de> 1.4.1-1
- Added opendbxplus.pc

* Sun Jun 15 2008 Norbert Sendetzky <norbert@linuxnetworks.de> 1.3.11-1
- Added items for odbc backend and utils

* Mon Mar 17 2008 Norbert Sendetzky <norbert@linuxnetworks.de> 1.3.7-1
- Added polish summary and descriptions (thanks to PLD team)
- Added items for oracle backend

* Wed Jan 31 2007 Norbert Sendetzky <norbert@linuxnetworks.de> 1.2.1-1
- Added german summary and descriptions
- Disabled static library builds and removed libtool files
- Added ldconfig call in post and postun sections
- Added gettext and pkgconfig as requirements
- Replaced language file handling with find_lang macro
- Used optflags macro instead of hard coded compiler flags
- Used macro style consistently
- Corrected mail addresses
- Removed oracle sections
- Fixed _without_pgqql
- Minor changes

* Sat Dec 09 2006 Norbert Sendetzky <norbert@linuxnetworks.de> 1.1.8-1
- Added mssql, sybase and oracle backend

* Tue Jun 13 2006 Kees Monshouwer <mind@monshouwer.com> 1.1.0-2
- Fixed a few minor problems
- Added conditional build support
- Added firefird and freetds backend

* Mon Jun 12 2006 Kees Monshouwer <mind@monshouwer.com> 1.1.0-1
- Initial build for CentOS 4.3
