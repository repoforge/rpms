# $Id$
# Authority: matthias

%define php_extdir %(php-config --extension-dir 2>/dev/null || echo %{_libdir}/php4)

Summary: PECL package to get file information through libmagic
Name: php-pecl-fileinfo
Version: 1.0.4
Release: 2%{?dist}
License: PHP
Group: Development/Languages
URL: http://pecl.php.net/package/Fileinfo
Source: http://pecl.php.net/get/Fileinfo-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: php, file
BuildRequires: php, php-devel, zlib-devel, file
# Required by phpize
BuildRequires: autoconf, automake, libtool, gcc-c++

Provides: php-pecl(fileinfo) = %{version}-%{release}

%description
This extension allows retrieval of information regarding the vast majority of
files.  This information may include dimensions, quality, length etc...

Additionally it can also be used to retrieve the mime type for a particular
file and the proper language encoding for text files.


%prep
%setup -n Fileinfo-%{version}


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
%{__cat} > %{buildroot}%{_sysconfdir}/php.d/fileinfo.ini << 'EOF'
; Enable fileinfo extension module
extension=fileinfo.so
EOF


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc CREDITS fileinfo.php
%config(noreplace) %{_sysconfdir}/php.d/fileinfo.ini
%{php_extdir}/fileinfo.so


%changelog
* Fri May 14 2010 Steve Huff <shuff@vecna.org> - 1.0.4-2
- Added Provides: to conform to upstream standards.

* Thu Jan 11 2007 Matthias Saou <http://freshrpms.net/> 1.0.4-1
- Update to 1.0.4.

* Tue Feb 21 2006 Matthias Saou <http://freshrpms.net/> 1.0.3-1
- Initial RPM package.

