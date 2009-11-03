# $Id$
# Authority: dag

%define real_name drupal

Summary: Drupal CMS
Name: drupal5
Version: 5.20
Release: 1%{?dist}
License: GPL
Group: Development/Languages
URL: http://drupal.org/

Source: http://ftp.drupal.org/files/projects/drupal-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: php >= 4.3.3
Requires: httpd, mysql, php >= 4.3.3
Requires: php-gd, php-mbstring, php-mysql

Obsoletes: drupal <= %{version}-%{release}
Provides: drupal = %{version}-%{release}

%description
Drupal is an open source content management platform. Drupal is equipped
with a powerful blend of features, Drupal can support a variety of
websites ranging from personal weblogs to large community-driven websites.

%prep
%setup -n %{real_name}-%{version}
%{__cat} <<EOF >drupal5.httpd
### Drupal 5
Alias /drupal %{_localstatedir}/www/drupal-%{version}

<Directory %{_localstatedir}/www/drupal-%{version}>
    AllowOverride All
</Directory>
EOF

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0644 drupal5.httpd %{buildroot}%{_sysconfdir}/httpd/conf.d/drupal5.conf
%{__install} -d -m0755 %{buildroot}%{_localstatedir}/www/drupal-%{version}/files/
%{__install} -Dp -m0644 .htaccess %{buildroot}%{_localstatedir}/www/drupal-%{version}/.htaccess
%{__cp} -av *.php %{buildroot}%{_localstatedir}/www/drupal-%{version}/
%{__cp} -av includes/ misc/ modules/ profiles/ scripts/ sites/ themes/ %{buildroot}%{_localstatedir}/www/drupal-%{version}/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, apache, apache, 0755)
%doc CHANGELOG.txt INSTALL.mysql.txt INSTALL.pgsql.txt INSTALL.txt LICENSE.txt MAINTAINERS.txt UPGRADE.txt
%config(noreplace) %{_localstatedir}/www/drupal-%{version}/sites/
%config(noreplace) %{_sysconfdir}/httpd/conf.d/drupal5.conf
%{_localstatedir}/www/drupal-%{version}/

%changelog
* Sun Sep 27 2009 Dag Wieers <dag@wieers.com> - 5.20-1
- Updated to release 5.20.

* Thu Jul 02 2009 Dag Wieers <dag@wieers.com> - 5.19-1
- Updated to release 5.19.

* Sun May 17 2009 Dag Wieers <dag@wieers.com> - 5.18-1
- Updated to release 5.18.

* Mon May 11 2009 Dag Wieers <dag@wieers.com> - 5.17-1
- Updated to release 5.17.

* Mon Jan 19 2009 Dag Wieers <dag@wieers.com> - 5.15-1
- Updated to release 5.15.

* Thu Dec 11 2008 Dag Wieers <dag@wieers.com> - 5.14-1
- Updated to release 5.14.

* Mon Feb 04 2008 Dag Wieers <dag@wieers.com> - 5.7-1
- Updated to release 5.7.

* Mon Jan 14 2008 Dag Wieers <dag@wieers.com> - 5.6-1
- Updated to release 5.6.

* Sun Oct 21 2007 Dag Wieers <dag@wieers.com> - 5.3-1
- Updated to release 5.3.

* Fri Oct 05 2007 Dag Wieers <dag@wieers.com> - 5.2-3
- Fixed typo in Requires. (Seán O Sullivan)

* Mon Oct 01 2007 Dag Wieers <dag@wieers.com> - 5.2-2
- Added missing php-gd and php-mbtstring requirements.
- Added empty files/ directory.

* Sun Sep 30 2007 Dag Wieers <dag@wieers.com> - 5.2-1
- Initial package. (using DAR)
