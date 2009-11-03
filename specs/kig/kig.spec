# $Id$
# Authority: dries
# Screenshot: http://edu.kde.org/kig/kig-snap-sine-curve.png
# ScreenshotURL: http://edu.kde.org/kig/screenshots.php

# Tag: test
# this program is now included in kde
# ExcludeDist: fc3 fc2 fc1 el3

%{?dtag: %{expand: %%define %dtag 1}}

Summary: Explore mathematical concepts with interactive geometry
Name: kig
Version: 0.9
Release: 2%{?dist}
License: GPL
Group: Applications/Engineering
URL: http://edu.kde.org/kig

Source: ftp://ftp.kde.org/pub/kde/stable/apps/KDE3.x/math/kig-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gettext, libart_lgpl-devel, libjpeg-devel, libpng-devel
BuildRequires: arts-devel, kdelibs-devel gcc, make, gcc-c++
BuildRequires: zlib-devel, qt-devel
Requires: kdelibs
#todo: needed for python scripting
#BuildRequires:	boost-python-devel

%description
Kig is an application meant to allow high school
students to interactively explore mathematical
concepts, much like Dr.Geo, KGeo, KSeg and Cabri.

%description -l nl
Kig is een programma bedoeld om studenten op een
interactieve manier kennis te laten maken met
wiskundige concepten.

%prep
%setup

%build
. /etc/profile.d/qt.sh
%configure --disable-kig-python-scripting
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
. /etc/profile.d/qt.sh
%{__make} install DESTDIR=%{buildroot}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING INSTALL README VERSION
%{_bindir}/kig
%{_libdir}/kde3/libkigpart*
%{_datadir}/applications/kde/kig.desktop
%{_datadir}/apps/kig/builtin-macros/*
%{_datadir}/apps/kig/*
%{_datadir}/apps/kigpart/kigpartui.rc
%{_datadir}/doc/HTML/en/kig/*
%{_datadir}/icons/*/*/apps/kig.png
%{_datadir}/mimelnk/application/*
%{_datadir}/services/kig_part.desktop

%changelog
* Thu Mar 30 2006 Dries Verachtert <dries@ulyssis.org> - 0.9-2
- Simplify buildequirements: kdelibs-devel already requires xorg-x11-devel/XFree86-devel

* Fri Oct 29 2004 Dries Verachtert <dries@ulyssis.org> 0.9-1
- Update to release 0.9.

* Sun Jan 11 2004 Dries Verachtert <dries@ulyssis.org> 0.6.0-4
- cleanup of spec file

* Thu Dec 11 2003 Dries Verachtert <dries@ulyssis.org> 0.6.0-3
- added some BuildRequires

* Sun Nov 30 2003 Dries Verachtert <dries@ulyssis.org> 0.6.0-2
- stripping of binaries added

* Sat Nov 29 2003 Dries Verachtert <dries@ulyssis.org> 0.6.0-1
- first packaging for Fedora Core 1, without python support

