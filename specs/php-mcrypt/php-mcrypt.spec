# $Id$
# Authority: shuff
# Upstream: John Smith <imipak$sourceforge,net>

%define real_name mcrypt


%{?el4:%define pversion %(rpm -q php-devel --qf '%{RPMTAG_VERSION}' | echo 4.3.9)}
%{?el5:%define pversion %(rpm -q php-devel --qf '%{RPMTAG_VERSION}' | echo 5.1.6)}
%{?el6:%define pversion %(rpm -q php-devel --qf '%{RPMTAG_VERSION}' | echo 5.3.3)}

%define php_extdir %(php-config --extension-dir 2>/dev/null || echo %{_libdir}/php4)

Summary: PHP module for using MCrypt encryption library
Name: php-mcrypt
Version: %{pversion}
Release: 2%{?dist}
License: GPL
Group: Development/Languages
URL: http://www.php.net/manual/en/book.mcrypt.php

Source:  http://www.php.net/distributions/php-%{pversion}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: binutils
BuildRequires: gcc
BuildRequires: libmcrypt-devel >= 2.5.6
BuildRequires: make
BuildRequires: php-devel = %{pversion}
BuildRequires: re2c
Requires: libmcrypt >= 2.5.6
Requires: php = %{pversion}

%description
PHP module for using MCrypt encryption library.

This module is built for PHP v%{pversion}.

%prep
%setup -n php-%{pversion}

%build
cd ext/%{real_name}

# Workaround for broken old phpize on 64 bits
%{__cat} %{_bindir}/phpize | sed 's|/lib/|/%{_lib}/|g' > phpize && sh phpize

%configure --with-mcrypt=%{_libdir}

# cause libtool to avoid passing -rpath when linking
# (this hack is well-known as "libtool rpath workaround")
%{__perl} -pi -e 's|^hardcode_libdir_flag_spec|hardcode_libdir_flag_spec=" -D__LIBTOOL_IS_A_FOOL__ "|;' libtool

%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
cd ext/%{real_name}
%{__make} install INSTALL_ROOT=%{buildroot}

# Drop in the bit of configuration
%{__mkdir_p} %{buildroot}%{_sysconfdir}/php.d
%{__cat} > %{buildroot}%{_sysconfdir}/php.d/mcrypt.ini << 'EOF'
; Enable mcrypt extension module
extension=mcrypt.so
EOF

%{__install} -m0755 -d %{buildroot}%{}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CREDITS TODO
%{php_extdir}/mcrypt.so
%config(noreplace) %{_sysconfdir}/php.d/mcrypt.ini

%changelog
* Fri Mar 09 2012 Bjarne Saltbaek <arnebjarne72@hotmail.com>
- Hardcoded PHP versions for EL4-6 to satisfy mock :-(

* Fri Oct 29 2010 Steve Huff <shuff@vecna.org>
- Initial package.
