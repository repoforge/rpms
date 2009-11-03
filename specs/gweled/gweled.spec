# $Id$
# Authority: dries
# Screenshot: http://sebdelestaing.free.fr/gweled/Images/gweled_screenshot.png

Summary: Clone of 'bjeweled' or 'diamond mine'
Name: gweled
Version: 0.7
Release: 1.2%{?dist}
License: GPL
Group: Amusements/Games
URL: http://sebdelestaing.free.fr/gweled/

Source: http://sebdelestaing.free.fr/gweled/Release/gweled-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: libgnomeui-devel, librsvg2-devel, libcroco-devel, mikmod-devel

%description
Gweled is a Gnome version of a popular PalmOS/Windows/Java game called
"Bejeweled" or "Diamond Mine". The aim of the game is to make alignment of 3
or more gems, both vertically or horizontally by swapping adjacent gems. The
game ends when there are no possible moves left.

%description -l nl
Gweled is een Gnome versie van het populaire PalmOS/Windows/Java spel
genaamd "Bejeweled" of "Diamond Mine". Het doel van het spel is een lijn
maken van 3 of meer juwelen, zowel verticaal als horizontaal door naast
elkaar liggende juwelen te wisselen. Het spel eindigt wanneer geen enkele
zet nog mogelijk is.

%prep
%setup

%build
%configure \
	--disable-setgid
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall scoredir=%{buildroot}/var/games
# The makefile installs the high score files in the wrong place.
%{__rm} -Rf %{buildroot}%{_var}/games
%{__install} -Dp -m0664 /dev/null %{buildroot}%{_var}/lib/games/gweled.easy.scores
%{__install} -Dp -m0664 /dev/null %{buildroot}%{_var}/lib/games/gweled.timed.scores

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING NEWS README
%attr(2551, root, games) %{_bindir}/gweled
%{_datadir}/applications/gweled.desktop
%{_datadir}/pixmaps/gweled.png
%{_datadir}/pixmaps/gweled
%{_datadir}/gweled
%defattr(-, root, games, 0755)
%config(noreplace) %{_var}/lib/games/gweled.easy.scores
%config(noreplace) %{_var}/lib/games/gweled.timed.scores


%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.7-1.2
- Rebuild for Fedora Core 5.

* Mon Oct 03 2005 Dries Verachtert <dries@ulyssis.org> - 0.7-1
- Updated to release 0.7.

* Sat Dec 04 2004 Dries Verachtert <dries@ulyssis.org> - 0.6-1
- Update to release 0.6.

* Sat Dec 04 2004 Richard Henderson <rth@twiddle.net> 0.5-2
- Fix installation directory and permissions for high score files.
- Install binary as setgid games.

* Wed Sep 01 2004 Dries Verachtert <dries@ulyssis.org> 0.5-1
- update to version 0.5.

* Wed Apr 21 2004 Dries Verachtert <dries@ulyssis.org> 0.4.1
- spec cleanup
- update to 0.4

* Mon Dec 1 2003 Dries Verachtert <dries@ulyssis.org> 0.3-1
- first packaging for Fedora Core 1
