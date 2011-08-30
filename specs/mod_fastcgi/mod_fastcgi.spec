# $Id$
# Authority: shuff
# Upstream: http://fastcgi.com/fastcgi-developers

Summary: Apache module that enables FastCGI
Name: mod_fastcgi
Version: 2.4.6
Release: 1%{?dist}
License: GPL/Apache License
Group: System Environment/Daemons
URL: http://www.fastcgi.com/

Source: http://www.fastcgi.com/dist/mod_fastcgi-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gcc-c++
BuildRequires: httpd-devel >= 2.0
Requires: httpd >= 2.0

%description
mod_fastcgi is a module for the Apache web server, that enables
FastCGI - a standards based protocol for communicating with
applications that generate dynamic content for web pages.

%prep
%setup -n %{name}-%{version}

%build
cp Makefile.AP2 Makefile
%{__make} top_dir="%{_libdir}/httpd"

%{__cat} <<EOF >fastcgi.httpd
LoadModule fastcgi_module modules/mod_fastcgi.so

# sample PHP config
# see %{_docdir}/%{name}-%{version} for php-wrapper script
# don't forget to disable mod_php in %{_sysconfdir}/httpd/conf.d/php.conf!
#
#FastCgiServer /var/www/cgi-bin/php-wrapper
#AddHandler php-fastcgi .php
#
#<Location /cgi-bin/php-wrapper>
#    SetHandler fastcgi-script
#</Location>
#
#Action php-fastcgi /cgi-bin/php-wrapper
#DirectoryIndex index.html index.shtml index.cgi index.php
#AddType application/x-httpd-php .php
EOF

%{__cat} <<WRAPPER >php-wrapper
#!/bin/sh

PHPRC="/etc/php.ini"
export PHPRC
PHP_FCGI_CHILDREN=4
export PHP_FCGI_CHILDREN
exec /usr/bin/php-cgi
WRAPPER

%{__chmod} +x php-wrapper

%install
%{__rm} -rf %{buildroot}
%{__make} install top_dir="%{_libdir}/httpd" DESTDIR="%{buildroot}"
%{__install} -Dp -m0644 fastcgi.httpd %{buildroot}%{_sysconfdir}/httpd/conf.d/fastcgi.conf

# make a log directory
%{__install} -d -m770 %{buildroot}%{_localstatedir}/log/httpd/fastcgi

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES INSTALL* README docs/ php-wrapper
%config(noreplace) %{_sysconfdir}/httpd/conf.d/fastcgi.conf
%{_libdir}/httpd/modules/mod_fastcgi.so
%dir %attr(770, apache, apache) %{_localstatedir}/log/httpd/fastcgi 

%changelog
* Fri Aug 26 2011 Philip Durbin <philipdurbin@gmail.com> 2.4.6-1
- Initial release, based on mod_suphp.spec
