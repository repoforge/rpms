# $Id$
# Authority: matthias

%define desktop_vendor rpmforge

Summary: Atomix clone where you create figures out of marbles
Name: lmarbles
Version: 1.0.7
Release: 1%{?dist}
License: GPL
Group: Amusements/Games
URL: http://lgames.sourceforge.net/
Source: http://dl.sf.net/lgames/lmarbles-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: SDL >= 1.1.4, SDL_mixer
BuildRequires: SDL-devel, SDL_mixer-devel, desktop-file-utils, ImageMagick
Obsoletes: marbles <= 1.0.5

%description
LMarbles is an Atomix clone with a slight change in concept. Instead of
assembling molecules you create figures out of marbles. Nevertheless, the
basic game play is the same: If a marble starts to move it will not stop
until it hits a wall or another marble. To make it more interesting there
are obstacles like one-way streets, crumbling walls and portals.
As Marbles is meant as a puzzle game you play against a move limit and not
a time limit. This way you have as much time as you need to think.


%prep
%setup


%build
%configure --localstatedir=%{_var}/lib/games
%{__make} %{?_smp_mflags}
# Having it as png seems more consistent
convert lmarbles48.gif lmarbles.png


%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}
%{__install} -Dp lmarbles.png %{buildroot}%{_datadir}/pixmaps/lmarbles.png

%{__cat} > %{name}.desktop << EOF
[Desktop Entry]
Name=LMarbles
Comment=Atomix clone where you create figures out of marbles
Exec=lmarbles
Icon=lmarbles.png
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


%post
update-desktop-database %{_datadir}/applications &>/dev/null || :

%postun
update-desktop-database %{_datadir}/applications &>/dev/null || :


%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING ChangeLog README TODO
%attr(2551, root, games) %{_bindir}/lmarbles
%{_datadir}/applications/%{desktop_vendor}-%{name}.desktop
%{_datadir}/lmarbles/
%{_datadir}/pixmaps/lmarbles.png
%{_mandir}/man6/lmarbles.6*
%config(noreplace) %attr(664, games, games) %{_var}/lib/games/lmarbles.prfs


%changelog
* Wed Jan 26 2005 Matthias Saou <http://freshrpms.net/> 1.0.7-1
- Update to 1.0.7.

* Wed May 19 2004 Matthias Saou <http://freshrpms.net/> 1.0.6-3
- Rebuild for Fedora Core 2.
- Added menu icon.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 1.0.6-2
- Rebuild for Fedora Core 1.
- Added missing SDL_mixer depencency.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Update to 1.0.6 and renamed to lmarbles.
- Rebuilt for Red Hat Linux 9.

* Fri Oct  4 2002 Matthias Saou <http://freshrpms.net/>
- Update to 1.0.5.
- Rebuilt for Red Hat Linux 8.0.
- New menu entry.

* Tue Jul  2 2002 Matthias Saou <http://freshrpms.net/>
- Update to 1.0.4.

* Tue Jun 25 2002 Matthias Saou <http://freshrpms.net/>
- Update to 1.0.3.

* Thu May  2 2002 Matthias Saou <http://freshrpms.net/>
- Update to 1.0.2.
- Rebuilt against Red Hat Linux 7.3.
- Added the %{?_smp_mflags} expansion.

* Fri Feb  8 2002 Matthias Saou <http://freshrpms.net/>
- Update to 1.0.1

* Thu Apr 24 2001 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat 7.1.

* Thu Mar  8 2001 Matthias Saou <http://freshrpms.net/>
- Update to 010307.

* Tue Jan  2 2001 Matthias Saou <http://freshrpms.net/>
- Initial RPM release for RedHat 7.0

