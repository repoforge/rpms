# $Id$
# Authority: dries

# Screenshot: http://pathological.sourceforge.net/screenshots/theabyss-small.jpg
# ScreenshotURL: http://pathological.sourceforge.net/screenshots.php

Summary: an enriched clone of the game "Logical" by Rainbow Arts
Name: pathological
Version: 1.1.3
Release: 4.2%{?dist}
License: GPL
Group: Amusements/Games
URL: http://pathological.sourceforge.net/

Source: http://dl.sf.net/pathological/pathological-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: netpbm-progs
Requires: python, python-game

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
%{__rm} -rf %{buildroot}
%setup

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
mkdir -p $RPM_BUILD_ROOT/usr/bin
sed -i "s/^DESTDIR =.*/DESTDIR=${RPM_BUILD_ROOT//\//\\/}/g;" Makefile
make install
mkdir -p %{buildroot}%{_datadir}/applications
cat <<EOF >%{buildroot}%{_datadir}/applications/pathological.desktop
[Desktop Entry]
Version=1.0
Type=Application
Encoding=UTF-8
Name=Pathological
Exec=/usr/games/pathological
Categories=Application;Game;ArcadeGame
EOF

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc LICENSE README TODO
%{_usr}/X11R6/include/X11/pixmaps/pathological.xpm
%{_usr}/games/pathological
%{_usr}/lib/pathological/
%{_docdir}/pathological/
%{_datadir}/games/pathological
%{_mandir}/man6/pathological.6.gz
%{_localstatedir}/games/pathological_scores
%{_datadir}/applications/pathological.desktop

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.1.3-4.2
- Rebuild for Fedora Core 5.

* Sun Jan 11 2004 Dries Verachtert <dries@ulyssis.org> 1.1.3-4
- cleanup of spec file

* Fri Jan 2 2004 Dries Verachtert <dries@ulyssis.org> 1.1.3-3
- added a desktop icon

* Wed Dec 24 2003 Dries Verachtert <dries@ulyssis.org> 1.1.3-2
- updated %doc part

* Tue Dec 23 2003 Dries Verachtert <dries@ulyssis.org> 1.1.3-1
- first packaging for Fedora Core 1
