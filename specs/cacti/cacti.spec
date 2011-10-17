# $Id$
# Authority: dag
# Upstream: <cacti-user$lists,sf,net>

%define logmsg logger -t %{name}/rpm

Summary: Complete network graphing solution designed on top of RRDTool
Name: cacti
Version: 0.8.7h
Release: 1%{?dist}
License: GPL
Group: Applications/System
URL: http://www.cacti.net/

Source: http://www.cacti.net/downloads/cacti-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: mysql-devel
BuildRequires: net-snmp-devel
BuildRequires: net-snmp-utils
BuildRequires: openssl-devel

Requires: mysql
Requires: net-snmp
Requires: net-snmp-utils
Requires: php
Requires: php-mysql
# el3 doesn't contain php-snmp
%{!?el3:Requires: php-snmp}
Requires: rrdtool
Requires: webserver

%description
Cacti is a complete frontend to RRDTool. It stores all of the necessary
information to create graphs and populate them with data in a MySQL
database.

The frontend is completely PHP driven. Along with being able to maintain
graphs, data sources, and round robin archives in a database, Cacti also
handles the data gathering. There is SNMP support for those used to
creating traffic graphs with MRTG.

%package docs
Summary: Documentation for the cacti network graphing solution
Group: Documentation

%description docs
Cacti is a complete frontend to RRDTool. It stores all of the necessary
information to create graphs and populate them with data in a MySQL
database.

This package includes the documentation for %{name}.

%prep
%setup

echo -e "*/5 * * * *\tcacti\tphp %{_localstatedir}/www/cacti/poller.php &>/dev/null" >cacti.crontab

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

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_localstatedir}/www/cacti/
%{__install} -p -m0644 *.php cacti.sql %{buildroot}%{_localstatedir}/www/cacti/
%{__cp} -av cli/ docs/ images/ include/ install/ lib/ log/ resource/ rra/ scripts/ %{buildroot}%{_localstatedir}/www/cacti/

%{__install} -Dp -m0644 cacti.crontab %{buildroot}%{_sysconfdir}/cron.d/cacti
%{__install} -Dp -m0644 cacti.httpd %{buildroot}%{_sysconfdir}/httpd/conf.d/cacti.conf

%pre
if ! /usr/bin/id cacti &>/dev/null; then
    /usr/sbin/useradd -r -d %{_localstatedir}/www/cacti -s /bin/sh -c "cacti" cacti || \
        %logmsg "Unexpected error adding user \"cacti\". Aborting installation."
fi

%postun
if [ $1 -eq 0 ]; then
    /usr/sbin/userdel cacti || %logmsg "User \"cacti\" could not be deleted."
