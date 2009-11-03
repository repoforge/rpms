# $Id$
# Authority: matthias

%define pear_dir %{_datadir}/pear

Summary: PEAR package of a regression testing framework for unit tests
Name: php-pear-phpunit
Version: 1.3.1
Release: 1%{?dist}
License: PHP
Group: Development/Languages
URL: http://pear.php.net/package/PHPUnit
Source0: http://pear.php.net/get/PHPUnit-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch
Requires: php
BuildRequires: php < 5

%description
PHPUnit is a regression testing framework used by the developer who implements
unit tests in PHP.


%prep


%install
%{__rm} -rf %{buildroot}
pear install -R %{buildroot} -n %{SOURCE0}
# Remove .filemap and .lock, we don't want to include those
%{__rm} -f %{buildroot}%{pear_dir}/{.filemap,.lock}


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(0644, root, root, 0755)
%{pear_dir}/


%changelog
* Wed Sep 28 2005 Matthias Saou <http://freshrpms.net/> 1.3.1-1
- Initial RPM package.

