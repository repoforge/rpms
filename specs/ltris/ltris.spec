# $Id$

%define desktop_vendor freshrpms

Summary: A tetris clone for Linux that uses the SDL
Name: ltris
Version: 1.0.5
Release: 2.fr
License: GPL
Group: Amusements/Games
URL: http://www.lgames.org/
Source: http://dl.sf.net/lgames/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: SDL >= 1.1.4
BuildRequires: SDL-devel, desktop-file-utils

%description
A tetris clone game for Linux that uses the SDL.
No need to say much more :-)

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

cat > %{name}.desktop << EOF
[Desktop Entry]
Name=LTris
Comment=%{summary}
Exec=%{name}
Icon=
Terminal=0
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
%doc AUTHORS COPYING ChangeLog README TODO
%attr(2551, root, games) %{_bindir}/%{name}
%{_datadir}/applications/%{desktop_vendor}-%{name}.desktop
%{_datadir}/games/%{name}
%config(noreplace) %attr(664, root, games) %{_localstatedir}/lib/games/%{name}.hscr

%changelog
* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 1.0.5-2.fr
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