fi

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc LICENSE README
%config(noreplace) %{_localstatedir}/www/cacti/include/config.php
%config(noreplace) %{_sysconfdir}/httpd/conf.d/cacti.conf
%config %{_sysconfdir}/cron.d/cacti
%dir %{_localstatedir}/www/cacti/
%{_localstatedir}/www/cacti/*.php
%{_localstatedir}/www/cacti/cacti.sql
%{_localstatedir}/www/cacti/cli/
%{_localstatedir}/www/cacti/docs/
%{_localstatedir}/www/cacti/images/
%{_localstatedir}/www/cacti/include/
%{_localstatedir}/www/cacti/install/
%{_localstatedir}/www/cacti/lib/
%{_localstatedir}/www/cacti/resource/
%{_localstatedir}/www/cacti/scripts/

%defattr(-, cacti, cacti, 0755 )
%{_localstatedir}/www/cacti/log/
%{_localstatedir}/www/cacti/rra/

%files docs
%defattr(-, root, root, 0755)
%doc docs/*

%changelog
* Tue Sep 27 2011 Dag Wieers <dag@wieers.com> - 0.8.7h-1
- Updated to release 0.8.7h.

* Wed Sep 22 2010 David Hrbáč <david@hrbac.cz> - 0.8.7g-3
- added ping.patch, poller_interval.patch

* Thu Aug 12 2010 Yury V. Zaytsev <yury@shurup.com> - 0.8.7g-2
- Added patches from http://www.cacti.net/download_patches.php?version=0.8.7g
- Thanks to Shane Goulden for the update.
- Minor cleanup.

* Tue Jul 13 2010 Dag Wieers <dag@wieers.com> - 0.8.7g-1
- Updated to release 0.8.7g.

* Tue May 25 2010 Christoph Maser <cmaser@gmx.de> - 0.8.7f-1
- Updated to version 0.8.7f.
- Remove 0.8.7e patches

* Thu Dec 17 2009 Yury V. Zaytsev <yury@shurup.com> - 0.8.7e-3
- Removed obsolete rh6/7/el2 defines.

* Thu Dec 17 2009 Christoph Maser <cmr@financial.com> - 0.8.7e-2
- Add patches from http://www.cacti.net/download_patches.php

* Mon Jul 27 2009 Dag Wieers <dag@wieers.com> - 0.8.7e-1
- Updated to release 0.8.7e.

* Sun Feb 22 2009 Dag Wieers <dag@wieers.com> - 0.8.7d-1
- Updated to release 0.8.7d.

* Sun Feb 01 2009 Dag Wieers <dag@wieers.com> - 0.8.7c-1
- Updated to release 0.8.7c.

* Fri Mar 14 2008 Dag Wieers <dag@wieers.com> - 0.8.7b-2
- Added missing CLI interface. (William Burns)

* Tue Feb 12 2008 Dag Wieers <dag@wieers.com> - 0.8.7b-1
- Updated to release 0.8.7b.

* Wed Nov 28 2007 Dag Wieers <dag@wieers.com> - 0.8.7a-1
- Updated to release 0.8.7a.

* Fri Oct 26 2007 Dag Wieers <dag@wieers.com> - 0.8.7-1
- Updated to release 0.8.7.

* Thu Jan 18 2007 Matthias Saou <http://freshrpms.net/> 0.8.6j-1
- Make package noarch, as it should be.

* Thu Jan 18 2007 Dag Wieers <dag@wieers.com> - 0.8.6j-1
- Updated to release 0.8.6j.

* Wed Oct 11 2006 Dag Wieers <dag@wieers.com> - 0.8.6i-1
- Updated to release 0.8.6i.

* Thu Jan 05 2006 Dag Wieers <dag@wieers.com> - 0.8.6h-1
- Updated to release 0.8.6h.

* Sun Sep 11 2005 Dag Wieers <dag@wieers.com> - 0.8.6g-1
- Updated to release 0.8.6g.

* Tue Jul  5 2005 Matthias Saou <http://freshrpms.net/> 0.8.6f-2
- Add *-snmp-utils requirement (snmpget/walk).
- Minor cosmetic changes.

* Sat Jul 02 2005 Dries Verachtert <dries@ulyssis.org> - 0.8.6f-1
- Updated to release 0.8.6f.

* Tue Jun 28 2005 Dries Verachtert <dries@ulyssis.org> - 0.8.6e-1
- Updated to release 0.8.6e.

* Sat Apr 30 2005 Dag Wieers <dag@wieers.com> - 0.8.6d-1
- Updated to release 0.8.6d.

* Mon Apr 04 2005 Dag Wieers <dag@wieers.com> - 0.8.6c-2
- Fix for the crontab entry. (Gilles Chauvin, Joe Pruett)
- Removed the php-rrdtool dependency. (Gilles Chauvin, Joe Pruett)

* Fri Mar 18 2005 Dag Wieers <dag@wieers.com> - 0.8.6c-1
- Updated to release 0.8.6c.

* Wed Sep 29 2004 Dag Wieers <dag@wieers.com> - 0.8.6-1
- Updated to release 0.8.6.

* Thu Jun 10 2004 Dag Wieers <dag@wieers.com> - 0.8.5-2.a
- Fixed correct location in cron script. (Alex Vitola)

* Fri Apr 02 2004 Dag Wieers <dag@wieers.com> - 0.8.5-1.a
- Updated to release 0.8.5a.

* Thu Apr 01 2004 Dag Wieers <dag@wieers.com> - 0.8.5-1
- Fixed cacti.httpd. (Dean Takemori)

* Tue Feb 17 2004 Dag Wieers <dag@wieers.com> - 0.8.5-0
- Cosmetic rebuild for Group-tag.
- Initial package. (using DAR)
