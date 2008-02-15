# $Id$

# Authority: dries
# Upstream: koen muylkens <koen,muylkens$esat,kuleuven,ac,be>
# Screenshot: http://www.esat.kuleuven.ac.be/~kmuylken/tuxsaver/screenshot1.jpg
# ScreenshotURL: http://www.esat.kuleuven.ac.be/~kmuylken/tuxsaver/

%{?dtag: %{expand: %%define %dtag 1}}

Summary: KDE screensaver showing the adventures of Tux, living at the SouthPole
Name: tuxsaver
Version: 1.0
Release: 4
License: GPL
Group: Amusements/Graphics
URL: http://www.esat.kuleuven.ac.be/~kmuylken/tuxsaver/

#Source: http://www.esat.kuleuven.ac.be/~kmuylken/tuxsaver/%{name}-%{version}.tar.gz
Source: http://users.telenet.be/muylkens/tuxsaver-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gettext, libart_lgpl-devel, libjpeg-devel, libpng-devel
BuildRequires: arts-devel, zlib-devel, kdelibs-devel, gcc, make
BuildRequires: gcc-c++, qt-devel
%{?fc3:BuildRequires: libselinux-devel}
%{?fc2:BuildRequires: libselinux-devel}

%description
A screensaver for KDE which shows the adventures of Tux, living at the
SouthPole.

%prep
%setup

%build
. /etc/profile.d/qt.sh
%configure LDFLAGS="$LDFLAGS -L/usr/X11R6/%{_lib}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
. /etc/profile.d/qt.sh
%makeinstall
%find_lang %{name}
%{__mkdir_p} %{buildroot}/usr/share/apps/kscreensaver/ScreenSavers/
%{__cp} -p %{buildroot}/usr/share/applnk/System/ScreenSavers/tuxsaver.desktop %{buildroot}/usr/share/apps/kscreensaver/ScreenSavers/

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%{_bindir}/tuxsaver.kss
%{_datadir}/apps/kscreensaver/ScreenSavers/tuxsaver.desktop
%{_datadir}/applnk/System/ScreenSavers/tuxsaver.desktop
%{_datadir}/apps/tuxsaver/objects
%{_datadir}/apps/tuxsaver/pics
%{_datadir}/apps/tuxsaver/sounds
%{_datadir}/apps/tuxsaver/stories
%{_datadir}/doc/HTML/en/tuxsaver

%changelog
* Thu Mar 30 2006 Dries Verachtert <dries@ulyssis.org> - 1.0-4
- Simplify buildequirements: kdelibs-devel already requires xorg-x11-devel/XFree86-devel

* Fri Oct 29 2004 Dries Verachtert <dries@ulyssis.org> 1.0-3
- Fix: screensaver desktop file now in two directories.

* Wed Apr 14 2004 Dries Verachtert <dries@ulyssis.org> 1.0-2
- spec file cleanup

* Sat Jan 10 2004 Dries Verachtert <dries@ulyssis.org> 1.0-1
- first packaging for Fedora Core 1
