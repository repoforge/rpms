# $Id$
# Authority: matthias

%define pear_dir %{_datadir}/pear

Summary: PEAR package for reading and writing OLE containers
Name: php-pear-ole
Version: 0.5
Release: 2%{?dist}
License: PHP
Group: Development/Languages
URL: http://pear.php.net/package/OLE/
Source0: http://pear.php.net/get/OLE-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch
Requires: php
BuildRequires: php

%description
This package allows reading and writing of OLE (Object Linking and Embedding)
files, the format used as container for Excel, Word and other MS file formats.
Documentation for the OLE format can be found at:
http://user.cs.tu-berlin.de/~schwartz/pmh/guide.html


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
* Fri Mar 17 2006 Matthias Saou <http://freshrpms.net/> 0.5-4
- Release bump to drop the disttag number in FC5 build.

* Fri Apr 15 2005 Matthias Saou <http://freshrpms.net/> 0.5-3
- Change single source from 1 to 0.
- Use %%{_datadir}/pear instead of the eval method, as it's triggering a
  nasty side-effect that prevents building.

* Fri May 21 2004 Matthias Saou <http://freshrpms.net/> 0.5-2
- Rebuilt for Fedora Core 2.

* Thu Mar 11 2004 Matthias Saou <http://freshrpms.net/> 0.5-1
- Initial RPM release.

