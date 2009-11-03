# $Id$
# Authority: dries
# Screenshot: http://trackballs.sourceforge.net/pic1.jpg

%{?dtag: %{expand: %%define %dtag 1}}

%{?el4:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}
%{?el2:%define _without_modxorg 1}
%{?fc4:%define _without_modxorg 1}
%{?fc3:%define _without_modxorg 1}
%{?fc2:%define _without_modxorg 1}
%{?fc1:%define _without_modxorg 1}

Summary: Steer a marble ball through a labyrinth
Name: trackballs
Version: 1.1.4
Release: 1%{?dist}
License: GPL
Group: Amusements/Games
URL: http://trackballs.sourceforge.net/

Source: http://dl.sf.net/trackballs/trackballs-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, guile, guile-devel, SDL-devel, SDL_ttf-devel
BuildRequires: zlib-devel, SDL_mixer-devel, SDL_image-devel
%{!?_without_modxorg:BuildRequires: mesa-libGL-devel, mesa-libGLU-devel}
%{?_without_modxorg:BuildRequires: XFree86-devel}
#!?_without_xorg:BuildRequires: xorg-x11-devel, xorg-x11-Mesa-libGL, xorg-x11-Mesa-libGLU

%description
Trackballs is a game for linux in which you steer a marble ball through
tracks of varying difficulty. The game is loosely based on Marable Madness
and features 3D graphics, an integerated level editor and highquality
soundeffects and background music.

%prep
%setup
# the install script does a chgrp to 'games', this doesn't work while
# building as a user. Is group=games required?
sed -i "s/chgrp/#chgrp/g;" share/Makefile*
%configure
# {__perl} -pi -e 's|^mkinstalldirs.*|mkinstalldirs=\$\(MKINSTALLDIRS\)|g;' po/Makefile

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__strip} %{buildroot}/%{_bindir}/trackballs
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc %{_mandir}/man6/trackballs.6*
%{_bindir}/trackballs
%{_datadir}/trackballs
%{_datadir}/icons/hicolor/*/apps/trackballs.png
%{_datadir}/applications/trackballs.desktop

%changelog
* Mon May 28 2007 Dries Verachtert <dries@ulyssis.org> - 1.1.4-1
- Updated to release 1.1.4.

* Mon Aug 07 2006 Dries Verachtert <dries@ulyssis.org> 1.1.2-1
- Update to release 1.1.2.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.1.1-1.2
- Rebuild for Fedora Core 5.

* Thu Nov 17 2005 Dries Verachtert <dries@ulyssis.org> 1.1.1-1
- Update to release 1.1.1.

* Sat Mar 05 2005 Dries Verachtert <dries@ulyssis.org> 1.1.0-1
- Update to release 1.1.0.

* Thu Feb 26 2004 Dries Verachtert <dries@ulyssis.org> 1.0.0-1
- first packaging for Fedora Core 1
