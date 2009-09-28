# $Id$
# Authority: shuff
# Upstream: Michael Wallner <mike$php,net>

%define php_extdir %(php-config --extension-dir 2>/dev/null || echo %{_libdir}/php4)
%define php_incdir %(php-config --include-dir 2>/dev/null || echo %{_includedir}/php4)

%define real_name pecl_http

Summary: PECL package to add HTTP request functionality
Name: php-pecl-http
Version: 1.6.5
Release: 1
License: PHP
Group: Development/Languages
URL: http://pecl.php.net/package/%{real_name}
Source: http://pecl.php.net/get/%{real_name}-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: php, curl, libevent, openssl
BuildRequires: php, php-devel, curl-devel, libevent-devel, openssl-devel
# Required by phpize
BuildRequires: autoconf, automake, libtool, gcc-c++

%description
This HTTP extension aims to provide a convenient and powerful
set of functionality for one of PHPs major applications.

It eases handling of HTTP urls, dates, redirects, headers and
messages, provides means for negotiation of clients preferred
language and charset, as well as a convenient way to send any
arbitrary data with caching and resuming capabilities.

It provides powerful request functionality, if built with CURL
support. Parallel requests are available for PHP 5 and greater.


%prep
%setup -n %{real_name}-%{version}


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
%{__cat} > %{buildroot}%{_sysconfdir}/php.d/http.ini << 'EOF'
; Enable http extension module
extension=http.so
EOF


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc CREDITS
%config(noreplace) %{_sysconfdir}/php.d/http.ini
%dir %{php_incdir}/ext/http
%dir %{php_incdir}/ext/http/phpstr
%{php_incdir}/ext/http/*.h
%{php_incdir}/ext/http/phpstr/*.h
%{php_extdir}/http.so


%changelog
* Mon Sep 28 2009 Steve Huff <shuff@vecna.org> - 1.6.5-1
- Initial package.
