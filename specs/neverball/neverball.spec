# $Id$
# Authority: matthias

%{?dist: %{expand: %%define %dist 1}}
                                                                                
%{?fc1:%define _without_xorg 1}
%{?el3:%define _without_xorg 1}
%{?rh9:%define _without_xorg 1}
%{?rh8:%define _without_xorg 1}
%{?rh7:%define _without_xorg 1}
%{?el2:%define _without_xorg 1}
%{?rh6:%define _without_xorg 1}
%{?yd3:%define _without_xorg 1}

%define desktop_vendor freshrpms

Summary: Test of skill, part puzzle game and part action game
Name: neverball
Version: 1.3.6
Release: 1
License: GPL
Group: Amusements/Games
URL: http://icculus.org/neverball/
Source: http://icculus.org/neverball/neverball-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: perl, zlib-devel
BuildRequires: SDL-devel, SDL_image-devel, SDL_mixer-devel, SDL_ttf-devel
# Mesa libGLU is required for correct linking
%{?_without_xorg:BuildRequires: XFree86-devel, XFree86-Mesa-libGLU}
%{!?_without_xorg:BuildRequires: xorg-x11-devel, xorg-x11-Mesa-libGLU}
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}

%description
Tilt the floor to roll a ball through an obstacle course before time runs out.
Neverball is part puzzle game, part action game, and entirely a test of skill.

If the ball falls or time expires, a ball is lost. Collect 100 coins to save
your progress and earn an extra ball. Red coins are worth 5, blue are worth 10.


%prep
%setup


%build
# Change the location where the binary will look for the "data" directory
%{__perl} -pi.orig -e 's|./data|%{_datadir}/%{name}|g' share/config.h
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
# Install the binary and the "data" directory
%{__install} -D -m 0755 %{name} %{buildroot}%{_bindir}/%{name}
%{__mkdir_p} %{buildroot}%{_datadir}
%{__cp} -a data %{buildroot}%{_datadir}/%{name}

%{__cat} > %{name}.desktop << EOF
[Desktop Entry]
Name=Neverball
Comment=Test of skill, part puzzle game and part action game
Exec=%{name}
Icon=%{_datadir}/%{name}/shot-rlk/risers.jpg
Terminal=false
Type=Application
Encoding=UTF-8
Categories=Application;Game;
EOF

%if %{!?_without_freedesktop:1}%{?_without_freedesktop:0}
%{__mkdir_p} %{buildroot}%{_datadir}/applications
desktop-file-install --vendor %{desktop_vendor} \
    --dir %{buildroot}%{_datadir}/applications \
    %{name}.desktop
%else
%{__install} -D -m 644 %{name}.desktop \
  %{buildroot}/etc/X11/applnk/Games/%{name}.desktop
%endif


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc CHANGES COPYING README
%{_bindir}/%{name}
%{_datadir}/%{name}
%{!?_without_freedesktop:%{_datadir}/applications/%{desktop_vendor}-%{name}.desktop}
%{?_without_freedesktop:/etc/X11/applnk/Games/%{name}.desktop}


%changelog
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

