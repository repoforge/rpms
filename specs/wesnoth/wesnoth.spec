# $Id: $

# Authority: dries
# Upstream: 

Summary: Battle for Wesnoth is a fantasy turn-based strategy game
Name: wesnoth
Version: 0.7.6
Release: 1
License: GPL
Group: Amusements/Games
URL: http://www.wesnoth.org/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://www.wesnoth.org/files/wesnoth-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: gcc-c++, make, SDL, SDL_net, SDL_mixer, SDL-devel, SDL_image-devel, SDL_ttf-devel, SDL_net-devel, SDL_mixer-devel
Requires: SDL, SDL_net, SDL_mixer, SDL_image, SDL_ttf, SDL_net

# Screenshot: http://www.wesnoth.org/images/sshots/wesnoth-10-175.jpg
# ScreenshotURL: http://www.wesnoth.org/sshots.htm

%description
Battle for Wesnoth is a fantasy turn-based strategy game. Battle 
for control of villages, using variety of units which have advantages 
and disadvantages in different types of terrains and against
different types of attacks. Units gain experience and advance levels, 
and are carried over from one scenario to the next campaign. 

%prep
%{__rm} -rf %{buildroot}
%setup

%build
%configure
make
cat > wesnoth.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Encoding=UTF-8
Name=Wesnoth
Exec=/usr/bin/wesnoth
Categories=Application;Game;ArcadeGame
EOF

%install
make install-strip DESTDIR=%{buildroot}
mkdir -p %{buildroot}/usr/share/applications/
cp wesnoth.desktop %{buildroot}/usr/share/applications/

%files
%defattr(-,root,root, 0755)
%doc README COPYING MANUAL MANUAL.danish MANUAL.french MANUAL.german MANUAL.italian MANUAL.spanish 
%{_bindir}/wesnoth
%{_datadir}/man/man6/wesnoth*
%{_datadir}/wesnoth
%{_datadir}/applications/wesnoth.desktop

%changelog
* Tue May 4 2004 Dries Verachtert <dries@ulyssis.org> 0.7.6-1
- update
* Fri Dec 22 2003 Dries Verachtert <dries@ulyssis.org> 0.6.1-2
- added a desktop file
* Sat Dec 20 2003 Dries Verachtert <dries@ulyssis.org> 0.6.1-1
- update from 0.6 to 0.6.1
* Sat Dec 13 2003 Dries Verachtert <dries@ulyssis.org> 0.6-1
- first packaging for Fedora Core 1
