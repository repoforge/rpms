# $Id$

# Authority: dries

Summary: Clone of 'bjeweled' or 'diamond mine'
Name: gweled
Version: 0.4
Release: 1
License: GPL
Group: Amusements/Games
URL: http://sebdelestaing.free.fr/gweled/

Source: http://sebdelestaing.free.fr/gweled/Release/gweled-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: libgnomeui-devel librsvg2-devel libcroco-devel

# Screenshot: http://sebdelestaing.free.fr/gweled/Images/gweled_screenshot.png

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
# export DESTDIR=$RPM_BUILD_ROOT
# make install
%makeinstall
%{__rm} -f ${RPM_BUILD_ROOT}/usr/share/pixmaps/gweled/tile_even.svg~
%{__rm} -f ${RPM_BUILD_ROOT}/usr/share/pixmaps/gweled/tile_odd.svg~

%files
%defattr(-,root,root,0755)
%doc README AUTHORS COPYING INSTALL NEWS 
%{_bindir}/gweled
%{_datadir}/applications/gweled.desktop
%{_datadir}/pixmaps/gweled.png
%{_datadir}/pixmaps/gweled
%{_var}/games/gweled.easy.scores
%{_datadir}/gweled

%changelog
* Wed Apr 21 2004 Dries Verachtert <dries@ulyssis.org> 0.4.1
- spec cleanup
- update to 0.4

* Mon Dec 1 2003 Dries Verachtert <dries@ulyssis.org> 0.3-1
- first packaging for Fedora Core 1
