# $Id$

# Authority: dries
# Upstream: koen muylkens <koen.muylkens@esat.kuleuven.ac.be>

Summary: KDE screensaver showing the adventures of Tux, living at the SouthPole
Name: tuxsaver
Version: 1.0
Release: 2
License: GPL
Group: Amusements/Graphics
URL: http://www.esat.kuleuven.ac.be/~kmuylken/tuxsaver/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://www.esat.kuleuven.ac.be/~kmuylken/tuxsaver/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
BuildRequires: gettext, libart_lgpl-devel, libjpeg-devel, libpng-devel, arts-devel, zlib-devel, kdelibs-devel, gcc, make, gcc-c++, XFree86-devel, qt-devel
%{?fc2:BuildRequires: libselinux-devel}
Requires: kdelibs

# Screenshot: http://www.esat.kuleuven.ac.be/~kmuylken/tuxsaver/screenshot1.jpg 
# ScreenshotURL: http://www.esat.kuleuven.ac.be/~kmuylken/tuxsaver/

%description
A screensaver for KDE which shows the adventures of Tux, living at the
SouthPole.

%prep
%setup

%build
. /etc/profile.d/qt.sh
%configure
%{__make} %{?_smp_mflags}

%install
. /etc/profile.d/qt.sh
%makeinstall
mkdir -p %{buildroot}/usr/share/apps/kscreensaver/ScreenSavers/
mv %{buildroot}/usr/share/applnk/System/ScreenSavers/tuxsaver.desktop %{buildroot}/usr/share/apps/kscreensaver/ScreenSavers/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root, 0755)
%{_bindir}/tuxsaver.kss
%{_datadir}/apps/kscreensaver/ScreenSavers/tuxsaver.desktop
%{_datadir}/apps/tuxsaver/objects
%{_datadir}/apps/tuxsaver/pics
%{_datadir}/apps/tuxsaver/sounds
%{_datadir}/apps/tuxsaver/stories
%{_datadir}/doc/HTML/en/tuxsaver
%{_datadir}/locale/*/LC_MESSAGES/tuxsaver.mo

%changelog
* Wed Apr 14 2004 Dries Verachtert <dries@ulyssis.org> 1.0-2
- spec file cleanup

* Sat Jan 10 2004 Dries Verachtert <dries@ulyssis.org> 1.0-1
- first packaging for Fedora Core 1
