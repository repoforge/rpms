# $Id$
# Authority: leet
# Upstream: Frank Becker <crittermail2005$telus,net>
# Screenshot: http://criticalmass.sourceforge.net/images-critter/pics.v097/snap04.jpeg
# ScreenshotURL: http://criticalmass.sourceforge.net/oldweb/screenshots.html

%define real_name CriticalMass


%define desktop_vendor rpmforge

Summary: SDL/OpenGL space shoot'em up game
Name: critter
Version: 1.0.0
Release: 2%{?dist}
License: GPL
Group: Amusements/Games
URL: http://criticalmass.sourceforge.net/critter.php

Source: http://dl.sf.net/criticalmass/%{real_name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: SDL-devel, SDL_mixer-devel, SDL_image-devel, zlib-devel
BuildRequires: libpng-devel >= 1.2, gcc-c++
BuildRequires: desktop-file-utils

%description
Critical Mass (aka Critter) is an SDL/OpenGL space shoot'em up game.

%prep
%setup -n %{real_name}-%{version}

%{__cat} <<EOF >critter.desktop
[Desktop Entry]
Name=Critical Mass
Comment=SDL/OpenGL space shoot'em up game
Exec=critter
Icon=critter.png
Terminal=false
Type=Application
StartupNotify=true
Encoding=UTF-8
Categories=Application;Game;
EOF

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%{__install} -Dp -m0644 critter.png %{buildroot}%{_datadir}/pixmaps/critter.png


%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install \
	--vendor %{desktop_vendor} \
	--add-category X-Red-Hat-Base \
	--dir %{buildroot}%{_datadir}/applications \
	critter.desktop

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING Readme.html TODO
%doc %{_mandir}/man6/critter.6*
%{_bindir}/critter
%{_bindir}/Packer
%{_datadir}/applications/%{desktop_vendor}-critter.desktop
%{_datadir}/Critical_Mass/
%{_datadir}/pixmaps/critter.png


%changelog
* Thu Mar 30 2006 Dries Verachtert <dries@ulyssis.org> - 1.0.0-2
- Simplify buildequirements: SDL-devel already requires xorg-x11-devel/XFree86-devel

* Mon Jan 02 2006 Dries Verachtert <dries@ulyssis.org> - 1.0.0-1
- Updated to release 1.0.0.

* Wed Oct 05 2005 Dag Wieers <dag@wieers.com> - 0.9.12-1
- Cosmetic changes.

* Thu Sep 29 2005 C.Lee Taylor <leet@leenx.co.za> 0.9.12-1
- Made some minor updates and fix icon

* Wed Aug 31 2005 C.Lee Taylor <leet@leenx.co.za> 0.9.12-0
- Initial package
