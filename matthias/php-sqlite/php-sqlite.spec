# Authority: dag
# Upstream: Wez Furlong <wez@php.net>

%define rname SQLite
%define pversion %(rpm -q php-devel --qf '%{RPMTAG_VERSION}' | tail -1)

Summary: PHP module for using SQLite databases.
Name: php-sqlite
Version: 1.0.2
Release: 1
License: GPL
Group: Development/Languages
URL: http://pecl.php.net/package/SQLite/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

### Source: http://pecl.php.net/get/SQLite
Source: SQLite-%{version}.tgz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: php-devel >= 4.0, sqlite >= 2.8
Requires: php = %{pversion}, sqlite >= 2.8

%description
PHP module for using SQLite databases.

This module is built for PHP v%{pversion}.

%prep
%setup -n %{rname}-%{version}

%build
${CC:-%{__cc}} %{optflags} -fpic -DNDEBUG -DCOMPILE_DL_SQLITE -I%{_includedir}/php -I%{_includedir}/php/main -I%{_includedir}/php/TSRM -I%{_includedir}/php/Zend -c -o sqlite.o sqlite.c
${CC:-%{__cc}} %{optflags} -shared -lsqlite -L%{_libdir} -rdynamic -o sqlite.so sqlite.o

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_libdir}/php4/
%{__install} -m0755 sqlite.so %{buildroot}%{_libdir}/php4/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CREDITS README TODO
%{_libdir}/php4/*.so

%changelog
* Sun Feb 29 2004 Dag Wieers <dag@wieers.com> - 1.0.2-1
- Fixed problematic sqlite requirement. (Alain Rykaert)

* Sun Feb 29 2004 Dag Wieers <dag@wieers.com> - 1.0.2-0
- Initial package. (using DAR)
