# $Id$
# Authority: dries
# Upstream: Calle Laakkonen <calle$luolamies,org>

# Screenshot: http://www.luolamies.org/software/luola/screens/screen6.png
# ScreenshotURL: http://www.luolamies.org/software/luola/#screenshots

%define desktop_vendor rpmforge

Summary: Multiplayer 2D arcade game
Name: luola
Version: 1.3.2
Release: 3
License: GPL
Group: Amusements/Games
URL: http://www.luolamies.org/software/luola/

Source0: http://www.luolamies.org/software/luola/luola-%{version}.tar.gz
Source1: luola.png
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: SDL-devel, SDL_image-devel, SDL_mixer-devel, SDL_gfx-devel
BuildRequires: SDL_ttf-devel, desktop-file-utils, zlib-devel
Requires: luola-levels

%description
Luola is a 2D arcade game where you fly a small V shaped ship in different
kinds of levels. It's genre "Luolalentely" (Cave-flying) is (or was) very
popular here in Finland. Though cavern-flying games are not originally
Finnish, nowdays most of them are.

%prep
%setup

%{__cat} <<EOF >luola.desktop
[Desktop Entry]
Name=Luola
Comment=2D arcade game
Exec=luola
Icon=luola.png
Terminal=false
Version=%{version}
Type=Application
StartupNotify=true
Encoding=UTF-8
Categories=Application;Game;X-Red-Hat-Extra;
EOF

%build
%configure --disable-sdltest
%{__perl} -pi -e 's|PACKAGE_DATA_DIR .*$|PACKAGE_DATA_DIR "%{_datadir}/luola"|g;' config.h
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor %{desktop_vendor}    \
    --add-category X-Red-Hat-Base              \
    --dir %{buildroot}%{_datadir}/applications \
    luola.desktop
%{__install} -Dp -m0644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/luola.png

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%{_bindir}/luola
%{_datadir}/applications/%{desktop_vendor}-luola.desktop
%{_datadir}/luola
%{_datadir}/pixmaps/luola.png

%changelog
* Mon Apr 27 2009 Dag Wieers <dag@wieers.com> - 1.3.2-3
- Rebuild against SDL_gfx 2.0.19.

* Thu Dec 28 2006 Dag Wieers <dag@wieers.com> - 1.3.2-2
- Rebuild against SDL_gfx 2.0.15.

* Mon Jan 06 2006 Dries Verachtert <dries@ulyssis.org> - 1.3.2-1
- Updated to release 1.3.2.

* Wed Dec 21 2005 Dries Verachtert <dries@ulyssis.org> - 1.3.1-1
- Updated to release 1.3.1.

* Fri Oct 28 2005 Dries Verachtert <dries@ulyssis.org> - 1.3.0-1
- Updated to release 1.3.0.

* Mon Aug 15 2005 C.Lee Taylor <leet@leenx.co.za> - 1.2.9-2
- Added icon and changed to new internet site.

* Sun Aug 14 2005 Dries Verachtert <dries@ulyssis.org> - 1.2.9-1
- Update to release 1.2.9.

* Thu Jul 28 2005 Dries Verachtert <dries@ulyssis.org> - 1.2.8-1
- Update to release 1.2.8.

* Sun Apr 10 2005 Dries Verachtert <dries@ulyssis.org> - 1.2.7-1
- Update to release 1.2.7.

* Sat Jan 01 2005 Dries Verachtert <dries@ulyssis.org> - 1.2.5-1
- Initial package.
