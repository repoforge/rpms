# ExclusiveDist: el6

%define pkgname	phpMyAdmin

Summary:	Handle the administration of MySQL over the World Wide Web
Name:		phpMyAdmin
Version:	3.5.1
Release:	1%{?dist}
License:	GPLv2+
Group:		Applications/Internet
URL:		http://www.phpmyadmin.net/
#Source0:	http://downloads.sourceforge.net/projects/phpmyadmin/files/%{version}/%{pkgname}/%{pkgname}-%{version}-all-languages.tar.bz2
Source0:    http://sourceforge.net/projects/phpmyadmin/files/%{pkgname}/%{version}/%{pkgname}-%{version}-all-languages.tar.bz2
Source1:    phpMyAdmin-config.inc.php
Source2:	phpMyAdmin.htaccess
%if 0%{?rhel} != 5
Requires:	httpd, php >= 5.2.0, php-mysql >= 5.2.0, php-mcrypt >= 5.2.0
Requires:	php-mbstring >= 5.2.0, php-gd >= 5.2.0
%else
Requires:	httpd, php53, php53-mysql, php53-mcrypt, php53-mbstring, php53-gd
Provides:	phpMyAdmin = %{version}-%{release}
%endif
Provides:	phpmyadmin = %{version}-%{release}
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
phpMyAdmin is a tool written in PHP intended to handle the administration of
MySQL over the World Wide Web. Most frequently used operations are supported
by the user interface (managing databases, tables, fields, relations, indexes,
users, permissions), while you still have the ability to directly execute any
SQL statement.

Features include an intuitive web interface, support for most MySQL features
(browse and drop databases, tables, views, fields and indexes, create, copy,
drop, rename and alter databases, tables, fields and indexes, maintenance
server, databases and tables, with proposals on server configuration, execute,
edit and bookmark any SQL-statement, even batch-queries, manage MySQL users
and privileges, manage stored procedures and triggers), import data from CSV
and SQL, export data to various formats: CSV, SQL, XML, PDF, OpenDocument Text
and Spreadsheet, Word, Excel, LATEX and others, administering multiple servers,
creating PDF graphics of your database layout, creating complex queries using
Query-by-example (QBE), searching globally in a database or a subset of it,
transforming stored data into any format using a set of predefined functions,
like displaying BLOB-data as image or download-link and much more...

%prep
%setup -q -n %{pkgname}-%{version}-all-languages

# Setup vendor config file
sed -e "/'CHANGELOG_FILE'/s@./ChangeLog@%{_datadir}/doc/%{name}-%{version}/ChangeLog@" \
    -e "/'LICENSE_FILE'/s@./LICENSE@%{_datadir}/doc/%{name}-%{version}/LICENSE@" \
    -e "/'CONFIG_DIR'/s@'./'@'%{_sysconfdir}/%{pkgname}/'@" \
    -e "/'SETUP_CONFIG_FILE'/s@./config/config.inc.php@%{_localstatedir}/lib/%{pkgname}/config/config.inc.php@" \
    -i libraries/vendor_config.php

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT{%{_datadir}/%{pkgname},%{_sysconfdir}/{httpd/conf.d,%{pkgname}}}
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/lib/%{pkgname}/{upload,save,config}
cp -ad * $RPM_BUILD_ROOT%{_datadir}/%{pkgname}
install -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d/%{pkgname}.conf
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/%{pkgname}/config.inc.php

rm -f $RPM_BUILD_ROOT%{_datadir}/%{pkgname}/{[CIRLT]*,*txt}
rm -f $RPM_BUILD_ROOT%{_datadir}/%{pkgname}/{libraries,setup/{lib,frames}}/.htaccess
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{pkgname}/contrib

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc ChangeLog README LICENSE Documentation.txt
%{_datadir}/%{pkgname}/
%dir %{_sysconfdir}/%{pkgname}/
%config(noreplace) %{_sysconfdir}/%{pkgname}/config.inc.php
%config(noreplace) %{_sysconfdir}/httpd/conf.d/%{pkgname}.conf
%dir %{_localstatedir}/lib/%{pkgname}/
%dir %attr(0755,apache,apache) %{_localstatedir}/lib/%{pkgname}/upload
%dir %attr(0755,apache,apache) %{_localstatedir}/lib/%{pkgname}/save
%dir %attr(0755,apache,apache) %{_localstatedir}/lib/%{pkgname}/config

%changelog
* Fri May 04 2012 David Hrbáč <david@hrbac.cz> - 3.5.1-1
- new upstream release

