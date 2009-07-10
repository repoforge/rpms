# $Id$
# Authority: matthias

%{?dtag: %{expand: %%define %dtag 1}}

%{?el4:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}

Summary: Set of portable libraries especially useful for games
Name: plib
Version: 1.8.4
Release: 1
License: LGPL
Group: System Environment/Libraries
URL: http://plib.sourceforge.net/

Source: http://plib.sourceforge.net/dist/plib-%{version}.tar.gz
Patch0: plib-1.8.4-extraqualif.patch
Patch1: plib-1.8.4-fullscreen.patch
Patch2: plib-1.8.4-js.patch
Patch3: plib-1.8.4-autorepeat.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, freeglut-devel, libpng-devel
%{!?_without_modxorg:BuildRequires: libXext-devel, libXi-devel, libXmu-devel, libSM-devel, libXxf86vm-devel}
%{?_without_modxorg:BuildRequires: Mesa-devel}

%description
This is a set of OpenSource (LGPL) libraries that will permit programmers
to write games and other realtime interactive applications that are 100%
portable across a wide range of hardware and operating systems. Here is
what you need - it's all free and available with LGPL'ed source code on
the web. All of it works well together.

%package devel
Summary: Set of portable libraries especially useful for games
Group: Development/Libraries
Obsoletes: plib <= 1.6.0

%description devel
This is a set of OpenSource (LGPL) libraries that will permit programmers
to write games and other realtime interactive applications that are 100%
portable across a wide range of hardware and operating systems. Here is
what you need - it's all free and available with LGPL'ed source code on
the web. All of it works well together.

%prep
%setup
%patch0 -p1 -b .extraqualif
%patch1 -p1 -b .fs
%patch2 -p1 -b .js
%patch3 -p1 -b .autorepeat

%build
%configure CXXFLAGS="%{optflags} -fPIC"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}

%clean
%{__rm} -rf %{buildroot}

%files devel
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING ChangeLog NOTICE README
%{_includedir}/plib/
%{_libdir}/libplib*.a

%changelog
* Wed Jun 06 2007 Dag Wieers <dag@wieers.com> - 1.8.4-2
- Added Fedora patches.

* Wed Apr  6 2005 Matthias Saou <http://freshrpms.net/> 1.8.4-1
- Update to 1.8.4.

* Wed Feb  9 2005 Matthias Saou <http://freshrpms.net/> 1.8.3-4
- Force -fPIC to be added to CXXFLAGS to fix linking against the lib on x86_64.

* Thu Jul 15 2004 Matthias Saou <http://freshrpms.net/> 1.8.3-3
- Only build a devel package now as all files are headers and static libs.

* Wed May 19 2004 Matthias Saou <http://freshrpms.net/> 1.8.3-2
- Rebuild for Fedora Core 2.

* Thu Apr 15 2004 Matthias Saou <http://freshrpms.net/> 1.8.3-1
- Update to 1.8.3.

* Tue Nov 11 2003 Matthias Saou <http://freshrpms.net/> 1.6.0-3
- Rebuild for Fedora Core 1.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.

* Wed Dec  4 2002 Matthias Saou <http://freshrpms.net/>
- Update to 1.6.0.

* Wed Jun 20 2001 Matthias Saou <http://freshrpms.net/>
- Initial RPM release.

