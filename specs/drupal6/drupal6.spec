# $Id$
# Authority: dag

%define real_name drupal

Summary: Drupal CMS
Name: drupal6
Version: 6.2
Release: 1
License: GPL
Group: Development/Languages
URL: http://drupal.org/

Source: http://ftp.drupal.org/files/projects/drupal-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: php >= 4.3.5
Requires: httpd, mysql, php >= 4.3.5
Requires: php-gd, php-mbstring, php-mysql

Obsoletes: drupal <= %{version}-%{release}
Provides: drupal = %{version}-%{release}

%description
Drupal is an open source content management platform. Drupal is equipped
with a powerful blend of features, Drupal can support a variety of
websites ranging from personal weblogs to large community-driven websites.

%prep
%setup -n %{real_name}-%{version}
%{__cat} <<EOF >drupal6.httpd
### Drupal 6
Alias /drupal %{_localstatedir}/www/drupal-%{version}

<Directory %{_localstatedir}/www/drupal-%{version}>
    AllowOverride All
</Directory>
EOF

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0644 drupal6.httpd %{buildroot}%{_sysconfdir}/httpd/conf.d/drupal6.conf
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
%config(noreplace) %{_sysconfdir}/httpd/conf.d/drupal6.conf
%{_localstatedir}/www/drupal-%{version}/

%changelog
* Fri Jun 13 2008 Dag Wieers <dag@wieers.com> - 6.2-1
- Updated to release 6.2.

* Thu Feb 28 2008 Dag Wieers <dag@wieers.com> - 6.1-1
- Updated to release 6.1.

* Fri Feb 15 2008 Dag Wieers <dag@wieers.com> - 6.0-1
- Initial package. (using DAR)
