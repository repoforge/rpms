# $Id$

# Authority: dries

Summary: KDE screensaver showing the adventures of Tux, living at the SouthPole
Name: tuxsaver
Version: 1.0
Release: 1
License: GPL
Group: Amusements/Graphics
URL: http://www.esat.kuleuven.ac.be/~kmuylken/tuxsaver/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://www.esat.kuleuven.ac.be/~kmuylken/tuxsaver/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{_name}-%{_version}
BuildRequires: gettext, libart_lgpl-devel, libjpeg-devel, libpng-devel, arts-devel, zlib-devel, kdelibs-devel, gcc, make, gcc-c++, XFree86-devel, qt-devel
Requires: kdelibs

#(d) primscreenshot: http://www.esat.kuleuven.ac.be/~kmuylken/tuxsaver/screenshot1.jpg 
#(d) screenshotsurl: http://www.esat.kuleuven.ac.be/~kmuylken/tuxsaver/

%description
A screensaver for KDE which shows the adventures of Tux, living at the
SouthPole.

%prep
%{__rm} -rf "${RPM_BUILD_ROOT}"
%setup

%build
. /etc/profile.d/qt.sh
%configure
%{__make} %{?_smp_mflags}

%install
. /etc/profile.d/qt.sh
export DESTDIR=$RPM_BUILD_ROOT
%{__make} install-strip
mkdir -p ${DESTDIR}/usr/share/apps/kscreensaver/ScreenSavers/
mv ${DESTDIR}/usr/share/applnk/System/ScreenSavers/tuxsaver.desktop ${DESTDIR}/usr/share/apps/kscreensaver/ScreenSavers/

%files
%defattr(-,root,root, 0755)
%{_bindir}/tuxsaver.kss
/usr/share/apps/kscreensaver/ScreenSavers/tuxsaver.desktop
/usr/share/apps/tuxsaver/objects
/usr/share/apps/tuxsaver/pics
/usr/share/apps/tuxsaver/sounds
/usr/share/apps/tuxsaver/stories
/usr/share/doc/HTML/en/tuxsaver
/usr/share/locale/*/LC_MESSAGES/tuxsaver.mo

%changelog
* Sat Jan 10 2004 Dries Verachtert <dries@ulyssis.org> 1.0-1
- first packaging for Fedora Core 1
