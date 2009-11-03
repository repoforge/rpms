# $Id$
# Authority: matthias


%{?fc4:%define _without_modxorg 1}
%{?el4:%define _without_modxorg 1}
%{?fc3:%define _without_modxorg 1}
%{?fc2:%define _without_modxorg 1}
%{?fc1:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}
%{?rh9:%define _without_modxorg 1}
%{?rh7:%define _without_modxorg 1}
%{?el2:%define _without_modxorg 1}
%{?rh6:%define _without_modxorg 1}
%{?yd3:%define _without_modxorg 1}

%{?fc1:%define _without_xorg 1}
%{?el3:%define _without_xorg 1}
%{?rh9:%define _without_xorg 1}
%{?rh8:%define _without_xorg 1}
%{?rh7:%define _without_xorg 1}
%{?el2:%define _without_xorg 1}
%{?rh6:%define _without_xorg 1}
%{?yd3:%define _without_xorg 1}

%define desktop_vendor rpmforge

Summary: Test of skill, part puzzle game and part action game
Name: neverball
Version: 1.4.0
Release: 1%{?dist}
License: GPL
Group: Amusements/Games
URL: http://icculus.org/neverball/
Source: http://icculus.org/neverball/neverball-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: perl, zlib-devel
BuildRequires: SDL-devel, SDL_image-devel, SDL_mixer-devel, SDL_ttf-devel
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}
# Mesa libGLU is required for correct linking
%if 0%{?_without_modxorg:1}
%{?_without_xorg:BuildRequires: XFree86-devel, XFree86-Mesa-libGLU}
%{!?_without_xorg:BuildRequires: xorg-x11-devel, xorg-x11-Mesa-libGLU}
%else
BuildRequires: libXt-devel, mesa-libGLU-devel
%endif

%description
Tilt the floor to roll a ball through an obstacle course before time runs out.
Neverball is part puzzle game, part action game, and entirely a test of skill.

Also included is Neverputt, a hot-seat multiplayer miniature golf game using
the physics and graphics of Neverball.


%prep
%setup


%build
# Change the location where the binary will look for the "data" directory
%{__perl} -pi.orig -e 's|./data|%{_prefix}/games/neverball/data|g' \
    share/config.h
# Override relevant part of the CFLAGS
%{__make} %{?_smp_mflags} \
    CFLAGS='-Wall %{optflags} -ansi $(shell sdl-config --cflags)'


%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}%{_prefix}/games/neverball
%{__mkdir_p} %{buildroot}%{_datadir}/pixmaps
# Install the binaries and the "data" directory
%{__install} -p -m0755 neverball neverputt mapc \
    %{buildroot}%{_prefix}/games/neverball/
%{__cp} -ap data %{buildroot}%{_prefix}/games/neverball/data
# Install the icons for the desktop files
%{__install} -p -m0644 icon/*.png %{buildroot}%{_datadir}/pixmaps/

# Install the desktop files
%{__cat} > neverball.desktop << EOF
[Desktop Entry]
Name=Neverball
Comment=Test of skill, part puzzle game and part action game
Exec=%{_prefix}/games/neverball/neverball
Icon=neverball.png
Terminal=false
Type=Application
Encoding=UTF-8
Categories=Application;Game;
EOF
%{__cat} > neverputt.desktop << EOF
[Desktop Entry]
Name=Neverputt
Comment=Multiplayer miniature golf game
Exec=%{_prefix}/games/neverball/neverputt
Icon=neverputt.png
Terminal=false
Type=Application
Encoding=UTF-8
Categories=Application;Game;
EOF

%if %{!?_without_freedesktop:1}%{?_without_freedesktop:0}
%{__mkdir_p} %{buildroot}%{_datadir}/applications
desktop-file-install \
    --vendor %{desktop_vendor} \
    --dir %{buildroot}%{_datadir}/applications \
    neverball.desktop
desktop-file-install \
    --vendor %{desktop_vendor} \
    --dir %{buildroot}%{_datadir}/applications \
    neverputt.desktop
%else
%{__install} -Dp -m 644 neverball.desktop \
    %{buildroot}/etc/X11/applnk/Games/neverball.desktop
%{__install} -Dp -m 644 neverputt.desktop \
    %{buildroot}/etc/X11/applnk/Games/neverputt.desktop
%endif


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc CHANGES COPYING README
%{_prefix}/games/neverball/
%{_datadir}/pixmaps/neverball.png
%{_datadir}/pixmaps/neverputt.png
%{!?_without_freedesktop:%{_datadir}/applications/%{desktop_vendor}-neverball.desktop}
%{!?_without_freedesktop:%{_datadir}/applications/%{desktop_vendor}-neverputt.desktop}
%{?_without_freedesktop:/etc/X11/applnk/Games/neverball.desktop}
%{?_without_freedesktop:/etc/X11/applnk/Games/neverputt.desktop}


%changelog
* Wed Nov  3 2004 Matthias Saou <http://freshrpms.net/> 1.4.0-1
- Update to 1.4.0.

* Wed Aug 11 2004 Matthias Saou <http://freshrpms.net/> 1.3.7-1
- Update to 1.3.7.

* Mon Aug  2 2004 Matthias Saou <http://freshrpms.net/> 1.3.6-2
- Add neverputt and mapc to the package, as suggested by Andrew Pam.
- Use the icons now provided in the source for the desktop entries.
- Move everything in %{_prefix}/games/neverball.

* Tue Jul 27 2004 Matthias Saou <http://freshrpms.net/> 1.3.6-1
- Update to 1.3.6.

* Thu Jul 22 2004 Matthias Saou <http://freshrpms.net/> 1.3.5-1
- Update to 1.3.5.

* Thu Jul 15 2004 Matthias Saou <http://freshrpms.net/> 1.3.4-1
- Update to 1.3.4.
- Added proper XFree/x.org and desktop-file-utils build switches.

* Mon Jul  5 2004 Matthias Saou <http://freshrpms.net/> 1.3.1-1
- Update to 1.3.1.

* Wed May 19 2004 Matthias Saou <http://freshrpms.net/> 1.2.5-1
- Update to 1.2.5.
- Rebuild for Fedora Core 2.
- Change build requirement to new xorg-x11-Mesa-libGLU.

* Wed Feb  4 2004 Matthias Saou <http://freshrpms.net/> 1.1.0-1
- Initial RPM release.

