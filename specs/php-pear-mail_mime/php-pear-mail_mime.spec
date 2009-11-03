# $Id$
# Authority: matthias

%define pear_dir %{_datadir}/pear

Summary: PEAR package for manipulating mime messages
Name: php-pear-mail_mime
Version: 1.3.1
Release: 1%{?dist}
License: PHP
Group: Development/Languages
URL: http://pear.php.net/package/Mail_Mime/
Source0: http://pear.php.net/get/Mail_Mime-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch
Requires: php
BuildRequires: php

%description
This package provides classes to deal with creation and manipulation of mime
messages, typically emails.


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
* Fri Nov 25 2005 Matthias Saou <http://freshrpms.net/> 1.3.1-1
- Initial RPM release.

