# $Id$

# Authority: dag

Summary: RPM correctness checker.
Name: rpmlint
Version: 0.52
Release: 0
License: GPL
Group: Development/Tools
URL: http://people.mandrakesoft.com/~flepied/projects/rpmlint/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://people.mandrakesoft.com/~flepied/projects/rpmlint/dist/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildArch: noarch
BuildRequires: python >= 1.5.2, rpm-python
Requires: python >= 1.5.2, rpm-python
#Requires: rpm-python, python >= 1.5.2, rpm-devel >= 3.0.3-35mdk, binutils, file, findutils, cpio, /lib/cpp, grep, /bin/bash

%description
Rpmlint is a tool to check common errors on rpm packages.
Binary and source packages can be checked.

%prep
%setup

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING README*
%config(noreplace) %{_sysconfdir}/rpmlint/
%{_bindir}/*
%{_datadir}/rpmlint/

%changelog
* Mon Sep 15 2003 Dag Wieers <dag@wieers.com> - 0.51-0
- Updated to release 0.51.

* Sun Feb 09 2003 Dag Wieers <dag@wieers.com> - 0.46-0
- Initial package. (using DAR)
