# Authority: dag
# Upstream: 

%define rname SQLiteManager

Summary: Multilingual web based tool to manage SQLite database.
Name: sqlitemanager
Version: 0.9.3
Release: 0
License: GPL
Group: Applications/
URL: http://sqlitemanager.sourceforge.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/sqlitemanager/SQLiteManager-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

Requires: php

%description
SQLiteManager is a multilingual web based tool to manage SQLite database.
The programming language used is: PHP4, but work fine with PHP5.

%prep
%setup -n %{rname}-%{version}

### FIXME: Add a default sqlitemanager.conf for Apache. (Please fix upstream)
%{__cat} <<EOF >sqlitemanager.conf
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
%{__install} -d -m0755 %{buildroot}%{_localstatedir}/www/sqlitemanager/{include,lang,theme/default,pics}/ \
			%{buildroot}%{_sysconfdir}/httpd/conf.d/
%{__install} -m0644 *.php *.sqlite %{buildroot}%{_localstatedir}/www/sqlitemanager/
%{__install} -m0644 include/*.{db,js,php} %{buildroot}%{_localstatedir}/www/sqlitemanager/include/
%{__install} -m0644 lang/*.inc.php %{buildroot}%{_localstatedir}/www/sqlitemanager/lang/
%{__install} -m0644 theme/default/*.{css,php} %{buildroot}%{_localstatedir}/www/sqlitemanager/theme/default/
%{__install} -m0644 pics/*.{gif,png} %{buildroot}%{_localstatedir}/www/sqlitemanager/pics/
%{__install} -m0644 sqlitemanager.conf %{buildroot}%{_sysconfdir}/httpd/conf.d/

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
* Sat Feb 29 2004 Dag Wieers <dag@wieers.com> - 
- Initial package. (using DAR)
