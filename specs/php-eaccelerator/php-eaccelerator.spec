# $Id$
# Authority: matthias

%define php_extdir %(php-config --extension-dir 2>/dev/null || echo /usr/lib/php4)
%{!?php_version:%define php_version %(php-config --version 2>/dev/null || echo 4.3.10)}

%define module_version 0.9.2a

Summary: PHP accelerator, optimizer, encoder and dynamic content cacher
Name: php-eaccelerator
Version: %{php_version}_%{module_version}
Release: 0
License: GPL
Group: Development/Languages
URL: http://eaccelerator.sourceforge.net/
Source: http://dl.sf.net/eaccelerator/eaccelerator-%{module_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: php = %{php_version}
Provides: php-zend_extension
BuildRequires: php, php-devel
# Required by phpize
BuildRequires: autoconf, automake, libtool, gcc-c++

%description
eAccelerator is a further development of the MMCache PHP Accelerator & Encoder.
It increases performance of PHP scripts by caching them in compiled state, so
that the overhead of compiling is almost completely eliminated.


%prep 
%setup -n eaccelerator


%build
phpize
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__make} install INSTALL_ROOT=%{buildroot}

# The cache directory where pre-compiled files will reside
%{__mkdir_p} %{buildroot}%{_localstatedir}/cache/php-eaccelerator

# Drop in the bit of configuration
%{__mkdir_p} %{buildroot}%{_sysconfdir}/php.d
%{__cat} > %{buildroot}%{_sysconfdir}/php.d/eaccelerator.ini << 'EOF'
; Enable eAccelerator extension module
zend_extension = %{php_extdir}/eaccelerator.so
; Options for the eAccelerator module
eaccelerator.cache_dir = %{_localstatedir}/cache/php-eaccelerator
eaccelerator.shm_size = 0
eaccelerator.enable = 1
eaccelerator.optimizer = 1
eaccelerator.check_mtime = 1
eaccelerator.filter = ""
eaccelerator.shm_max = 0
eaccelerator.shm_ttl = 3600
eaccelerator.shm_prune_period = 0
eaccelerator.shm_only = 0
eaccelerator.compress = 1
eaccelerator.compress_level = 9
eaccelerator.debug = 0
EOF


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README*
%doc eaccelerator.ini *.php
%config(noreplace) %{_sysconfdir}/php.d/eaccelerator.ini
%{php_extdir}/eaccelerator.so
%attr(0750, apache, apache) %{_localstatedir}/cache/php-eaccelerator


%changelog
* Tue Jan 11 2005 Matthias Saou <http://freshrpms.net/> 4.x.x_0.9.2a-0
- Initial RPM release based on my php-mmcache spec file.

