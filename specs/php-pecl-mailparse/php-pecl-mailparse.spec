# $Id: php-pear-ole.spec 97 2004-03-11 18:31:17Z dude $

%define php_extdir %(php-config --extension-dir)

Summary: RECL package for parsing and working with email messages
Name: php-pecl-mailparse
Version: 2.0b
Release: 1
License: PHP
Group: Development/Languages
URL: http://pecl.php.net/package/mailparse
Source0: http://pecl.php.net/get/mailparse-%{version}.tgz
Source1: mbfl-4.3.4.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: php
BuildRequires: php, php-devel
# Required by phpize
BuildRequires: autoconf, automake, libtool, gcc-c++

%description
Mailparse is an extension for parsing and working with email messages.
It can deal with rfc822 and rfc2045 (MIME) compliant messages.


%prep 
%setup -a 1 -n mailparse-%{version}


%build
mkdir -p ext/mbstring/libmbfl/
mv mbfl-* ext/mbstring/libmbfl/mbfl
phpize
%configure
make


%install
%{__rm} -rf %{buildroot}
make install INSTALL_ROOT=%{buildroot}


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc README try.php
%{php_extdir}/mailparse.so


%changelog
* Mon Apr 26 2004 Matthias Saou <http://freshrpms.net/> 2.0b-1
- Initial RPM release.
- Included part of php-4.3.4's mbfl includes, ugly.

