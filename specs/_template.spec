# $Id$
# Authority: dag
# Upstream: Dag Wieers <dag@wieers.com>

Summary: Tool to set up a Yum/Apt mirror from various sources (ISO, ftp, ...)
Name: yam
Version: 0.2
Release: 1
License: GPL
Group: System Environment/Base
URL: http://dag.wieers.com/home-made/yam/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dag.wieers.com/home-made/yam/yam-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Requires: python

%description
yam builds a local Apt/Yum RPM repository from local ISO files,
downloaded updates and extra packages from 3rd party repositories.

%prep
%setup

%build

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING README THANKS TODO
%doc %{_mandir}/man?/*
%{_bindir}/*
/mnt/iso
%{_localstatedir}/www/yam

%changelog
* Fri May 14 2004 Dag Wieers <dag@wieers.com> - 0.2-1
- Initial package. (using DAR)
