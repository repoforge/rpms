# $Id$
# Authority: dag
# Upstream: Nils Philippsen <nphilipp$redhat,com>

Summary: Display expanded Source/Patch macros from SPEC files
Name: spectool
Version: 1.0.11
Release: 1%{?dist}
License: GPL
Group: System Environment/Base
URL: http://people.redhat.com/nphilipp/spectool/

Source: http://people.redhat.com/nphilipp/spectool/spectool-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
Requires: perl, rpm-build

%description
spectool is a tool to display expanded Source/Patch macros from a SPEC file.

%prep
%setup

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 spectool %{buildroot}%{_bindir}/spectool

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING README
%{_bindir}/spectool

%changelog
* Tue Oct 14 2008 Dag Wieers <dag@wieers.com> - 1.0.11-1
- Updated to release 1.0.11.

* Fri Dec 14 2007 Dag Wieers <dag@wieers.com> - 1.0.9-1
- Updated to release 1.0.9.

* Thu Mar 16 2006 Dag Wieers <dag@wieers.com> - 1.0.7-1
- Updated to release 1.0.7.

* Wed Mar 16 2004 Dag Wieers <dag@wieers.com> - 1.0.3-1
- Updated to release 1.0.3.

* Fri Mar 12 2004 Dag Wieers <dag@wieers.com> - 1.0.2-2
- Changed BuildArch to noarch. (Bert de Bruijn)
- Added fix to make spectool work better. (Bert de Bruijn)

* Thu Mar 11 2004 Dag Wieers <dag@wieers.com> - 1.0.2-1
- Updated to release 1.0.2.

* Sun Mar 07 2004 Dag Wieers <dag@wieers.com> - 1.0.1-1
- Updated to release 1.0.1.

* Wed Mar 03 2004 Dag Wieers <dag@wieers.com> - 1.0-1
- Initial package. (using DAR)
