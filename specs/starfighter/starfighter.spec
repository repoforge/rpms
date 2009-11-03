# $Id$
# Authority: matthias

%define desktop_vendor rpmforge


%{?el2:%define _without_freedesktop 1}
%{?rh7:%define _without_freedesktop 1}

Summary: Project: Starfighter, a space arcade game
Name: starfighter
Version: 1.1
Release: 1%{?dist}
License: GPL
Group: Amusements/Games
URL: http://www.parallelrealities.co.uk/starfighter.php
Source0: starfighter-%{version}-1.tar.gz
Source1: starfighter.png
Patch: starfighter-1.1-makefile.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: SDL-devel, SDL_mixer-devel, SDL_image-devel, gcc-c++
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}

%description
After decades of war one company, who had gained powerful supplying both sides
with weaponary, steps forwards and crushes both warring factions in one swift
movement. Using far superior weaponary and AI craft, the company was completely
unstoppable and now no one can stand in their way. Thousands began to perish
under the iron fist of the company. The people cried out for a saviour, for
someone to light this dark hour... and someone did.

This game features 26 missions over 4 star systems and boss battles.

Available rpmbuild rebuild options :
--without : freedesktop


%prep
%setup
%patch0 -p1 -b .makefile


%build
%{__make} %{?_smp_mflags} \
	PREFIX="%{_prefix}" \
	OPTFLAGS="%{optflags}"


%install
%{__rm} -rf %{buildroot}
%{__make} install PREFIX="%{_prefix}" DESTDIR="%{buildroot}"

# Install menu icon
%{__install} -Dp -m 0644 %{SOURCE1} \
    %{buildroot}%{_datadir}/pixmaps/starfighter.png

# Install menu entry
%{__cat} > %{name}.desktop << EOF
[Desktop Entry]
Name=Project: Starfighter
Comment=Space Arcade Game
Icon=starfighter.png
Exec=%{_prefix}/games/starfighter
Terminal=false
Type=Application
Categories=Application;Game;ArcadeGame;
Encoding=UTF-8
EOF

%if %{!?_without_freedesktop:1}0
%{__mkdir_p} %{buildroot}%{_datadir}/applications
desktop-file-install \
    --vendor %{desktop_vendor} \
    --dir %{buildroot}%{_datadir}/applications \
    %{name}.desktop
%else
%{__install} -Dp -m 0644 %{name}.desktop \
    %{buildroot}%{_sysconfdir}/X11/applnk/Games/%{name}.desktop
%endif


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc docs/*
%{_prefix}/games/starfighter
%{_prefix}/share/games/starfighter
%{_datadir}/pixmaps/starfighter.png
%if %{!?_without_freedesktop:1}0
%{_datadir}/applications/%{desktop_vendor}-%{name}.desktop
%else
%{_sysconfdir}/X11/applnk/Games/%{name}.desktop
%endif


%changelog
* Tue Jun  8 2004 Matthias Saou <http://freshrpms.net/> 1.1-1
- Initial RPM release.

