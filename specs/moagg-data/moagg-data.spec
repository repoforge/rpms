# $Id$
# Authority: dries
# Upstream: <moagg-devel$lists,sourceforge,net>

# Screenshot: http://moagg.sourceforge.net/screenshots/blackhole.png
# ScreenshotURL: http://moagg.sourceforge.net/screenshots.php

# Dist: nodist

Summary: The data of the game Mother of all Gravity Games
Name: moagg-data
Version: 0.16
Release: 2.2%{?dist}
License: GPL
Group: Amusements/Games
URL: http://moagg.sourceforge.net/

BuildArch: noarch
Requires: moagg >= %{version}

Source: http://dl.sf.net/moagg/moagg-%{version}-data.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Moagg combines several game types of other genres like races, search and
rescue, seek and destroy et cetera into a 2D gravity game. You are pilot of a
small space ship and have to navigate that ship through different levels.
But beside the gravity that drags you down there are other obstacles like
laser ports, magnets, black holes, cannons, rockets and grinders you have to
master.

This package contains all the data of this game.

%prep
%setup -n moagg-%{version}

%build
# nothing to do..

%install
%{__rm} -rf %{buildroot}
%{__install} -d %{buildroot}%{_datadir}/moagg
%{__cp} -pR cfg gfx sound levels %{buildroot}%{_datadir}/moagg

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_datadir}/moagg

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.16-2.2
- Rebuild for Fedora Core 5.

* Mon Dec 20 2004 Dries Verachtert <dries@ulyssis.org> 0.16-2
- Moved the data to a separate package.

* Tue Nov 23 2004 Dries Verachtert <dries@ulyssis.org> 0.16-1
- Update to version 0.16.

* Thu Nov 04 2004 Dries Verachtert <dries@ulyssis.org> 0.15-1
- Update to version 0.15.

* Wed Sep 01 2004 Dries Verachtert <dries@ulyssis.org> 0.14-1
- Update to version 0.14.

* Wed Jul 28 2004 Dries Verachtert <dries@ulyssis.org> 0.13-1
- Update to version 0.13.

* Mon Jul 12 2004 Dries Verachtert <dries@ulyssis.org> 0.12-1
- Update to version 0.12.

* Fri Jun 25 2004 Dries Verachtert <dries@ulyssis.org> 0.11-1
- Update to version 0.11.

* Fri Jun 4 2004 Dries Verachtert <dries@ulyssis.org> 0.10-1
- Update to version 0.10.

* Mon Apr 26 2004 Dries Verachtert <dries@ulyssis.org> 0.8-1
- Initial package.
