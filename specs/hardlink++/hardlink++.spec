# $Id$

Summary: A rewrite in C++ of the hardlink utility
Name: hardlink++
Version: 0.02
Release: 1
License: GPL
Group: System Environment/Base
Source: http://www.sodarock.com/hardlink/hardlink++-%{version}.tgz
Patch: hardlink++-0.02-stdio.patch
URL: http://www.sodarock.com/hardlink/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: libstdc++
BuildRequires: gcc-c++, libstdc++-devel

%description
A rewrite in C++ of the hardlink utility, which recursively parses directory
structures and creates hard links for identical files found.


%prep
%setup
%patch -p1 -b .stdio


%build
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 hardlink++ %{buildroot}%{_bindir}/hardlink++


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc COPYING README
%{_bindir}/hardlink++


%changelog
* Fri Jan  9 2004 Matthias Saou <http://freshrpms.net/> 0.02-1
- Initial RPM release.

