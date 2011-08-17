# $ID$
# Authority: shuff

%define real_name xcache

%define default_extdir  %{_libdir}/php/modules

%define php_extdir %(php-config --extension-dir 2>/dev/null || echo %{default_extdir})

Summary: PHP accelerator, optimizer, encoder and dynamic content cacher
Name: php-xcache
Version: 1.3.2
Release: 1%{?dist}
License: GPL
Group: Development/Languages
URL: http://xcache.lighttpd.net/

Source: http://xcache.lighttpd.net/pub/Releases/%{version}/xcache-%{version}.tar.gz
Source1: xcache.ini

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: php
BuildRequires: php-devel
BuildRequires: sed
# Required by phpize
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool

Requires: php(zend-abi)
Requires: php(api)

Conflicts: php-apc
Conflicts: php-eaccelerator
Conflicts: php-mmcache

Provides: php-zend_extension

%description
XCache is a fast, stable PHP opcode cacher that has been tested and is now
running on production servers under high load. It is tested (on linux) and
supported on all of the latest PHP cvs branches such as PHP_4_3 PHP_4_4
PHP_5_1 PHP_5_2 HEAD(6.x). ThreadSafe/Windows is also supported.

%prep
%setup -n %{real_name}-%{version}

%build
phpize
%configure --enable-xcache

%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install INSTALL_ROOT=%{buildroot}

# The cache directory where pre-compiled files will reside
%{__mkdir_p} %{buildroot}%{_var}/cache/php-xcache
%{__mkdir_p} %{buildroot}%{_var}/www/html/xcache/

# Drop in the bit of configuration
%{__install} -D -m 0644 $RPM_SOURCE_DIR/xcache.ini $RPM_BUILD_ROOT%{_sysconfdir}/php.d/xcache.ini
%{__sed} -i -e 's|/REPLACEME|%{php_extdir}|g' $RPM_BUILD_ROOT%{_sysconfdir}/php.d/xcache.ini
%{__install} -D -m 0644 admin/* $RPM_BUILD_ROOT%{_var}/www/html/xcache/


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc xcache.ini admin/
%config(noreplace) %{_sysconfdir}/php.d/xcache.ini
%{php_extdir}/xcache.so
%{_var}/www/html/xcache/*

%changelog
* Wed Aug 17 2011 Steve Huff <shuff@vecna.org> - 1.3.2-1
- Ported from Jason Litka's spec.
- Updated to version 1.3.2.

* Fri Dec 17 2010 Jason Litka <http://www.jasonlitka.com> 1:1.3.1-jason.1
- Updated source to 1.3.1

* Tue Nov 17 2009 Jason Litka <http://www.jasonlitka.com> 1:1.3.0-jason.1
- Updated source to 1.3.0

* Fri Sep 18 2009 Jason Litka <http://www.jasonlitka.com> 1:1.2.2-jason.3
- Updated source to 1.2.2
- Added conflict with php-mmcache, php-apc, and php-eaccelerator
- Replaced php version dep with api version
- Bumped epoch so upgrade would work with new "correct" versioning

* Tue Jul  3 2007 Jason Litka <http://www.jasonlitka.com/> 1.2.1-jason.2
- Changed the config file back to "noreplace"
- Removed the check for # of CPU cores since it couldn't tell the difference
  between real cores and virtual ones
- Changed the php requirement for install to the same version found during
  the build

* Tue Jul  3 2007 Jason Litka <http://www.jasonlitka.com/> 1.2.1-jason.1
- Updated sources to 1.2.1
- Changed naming convention to match my other packages

* Thu Dec 28 2006 Jason Litka <http://www.jasonlitka.com/> 1.2.0_0.2
- Removed the PHP API check so that the package would build on PHP 4.

* Wed Dec 20 2006 Jason Litka <http://www.jasonlitka.com/> 1.2.0_0.1
- Initial build
- Has Cache, Optimizer, and Coverager modules built but only the first two
  are enabled

