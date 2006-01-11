# $Id$
# Authority: matthias

%define php_extdir %(php-config --extension-dir 2>/dev/null || echo %{_libdir}/php4)

Summary: PECL package to use the memcached distributed caching system
Name: php-pecl-memcache
Version: 2.0.0
Release: 1
License: PHP
Group: Development/Languages
URL: http://pecl.php.net/package/memecache
Source: http://pecl.php.net/get/memcache-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: php
BuildRequires: php, php-devel, zlib-devel
# Required by phpize
BuildRequires: autoconf, automake, libtool, gcc-c++

%description
Memcached is a caching daemon designed especially for dynamic web applications
to decrease database load by storing objects in memory.  This extension allows
you to work with memcached through handy OO and procedural interfaces.


%prep
%setup -n memcache-%{version}
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
%defattr(-, root, root, 0755)
%doc CREDITS README
%config(noreplace) %{_sysconfdir}/php.d/memcache.ini
%{php_extdir}/memcache.so


%changelog
* Wed Jan 11 2006 Matthias Saou <http://freshrpms.net/> 2.0.0-1
- Initial RPM package.

