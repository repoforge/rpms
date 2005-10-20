# $Id$

# Authority: dries
# Screenshot: http://www.pygame.org/shredwheat/solarwolf/screen/shot4.jpg
# ScreenshotURL: http://www.pygame.org/shredwheat/solarwolf/

Summary: Python SDL game where you have to collect energy cubes
Name: solarwolf
Version: 1.5
Release: 2
License: LGPL
Group: Amusements/Games
URL: http://www.pygame.org/shredwheat/solarwolf/

Source: http://www.pygame.org/shredwheat/solarwolf/%{name}-%{version}.tar.gz
Source1: makefileandshellscript.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: python, python-game

%description
In SolarWolf you play a pilot collecting energy cubes from the defending
guardians. Avoid the deadly bullets, which become ever more popular as you
race through 48 levels. Good Luck. 

%prep
%setup -a 1

%build
make

%install
%{__rm} -rf %{buildroot}
export DESTDIR=%{buildroot}
make install

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc lgpl.txt readme.txt
%{_datadir}/games/solarwolf
%{_usr}/games/solarwolf
%{_datadir}/applications/solarwolf.desktop

%changelog
* Mon Mar 14 2005 Dries Verachtert <dries@ulyssis.org> 1.5-1
- update to release 1.5

* Sun Jan 25 2004 Dries Verachtert <dries@ulyssis.org> 1.4-2
- update of spec file

* Fri Dec 9 2003 Dries Verachtert <dries@ulyssis.org> 1.4-1
- update to version 1.4

* Fri Dec 2 2003 Dries Verachtert <dries@ulyssis.org> 1.3-2
- added a desktop file

* Wed Nov 24 2003 Dries Verachtert <dries@ulyssis.org> 1.3-1
- first packaging for Fedora Core 1
