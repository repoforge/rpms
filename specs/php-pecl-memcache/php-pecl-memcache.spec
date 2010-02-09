# $Id$
# Authority: matthias
# Upstream: Antony Dovgal <tony$daylessday,org>

%define php_extdir %(php-config --extension-dir 2>/dev/null || echo %{_libdir}/php4)

Summary: PECL package to use the memcached distributed caching system
Name: php-pecl-memcache
Version: 2.2.5
Release: 1%{?dist}
License: PHP
Group: Development/Languages
URL: http://pecl.php.net/package/memcache
Source: http://pecl.php.net/get/memcache-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: php
BuildRequires: php, php-devel, zlib-devel, openssl-devel
# Required by phpize
BuildRequires: autoconf, automake, libtool

%description
Memcached is a caching daemon designed especially for dynamic web applications
to decrease database load by storing objects in memory.  This extension allows
you to work with memcached through handy OO and procedural interfaces.


%prep
%setup -q -n memcache-%{version}
# Docs are +x (as of 2.0.0), so fix here
%{__chmod} -x CREDITS README


%build
# Workaround for broken old phpize on 64 bits
%{__cat} %{_bindir}/phpize | sed 's|/lib/|/%{_lib}/|g' > phpize && sh phpize
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__make} install INSTALL_ROOT=%{buildroot}

# Drop in the bit of configuration
%{__mkdir_p} %{buildroot}%{_sysconfdir}/php.d
%{__cat} > %{buildroot}%{_sysconfdir}/php.d/memcache.ini << 'EOF'
; Enable memcache extension module
extension=memcache.so
EOF


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc CREDITS README
%config(noreplace) %{_sysconfdir}/php.d/memcache.ini
%{php_extdir}/memcache.so


%changelog
* Tue Feb 09 2010 Steve Huff <shuff@vecna.org> - 2.2.5-1
- Update to 2.2.5.

* Mon Sep  1 2008 Dries Verachtert <dries@ulyssis.org> 2.2.3-1
- Update to 2.2.3.

* Mon Sep 18 2006 Matthias Saou <http://freshrpms.net/> 2.1.2-1
- Update to 2.1.2.

* Mon Sep 18 2006 Matthias Saou <http://freshrpms.net/> 2.0.4-1
- Update to 2.0.4.

* Thu Feb 16 2006 Matthias Saou <http://freshrpms.net/> 2.0.1-1
- Update to 2.0.1.
- Add openssl-devel build requirement, as it's needed at least on RHEL4.

* Wed Jan 11 2006 Matthias Saou <http://freshrpms.net/> 2.0.0-1
- Initial RPM package.

