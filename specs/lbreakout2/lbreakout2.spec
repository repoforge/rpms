# $Id$

%define	desktop_vendor	freshrpms
%define beta 3

Summary: A breakout-style arcade game for Linux
Name: lbreakout2
Version: 2.5
Release: %{?beta:0.beta%{beta}.}1.fr
License: GPL
Group: Amusements/Games
Source: http://dl.sf.net/lgames/%{name}-%{version}%{?beta:beta-%{beta}}.tar.gz
URL: http://www.lgames.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: SDL >= 1.1.5, SDL_mixer
Requires: zlib, libpng
BuildRequires: SDL-devel, SDL_mixer-devel, desktop-file-utils
BuildRequires: zlib-devel, libpng-devel

%description
A breakout-style arcade game for Linux that uses the SDL

%prep
%setup -q -n %{name}-%{version}%{?beta:beta-%{beta}}

%build
%configure \
    --with-highscore-path=%{_localstatedir}/lib/games \
    --with-doc-path=%{_docdir}
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_localstatedir}/lib/games
make install DESTDIR=%{buildroot}
install -m 644 -D lbreakout48.gif %{buildroot}%{_datadir}/pixmaps/lbreakout.gif

# Put the doc back into place
mv %{buildroot}%{_docdir}/%{name} doc

# Create the system menu entry
cat > %{name}.desktop << EOF
[Desktop Entry]
Name=Linux Breakout 2
Comment=%{summary}
Exec=lbreakout2
Icon=lbreakout.gif
Terminal=false
Type=Application
EOF

mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install --vendor %{desktop_vendor} --delete-original \
  --dir %{buildroot}%{_datadir}/applications                      \
  --add-category X-Red-Hat-Extra                                  \
  --add-category Application                                      \
  --add-category Game                                             \
  %{name}.desktop

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog README TODO doc/
%attr(2551, root, games) %{_bindir}/%{name}*
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/games/%{name}
%{_datadir}/pixmaps/lbreakout.gif
%config(noreplace) %attr(664, games, games) %{_localstatedir}/lib/games/%{name}.hscr

%changelog
* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 1.3.0-2.fr
- Update to 2.5beta-3.
- Added missing zlib and libpng dependencies.
- Rebuild for Fedora Core 1.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.

* Sun Mar  9 2003 Matthias Saou <http://freshrpms.net/>
- Update to 2.4.1.

* Fri Jan  3 2003 Matthias Saou <http://freshrpms.net/>
- Update to 2.4.

* Sat Oct 26 2002 Matthias Saou <http://freshrpms.net/>
- Fixed the menu entry, thanks to Erwin J. Prinz.

* Sat Sep 28 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 8.0.
- New menu entry with icon.

* Mon Sep 23 2002 Matthias Saou <http://freshrpms.net/>
- Update to 2.3.5.

* Tue Sep 10 2002 Matthias Saou <http://freshrpms.net/>
- Update to 2.3.3.

* Tue Sep 10 2002 Matthias Saou <http://freshrpms.net/>
- Update to 2.3.3.

* Mon Aug 19 2002 Matthias Saou <http://freshrpms.net/>
- Update to 2.3.2.

* Wed Aug 14 2002 Matthias Saou <http://freshrpms.net/>
- Update to 2.3.1.

* Thu May  2 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt against Red Hat Linux 7.3.
- Added the %{?_smp_mflags} expansion.

* Sun Feb 24 2002 Matthias Saou <http://freshrpms.net/>
- Update to 2.2.2.

* Tue Feb  5 2002 Matthias Saou <http://freshrpms.net/>
- Update to 2.2.1.

* Mon Jan 28 2002 Matthias Saou <http://freshrpms.net/>
- Update to 2.2.

* Sun Jan  6 2002 Matthias Saou <http://freshrpms.net/>
- Update to 2.1.2.

* Tue Jan  1 2002 Matthias Saou <http://freshrpms.net/>
- Update to 2.1.1.

* Sat Dec  8 2001 Matthias Saou <http://freshrpms.net/>
- Update to 2.0.1.

* Thu Nov 29 2001 Matthias Saou <http://freshrpms.net/>
- Update to 2.0-pre2.

* Thu Nov 22 2001 Matthias Saou <http://freshrpms.net/>
- Update to 2.0beta2.

* Tue Apr 10 2001 Matthias Saou <http://freshrpms.net/>
- Update to 010315.

* Mon Nov 27 2000 Matthias Saou <http://freshrpms.net/>
- Initial RPM release for RedHat 7.0

