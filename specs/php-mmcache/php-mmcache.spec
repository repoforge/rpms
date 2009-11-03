# $Id$
# Authority: matthias

### FIXME: phpize on fc2/x86_64 is utterly broken as it uses /usr/lib/php4
%define php_extdir %(php-config --extension-dir 2>/dev/null || echo %{_libdir}/php4)
%{!?php_version:%define php_version %(php-config --version 2>/dev/null || echo 4.3.10)}

%define module_version 2.4.6

Summary: PHP accelerator, optimizer, encoder and dynamic content cacher
Name: php-mmcache
Version: %{php_version}_%{module_version}
Release: 4%{?dist}
License: GPL
Group: Development/Languages
URL: http://turck-mmcache.sourceforge.net/
Source: http://dl.sf.net/turck-mmcache/turck-mmcache-%{module_version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: php = %{php_version}
Provides: php-zend_extension
BuildRequires: php, php-devel
# Required by phpize
BuildRequires: autoconf, automake, libtool, gcc-c++

%description
Turck MMCache is a free open source PHP accelerator, optimizer, encoder and
dynamic content cache for PHP. It increases performance of PHP scripts by
caching them in compiled state, so that the overhead of compiling is almost
completely eliminated. Also it uses some optimizations to speed up execution
of PHP scripts. Turck MMCache typically reduces server load and increases the
speed of your PHP code by 1-10 times.


%prep
%setup -n turck-mmcache-%{module_version}


%build
# Workaround for broken phpize on 64 bits
%{__cat} %{_bindir}/phpize | sed 's|/lib/|/%{_lib}/|g' > phpize && sh phpize
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__make} install INSTALL_ROOT=%{buildroot}

# The cache directory where pre-compiled files will reside
%{__mkdir_p} %{buildroot}%{_localstatedir}/cache/php-mmcache

# Drop in the bit of configuration
%{__mkdir_p} %{buildroot}%{_sysconfdir}/php.d
%{__cat} > %{buildroot}%{_sysconfdir}/php.d/mmcache.ini << 'EOF'
; Enable Turck MMCache extension module
zend_extension = %{php_extdir}/mmcache.so
; Options for the MMCache module
mmcache.cache_dir = %{_localstatedir}/cache/php-mmcache
mmcache.shm_size = 0
mmcache.enable = 1
mmcache.optimizer = 1
mmcache.debug = 0
mmcache.check_mtime = 1
mmcache.filter = ""
mmcache.shm_max = 0
mmcache.shm_ttl = 3600
mmcache.shm_prune_period = 0
mmcache.shm_only = 0
mmcache.compress = 1
mmcache.keys = shm
mmcache.sessions = shm
mmcache.content = shm
EOF


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc CREDITS EXPERIMENTAL LICENSE README README.loader TODO
%config(noreplace) %{_sysconfdir}/php.d/mmcache.ini
%{php_extdir}/mmcache.so
%attr(0750, apache, apache) %{_localstatedir}/cache/php-mmcache


%changelog
* Fri May 21 2004 Matthias Saou <http://freshrpms.net/> 4.x.x_2.4.6-1
- Change the version to be phpversion_mmcacheversion since each build
  is tightly tied to a version, and to have an easy upgrade path.

* Mon May 10 2004 Matthias Saou <http://freshrpms.net/> 2.4.6-1
- Initial RPM release.

