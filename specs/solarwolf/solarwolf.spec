# $Id$

# Authority: dries
# Screenshot: http://www.pygame.org/shredwheat/solarwolf/screen/shot4.jpg
# ScreenshotURL: http://www.pygame.org/shredwheat/solarwolf/

Summary: Python SDL game where you have to collect energy cubes
Name: solarwolf
Version: 1.4
Release: 2
License: LGPL
Group: Amusements/Games
URL: http://www.pygame.org/shredwheat/solarwolf/

Packager:	Dries Verachtert <dries@ulyssis.org>
Vendor:		Dries Apt/Yum Repository, http://dries.ulyssis.org/ayo/

Source: http://www.pygame.org/shredwheat/solarwolf/%{name}-%{version}.tar.gz
Source1: makefileandshellscript.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: python, python-game

%description
In SolarWolf you play a pilot collecting energy cubes from the defending
guardians. Avoid the deadly bullets, which become ever more popular as you
race through 48 levels. Good Luck. 

%prep
%{__rm} -rf "${RPM_BUILD_ROOT}"
%setup -a 1

%build
make

%install
export DESTDIR=$RPM_BUILD_ROOT
make install

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc readme.txt lgpl.txt
/usr/share/games/solarwolf
/usr/games/solarwolf
/usr/share/applications/solarwolf.desktop

%changelog
* Sun Jan 25 2004 Dries Verachtert <dries@ulyssis.org> 1.4-2
- update of spec file

* Fri Dec 9 2003 Dries Verachtert <dries@ulyssis.org> 1.4-1
- update to version 1.4

* Fri Dec 2 2003 Dries Verachtert <dries@ulyssis.org> 1.3-2
- added a desktop file

* Wed Nov 24 2003 Dries Verachtert <dries@ulyssis.org> 1.3-1
- first packaging for Fedora Core 1
