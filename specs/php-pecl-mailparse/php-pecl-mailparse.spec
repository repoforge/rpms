# $Id$
# Authority: matthias

%define php_extdir %(php-config --extension-dir 2>/dev/null || echo %{_libdir}/php4)

Summary: PECL package for parsing and working with email messages
Name: php-pecl-mailparse
Version: 2.1.5
Release: 2%{?dist}
License: PHP
Group: Development/Languages
URL: http://pecl.php.net/package/mailparse
Source0: http://pecl.php.net/get/mailparse-%{version}.tgz
# Tarball created from the ext/mbstring/libmbfl/mbfl/ dir of the PHP sources
Source1: mbfl-4.4.0.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: php
BuildRequires: php, php-devel, re2c >= 0.9.11
# Required by phpize
BuildRequires: autoconf, automake, libtool, gcc-c++

Provides: php-pecl(mailparse) = %{version}-%{release}

%description
Mailparse is an extension for parsing and working with email messages.
It can deal with rfc822 and rfc2045 (MIME) compliant messages.


%prep
%setup -a 1 -n mailparse-%{version}


%build
%{__mkdir_p} ext/mbstring/libmbfl/
%{__mv} mbfl-* ext/mbstring/libmbfl/mbfl
# Workaround for broken phpize on 64 bits
%{__cat} %{_bindir}/phpize | sed 's|/lib/|/%{_lib}/|g' > phpize && sh phpize
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__make} install INSTALL_ROOT=%{buildroot}

# Drop in the bit of configuration
%{__mkdir_p} %{buildroot}%{_sysconfdir}/php.d
%{__cat} > %{buildroot}%{_sysconfdir}/php.d/z-mailparse.ini << 'EOF'
; Enable mailparse extension module
extension=mailparse.so

; Set the default charset
;mailparse.def_charset = us-ascii
EOF


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc README try.php
%config(noreplace) %{_sysconfdir}/php.d/z-mailparse.ini
%{php_extdir}/mailparse.so


%changelog
* Fri May 14 2010 Steve Huff <shuff@vecna.org> - 2.1.5-2
- Added Provides: to conform to upstream standards.

* Thu Sep 24 2009 Steve Huff <shuff@vecna.org> - 2.1.5-1
- Update to 2.1.5.
- Added build dependency on re2c per warning from ./configure.

* Wed Jul 20 2005 Matthias Saou <http://freshrpms.net/> 2.1.1-1
- Update to 2.1.1.
- Update mbfl tarball to 4.4.0 PHP sources.
- Rename .ini file to "z-<name>" to have it load after mbstring.so.

* Wed Feb 16 2005 Matthias Saou <http://freshrpms.net/> 2.1-1
- Update to 2.1.

* Tue Jul 27 2004 Matthias Saou <http://freshrpms.net/> 2.0b-4
- Update included mbfl source to 4.3.8 as the current 4.3.4 doesn't work
  anymore.

* Fri May 21 2004 Matthias Saou <http://freshrpms.net/> 2.0b-3
- Rebuild for Fedora Core 2.
- No need for a strict dependency on this package, it works fine with
  php 4.3.6 when compiled against 4.3.4.

* Fri May  7 2004 Matthias Saou <http://freshrpms.net/> 2.0b-2
- Added php.d entry to auto-load the module with recent php packages.
- Added more macros to the spec file.

* Mon Apr 26 2004 Matthias Saou <http://freshrpms.net/> 2.0b-1
- Initial RPM release.
- Included part of php-4.3.4's mbfl includes, ugly.

