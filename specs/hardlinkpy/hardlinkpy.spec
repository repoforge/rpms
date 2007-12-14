# $Id$
# Authority: dag

Summary: Rewrite in python of the hardlink utility
Name: hardlinkpy
Version: 0.0.20071114
Release: 1
License: GPL
Group: System Environment/Base
URL: http://hardlinkpy.googlecode.com/

Source0: http://hardlinkpy.googlecode.com/svn/trunk/hardlink.py
Source1: http://hardlinkpy.googlecode.com/svn/trunk/COPYING
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python >= 2.2.3
Requires: python >= 2.2.3

Obsoletes: hardlink++
Provides: hardlink++

%description
A rewrite in python of the hardlink utility, which recursively parses directory
structures and creates hard links for identical files found.

%prep
%setup -cT

%{__cp} -av %{SOURCE0} hardlink.py
%{__cp} -av %{SOURCE1} COPYING

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 hardlink.py %{buildroot}%{_bindir}/hardlinkpy

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING
%{_bindir}/hardlinkpy

%changelog
* Mon Dec 10 2007 Dag Wieers <dag@wieers.com> - 0.0.20071114-1
- Obsoletes hardlink++.
- Initial package. (using DAR)
