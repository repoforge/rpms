# $Id: pathological.spec,v 1.2 2004/02/27 17:08:22 driesve Exp $

# Authority: dries

Summary: an enriched clone of the game "Logical" by Rainbow Arts
Name: pathological
Version: 1.1.3
Release: 4
License: GPL
Group: Amusements/Games
URL: http://pathological.sourceforge.net/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://dl.sf.net/pathological/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Requires: python, python-game

#(d) primscreenshot: http://pathological.sourceforge.net/screenshots/theabyss-small.jpg
#(d) screenshotsurl: http://pathological.sourceforge.net/screenshots.php

%description
Pathological is an enriched clone of the game "Logical" by Rainbow Arts. To
solve a level, fill each wheel with four marbles of matching color. Various
board elements such as teleporters, switches, filters, etc., make the game
interesting and challenging. New levels can be created using your favorite
text editor. 

%description -l nl
Pathological is een kloon van het spel "Logical" met extra uitbreidingen. Om
een level op te lossen moet je elk wiel vullen met vier knikkers met
dezelfde kleur. Verschillende bordelementen zoals teleporters, schakelaars,
filters enzovoort maken het spel interessant en uitdagend. Nieuwe levels
kunnen gemaakt worden met een gewone teksteditor.

%prep
%{__rm} -rf "${RPM_BUILD_ROOT}"
%setup

%build
%{__make} %{?_smp_mflags}

%install
echo RPM_BUILD_ROOT is $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin
sed -i "s/^DESTDIR =.*/DESTDIR=${RPM_BUILD_ROOT//\//\\/}/g;" Makefile
make install
mkdir -p $RPM_BUILD_ROOT/usr/share/applications
cat > $RPM_BUILD_ROOT/usr/share/applications/pathological.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Encoding=UTF-8
Name=Pathological
Exec=/usr/games/pathological
Categories=Application;Game;ArcadeGame
EOF

%files
%defattr(-,root,root,0755)
%doc README TODO LICENSE
/usr/X11R6/include/X11/pixmaps/pathological.xpm
/usr/games/pathological
/usr/lib/pathological/bin/write-highscores
/usr/share/doc/pathological/html
/usr/share/games/pathological
/usr/share/man/man6/pathological.6.gz
/var/games/pathological_scores
/usr/share/applications/pathological.desktop

%changelog
* Sun Jan 11 2004 Dries Verachtert <dries@ulyssis.org> 1.1.3-4
- cleanup of spec file

* Fri Jan 2 2004 Dries Verachtert <dries@ulyssis.org> 1.1.3-3
- added a desktop icon

* Wed Dec 24 2003 Dries Verachtert <dries@ulyssis.org> 1.1.3-2
- updated %doc part

* Tue Dec 23 2003 Dries Verachtert <dries@ulyssis.org> 1.1.3-1
- first packaging for Fedora Core 1
