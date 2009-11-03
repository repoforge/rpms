# $Id$
# Authority: matthias

%define php_extdir %(php-config --extension-dir 2>/dev/null || echo %{_libdir}/php4)
%{!?php_version:%define php_version %(php-config --version 2>/dev/null || echo 4.3.11)}

%define module_version 0.9.5.2

Summary: PHP accelerator, optimizer, encoder and dynamic content cacher
Name: php-eaccelerator
Version: %{php_version}_%{module_version}
Release: 4%{?dist}
License: GPL
Group: Development/Languages
URL: http://eaccelerator.sourceforge.net/
Source: http://dl.sf.net/eaccelerator/eaccelerator-%{module_version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: php = %{php_version}
Provides: php-zend_extension
Conflicts: php-mmcache
BuildRequires: php, php-devel
# Required by phpize
BuildRequires: autoconf, automake, libtool, gcc-c++

%description
eAccelerator is a further development of the MMCache PHP Accelerator & Encoder.
It increases performance of PHP scripts by caching them in compiled state, so
that the overhead of compiling is almost completely eliminated.


%prep
%setup -n eaccelerator-%{module_version}


%build
# Workaround for broken phpize on 64 bits
%{__cat} %{_bindir}/phpize | sed 's|/lib/|/%{_lib}/|g' > phpize && sh phpize
%configure
# Set fcntl based semaphores to avoid ipc based locking issues
%{__perl} -pi -e 's|.*(MM_SEM_[A-Z]+).*|/* #undef $1 */|g' config.h
%{__perl} -pi -e 's|.*(MM_SEM_FCNTL).*|#define $1 1|g' config.h
# Compile!
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
eaccelerator.keys = "shm_and_disk"
eaccelerator.sessions = "shm_and_disk"
eaccelerator.content = "shm_and_disk"
eaccelerator.debug = 0
EOF


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README*
%doc *.php eaccelerator.ini
%config(noreplace) %{_sysconfdir}/php.d/eaccelerator.ini
%{php_extdir}/eaccelerator.so
%attr(0750, apache, apache) %{_localstatedir}/cache/php-eaccelerator


%changelog
* Fri Oct 05 2007 Dag Wieers <dag@wieers.com> - x.x.x_0.9.5.2-1
- Updated to release 0.9.5.2.

* Tue Jul 12 2005 Matthias Saou <http://freshrpms.net/> 4.x.x_0.9.3-4
- Force SEM to FCNTL as the IPC version is buggy on SMP systems at least.

* Fri Jul  1 2005 Matthias Saou <http://freshrpms.net/> 4.x.x_0.9.3-1
- Include buffer overflow patch from zoeloelip.

* Tue Jun 21 2005 Matthias Saou <http://freshrpms.net/> 4.x.x_0.9.3-0
- Update to 0.9.3, bugfix release.

* Tue Jan 11 2005 Matthias Saou <http://freshrpms.net/> 4.x.x_0.9.2a-0
- Initial RPM release based on the php-mmcache spec file.

