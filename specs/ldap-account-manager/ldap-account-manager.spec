# $Id: _template.spec 765 2004-05-20 17:33:53Z dag $
# Authority: dag
# Upstream: 

Summary:  LDAP Account Manager
Name: ldap-account-manager
Version: 0.4.6
Release: 1
License: GPL
Group: Applications/Internet
URL: http://lam.sourceforge.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/lam/ldap-account-manager_%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
Requires: php, openldap >= 2.0, perl

%description
LDAP Account Manager (LAM) is a webfrontend for managing accounts stored
in an openLDAP server.

%prep
%setup

### FIXME: Add a default sqlitemanager.conf for Apache. (Please fix upstream)
%{__cat} <<EOF >lam.httpd
### You need to include conf.d/php.conf to make it work.

Alias /lam/ %{_localstatedir}/www/lam/

<Directory %{_localstatedir}/www/lam/>
	DirectoryIndex index.php
	order deny,allow
	deny from all
	allow from 127.0.0.1
</Directory>

<FilesMatch "\.inc$">
	order deny,allow
	deny from all
</FilesMatch>
EOF

%build

%install
%{__rm} -rf %{buildroot}

%{__install} -D -m0644 lam.httpd %{buildroot}%{_sysconfdir}/httpd/conf.d/lam.conf
%{__rm} -f lam.httpd

%{__install} -d -m0755 %{buildroot}%{_localstatedir}/www/lam/
%{__cp} -avx config/ %{buildroot}%{_localstatedir}/www/lam/
%{__cp} -avx lib/ %{buildroot}%{_localstatedir}/www/lam/
%{__cp} -avx sess/ %{buildroot}%{_localstatedir}/www/lam/
%{__cp} -avx tmp/ %{buildroot}%{_localstatedir}/www/lam/

find %{buildroot} -name "*.pl" -exec chmod a+x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING HISTORY INSTALL README TODO copyright docs/*
%config(noreplace) %{_sysconfdir}/httpd/conf.d/lam.conf
%dir %{_localstatedir}/www/lam/
%{_localstatedir}/www/lam/lib/

%defattr(-, apache, apache, 0755)
%config(noreplace) %{_localstatedir}/www/lam/config/
%{_localstatedir}/www/lam/sess/
%{_localstatedir}/www/lam/tmp/

%changelog
* Tue Jun 29 2004 Dag Wieers <dag@wieers.com> - 0.4.6-1
- Initial package. (using DAR)
