# $Id$

# Authority: dries
# Screenshot: http://sebdelestaing.free.fr/gweled/Images/gweled_screenshot.png

# NeedsCleanup

Summary: gnome clone of 'bjeweled' or 'diamond mine'
Summary(nl): gnome kloon van 'bjeweled' of 'diamond mine'
Name: gweled
Version: 0.3
Release: 1.dries
License: GPL
Group: Amusements/Games
URL: http://sebdelestaing.free.fr/gweled/

Source: http://sebdelestaing.free.fr/gweled/Release/gweled-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libgnomeui-devel librsvg2-devel libcroco-devel

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
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
export DESTDIR=$RPM_BUILD_ROOT
make install
%{__rm} -f ${RPM_BUILD_ROOT}/usr/share/pixmaps/gweled/tile_even.svg~
%{__rm} -f ${RPM_BUILD_ROOT}/usr/share/pixmaps/gweled/tile_odd.svg~

%files
%defattr(-,root,root)
%doc README AUTHORS COPYING INSTALL NEWS 
/usr/bin/gweled
/usr/share/applications/gweled.desktop
/usr/share/pixmaps/gweled.png
/usr/share/pixmaps/gweled
/var/games/gweled.easy.scores

%changelog
* Mon Dec 1 2003 Dries Verachtert <dries@ulyssis.org> 0.3-1.dries
- first packaging for Fedora Core 1
