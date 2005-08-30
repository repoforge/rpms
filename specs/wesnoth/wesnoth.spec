# $Id$
# Authority: dries

# Screenshot: http://www.wesnoth.org/images/sshots/wesnoth-10-175.jpg
# ScreenshotURL: http://www.wesnoth.org/sshots.htm

%define desktop_vendor rpmforge

Summary: Battle for Wesnoth is a fantasy turn-based strategy game
Name: wesnoth
Version: 0.9.6
Release: 1
License: GPL
Group: Amusements/Games
URL: http://www.wesnoth.org/

Source: http://www.wesnoth.org/files/wesnoth-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc-c++, make, SDL-devel >= 1.2.7
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
%setup

%{__cat} <<EOF >wesnoth.desktop
[Desktop Entry]
Version=1.0
Type=Application
Encoding=UTF-8
Name=Wesnoth
Exec=wesnoth
Categories=Application;Game;ArcadeGame;
EOF

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install \
	DESTDIR="%{buildroot}"

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor %{desktop_vendor}    \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	wesnoth.desktop

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING MANUAL MANUAL.* README
%doc %{_mandir}/man6/wesnoth*
%doc %{_mandir}/*/man6/wesnoth*
%{_bindir}/wesnoth
%{_bindir}/wmlxgettext
%{_datadir}/applications/%{desktop_vendor}-wesnoth.desktop
%{_datadir}/wesnoth/

%changelog
* Mon Aug 29 2005 Dries Verachtert <dries@ulyssis.org> - 0.9.6
- Update to release 0.9.6.

* Mon Aug 22 2005 Dries Verachtert <dries@ulyssis.org> - 0.9.5
- Update to release 0.9.5.

* Mon Jul 25 2005 Dries Verachtert <dries@ulyssis.org> - 0.9.4
- Update to release 0.9.4.

* Thu Jun 09 2005 Dries Verachtert <dries@ulyssis.org> - 0.9.2
- Update to release 0.9.2.

* Tue Feb 22 2005 Dag Wieers <dag@wieers.com> - 0.8.11-1
- Update to version 0.8.11.

* Tue Feb 08 2005 Dries Verachtert <dries@ulyssis.org> 0.8.10-1
- Update to version 0.8.10.

* Thu Dec 09 2004 Dries Verachtert <dries@ulyssis.org> 0.8.8-1
- Update to version 0.8.8.

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
