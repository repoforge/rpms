# $Id: suphp.spec 3469 2005-08-11 22:23:52Z dag $
# Authority: dag

%{?el4:%define _without_apr1 1}
%{?el3:%define _without_apr1 1}

%define real_name suphp

Summary: Apache module that enables running PHP scripts under different users
Name: mod_suphp
Version: 0.7.1
Release: 1%{?dist}
License: GPL/Apache License
Group: System Environment/Daemons
URL: http://www.suphp.org/

Source: http://projects.marsching.org/suphp/download/suphp-%{version}.tar.gz
Patch0: suphp-0.6.0-handler.patch
Patch1: suphp-0.6.0-handler2.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: httpd-devel >= 2.0, gcc-c++, automake, autoconf
Requires: httpd >= 2.0, php

%description
The suPHP Apache module together with suPHP itself provides an easy way to
run PHP scripts with different users on the same server. It provides security,
because the PHP scripts are not run with the rights of the webserver's user.
In addition to that you probably won't have to use PHP's "safe mode", which
applies many restrictions on the scripts.

%prep
%setup -n %{real_name}-%{version}
#patch0
#patch1

%{__cat} <<EOF >suphp.conf
[global]
logfile=%{_localstatedir}/log/httpd/suphp_log
loglevel=info
webserver_user=apache
docroot=/
env_path=/bin:/usr/bin
umask=0077
min_uid=500
min_gid=500

; Security options
allow_file_group_writeable=false
allow_file_others_writeable=false
allow_directory_group_writeable=false
allow_directory_others_writeable=false

;Check wheter script is within DOCUMENT_ROOT
check_vhost_docroot=true

;Send minor error messages to browser
errors_to_browser=false

[handlers]
;Handler for php-scripts
x-httpd-php="php:%{_bindir}/php"

;Handler for CGI-scripts
x-suphp-cgi="execute:!self"
EOF

%{__cat} <<EOF >suphp.httpd
# This is the Apache server configuration file providing suPHP support.
# It contains the configuration directives to instruct the server how to
# serve php pages while switching to the user context before rendering.

LoadModule suphp_module modules/mod_suphp.so

# This option tells mod_suphp if a PHP-script requested on this server (or
# VirtualHost) should be run with the PHP-interpreter or returned to the
# browser "as it is".
suPHP_Engine off

# Disable php when suphp is used, to avoid having both.
#<IfModule mod_php5.c>
#php_admin_flag engine off
#</IfModule>
#<IfModule mod_php4.c>
#php_admin_flag engine off
#</IfModule>

# To use suPHP to parse PHP-Files
AddHandler x-httpd-php .php
AddHandler x-httpd-php .php .php4 .php3 .phtml

# This option tells mod_suphp which path to pass on to the PHP-interpreter
# (by setting the PHPRC environment variable).
# Do *NOT* refer to a file but to the directory the file resides in.
#
# E.g.: If you want to use "/path/to/server/config/php.ini", use "suPHP_Config
# /path/to/server/config".
#
# If you don't use this option, PHP will use its compiled in default path.
# suPHP_ConfigPath /etc

# If you compiled suphp with setid-mode "force" or "paranoid", you can
# specify the user- and groupname to run PHP-scripts with.
# Example: suPHP_UserGroup foouser bargroup
# suPHP_UserGroup apache apache

# This option tells mod_suphp to handle requests with the type <mime-type>.
# Please note this only works, if an action for the handler is specified
# in the suPHP configuration file.
# suPHP_AddHandler x-httpd-php

# This option tells mod_suphp to NOT handle requests with the type <mime-type>.
# suPHP_RemoveHandler <mime-type>
EOF

%build
#export CPPFLAGS="-I/usr/include/apr-0 -I/usr/include/apr-1"
%configure \
	--disable-checkpath \
	--with-apache-user="apache" \
%{!?_without_apr1:--with-apr="%{_bindir}/apr-1-config"} \
%{?_without_apr1:--with-apr="%{_bindir}/apr-config"} \
	--with-apxs="%{_sbindir}/apxs" \
	--with-logfile="%{_localstatedir}/log/httpd/suphp_log" \
	--with-min-uid="500" \
	--with-min-gid="500" \
	--with-php="%{_bindir}/php" \
	--with-setid-mode="paranoid"
#	--with-setid-mode="owner"
%{__make} %{?_smp_mflags} clean all

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%{__install} -Dp -m0644 suphp.conf %{buildroot}%{_sysconfdir}/suphp.conf
%{__install} -Dp -m0644 suphp.httpd %{buildroot}%{_sysconfdir}/httpd/conf.d/suphp.conf

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING doc/ NEWS README
%config(noreplace) %{_sysconfdir}/suphp.conf
%config(noreplace) %{_sysconfdir}/httpd/conf.d/suphp.conf
%{_libdir}/httpd/modules/mod_suphp.so
%{_sbindir}/suphp

%changelog
* Thu Apr 05 2012 Samuel Stringham <me@samuelstringham.com> - 0.7.1-2
- Correct syntax in conf file

* Tue Mar 30 2010 Yury V. Zaytsev <yury@shurup.com> - 0.7.1
- Updated to release 0.7.1 (thanks to Alessandro Iurlano).

* Tue Jan 20 2009 Dag Wieers <dag@wieers.com> - 0.7.0-1 - 6446+/dries
- Updated to release 0.7.0.

* Mon Aug 18 2008 Dries Verachtert <dries@ulyssis.org> - 0.6.3-1
- Updated to release 0.6.3.

* Thu Aug 23 2007 Dag Wieers <dag@wieers.com> - 0.6.2-1
- Updated to release 0.6.2.

* Tue Feb 28 2006 Dag Wieers <dag@wieers.com> - 0.6.1-2
- Added suPHP_AddHandler/suPHP_RemoveHandler patch for Apache2. (Asheesh Laroia)

* Fri Dec 02 2005 Dag Wieers <dag@wieers.com> - 0.6.1-1
- Updated to release 0.6.1.

* Fri Aug 12 2005 Dag Wieers <dag@wieers.com> - 0.6.0-2
- Added suPHP_AddHandler/suPHP_RemoveHandler patch.

* Thu Aug 11 2005 Dag Wieers <dag@wieers.com> - 0.6.0-1
- Initial package. (using DAR)
