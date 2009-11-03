# $Id$
# Authority: dag

%define real_name drupal

Summary: Drupal CMS
Name: drupal4
Version: 4.7.11
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
%{__cat} <<EOF >drupal4.httpd
### Drupal 4
Alias /drupal %{_localstatedir}/www/drupal-%{version}

<Directory %{_localstatedir}/www/drupal-%{version}>
    AllowOverride All
</Directory>
EOF

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0644 drupal4.httpd %{buildroot}%{_sysconfdir}/httpd/conf.d/drupal4.conf
%{__install} -Dp -m0644 .htaccess %{buildroot}%{_localstatedir}/www/drupal-%{version}/.htaccess
%{__cp} -av *.php %{buildroot}%{_localstatedir}/www/drupal-%{version}/
%{__cp} -av includes/ misc/ modules/ scripts/ sites/ themes/ %{buildroot}%{_localstatedir}/www/drupal-%{version}/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, apache, apache, 0755)
%doc CHANGELOG.txt INSTALL.mysql.txt INSTALL.pgsql.txt INSTALL.txt LICENSE.txt MAINTAINERS.txt UPGRADE.txt
%config(noreplace) %{_localstatedir}/www/drupal-%{version}/sites/
%config(noreplace) %{_sysconfdir}/httpd/conf.d/drupal4.conf
%{_localstatedir}/www/drupal-%{version}/

%changelog
* Mon Jan 14 2008 Dag Wieers <dag@wieers.com> - 4.7.11-1
- Updated to release 4.7.11

* Sun Oct 21 2007 Dag Wieers <dag@wieers.com> - 4.7.8-1
- Updated to release 4.7.8.

* Sun Sep 30 2007 Dag Wieers <dag@wieers.com> - 4.7.7-1
- Initial package. (using DAR)
