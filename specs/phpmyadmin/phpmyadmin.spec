# $Id$
# Authority: jim

%define real_name phpMyAdmin

Summary: Web application to manage MySQL
Name: phpmyadmin
Version: 2.11.11
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://www.phpmyadmin.net/

#Source: http://dl.sf.net/phpmyadmin/phpMyAdmin-%{version}-all-languages.tar.bz2
Source: http://downloads.sourceforge.net/project/phpmyadmin/phpMyAdmin/%{version}/phpMyAdmin-%{version}-all-languages.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
Requires: php-mysql >= 4.1.0
Requires: php-mbstring >= 4.1.0
%{?el5:Requires: php-mcrypt}
Requires: webserver
Obsoletes: phpMyAdmin <= %{version}-%{release}
Provides: phpMyAdmin = %{version}-%{release}

%description
phpMyAdmin can manage a whole MySQL server (needs a super-user) as well as a
single database. To accomplish the latter you'll need a properly set up MySQL
user who can read/write only the desired database. It's up to you to look up
the appropriate part in the MySQL manual.

%prep
%setup -n %{real_name}-%{version}-all-languages

%{__cat} <<EOF >phpmyadmin.conf
#
#  %{summary}
#

<Directory "%{_datadir}/phpmyadmin">
  Order Deny,Allow
  Deny from all
  Allow from 127.0.0.1
</Directory>

Alias /phpmyadmin %{_datadir}/%{name}
Alias /phpMyAdmin %{_datadir}/%{name}
Alias /mysqladmin %{_datadir}/%{name}
EOF

%build

%install
%{__rm} -rf %{buildroot}
%{__mkdir} -p %{buildroot}/%{_datadir}/%{name}
%{__mkdir} -p %{buildroot}/%{_sysconfdir}/httpd/conf.d/
%{__mkdir} -p %{buildroot}/%{_sysconfdir}/%{name}

%{__install} -d -m0755 %{buildroot}%{_datadir}/%{name}/
%{__cp} -av *.{php,html,css,ico} %{buildroot}%{_datadir}/%{name}/
%{__cp} -av contrib/ js/ lang/ libraries/ pmd/ scripts/ themes/ %{buildroot}%{_datadir}/%{name}/

%{__install} -Dp -m0644 config.sample.inc.php %{buildroot}%{_datadir}/%{name}/config.inc.php
%{__install} -Dp -m0644 phpmyadmin.conf %{buildroot}%{_sysconfdir}/httpd/conf.d/phpmyadmin.conf

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog CREDITS Documentation.* INSTALL LICENSE README RELEASE-DATE* TODO
%config(noreplace) %{_sysconfdir}/httpd/conf.d/phpmyadmin.conf
%{_datadir}/%{name}/

%defattr(0640, root, apache, 0755)
%config(noreplace) %{_datadir}/%{name}/config.inc.php

%changelog
* Wed Sep 08 2010 David Hrbáč <david@hrbac.cz> - 2.11.11-1
- new upstream version

* Wed Sep 01 2010 David Hrbáč <david@hrbac.cz> - 2.11.10.1-1
- new upstream release - CVE-2010-3056, CVE-2010-3055
- added Requires: php-mbstring

* Mon Jan 4 2010 Fabian Arrotin <fabian.arrotin@arrfab.net>- 2.11.10-2
- Fixed a conditional Requires: php-mcrypt only for EL5

* Tue Dec 29 2009 Christoph Maser <cmr@financial.com> - 2.11.10-1
- Updated to version 2.11.10.

* Fri Oct 16 2009 David Hrbáč <david@hrbac.cz> - 2.11.9.6-1
- new upstream release

* Fri Apr 03 2009 Jim <quien-sabe@metaorg.com> - 2.11.9.5-1
- Updated to release 2.11.9.5.

* Mon Nov 03 2008 Dag Wieers <dag@wieers.com> - 2.11.9.3-1
- Updated to release 2.11.9.3.

* Mon Sep 22 2008 Jim <quien-sabe@metaorg.com> - 2.11.9.2-1
- Updated to release 2.11.9.2.

* Mon Sep 15 2008 Jim <quien-sabe@metaorg.com> - 2.11.9.1-1
- Updated to release 2.11.9.1.

* Thu Aug 28 2008 Jim <quien-sabe@metaorg.com> - 2.11.9-1
- Updated to release 2.11.9.

