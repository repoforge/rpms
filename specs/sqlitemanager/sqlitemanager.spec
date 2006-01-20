# $Id$
# Authority: dag
# Upstream: Frédéric Henninot <fhenninot$freesurf,fr>

%define real_name SQLiteManager

Summary: Multilingual web based tool to manage SQLite database
Name: sqlitemanager
Version: 0.9.6
Release: 1
License: GPL
Group: Applications/Databases
URL: http://sqlitemanager.sourceforge.net/

Source: http://dl.sf.net/sqlitemanager/SQLiteManager-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
Requires: php

%description
SQLiteManager is a multilingual web based tool to manage SQLite database.
The programming language used is: PHP4, but work fine with PHP5.

%prep
%setup -n %{real_name}-%{version}

### FIXME: Add a default sqlitemanager.conf for Apache. (Please fix upstream)
%{__cat} <<EOF >sqlitemanager.httpd
### You need to include conf.d/php.conf to make it work.

Alias /sqlitemanager/ %{_localstatedir}/www/sqlitemanager/

<Directory %{_localstatedir}/www/sqlitemanager/>
	DirectoryIndex index.php
	order deny,allow
	deny from all
	allow from 127.0.0.1
</Directory>

<FilesMatch "\.inc\.php$">
	order deny,allow
	deny from all
</FilesMatch>
EOF

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_localstatedir}/www/sqlitemanager/{include,lang,theme/default,pics}/
%{__install} -p -m0644 *.php *.sqlite %{buildroot}%{_localstatedir}/www/sqlitemanager/
%{__install} -p -m0644 include/*.{db,js,php} %{buildroot}%{_localstatedir}/www/sqlitemanager/include/
%{__install} -p -m0644 lang/*.inc.php %{buildroot}%{_localstatedir}/www/sqlitemanager/lang/
%{__install} -p -m0644 theme/default/*.{css,php} %{buildroot}%{_localstatedir}/www/sqlitemanager/theme/default/
%{__install} -p -m0644 pics/*.{gif,png} %{buildroot}%{_localstatedir}/www/sqlitemanager/pics/

%{__install} -Dp -m0644 sqlitemanager.httpd %{buildroot}%{_sysconfdir}/httpd/conf.d/sqlitemanager.conf

%post
if [ -f %{_sysconfdir}/httpd/conf/httpd.conf ]; then
	if ! grep -q "Include .*/apcupsd.conf" %{_sysconfdir}/httpd/conf/httpd.conf; then
		echo -e "\n# Include %{_sysconfdir}/httpd/conf.d/sqlitemanager.conf" >> %{_sysconfdir}/httpd/conf/httpd.conf
#		/sbin/service httpd restart
	fi
fi

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, apache, apache, 0755)
%doc CHANGES LICENCE TODO
%config(noreplace) %{_sysconfdir}/httpd/conf.d/*.conf
%{_localstatedir}/www/sqlitemanager/

%changelog
* Thu Apr 29 2004 Dag Wieers <dag@wieers.com> - 0.9.6-1
- Updated to release 0.9.6.

* Wed Mar 31 2004 Dag Wieers <dag@wieers.com> - 0.9.4-2
- Cosmetic rebuild for Group-tag and BuildArch-tag.

* Thu Mar 11 2004 Dag Wieers <dag@wieers.com> - 0.9.4-1
- Updated to release 0.9.4.

* Sat Feb 29 2004 Dag Wieers <dag@wieers.com> - 0.9.3-0
- Initial package. (using DAR)
