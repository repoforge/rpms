# $Id$
# Authority: matthias

%define desktop_vendor rpmforge

%{?dtag: %{expand: %%define %dtag 1}}

%{?fc4:%define _without_modxorg 1}
%{?el4:%define _without_modxorg 1}
%{?fc3:%define _without_modxorg 1}
%{?fc2:%define _without_modxorg 1}
%{?fc1:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}
%{?rh9:%define _without_modxorg 1}
%{?rh7:%define _without_modxorg 1}
%{?el2:%define _without_modxorg 1}
%{?yd3:%define _without_modxorg 1}

%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}

Summary: Arcade 2D shoot-them-up game
Name: powermanga
Version: 0.79
Release: 1%{?dist}
License: GPL
Group: Amusements/Games
URL: http://linux.tlk.fr/games/Powermanga/
Source0: http://linux.tlk.fr/games/Powermanga/download/powermanga-%{version}.tgz
Source1: powermanga.png
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc-c++, SDL-devel, SDL_mixer-devel
%{!?_without_modxorg:BuildRequires: libX11-devel}
%{?_without_modxorg:BuildRequires: XFree86-devel}
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}

%description
Powermanga is an arcade 2D shoot-them-up game with 41 levels and more than
200 sprites.


%prep
%setup

%{__cat} > %{name}.desktop << EOF
[Desktop Entry]
Name=Powermanga
Comment=Arcade 2D shoot-them-up game
Icon=powermanga.png
Exec=/usr/games/powermanga
Terminal=false
Type=Application
Categories=Application;Game;ArcadeGame;
Encoding=UTF-8
EOF


%build
%configure
%{__make} %{?_smp_mflags} CXXFLAGS="%{optflags}"


%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}

# Fix location of the man page
%{__mkdir_p} %{buildroot}%{_mandir}/man6
%{__mv} %{buildroot}%{_prefix}/share/man/powermanga.6 \
        %{buildroot}%{_mandir}/man6/

# Install pixmap for the menu entry
%{__install} -Dp -m 644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/powermanga.png

# Install menu entry
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
%doc AUTHORS CHANGES COPYING README
%attr(2755, root, games) %{_prefix}/games/powermanga
%{_datadir}/games/powermanga
%{_datadir}/pixmaps/powermanga.png
%{_mandir}/man6/powermanga.6*
%config(noreplace) %attr(664, root, games) /var/games/powermanga.hi
%config(noreplace) %attr(664, root, games) /var/games/powermanga.hi-easy
%config(noreplace) %attr(664, root, games) /var/games/powermanga.hi-hard
%if %{!?_without_freedesktop:1}0
%{_datadir}/applications/%{desktop_vendor}-%{name}.desktop
%else
%{_sysconfdir}/X11/applnk/Games/%{name}.desktop
%endif


%changelog
* Tue Aug 10 2004 Matthias Saou <http://freshrpms.net/> 0.79-1
- Spec file cleanup.
- Included the menu pixmap from the Mandrake package.
- Update to 0.79.

* Wed Dec 20 2000 Matthias Saou <http://freshrpms.net/> 0.71c-2
- Initial RPM release.

