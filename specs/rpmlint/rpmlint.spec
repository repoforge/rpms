# $Id$
# Authority: matthias

Summary: RPM correctness checker
Name: rpmlint
Version: 0.61
Release: 0%{?dist}
License: GPL
Group: Development/Tools
URL: http://people.mandrakesoft.com/~flepied/projects/rpmlint/
Source: http://people.mandrakesoft.com/~flepied/projects/rpmlint/dist/rpmlint-%{version}.tar.bz2
Source1: config.fedora
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: python >= 1.5.2, rpm-python
BuildRequires: python >= 1.5.2, rpm-python
BuildArch: noarch

%description
Rpmlint is a tool to check common errors on rpm packages.
Binary and source packages can be checked.

%prep
%setup
%{__cp} -p %{SOURCE1} config

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
%dir %{_sysconfdir}/rpmlint/
%config(noreplace) %{_sysconfdir}/rpmlint/config
%{_bindir}/*
%{_datadir}/rpmlint/

%changelog
* Wed Sep  1 2004 Matthias Saou <http://freshrpms.net/> 0.61-0
- Update to 0.61.
- Include an updated default configuration suitable for Red Hat Linux and
  Fedora Core made from scratch today.

* Mon Sep 15 2003 Dag Wieers <dag@wieers.com> - 0.51-0
- Updated to release 0.51.

* Sun Feb 09 2003 Dag Wieers <dag@wieers.com> - 0.46-0
- Initial package. (using DAR)

