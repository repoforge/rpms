# $Id$
# Authority: matthias

%define pear_dir %{_datadir}/pear

Summary: PEAR package for logging
Name: php-pear-log
Version: 1.9.3
Release: 1%{?dist}
License: PHP
Group: Development/Languages
URL: http://pear.php.net/package/Log/
Source0: http://pear.php.net/get/Log-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch
Requires: php
BuildRequires: php

%description
The Log framework provides an abstracted logging system. It supports logging
to console, file, syslog, SQL, Sqlite, mail, and mcal targets. It also
provides a subject - observer mechanism.


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
* Tue Feb 21 2006 Matthias Saou <http://freshrpms.net/> 1.9.3-1
- Initial RPM release.

