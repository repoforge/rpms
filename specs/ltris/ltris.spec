# $Id$
# Authority: matthias

%define desktop_vendor freshrpms

Summary: Tetris clone
Name: ltris
Version: 1.0.6
Release: 1
License: GPL
Group: Amusements/Games
URL: http://www.lgames.org/
Source: http://dl.sf.net/lgames/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: SDL >= 1.1.4, SDL_mixer
BuildRequires: SDL-devel, SDL_mixer-devel, desktop-file-utils, ImageMagick

%description
A tetris clone game for Linux that uses the SDL.
No need to say much more :-)


%prep
%setup


%build
%configure
%{__make} %{?_smp_mflags}
# Having it as png seems more consistent
convert icons/ltris48.xpm %{name}.png


%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}
%{__install} -D %{name}.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

%{__cat} > %{name}.desktop << EOF
[Desktop Entry]
Name=LTris
Comment=Tetris clone
Exec=%{name}
Icon=%{name}.png
Terminal=false
Type=Application
Categories=Application;Game;
Encoding=UTF-8
EOF

%{__mkdir_p} %{buildroot}%{_datadir}/applications
desktop-file-install --vendor %{desktop_vendor} \
    --dir %{buildroot}%{_datadir}/applications \
    %{name}.desktop


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING ChangeLog README TODO
%attr(2551, root, games) %{_bindir}/%{name}
%{_datadir}/applications/%{desktop_vendor}-%{name}.desktop
%{_datadir}/games/%{name}
%{_datadir}/pixmaps/%{name}.png
%config(noreplace) %attr(664, root, games) %{_localstatedir}/lib/games/%{name}.hscr


%changelog
* Thu May 20 2004 Matthias Saou <http://freshrpms.net/> 1.0.6-1
- Rebuild for Fedora Core 2.
- Update to 1.0.6.
- Added menu entry icon.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 1.0.5-2
- Rebuild for Fedora Core 1.

* Sun Oct  5 2003 Matthias Saou <http://freshrpms.net/>
- Update to 1.0.5.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Update to 1.0.4, doh!
- Rebuilt for Red Hat Linux 9.

* Fri Oct  4 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 8.0.
- New menu entry.

* Fri Jul 26 2002 Matthias Saou <http://freshrpms.net/>
- Update to 1.0.3.

* Thu May  2 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt against Red Hat Linux 7.3.
- Added the %{?_smp_mflags} expansion.

* Mon Jan 14 2002 Matthias Saou <http://freshrpms.net/>
- Update to 1.0.1.

* Thu Jan 10 2002 Matthias Saou <http://freshrpms.net/>
- Update to 1.0.

* Tue Apr 24 2001 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat 7.1.

* Tue Mar 13 2001 Matthias Saou <http://freshrpms.net/>
- Update to 010310.

* Tue Jan  2 2001 Matthias Saou <http://freshrpms.net/>
- Initial RPM release for RedHat 7.0

