# $Id$
# Authority: matthias

Summary: Rewrite in C++ of the hardlink utility
Name: hardlink++
Version: 0.02
Release: 3%{?dist}
License: GPL
Group: System Environment/Base
URL: http://www.sodarock.com/hardlink/

Source: http://www.sodarock.com/hardlink/hardlink++-%{version}.tgz
Patch0: hardlink++-0.02-stdio.patch
Patch1: hardlink++-0.02-sane-makefile.patch
Patch2: hardlink++-0.02-gcc34-optimize-help.patch
Patch3: hardlink++-0.02-cstdlib.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++

%description
A rewrite in C++ of the hardlink utility, which recursively parses directory
structures and creates hard links for identical files found.

%prep
%setup
%patch0 -p1 -b .stdio
%patch1 -p1 -b .sane-makefile
%patch2 -p1 -b .gcc34-optimize-help
%patch3 -b .cstdlib

%build
%{__make} %{?_smp_mflags} CXXFLAGS="%{optflags}"

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
* Fri Mar 17 2006 Matthias Saou <http://freshrpms.net/> 0.02-3
- Release bump to drop the disttag number in FC5 build.

* Mon Nov 14 2004 Matthias Saou <http://freshrpms.net/> 0.02-2
- Include sane-makefile and gcc43-optimize-help patches from Gentoo.
- Pass CXXFLAGS to the build.

* Fri Jan  9 2004 Matthias Saou <http://freshrpms.net/> 0.02-1
- Initial RPM release.

