# $Id$
# Authority: matthias

%define desktop_vendor freshrpms

Summary: An Atomix clone for Linux that uses the SDL
Name: lmarbles
Version: 1.0.6
Release: 2
License: GPL
Group: Amusements/Games
URL: http://www.lgames.org/
Source: http://dl.sf.net/lgames/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: SDL >= 1.1.4, SDL_mixer
BuildRequires: SDL-devel, SDL_mixer-devel, desktop-file-utils
Obsoletes: marbles <= 1.0.5

%description
An Atomix clone game for Linux that uses the SDL.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}

cat > %{name}.desktop << EOF
[Desktop Entry]
Name=LMarbles
Comment=%{summary}
Exec=lmarbles
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
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING ChangeLog README TODO
%attr(2551, root, games) %{_bindir}/%{name}
%{_datadir}/applications/%{desktop_vendor}-%{name}.desktop
%{_datadir}/games/%{name}
%{_mandir}/man6/%{name}*
%config(noreplace) %attr(664, games, games) %{_localstatedir}/lib/games/marbles.prfs

%changelog
* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 1.0.6-2.fr
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

