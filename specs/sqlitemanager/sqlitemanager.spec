# $Id$
# Authority: dag
# Upstream: Frédéric Henninot <fhenninot$freesurf,fr>

%define real_name SQLiteManager

Summary: Multilingual web based tool to manage SQLite database
Name: sqlitemanager
Version: 1.2.0
Release: 1%{?dist}
License: GPL
Group: Applications/Databases
URL: http://sqlitemanager.sourceforge.net/

Patch0: config.patch
Source: http://dl.sf.net/sqlitemanager/SQLiteManager-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
Requires: php

%description
SQLiteManager is a multilingual web based tool to manage SQLite database.
The programming language used is: PHP4, but work fine with PHP5.

%prep
%setup -n %{real_name}-%{version}
%patch -p1

### FIXME: Add a default sqlitemanager.conf for Apache. (Please fix upstream)
%{__cat} <<EOF >sqlitemanager.httpd
### You need to include conf.d/php.conf to make it work.

Alias /sqlitemanager/ %{_localstatedir}/www/sqlitemanager/

<Directory %{_localstatedir}/www/sqlitemanager/>
	DirectoryIndex index.php
	order deny,allow
	deny from all
	allow from 127.0.0.1
	<FilesMatch "(\.inc\.php|\.db)$">
		order deny,allow
		deny from all
	</FilesMatch>
</Directory>

EOF

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_localstatedir}/www/sqlitemanager/
%{__install} -p -m0644 *.php *.ico *.sqlite *.sqlite3 %{buildroot}%{_localstatedir}/www/sqlitemanager/
%{__cp} -R include jscalendar lang plugins spaw theme  %{buildroot}%{_localstatedir}/www/sqlitemanager/

find %{buildroot}%{_localstatedir}/www/sqlitemanager -type f -exec chmod -x {} \;

%{__install} -d %{buildroot}%{_localstatedir}/www/sqlitemanager/config
%{__mv} %{buildroot}%{_localstatedir}/www/sqlitemanager/include/*.db %{buildroot}%{_localstatedir}/www/sqlitemanager/config/

%{__install} -Dp -m0644 sqlitemanager.httpd %{buildroot}%{_sysconfdir}/httpd/conf.d/sqlitemanager.conf

%post
if [ -f %{_sysconfdir}/httpd/conf/httpd.conf ]; then
	if ! grep -q "Include .*/sqlitemanager.conf" %{_sysconfdir}/httpd/conf/httpd.conf; then
		echo -e "\n# Include %{_sysconfdir}/httpd/conf.d/sqlitemanager.conf" >> %{_sysconfdir}/httpd/conf/httpd.conf
#		/sbin/service httpd restart
	fi
fi

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, apache, apache, 0755)
%doc CHANGES LICENCE TODO INSTALL
%config(noreplace) %{_sysconfdir}/httpd/conf.d/*.conf
%config(noreplace) %{_localstatedir}/www/sqlitemanager/config/*.db
%{_localstatedir}/www/sqlitemanager/

%changelog
* Sat May 13 2006 Edward Rudd <rpms@outoforder.cc> 1.2.0-1
- updated to 1.2.0
- moved config*.db files to different directory and tagged them as config
- patched config.inc.php to reflect new config*.db location

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.9.6-1.2
- Rebuild for Fedora Core 5.

* Thu Apr 29 2004 Dag Wieers <dag@wieers.com> - 0.9.6-1
- Updated to release 0.9.6.

* Wed Mar 31 2004 Dag Wieers <dag@wieers.com> - 0.9.4-2
- Cosmetic rebuild for Group-tag and BuildArch-tag.

* Thu Mar 11 2004 Dag Wieers <dag@wieers.com> - 0.9.4-1
- Updated to release 0.9.4.

* Sat Feb 29 2004 Dag Wieers <dag@wieers.com> - 0.9.3-0
- Initial package. (using DAR)
