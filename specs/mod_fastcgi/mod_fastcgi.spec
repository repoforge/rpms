# $Id$
# Authority: shuff
# Upstream: http://fastcgi.com/fastcgi-developers

%{?el4:%define _without_selinux 1}
%{?el3:%define _without_selinux 1}
%{?rh9:%define _without_selinux 1}
%{?rh7:%define _without_selinux 1}

Summary: Apache module that enables FastCGI
Name: mod_fastcgi
Version: 2.4.6
Release: 2%{?dist}
License: GPL/Apache License
Group: System Environment/Daemons
URL: http://www.fastcgi.com/

Source0: http://www.fastcgi.com/dist/mod_fastcgi-%{version}.tar.gz
Source1: mod_fastcgi.te
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gcc-c++
BuildRequires: httpd-devel >= 2.0
Requires: httpd >= 2.0

%{!?_without_selinux:BuildRequires: checkpolicy, policycoreutils}

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
# WARNING: this is a kludge:
## The User/Group for httpd need to be set before we can load mod_fastcgi,
## but /etc/httpd/conf.d/fastcgi.conf on RHEL gets loaded before
## /etc/httpd/conf/httpd.conf, so we need to set them here :(
## mod_fcgid does not have this bug,
## but it does not handle child PHP processes appropriately per
## http://serverfault.com/questions/303535/a-single-php-fastcgi-process-blocks-all-other-php-requests/305093#305093

User apache
Group apache

LoadModule fastcgi_module modules/mod_fastcgi.so

# dir for IPC socket files
FastCgiIpcDir %{_localstatedir}/run/%{name}

# wrap all fastcgi script calls in suexec
FastCgiWrapper On

# global FastCgiConfig can be overridden by FastCgiServer options in vhost config
FastCgiConfig -idle-timeout 20 -maxClassProcesses 1

# sample PHP config
# see /usr/share/doc/mod_fastcgi-2.4.6 for php-wrapper script
# don't forget to disable mod_php in /etc/httpd/conf.d/php.conf!
#
# to enable privilege separation, add a "SuexecUserGroup" directive
# and chown the php-wrapper script and parent directory accordingly
# see also http://www.brandonturner.net/blog/2009/07/fastcgi_with_php_opcode_cache/
#
#FastCgiServer /var/www/cgi-bin/php-wrapper
#AddHandler php-fastcgi .php
#Action php-fastcgi /cgi-bin/php-wrapper
#AddType application/x-httpd-php .php
#DirectoryIndex index.php
#
#<Location /cgi-bin/php-wrapper>
#    Order Deny,Allow
#    Deny from All
#    Allow from env=REDIRECT_STATUS
#    Options ExecCGI
#    SetHandler fastcgi-script
#</Location>
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

# make an IPC sockets dir
%{__install} -d -m770 %{buildroot}%{_localstatedir}/run/%{name}

### set up SELinux module if called for (adapted from munin.spec)
%if %{!?_without_selinux:1}
checkmodule -M -m -o %{name}.mod %{SOURCE1}
semodule_package -o %{name}.pp -m %{name}.mod
%{__install} -D -d -m0755 %{buildroot}%{_datadir}/selinux/targeted/
%{__install} %{name}.pp %{buildroot}%{_datadir}/selinux/targeted/
%endif

%clean
%{__rm} -rf %{buildroot}

%post
%if %{!?_without_selinux:1}
semodule -i %{_datadir}/selinux/targeted/%{name}.pp
%endif

%files
%defattr(-, root, root, 0755)
%doc CHANGES INSTALL* README docs/ php-wrapper
%config(noreplace) %{_sysconfdir}/httpd/conf.d/fastcgi.conf
%{_libdir}/httpd/modules/mod_fastcgi.so
%dir %attr(770,apache,apache) %{_localstatedir}/run/%{name}
%attr(0644, root, root) %{_datadir}/selinux/targeted/*

%changelog
* Mon May 07 2012 William Horka <whorka@hmdc.harvard.edu> 2.4.6-2
- Add selinux module
- Remove unused log dir and add IPC socket dir
- Add FastCgiWrapper, FastCgiConfig, and FastCgiWrapper to fastcgi.conf
- Set httpd User and Group in fastcgi.conf so mod_fastcgi.so will load

* Fri Aug 26 2011 Philip Durbin <philipdurbin@gmail.com> 2.4.6-1
- Initial release, based on mod_suphp.spec
