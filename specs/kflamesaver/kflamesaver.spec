# $Id$
# Authority: dries
# Screenshot: http://kde-apps.org/content/pics/4485-1.png

%{?dist: %{expand: %%define %dist 1}}

%{?fc1:%define _without_xorg 1}
%{?el3:%define _without_xorg 1}
%{?rh9:%define _without_xorg 1}
%{?rh8:%define _without_xorg 1}
%{?rh7:%define _without_xorg 1}
%{?el2:%define _without_xorg 1}
%{?rh6:%define _without_xorg 1}

Summary: Screensaver with flames
Name: kflamesaver
Version: 0.1
Release: 1
License: GPL
Group: Amusements/Graphics
URL: http://kde-apps.org/content/show.php?content=4485

Source: %{name}-%{version}.tar.gz
Patch: gcc34-fixes.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gettext, libart_lgpl-devel, libjpeg-devel
BuildRequires: libpng-devel, arts-devel, zlib-devel, kdelibs-devel
BuildRequires: gcc, make, gcc-c++, qt-devel
%{?el4:BuildRequires:libselinux-devel}
%{?fc3:BuildRequires:libselinux-devel}
%{?fc2:BuildRequires:libselinux-devel}
%{?_without_xorg:BuildRequires: XFree86-devel}
%{!?_without_xorg:BuildRequires: xorg-x11-devel}

%description
A screensaver for KDE with flame effects like in Twin Peaks.

%prep
%setup
%patch -p1

%build
. /etc/profile.d/qt.sh
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
. /etc/profile.d/qt.sh
%{__make} install DESTDIR=%{buildroot}
%{__mkdir_p} %{buildroot}/usr/share/apps/kscreensaver/ScreenSavers/
%{__mv} %{buildroot}/usr/share/applnk/System/ScreenSavers/kflamesaver.desktop %{buildroot}/usr/share/apps/kscreensaver/ScreenSavers/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_bindir}/kflamesaver.kss
%{_datadir}/apps/kscreensaver/ScreenSavers/kflamesaver.desktop
%{_datadir}/apps/kflamesaver/laura_and_coop.png

%changelog
* Sat Jan 10 2004 Dries Verachtert <dries@ulyssis.org> 0.1-1
- first packaging for Fedora Core 1

