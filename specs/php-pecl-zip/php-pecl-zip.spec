# $Id: php-pecl-fileinfo.spec 5204 2007-02-24 14:39:44Z thias $
# Authority: matthias

%define php_extdir %(php-config --extension-dir 2>/dev/null || echo %{_libdir}/php4)

Summary: A zip management extension for php
Name: php-pecl-zip
Version: 1.8.10
Release: 2%{?dist}
License: PHP
Group: Development/Languages
URL: http://pecl.php.net/package/zip
Source: http://pecl.php.net/get/zip-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: php, file
BuildRequires: php, php-devel, zlib-devel, file
# Required by phpize
BuildRequires: autoconf, automake, libtool, gcc-c++

Provides: php-pecl(zip) = %{version}-%{release}

%description
Zip is an extension to create, modify and read zip files.


%prep
%setup -n zip-%{version}


%build
# Workaround for broken old phpize on 64 bits
%{__cat} %{_bindir}/phpize | sed 's|/lib/|/%{_lib}/|g' > phpize && sh phpize
%configure
%{__make} %{?_smp_mflags} test
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__make} install INSTALL_ROOT=%{buildroot}

# Drop in the bit of configuration
%{__mkdir_p} %{buildroot}%{_sysconfdir}/php.d
%{__cat} > %{buildroot}%{_sysconfdir}/php.d/zip.ini << 'EOF'
; Enable zip extension module
extension=zip.so
EOF

%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc CREDITS examples
%config(noreplace) %{_sysconfdir}/php.d/zip.ini
%{php_extdir}/zip.so


%changelog
* Fri May 14 2010 Steve Huff <shuff@vecna.org> - 1.8.10-2
- Added Provides: to conform to upstream standards.

* Wed Apr 15 2009 Christoph Maser <cmr@financial.com> - 1.8.10
- Initial RPM package.

