# $Id$
# Authority: dries

Summary: sokoban game
Name: easysok
Version: 0.3.3
Release: 1
License: GPL
Group: Amusements/Games
URL: http://easysok.sourceforge.net/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://dl.sf.net/easysok/%{name}-%{version}.tar.bz2 
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Patch: assert-include.patch
BuildRequires: gettext, libart_lgpl-devel, libjpeg-devel, libpng-devel, arts-devel, zlib-devel, kdelibs-devel, gcc, make, gcc-c++, XFree86-devel, qt-devel
%{?fc2:BuildRequires: libselinux-devel}
Requires: kdelibs

# Screenshot: http://easysok.sourceforge.net/snapshot1.png
# ScreenshotURL: http://easysok.sourceforge.net/screenshots.html

%description
Easysok is a sokoban game for KDE3. In sokoban you are a warehouse keeper
which has to push gems on their goals. The problem is, that the keeper can
only push one gem and there are walls which stand in his way. Sokoban was
originally invented in 1982 by Hiroyuki Imabayashi at the Japanese company
Thinking Rabbit, Inc.

%description -l nl
Easysok is een sokoban spel voor KDE3. In sokoban bent u een winkelier die
stenen moet duwen naar bepaalde plaatsen. U kan slechts 1 steen
tegelijkertijd bewegen en er zijn muren die in de weg staan. Sokoban is
uitgevonden door in 1982 door Hiroyuki Imabayashi in het Japans bedrijf
Thinking Rabbit, Inc.

%prep
%{__rm} -rf %{buildroot}
%setup
%patch -p 1

%build
. /etc/profile.d/qt.sh
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
. /etc/profile.d/qt.sh
%{__make} install DESTDIR=%{buildroot}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README AUTHORS THANKS TODO VERSION
%{_bindir}/easysok
%{_libdir}/easysok.*
%{_datadir}/applnk/Games/TacticStrategy/easysok.desktop
%{_datadir}/apps/easysok
%{_datadir}/doc/HTML/en/easysok
%{_datadir}/icons/*/*/apps/easysok.png
%{_datadir}/locale/de/LC_MESSAGES/easysok.mo
%{_datadir}/wallpapers/GreenBallThemeBackground.jpg
%{_datadir}/wallpapers/KSokobanThemeBackground.jpg
%{_datadir}/wallpapers/SpaceThemeBackground.png
%{_datadir}/wallpapers/WarehouseKeeperThemeBackground.jpg


%changelog
* Sun Jan 11 2004 Dries Verachtert <dries@ulyssis.org> 0.3.3-1
- cleanup of spec file
- update to 0.3.3

* Sun Dec 13 2003 Dries Verachtert <dries@ulyssis.org> 0.3.2-2
- completion of the spec file

* Sun Dec 7 2003 Dries Verachtert <dries@ulyssis.org> 0.3.2-1
- first packaging for Fedora Core 1