* Tue Jul 29 2008 Jim <quien-sabe@metaorg.com> - 2.11.8.1-1
- Updated to release 2.11.8.1.

* Mon Jul 28 2008 Jim <quien-sabe@metaorg.com> - 2.11.8-1
- Updated to release 2.11.8.

* Tue Jul 15 2008 Jim <quien-sabe@metaorg.com> - 2.11.7.1-1
- Updated to release 2.11.7.1.

* Mon Jun 23 2008 Jim <quien-sabe@metaorg.com> - 2.11.7-1
- Updated to release 2.11.7.

* Tue Apr 29 2008 Jim <quien-sabe@metaorg.com> - 2.11.6-1
- Updated to release 2.11.6.

* Tue Apr 22 2008 Jim <quien-sabe@metaorg.com> - 2.11.5.2-1
- Updated to release 2.11.5.2.

* Mon Mar 31 2008 Jim <quien-sabe@metaorg.com> - 2.11.5.1-1
- Updated to release 2.11.5.1.

* Sun Mar 02 2008 Dag Wieers <dag@wieers.com> - 2.11.5-1
- Updated to release 2.11.5.

* Sat Jan 12 2008 Jim <quien-sabe@metaorg.com> - 2.11.4-1
- Updated to release 2.11.4.

* Tue Dec 11 2007 Dag Wieers <dag@wieers.com> - 2.11.3-1
- Updated to release 2.11.3.

* Tue Nov 27 2007 Dag Wieers <dag@wieers.com> - 2.11.2.2-1
- Updated to release 2.11.2.2.

* Wed Oct 17 2007 Dag Wieers <dag@wieers.com> - 2.11.1.2-1
- Updated to release 2.11.1.2.

* Sat Sep 22 2007 Dag Wieers <dag@wieers.com> - 2.11.1-1
- Updated to release 2.11.1.

* Thu Aug 23 2007 Jim <quien-sabe@metaorg.com> - 2.11.0-1
- Updated to release 2.11.0.

* Thu Jul 26 2007 Dag Wieers <dag@wieers.com> - 2.10.3-2
- Cosmetic cleanup.

* Fri Jul 20 2007 Jim <quien-sabe@metaorg.com> - 2.10.3-1
- Updated to latest upstream version

* Sun Jun 17 2007 Jim <quien-sabe@metaorg.com> - 2.10.2-1
- Updated to latest upstream version

* Tue Mar 6 2007 Jim <quien-sabe@metaorg.com> - 2.10.0.2-1
- Updated to latest upstream version

* Tue Jan 16 2007 Jim <quien-sabe@metaorg.com> - 2.9.2-1
- Updated to latest upstream version

* Tue Jan 16 2007 Jim <quien-sabe@metaorg.com> - 2.9.2-1
- Updated to latest upstream version

* Mon Nov 20 2006 Jim <quien-sabe@metaorg.com> - 2.9.1.1-1
- Updated to latest upstream version

* Fri Nov 10 2006 Jim <quien-sabe@metaorg.com> - 2.9.1-1
- Updated to latest upstream version

* Sun Nov 5 2006 Jim <quien-sabe@metaorg.com> - 2.9.0.3-1
- Updated to latest upstream version

* Wed Oct 4 2006 Jim <quien-sabe@metaorg.com> - 2.9.0.2-1
- Updated to latest upstream version

* Mon Oct 2 2006 Jim <quien-sabe@metaorg.com> - 2.9.0.1-1
- Updated to latest upstream version

* Wed Sep 20 2006 Jim <quien-sabe@metaorg.com> - 2.9.0-1
- Updated to latest upstream version

* Tue Aug 22 2006 Jim <quien-sabe@metaorg.com> - 2.8.2.4-1
- Updated to latest upstream version

* Wed Aug 2 2006 Jim <quien-sabe@metaorg.com> - 2.8.2.1-1
- Updated to latest upstream version

* Sun May 21 2006 Jim <quien-sabe@metaorg.com> - 2.8.1-2
- Fixed an issue with the apache conf file

* Sat May 20 2006 Jim <quien-sabe@metaorg.com> - 2.8.1-1
- Updated to lastest upstream version

* Fri Apr 7 2006 Jim Richardson <devlop@aidant.net> - 2.8.0.3-1
- Initial package.
