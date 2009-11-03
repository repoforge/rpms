# $Id$
# Authority: matthias

%define desktop_vendor rpmforge

Summary: Game of skill with falling blocks
Name: ltris
Version: 1.0.12
Release: 1%{?dist}
License: GPL
Group: Amusements/Games
URL: http://lgames.sourceforge.net/
Source: http://dl.sf.net/lgames/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: SDL >= 1.1.4, SDL_mixer
BuildRequires: SDL-devel, SDL_mixer-devel, desktop-file-utils, ImageMagick

%description
LTris as a tetris clone which means you have a bowl with blocks falling down.
By rotating and moving the blocks you try to assemble whole lines which then
disappear. LTris has three modes for this: Classic is the classical one where
you play until the bowl becomes filled, Figures resets the bowl contents to a
new figure for each level and adds suddenly appearing tiles and lines later
on and Multiplayer where up to three players either controlled by human or
CPU(!) compete and send completed lines to each other.


%prep
%setup


%build
%configure --localstatedir=%{_var}/lib/games
%{__make} %{?_smp_mflags}
# Having it as png seems more consistent
convert icons/ltris48.xpm ltris.png


%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}
%find_lang %{name}
%{__install} -D -p ltris.png %{buildroot}%{_datadir}/pixmaps/ltris.png

%{__cat} > %{name}.desktop << EOF
[Desktop Entry]
Name=LTris
Comment=Tetris clone
Exec=ltris
Icon=ltris.png
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


%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING ChangeLog README TODO
%attr(2551, root, games) %{_bindir}/ltris
%{_datadir}/applications/%{desktop_vendor}-%{name}.desktop
%{_datadir}/ltris/
%{_datadir}/pixmaps/ltris.png
%config(noreplace) %attr(664, root, games) %{_localstatedir}/lib/games/ltris.hscr


%changelog
* Mon Mar 31 2008 Matthias Saou <http://freshrpms.net/> 1.0.12-1
- Update to 1.0.12.

* Fri Mar 17 2006 Matthias Saou <http://freshrpms.net/> 1.0.11-2
- Release bump to drop the disttag number in FC5 build.

* Fri Oct  7 2005 Matthias Saou <http://freshrpms.net/> 1.0.11-1
- Update to 1.0.11.
- Include new translation.

* Sat Feb 19 2005 Matthias Saou <http://freshrpms.net/> 1.0.10-1
- Update to 1.0.10.

* Wed Jan 26 2005 Matthias Saou <http://freshrpms.net/> 1.0.9-1
- Update to 1.0.9.

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

