# $Id$

# Authority: dries

Summary: Explore mathematical concepts with interactive geometry.
Name: kig
Version: 0.6.0
Release: 4
License: GPL
Group: Applications/Math
URL: http://edu.kde.org/kig

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: ftp://ftp.kde.org/pub/kde/stable/apps/KDE3.x/math/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/root-%{name}-%{version}
BuildRequires:	libjpeg-devel, libpng-devel, arts-devel, kdelibs-devel gcc, make, gcc-c++, XFree86-devel, zlib-devel, qt-devel
Requires: kdelibs
#todo: needed for python scripting
#BuildRequires:	boost-python-devel

#(d) primscreenshot: http://edu.kde.org/kig/kig-snap-sine-curve.png
#(d) screenshotsurl: http://edu.kde.org/kig/screenshots.php

%description
Kig is an application meant to allow high school 
students to interactively explore mathematical
concepts, much like Dr.Geo, KGeo, KSeg and Cabri.

%description -l nl
Kig is een programma bedoeld om studenten op een 
interactieve manier kennis te laten maken met 
wiskundige concepten.

%prep
%{__rm} -rf "${RPM_BUILD_ROOT}"
%setup

%build
. /etc/profile.d/qt.sh
%configure --disable-kig-python-scripting
%{__make} %{?_smp_mflags}

%install
. /etc/profile.d/qt.sh
export DESTDIR=$RPM_BUILD_ROOT
make install-strip

%files
%defattr(-,root,root)
%doc README COPYING AUTHORS VERSION INSTALL
%{_bindir}/kig
/usr/lib/kde3/libkigpart*
/usr/share/applications/kde/kig.desktop
/usr/share/apps/kig/builtin-macros/*
/usr/share/apps/kig/*
/usr/share/apps/kigpart/kigpartui.rc
/usr/share/doc/HTML/en/kig/*
/usr/share/icons/*/*/apps/kig.png
/usr/share/mimelnk/application/*
/usr/share/services/kig_part.desktop

%changelog
* Sun Jan 11 2004 Dries Verachtert <dries@ulyssis.org> 0.6.0-4
- cleanup of spec file

* Thu Dec 11 2003 Dries Verachtert <dries@ulyssis.org> 0.6.0-3
- added some BuildRequires

* Sun Nov 30 2003 Dries Verachtert <dries@ulyssis.org> 0.6.0-2
- stripping of binaries added

* Sat Nov 29 2003 Dries Verachtert <dries@ulyssis.org> 0.6.0-1
- first packaging for Fedora Core 1, without python support
