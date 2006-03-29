# $Id$
# Authority: dries

# Screenshot: http://www.kmuddy.org/shots/kmuddy1.png
# ScreenshotURL: http://www.kmuddy.org/screenshots.php

# ExcludeDist: el3

%{?dist: %{expand: %%define %dist 1}}

%{?fc1:%define _without_xorg 1}
%{?el3:%define _without_xorg 1}
%{?rh9:%define _without_xorg 1}
%{?rh8:%define _without_xorg 1}
%{?rh7:%define _without_xorg 1}
%{?el2:%define _without_xorg 1}
%{?rh6:%define _without_xorg 1}

Summary: MUD (multi user dungeon) client
Name: kmuddy
Version: 0.7.1
Release: 1
License: GPL
Group: Amusements/Games
URL: http://www.kmuddy.org/

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Source: http://www.kmuddy.net/files/kmuddy-%{version}.tar.gz

BuildRequires: gettext, libart_lgpl-devel, libjpeg-devel, libpng-devel
BuildRequires: arts-devel, zlib-devel, kdelibs-devel, gcc, make
BuildRequires: gcc-c++, qt-devel >= 3.2
%{?el4:BuildRequires: libselinux-devel}
%{?fc3:BuildRequires: libselinux-devel}
%{?fc2:BuildRequires: libselinux-devel}
%{?_without_xorg:BuildRequires: XFree86-devel}
%{!?_without_xorg:BuildRequires: xorg-x11-devel}

%description
Kmuddy is a MUD client for KDE. A MUD is a multi user dungeon, a
text-based online multi-player role-playing game.

%prep
%setup

%{__perl} -pi.orig -e 's|/lib\b|/%{_lib}|g' configure

%build
. /etc/profile.d/qt.sh
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
. /etc/profile.d/qt.sh
%{__make} install DESTDIR=%{buildroot}
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS CHANGELOG README README.MIDI TODO
%doc %{_mandir}/man1/kmuddy*
%{_bindir}/kmuddy
%{_datadir}/applnk/Games/kmuddy.desktop
%{_datadir}/doc/HTML/en/kmuddy
%{_datadir}/icons/hicolor/16x16/actions/aliases.png
%{_datadir}/icons/*/*/apps/kmuddy.png
%{_datadir}/kmuddy

%changelog
* Thu Mar 31 2005 Dries Verachtert <dries@ulyssis.org> - 0.7.1-1
- Update to release 0.7.1.

* Sat Dec 04 2004 Dries Verachtert <dries@ulyssis.org> - 0.7-1
- Update to release 0.7.

* Mon May 24 2004 Dries Verachtert <dries@ulyssis.org> 0.6.1-1
- update to 0.6.1

* Fri Dec 13 2003 Dries Verachtert <dries@ulyssis.org> 0.6-1
- first packaging for Fedora Core 1
