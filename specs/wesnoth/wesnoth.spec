# $Id$
# Authority: dries

# Screenshot: http://www.wesnoth.org/images/sshots/wesnoth-10-175.jpg
# ScreenshotURL: http://www.wesnoth.org/sshots.htm

%define desktop_vendor rpmforge

Summary: Battle for Wesnoth is a fantasy turn-based strategy game
Name: wesnoth
Version: 1.6.4
Release: 1%{?dist}
License: GPL
Group: Amusements/Games
URL: http://www.wesnoth.org/

Source: http://www.wesnoth.org/files/wesnoth-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc-c++, make, SDL-devel >= 1.2.7
BuildRequires: SDL_image-devel, SDL_ttf-devel, SDL_net-devel
BuildRequires: SDL_mixer-devel, desktop-file-utils
BuildRequires: gettext, kdelibs-devel
Requires: SDL, SDL_net, SDL_mixer, SDL_image, SDL_ttf, SDL_net

%description
Battle for Wesnoth is a fantasy turn-based strategy game. Battle
for control of villages, using variety of units which have advantages
and disadvantages in different types of terrains and against
different types of attacks. Units gain experience and advance levels,
and are carried over from one scenario to the next campaign.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING README
%doc %{_docdir}/wesnoth/
%doc %{_mandir}/man6/wesnoth.6*
%doc %{_mandir}/*/man6/wesnoth.6*
%{_bindir}/wesnoth
%{_bindir}/wesnothd
%{_datadir}/applications/wesnoth.desktop
%{_datadir}/applications/wesnoth_editor.desktop
%{_datadir}/icons/wesnoth-icon.png
%{_datadir}/icons/wesnoth_editor-icon.png
%{_datadir}/wesnoth/

%changelog
* Sat Jul 11 2009 Dries Verachtert <dries@ulyssis.org> - 1.6.4-1
- Updated to release 1.6.4.

* Thu Mar 13 2008 Dries Verachtert <dries@ulyssis.org> - 1.4-1
- Updated to release 1.4.

* Mon Apr 16 2007 Dries Verachtert <dries@ulyssis.org> - 1.2.4-1
- Updated to release 1.2.4.

* Mon Dec 25 2006 Dries Verachtert <dries@ulyssis.org> - 1.2-1
- Updated to release 1.2.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.0.2-1.2
- Rebuild for Fedora Core 5.

* Tue Dec 06 2005 Dries Verachtert <dries@ulyssis.org> - 1.0.2-1
- Updated to release 1.0.2.

* Fri Oct 28 2005 Dries Verachtert <dries@ulyssis.org> - 1.0.1-1
- Updated to release 1.0.1.

* Mon Oct 03 2005 Dries Verachtert <dries@ulyssis.org> - 1.0-1
- Updated to release 1.0.

* Wed Sep 14 2005 Dries Verachtert <dries@ulyssis.org> - 0.9.7
- Update to release 0.9.7.

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
