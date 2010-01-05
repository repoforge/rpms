# $Id$
# Authority: matthias

Summary: RPM correctness checker
Name: rpmlint
Version: 0.92
Release: 1%{?dist}
License: GPL
Group: Development/Tools
URL: http://rpmlint.zarb.org/

Source: http://rpmlint.zarb.org/download/rpmlint-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python >= 2.4
BuildRequires: rpm-python
Requires: python >= 2.4
Requires: rpm-python

%description
Rpmlint is a tool to check common errors on rpm packages.
Binary and source packages can be checked.

%prep
%setup

%build
%{__make} %{?_smp_mflags} COMPILE_PYC=1

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING README*
%doc %{_mandir}/man1/rpmlint.1*
%dir %{_sysconfdir}/rpmlint/
%config(noreplace) %{_sysconfdir}/bash_completion.d/rpmlint
%config(noreplace) %{_sysconfdir}/rpmlint/config
%{_bindir}/*
%{_datadir}/rpmlint/

%changelog
* Mon Jan 04 2010 Bjarne Saltbaek <arnebjarne72@hotmail.com> - 0.92-1
- Updated to release 0.92.
- Added COMPILE_PYC=1 for *.pyc compilation.
- Python >= 2.4 now required.

* Wed Sep  1 2004 Matthias Saou <http://freshrpms.net/> 0.61-0
- Update to 0.61.
- Include an updated default configuration suitable for Red Hat Linux and
  Fedora Core made from scratch today.

* Mon Sep 15 2003 Dag Wieers <dag@wieers.com> - 0.51-0
- Updated to release 0.51.

* Sun Feb 09 2003 Dag Wieers <dag@wieers.com> - 0.46-0
- Initial package. (using DAR)

