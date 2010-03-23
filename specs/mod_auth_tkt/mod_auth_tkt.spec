# $Id$
# Authority: shuff
# Upstream: <modauthtkt-users$lists,sourceforge,net>
# ExcludeDist: el3 el4

Summary: Single-sign-on authentication module for Apache
Name: mod_auth_tkt
Version: 2.1.0
Release: 2%{?dist}
License: GPL
Group: System Environment/Daemons
URL: http://www.openfusion.com.au/labs/mod_auth_tkt/

Source: http://www.openfusion.com.au/labs/dist/mod_auth_tkt/mod_auth_tkt-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: httpd-devel
Requires: httpd

%description
mod_auth_tkt is a lightweight single-sign-on authentication module for apache,
supporting versions 2.0.x and 2.2.x. It uses secure cookie-based tickets to
implement a single-signon framework that works across multiple apache instances
and servers.

mod_auth_tkt itself is completely repository-agnostic, as the actual
authentication is done by a user-supplied CGI or script in your language of
choice (examples are provided in Perl, with contrib libraries for use with
python and PHP). This allows authentication against virtually any kind of user
repository you can imagine (password files, ldap directories, databases, etc.)

mod_auth_tkt supports inactivity timeouts (including the ability to control how
aggressively the ticket is refreshed), the ability to include arbitrary user
data within the cookie, configurable cookie names and domains, and token-based
access to subsections of a site.

mod_auth_tkt works by checking incoming Apache requests for a (user-defined)
cookie containing a valid authentication ticket. The ticket is checked by
generating an MD5 checksum for the username and any (optional) user data from
the ticket together with the requesting IP address and a shared secret
available to the server. If the generated MD5 checksum matches the ticket's
checksum, the ticket is valid and the request is authorised. Requests without a
valid ticket are redirected to a configurable URL which is expected to validate
the user and generate a ticket for them. This package includes a Perl module
and working CGI scripts for generating the cookies, as well as contributed
classes for PHP and Python environments.

%package cgi
Summary: CGI scripts for mod_auth_tkt
Group: Applications/System
Requires: %{name} = %{version}
Requires: perl(Apache::Htpasswd)

%description cgi
Perl CGI scripts for use with mod_auth_tkt.

%prep
%setup -n %{name}-%{version}

%build
./configure --apxs="%{_sbindir}/apxs" --apachever="2.2"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
mkdir -p $RPM_BUILD_ROOT%{_libdir}/httpd/modules
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d
mkdir -p $RPM_BUILD_ROOT/var/www/auth
/usr/sbin/apxs -i -n "auth_tkt" -S LIBEXECDIR=$RPM_BUILD_ROOT%{_libdir}/httpd/modules src/mod_auth_tkt.la
install -m 644 conf/02_auth_tkt.conf $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d/
install -m 644 conf/auth_tkt_cgi.conf $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d/
cp -pr cgi/* $RPM_BUILD_ROOT/var/www/auth
rm -rf $RPM_BUILD_ROOT/var/www/auth/Apache
pushd doc
make DESTDIR=$RPM_BUILD_ROOT install
popd

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root)
%doc README* INSTALL LICENSE ChangeLog CREDITS contrib/
%doc %{_mandir}/man?/*
%config(noreplace) %{_sysconfdir}/httpd/conf.d/02_auth_tkt.conf
%{_libdir}/httpd/modules/*

%files cgi
%defattr(-, root, root)
%attr(0640,root,apache) %config(noreplace) %{_sysconfdir}/httpd/conf.d/auth_tkt_cgi.conf
%config(noreplace)/var/www/auth/AuthTktConfig.pm
%config(noreplace)/var/www/auth/tkt.css
/var/www/auth/*.cgi

%changelog
* Tue Mar 23 2010 Steve Huff <shuff@vecna.org> - 2.1.0-2
- The CGI Apache config file goes in the cgi package.

* Wed Feb 10 2010 Steve Huff <shuff@vecna.org> - 2.1.0-1
- Initial package.
