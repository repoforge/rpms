# $Id$

# Authority: dries
# Upstream: 
# Screenshot: http://www.wesnoth.org/images/sshots/wesnoth-10-175.jpg
# ScreenshotURL: http://www.wesnoth.org/sshots.htm

Summary: Battle for Wesnoth is a fantasy turn-based strategy game
Name: wesnoth
Version: 0.8.7
Release: 1
License: GPL
Group: Amusements/Games
URL: http://www.wesnoth.org/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://www.wesnoth.org/files/wesnoth-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc-c++, make, SDL, SDL_net, SDL_mixer, SDL-devel
BuildRequires: SDL_image-devel, SDL_ttf-devel, SDL_net-devel
BuildRequires: SDL_mixer-devel, desktop-file-utils
BuildRequires: gettext
Requires: SDL, SDL_net, SDL_mixer, SDL_image, SDL_ttf, SDL_net

%description
Battle for Wesnoth is a fantasy turn-based strategy game. Battle 
for control of villages, using variety of units which have advantages 
and disadvantages in different types of terrains and against
different types of attacks. Units gain experience and advance levels, 
and are carried over from one scenario to the next campaign. 

%prep
%{__rm} -rf %{buildroot}
%setup
%{__cat} > wesnoth.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Encoding=UTF-8
Name=Wesnoth
Exec=/usr/bin/wesnoth
Categories=Application;Game;ArcadeGame;
EOF

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install-strip DESTDIR=%{buildroot}
%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor rpmforge             \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	wesnoth.desktop

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README COPYING MANUAL MANUAL.*
%{_bindir}/wesnoth
%{_mandir}/man6/wesnoth*
%{_datadir}/wesnoth
%{_datadir}/applications/*.desktop

%changelog
* Tue Nov 02 2004 Dries Verachtert <dries@ulyssis.org> 0.8.7-1
- Update to version 0.8.7.

* Mon Oct 25 2004 Dries Verachtert <dries@ulyssis.org> 0.8.5-1
- Update to version 0.8.5.

* Sun Sep 12 2004 Dries Verachtert <dries@ulyssis.org> 0.8.4-1
- Update to version 0.8.4.

* Wed Sep 01 2004 Dries Verachtert <dries@ulyssis.org> 0.8.3-1
- Update to version 0.8.3.

* Mon Jul 19 2004 Dries Verachtert <dries@ulyssis.org> 0.8-1
- Update to version 0.8.

* Wed Jun 30 2004 Dries Verachtert <dries@ulyssis.org> 0.7.11-1
- Update to version 0.7.11.

* Mon Jun 21 2004 Dries Verachtert <dries@ulyssis.org> 0.7.10-1
- Update to version 0.7.10.

* Sat Jun 12 2004 Dries Verachtert <dries@ulyssis.org> 0.7.9-1
- Update to version 0.7.9.

* Tue May 4 2004 Dries Verachtert <dries@ulyssis.org> 0.7.6-1
- Update to version 0.7.6.

* Fri Dec 22 2003 Dries Verachtert <dries@ulyssis.org> 0.6.1-2
- Added a desktop file.

* Sat Dec 20 2003 Dries Verachtert <dries@ulyssis.org> 0.6.1-1
- Update from 0.6 to 0.6.1.

* Sat Dec 13 2003 Dries Verachtert <dries@ulyssis.org> 0.6-1
- Initial packaging.
