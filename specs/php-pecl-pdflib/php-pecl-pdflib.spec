# $Id$
# Authority: matthias

%define php_extdir %(php-config --extension-dir 2>/dev/null || echo %{_libdir}/php4)

Summary: PECL package for generating PDF files
Name: php-pecl-pdflib
Version: 2.0.4
Release: 1%{?dist}
License: PHP
Group: Development/Languages
URL: http://pecl.php.net/package/pdflib
Source: http://pecl.php.net/get/pdflib-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: php
BuildRequires: php, php-devel, pdflib-devel
# Required by phpize
BuildRequires: autoconf, automake, libtool, gcc-c++
Obsoletes: php-pdf <= 4.3.11

%description
This PHP extension wraps the PDFlib programming library for processing PDF
on the fly.


%prep
%setup -n pdflib-%{version}


%build
# Workaround for broken phpize on 64 bits
%{__cat} %{_bindir}/phpize | sed 's|/lib/|/%{_lib}/|g' > phpize && sh phpize
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__make} install INSTALL_ROOT=%{buildroot}

# Drop in the bit of configuration
%{__mkdir_p} %{buildroot}%{_sysconfdir}/php.d
%{__cat} > %{buildroot}%{_sysconfdir}/php.d/pdf.ini << 'EOF'
; Enable PDFlib extension module
extension=pdf.so
EOF


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc CREDITS
%config(noreplace) %{_sysconfdir}/php.d/pdf.ini
%{php_extdir}/pdf.so


%changelog
* Tue May 17 2005 Matthias Saou <http://freshrpms.net/> 2.0.4-1
- Initial RPM release.

