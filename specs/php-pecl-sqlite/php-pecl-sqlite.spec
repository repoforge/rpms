# $Id$
# Authority: matthias

%define php_extdir %(php-config --extension-dir 2>/dev/null || echo %{_libdir}/php4)

Summary: PECL package for accessing SQLite databases
Name: php-pecl-sqlite
Version: 1.0.3
Release: 2%{?dist}
License: PHP
Group: Development/Languages
URL: http://pecl.php.net/package/SQLite
Source: http://pecl.php.net/get/SQLite-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: php
BuildRequires: php, php-devel
# Required by phpize

BuildRequires: autoconf, automake, libtool, gcc-c++
BuildRequires: sqlite-devel

Provides: php-pecl(sqlite) = %{version}-%{release}

%description
SQLite is a C library that implements an embeddable SQL database engine.
Programs that link with the SQLite library can have SQL database access
without running a separate RDBMS process.
This extension allows you to access SQLite databases from within PHP.


%prep
%setup -n SQLite-%{version}


%build
# Workaround for broken phpize on 64 bits
%{__cat} %{_bindir}/phpize | sed 's|/lib/|/%{_lib}/|g' > phpize && sh phpize
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__make} install INSTALL_ROOT=%{buildroot}

# Drop in the bit of configuration
%{__mkdir_p} %{buildroot}%{_sysconfdir}/php.d
%{__cat} > %{buildroot}%{_sysconfdir}/php.d/sqlite.ini << 'EOF'
; Enable SQLite extension module
extension=sqlite.so
EOF


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc CREDITS README TODO
%config(noreplace) %{_sysconfdir}/php.d/sqlite.ini
%{php_extdir}/sqlite.so


%changelog
* Fri May 14 2010 Steve Huff <shuff@vecna.org> - 1.0.3-2
- Added Provides: to conform to upstream standards.

* Wed Feb 16 2005 Matthias Saou <http://freshrpms.net/> 1.0.3-1
- Update to 1.0.3.

* Thu Jun  3 2004 Matthias Saou <http://freshrpms.net/> 1.0.2-1
- Initial RPM release.

