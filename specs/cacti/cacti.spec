# $Id$

# Authority: dag
# Upstream: <cacti-user@lists.sourceforge.net>

%define real_version 0.8.5a

Summary: Network monitoring/graphing tool
Name: cacti
Version: 0.8.5
Release: 1.a
License: GPL
Group: Applications/System
URL: http://www.raxnet.net/products/cacti/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.raxnet.net/downloads/cacti/cacti-%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: mysql-devel
%{?rhel3:BuildRequires: net-snmp-devel}
%{?rh90:BuildRequires: net-snmp-devel}
%{?rh80:BuildRequires: net-snmp-devel}
%{?rh73:BuildRequires: ucd-snmp-devel}
%{?rhel21:BuildRequires: ucd-snmp-devel}
%{?rh62:BuildRequires: ucd-snmp-devel}

Requires: webserver, mysql, net-snmp, rrdtool
Requires: php, php-mysql, php-snmp, php-rrdtool

%description
Cacti is a complete frontend to RRDTool. It stores all of the necessary 
information to create graphs and populate them with data in a MySQL
database. 

The frontend is completely PHP driven. Along with being able to maintain
graphs, data sources, and round robin archives in a database, Cacti also
handles the data gathering. There is SNMP support for those used to
creating traffic graphs with MRTG.

%package docs
Summary: Documentation for package %{name}
Group: Documentation

%description docs
Cacti is a complete frontend to RRDTool. It stores all of the necessary 
information to create graphs and populate them with data in a MySQL
database. 

This package includes the documentation for %{name}.

%prep
%setup -n %{name}-%{real_version}

echo -e "*/5 * * * *\tcacti\tphp %{_localstatedir}/www/html/cacti/cmd.php &>/dev/null" >cacti.crontab

### Add a default cacti.conf for Apache.
%{__cat} <<EOF >cacti.httpd
Alias /cacti/ %{_localstatedir}/www/cacti/
<Directory %{_localstatedir}/www/cacti/>
        DirectoryIndex index.php
	Options -Indexes
	AllowOverride all
        order deny,allow
        deny from all
        allow from 127.0.0.1
	AddType application/x-httpd-php .php
	php_flag magic_quotes_gpc on
	php_flag track_vars on
</Directory>
EOF

%build
cd cactid
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_localstatedir}/www/cacti/
%{__install} -m0644 *.php cacti.sql %{buildroot}%{_localstatedir}/www/cacti/
%{__cp} -avx docs/ images/ include/ install/ lib/ log/ resource/ rra/ scripts/ %{buildroot}%{_localstatedir}/www/cacti/

%{__install} -D -m0755 cactid/cactid %{buildroot}%{_bindir}/cactid
%{__install} -D -m0644 cactid/cactid.conf %{buildroot}%{_sysconfdir}/cactid.conf
%{__install} -D -m0644 cacti.crontab %{buildroot}%{_sysconfdir}/cron.d/cacti
%{__install} -D -m0644 cacti.httpd %{buildroot}%{_sysconfdir}/httpd/conf.d/cacti.conf

%pre
useradd -d %{_localstatedir}/www/cacti cacti &>/dev/null || :

%postun
userdel cacti &>/dev/null || :

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc LICENSE README cactid/AUTHORS cactid/ChangeLog cactid/COPYING cactid/INSTALL cactid/NEWS
%config(noreplace) %{_sysconfdir}/cactid.conf
%config(noreplace) %{_localstatedir}/www/cacti/include/config.php
%config(noreplace) %{_sysconfdir}/httpd/conf.d/*
%config %{_sysconfdir}/cron.d/*
%dir %{_localstatedir}/www/cacti/
%{_localstatedir}/www/cacti/*.php
%{_localstatedir}/www/cacti/cacti.sql
%{_localstatedir}/www/cacti/docs/
%{_localstatedir}/www/cacti/images/
%{_localstatedir}/www/cacti/include/
%{_localstatedir}/www/cacti/install/
%{_localstatedir}/www/cacti/lib/
%{_localstatedir}/www/cacti/resource/
%{_localstatedir}/www/cacti/scripts/
%{_bindir}/*
%defattr(-, cacti, cacti, 0755 )
%{_localstatedir}/www/cacti/log/
%{_localstatedir}/www/cacti/rra/

%files docs
%defattr(-, root, root, 0755)
%doc docs/

%changelog
* Fri Apr 02 2004 Dag Wieers <dag@wieers.com> - 0.8.5-1.a
- Updated to release 0.8.5a.

* Thu Apr 01 2004 Dag Wieers <dag@wieers.com> - 0.8.5-1
- Fixed cacti.httpd. (Dean Takemori)

* Tue Feb 17 2004 Dag Wieers <dag@wieers.com> - 0.8.5-0
- Cosmetic rebuild for Group-tag.
- Initial package. (using DAR)
