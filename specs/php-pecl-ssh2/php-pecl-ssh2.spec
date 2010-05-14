# $Id$
# Authority: stefan

%define php_extdir %(php-config --extension-dir)

Summary: PECL package for SSH2
Name: php-pecl-ssh2
Version: 0.10
Release: 2%{?dist}
License: PHP
Group: Development/Languages
URL: http://pecl.php.net/package/ssh2

Source: http://pecl.php.net/get/ssh2-%{version}.tgz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: php
BuildRequires: php, php-devel, libssh2
# Required by phpize
BuildRequires: autoconf, automake, libtool, gcc-c++

Provides: php-pecl(ssh2) = %{version}-%{release}

%description
Provides bindings to the functions of libssh2 which implements the SSH2 protocol.
libssh2 is available from http://www.sourceforge.net/projects/libssh2


%prep
%setup -n ssh2-%{version}


%build
# Workaround for broken phpize on 64 bits
%{_bindir}/phpize
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__make} install INSTALL_ROOT=%{buildroot}

# Drop in the bit of configuration
%{__mkdir_p} %{buildroot}%{_sysconfdir}/php.d
%{__cat} > %{buildroot}%{_sysconfdir}/php.d/ssh2.ini << 'EOF'
; Enable ssh2 extension module
extension=ssh2.so
EOF


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%config(noreplace) %{_sysconfdir}/php.d/ssh2.ini
%{php_extdir}/ssh2.so


%changelog
* Fri May 14 2010 Steve Huff <shuff@vecna.org> - 0.10-2
- Added Provides: to conform to upstream standards.

* Tue Dec 06 2005 Stefan Pietsch <stefan.pietsch@eds.com> 0.10-1
- update to new release

* Tue Oct 25 2005 Stefan Pietsch <stefan.pietsch@eds.com> 0.9-1
- Initial RPM release.

