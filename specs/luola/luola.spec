# $Id$

# Authority: dries
# Upstream: Calle Laakkonen <calle,laakkonen$saunalahti,fi>
# Screenshot: http://www.saunalahti.fi/~laakkon1/linux/luola/bin/screenshot7.jpg
# ScreenshotURL: http://www.saunalahti.fi/~laakkon1/linux/luola/index.php#screenshots

Summary: Multiplayer 2D arcade game 
Name: luola
Version: 1.2.7
Release: 1
License: GPL
Group: Amusements/Games
URL: http://www.saunalahti.fi/~laakkon1/linux/luola/index.php

Source: http://www.saunalahti.fi/~laakkon1/linux/luola/bin/luola-%{version}.tar.gz
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

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=Luolo
Comment=2D arcade game
Exec=luolo
Terminal=false
Type=Application
StartupNotify=true
Encoding=UTF-8
Categories=Application;Game;X-Red-Hat-Extra;
EOF

%build
%configure --disable-sdltest
%{__perl} -pi -e 's|PACKAGE_DATA_DIR .*|PACKAGE_DATA_DIR "%{_datadir}/luola"|g;' config.h
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor rpmforge             \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	%{name}.desktop

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%{_bindir}/luola
%{_datadir}/luola
%{_datadir}/applications/*.desktop

%changelog
* Sun Apr 10 2005 Dries Verachtert <dries@ulyssis.org> - 1.2.7-1
- Update to release 1.2.7.

* Sat Jan 01 2005 Dries Verachtert <dries@ulyssis.org> - 1.2.5-1
- Initial package.