* Mon Apr 02 2012 David Hrbáč <david@hrbac.cz> - 3.4.10.2-1
- new upstream release

* Sat Feb 18 2012 David Hrbáč <david@hrbac.cz> - 3.4.10.1-1
- new upstream release

* Wed Feb 15 2012 David Hrbáč <david@hrbac.cz> - 3.4.10-1
- new upstream release

* Mon Jan 02 2012 David Hrbáč <david@hrbac.cz> - 3.4.9-1
- new upstream release

* Mon Dec 12 2011 David Hrbáč <david@hrbac.cz> - 3.4.8-1
- new upstream release

* Thu Nov 10 2011 David Hrbáč <david@hrbac.cz> - 3.4.7.1-1
- new upstream release

* Thu Oct 27 2011 David Hrbáč <david@hrbac.cz> - 3.4.7-1
- initial rebuild

* Sun Sep 18 2011 Robert Scheck <robert@fedoraproject.org> 3.4.5-1
- Upgrade to 3.4.5 (#733638, #738681, #629214)

* Thu Aug 25 2011 Robert Scheck <robert@fedoraproject.org> 3.4.4-1
- Upgrade to 3.4.4 (#733475, #733477, #733480)

* Tue Jul 26 2011 Robert Scheck <robert@fedoraproject.org> 3.4.3.2-2
- Disabled the warning for missing internal database relation
- Reworked spec file to build phpMyAdmin3 for RHEL 5 (#725885)

* Mon Jul 25 2011 Robert Scheck <robert@fedoraproject.org> 3.4.3.2-1
- Upgrade to 3.4.3.2 (#725377, #725381, #725382, #725383, #725384)

* Wed Jul 06 2011 Robert Scheck <robert@fedoraproject.org> 3.4.3.1-1
- Upgrade to 3.4.3.1 (#718964)

* Mon Jun 13 2011 Robert Scheck <robert@fedoraproject.org> 3.4.2-1
- Upgrade to 3.4.2 (#711743)

* Sun May 29 2011 Robert Scheck <robert@fedoraproject.org> 3.4.1-1
- Upgrade to 3.4.1 (#704171)

* Mon Mar 21 2011 Robert Scheck <robert@fedoraproject.org> 3.3.10-1
- Upstream released 3.3.10 (#661335, #662366, #662367, #689213)

* Sun Feb 13 2011 Robert Scheck <robert@fedoraproject.org> 3.3.9.2-1
- Upstream released 3.3.9.2 (#676172)

* Thu Feb 10 2011 Robert Scheck <robert@fedoraproject.org> 3.3.9.1-1
- Upstream released 3.3.9.1 (#676172)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 03 2011 Robert Scheck <robert@fedoraproject.org> 3.3.9-1
- Upstream released 3.3.9 (#666925)

* Mon Nov 29 2010 Robert Scheck <robert@fedoraproject.org> 3.3.8.1-1
- Upstream released 3.3.8.1

* Fri Oct 29 2010 Robert Scheck <robert@fedoraproject.org> 3.3.8-1
- Upstream released 3.3.8 (#631748)

* Wed Sep 08 2010 Robert Scheck <robert@fedoraproject.org> 3.3.7-1
- Upstream released 3.3.7 (#631824, #631829)

* Sun Aug 29 2010 Robert Scheck <robert@fedoraproject.org> 3.3.6-1
- Upstream released 3.3.6 (#628301)

* Fri Aug 20 2010 Robert Scheck <robert@fedoraproject.org> 3.3.5.1-1
- Upstream released 3.3.5.1 (#625877, #625878)
- Added patch to fix wrong variable check at nopassword (#622428)

* Tue Jul 27 2010 Robert Scheck <robert@fedoraproject.org> 3.3.5-1
- Upstream released 3.3.5 (#618586)

* Tue Jun 29 2010 Robert Scheck <robert@fedoraproject.org> 3.3.4-1
- Upstream released 3.3.4 (#609057)

* Sat Jun 26 2010 Robert Scheck <robert@fedoraproject.org> 3.3.3-1
- Upstream released 3.3.3 (#558322, #589288, #589487)

* Sun Jan 10 2010 Robert Scheck <robert@fedoraproject.org> 3.2.5-1
- Upstream released 3.2.5

* Thu Dec 03 2009 Robert Scheck <robert@fedoraproject.org> 3.2.4-1
- Upstream released 3.2.4 (#540871, #540891)

* Thu Nov 05 2009 Robert Scheck <robert@fedoraproject.org> 3.2.3-1
- Upstream released 3.2.3

* Tue Oct 13 2009 Robert Scheck <robert@fedoraproject.org> 3.2.2.1-1
- Upstream released 3.2.2.1 (#528769)
- Require php-mcrypt for cookie authentication (#526979)

* Sun Sep 13 2009 Robert Scheck <robert@fedoraproject.org> 3.2.2-1
- Upstream released 3.2.2

* Sun Sep 06 2009 Robert Scheck <robert@fedoraproject.org> 3.2.1-2
- Added ::1 for localhost/loopback access (for IPv6 users)

* Mon Aug 10 2009 Robert Scheck <robert@fedoraproject.org> 3.2.1-1
- Upstream released 3.2.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jun 30 2009 Robert Scheck <robert@fedoraproject.org> 3.2.0.1-1
- Upstream released 3.2.0.1 (#508879)

* Tue Jun 30 2009 Robert Scheck <robert@fedoraproject.org> 3.2.0-1
- Upstream released 3.2.0

* Fri May 15 2009 Robert Scheck <robert@fedoraproject.org> 3.1.5-1
- Upstream released 3.1.5

* Sat Apr 25 2009 Robert Scheck <robert@fedoraproject.org> 3.1.4-1
- Upstream released 3.1.4

* Tue Apr 14 2009 Robert Scheck <robert@fedoraproject.org> 3.1.3.2-1
- Upstream released 3.1.3.2 (#495768)

* Wed Mar 25 2009 Robert Scheck <robert@fedoraproject.org> 3.1.3.1-1
- Upstream released 3.1.3.1 (#492066)

* Sun Mar 01 2009 Robert Scheck <robert@fedoraproject.org> 3.1.3-1
- Upstream released 3.1.3

* Mon Feb 23 2009 Robert Scheck <robert@fedoraproject.org> 3.1.2-2
- Rebuilt against rpm 4.6

* Tue Jan 20 2009 Robert Scheck <robert@fedoraproject.org> 3.1.2-1
- Upstream released 3.1.2

* Thu Dec 11 2008 Robert Scheck <robert@fedoraproject.org> 3.1.1-1
- Upstream released 3.1.1 (#475954)

* Sat Nov 29 2008 Robert Scheck <robert@fedoraproject.org> 3.1.0-1
- Upstream released 3.1.0
- Replaced LocationMatch with Directory directive (#469451)

* Thu Oct 30 2008 Robert Scheck <robert@fedoraproject.org> 3.0.1.1-1
- Upstream released 3.0.1.1 (#468974)

* Wed Oct 22 2008 Robert Scheck <robert@fedoraproject.org> 3.0.1-1
- Upstream released 3.0.1

* Sun Oct 19 2008 Robert Scheck <robert@fedoraproject.org> 3.0.0-1
- Upstream released 3.0.0

* Mon Sep 22 2008 Robert Scheck <robert@fedoraproject.org> 2.11.9.2-1
- Upstream released 2.11.9.2 (#463260)

* Tue Sep 16 2008 Robert Scheck <robert@fedoraproject.org> 2.11.9.1-1
- Upstream released 2.11.9.1 (#462430)

* Fri Aug 29 2008 Robert Scheck <robert@fedoraproject.org> 2.11.9-1
- Upstream released 2.11.9

* Mon Jul 28 2008 Robert Scheck <robert@fedoraproject.org> 2.11.8.1-1
- Upstream released 2.11.8.1 (#456637, #456950)

* Mon Jul 28 2008 Robert Scheck <robert@fedoraproject.org> 2.11.8-1
- Upstream released 2.11.8 (#456637)

* Tue Jul 15 2008 Robert Scheck <robert@fedoraproject.org> 2.11.7.1-1
- Upstream released 2.11.7.1 (#455520)

* Mon Jun 23 2008 Robert Scheck <robert@fedoraproject.org> 2.11.7-1
- Upstream released 2.11.7 (#452497)

* Tue Apr 29 2008 Robert Scheck <robert@fedoraproject.org> 2.11.6-1
- Upstream released 2.11.6

* Tue Apr 22 2008 Robert Scheck <robert@fedoraproject.org> 2.11.5.2-1
- Upstream released 2.11.5.2 (#443683)

* Sat Mar 29 2008 Robert Scheck <robert@fedoraproject.org> 2.11.5.1-1
- Upstream released 2.11.5.1

* Mon Mar 03 2008 Robert Scheck <robert@fedoraproject.org> 2.11.5-1
- Upstream released 2.11.5

* Sun Jan 13 2008 Robert Scheck <robert@fedoraproject.org> 2.11.4-1
- Upstream released 2.11.4
- Corrected mod_security example in configuration file (#427119)

* Sun Dec 09 2007 Robert Scheck <robert@fedoraproject.org> 2.11.3-1
- Upstream released 2.11.3
- Removed the RPM scriptlets doing httpd restarts (#227025)
- Patched an information disclosure known as CVE-2007-0095 (#221694)
- Provide virtual phpmyadmin package and a httpd alias (#231431)

* Wed Nov 21 2007 Robert Scheck <robert@fedoraproject.org> 2.11.2.2-1
- Upstream released 2.11.2.2 (#393771)

* Tue Nov 20 2007 Mike McGrath <mmcgrath@redhat.com> 2.11.2.1-1
- Upstream released new version

* Fri Oct 29 2007 Mike McGrath <mmcgrath@redhat.com> 2.11.2-1
* upstream released new version

* Mon Oct 22 2007 Mike McGrath <mmcgrath@redhat.com> 2.11.1.2-1
* upstream released new version

* Thu Sep 06 2007 Mike McGrath <mmcgrath@redhat.com> 2.11.0-1
- Upstream released new version
- Altered sources file as required
- Added proper license

* Mon Jul 23 2007 Mike McGrath <mmcgrath@redhat.com> 2.10.3-1
- Upstream released new version

* Sat Mar 10 2007 Mike McGrath <mmcgrath@redhat.com> 2.10.0.2-3
- Switched to the actual all-languages, not just utf-8

* Sun Mar 04 2007 Mike McGrath <mmcgrath@redhat.com> 2.10.0.2-1
- Upstream released new version

* Sat Jan 20 2007 Mike McGrath <imlinux@gmail.com> 2.9.2-1
- Upstream released new version

* Fri Dec 08 2006 Mike McGrath <imlinux@gmail.com> 2.9.1.1-2
- Fixed bug in spec file

* Fri Dec 08 2006 Mike McGrath <imlinux@gmail.com> 2.9.1.1-1
- Upstream released new version

* Wed Nov 15 2006 Mike McGrath <imlinux@gmail.com> 2.9.1-3alpha
- Added dist tag

* Wed Nov 15 2006 Mike McGrath <imlinux@gmail.com> 2.9.1-2alpha
- Fixed 215159

* Fri Nov 10 2006 Mike McGrath <imlinux@gmail.com> 2.9.1-1alpha
- Added alpha tag since this is a release candidate

* Tue Nov 07 2006 Mike McGrath <imlinux@gmail.com> 2.9.1-1
- Upstream released new version

* Wed Oct 04 2006 Mike McGrath <imlinux@gmail.com> 2.9.0.2-1
- Upstream released new version

* Thu Jul 06 2006 Mike McGrath <imlinux@gmail.com> 2.8.2-2
- Fixed a typo in the Apache config

* Mon Jul 03 2006 Mike McGrath <imlinux@gmail.com> 2.8.2-1
- Upstream released 2.8.2
- Added more restrictive directives to httpd/conf.d/phpMyAdmin.conf
- removed htaccess file from the libraries dir
- Specific versions for various requires

* Sat May 13 2006 Mike McGrath <imlinux@gmail.com> 2.8.0.4-1
- Upstream released 2.8.0.4
- Added requires php, instead of requires httpd, now using webserver

* Sun May 07 2006 Mike McGrath <imlinux@gmail.com> 2.8.0.3-2
- Added mysql-php and php-mbstring as a requires

* Thu Apr 07 2006 Mike McGrath <imlinux@gmail.com> 2.8.0.3-1
- Fixed XSS vulnerability: PMASA-2006-1
- It was possible to conduct an XSS attack with a direct call to some scripts
- under the themes directory.

* Tue Apr 04 2006 Mike McGrath <imlinux@gmail.com> 2.8.0.2-3
- Made config files actually configs
- Moved doc files to the doc dir

* Tue Apr 04 2006 Mike McGrath <imlinux@gmail.com> 2.8.0.2-2
- Moved everything to %{_datadir}
- Moved config file to /etc/
- Used description from phpMyAdmin project info

* Mon Apr 03 2006 Mike McGrath <imlinux@gmail.com> 2.8.0.2-1
- Initial Spec file creation for Fedora
