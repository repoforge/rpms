# $Id$

# Authority: dries

# NeedsCleanup

%define _name		gweled
%define _version	0.3
%define _release	1.dries

Summary: gnome clone of 'bjeweled' or 'diamond mine'
Summary(nl): gnome kloon van 'bjeweled' of 'diamond mine'

BuildRoot:	%{_tmppath}/build-%{_name}-%{_version}
Name:		%{_name}
Version:	%{_version}
Release:	%{_release}
License:	GPL
Group:		Applications/Games
URL: http://sebdelestaing.free.fr/gweled/
Source: http://sebdelestaing.free.fr/gweled/Release/gweled-0.3.tar.gz
BuildRequires: libgnomeui-devel librsvg2-devel libcroco-devel

#(d) primscreenshot: http://sebdelestaing.free.fr/gweled/Images/gweled_screenshot.png

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
%{__rm} -rf "${RPM_BUILD_ROOT}"
%setup

%build
%configure
make

%install
echo RPM_BUILD_ROOT is $RPM_BUILD_ROOT
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
