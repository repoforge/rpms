# $Id$

# Authority: dries

Summary: unique multiplayer wargame with liquid armies
Name: liquidwar
Version: 5.6.2
Release: 2
License: GPL
Group: Amusements/Games
URL: http://www.ufoot.org/liquidwar/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://liquidwar.sunsite.dk/archive/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: allegro-devel, allegro, allegro-tools, gcc, tetex-latex, python, texinfo
Requires: allegro

# Screenshot: http://www.ufoot.org/images/liquidwarshot5s.jpg
# ScreenshotURL: http://www.ufoot.org/liquidwar/screenshots.php3

%description
Liquid War is a unique multiplayer wargame. You control an army of liquid
and have to try and eat your opponents. A single player mode is available,
but the game is definitely designed to be multiplayer, and has network
support. 

%prep
%{__rm} -rf "${RPM_BUILD_ROOT}"
%setup

%build
# little problem in Makefile.in
sed -i "s/ \$.DESKTOPDIR./ \$(DESTDIR)\/\$(DESKTOPDIR)/" Makefile.in
%configure
%{__make} %{?_smp_mflags}

%install
export DESTDIR=$RPM_BUILD_ROOT
%{__make} install
# fix the desktop file
sed -i 's/Exec=/Exec=\/usr\/games\//' ${RPM_BUILD_ROOT}/usr/share/applications/liquidwar.desktop

%package doc
Summary: documentation of the game LiquidWar
Group: Amusements/Games
Requires: liquidwar = %{version}-%{release}

%description doc
This package contains the documentation of LiquidWar in html, pdf, ps, txt
and info format.

%files
%defattr(-,root,root,0755)
%{_datadir}/games/liquidwar
%{_datadir}/pixmaps/liquidwar.xpm
/usr/games/liquidwar
/usr/games/liquidwar-mapgen
/usr/games/liquidwar-server
%{_datadir}/applications/liquidwar.desktop

%files doc
%defattr(-,root,root,0755)
%doc README
%{_datadir}/doc/liquidwar/COPYING
%{_datadir}/doc/liquidwar/README
%{_datadir}/doc/liquidwar/README.de
%{_datadir}/doc/liquidwar/README.fr
%{_datadir}/doc/liquidwar/README.dk
%{_datadir}/doc/liquidwar/html/*
%{_datadir}/doc/liquidwar/pdf/*
%{_datadir}/doc/liquidwar/ps/*
%{_datadir}/doc/liquidwar/txt/*
%{_datadir}/info/liquidwar.*
%{_datadir}/man/man6/liquidwar-mapgen.6.gz
%{_datadir}/man/man6/liquidwar-server.6.gz
%{_datadir}/man/man6/liquidwar.6.gz

%changelog
* Sun May 23 2004 Dries Verachtert <dries@ulyssis.org> 5.6.2-2
- fixed the ownership of the files in the doc package

* Thu Feb 26 2004 Dries Verachtert <dries@ulyssis.org> 5.6.2-1
- update to 5.6.2

* Tue Jan 13 2004 Dries Verachtert <dries@ulyssis.org> 5.6.1-1
- update to 5.6.1
- docs are moved to a separate package

* Sun Jan 11 2004 Dries Verachtert <dries@ulyssis.org> 5.6.0-3
- cleanup of spec file

* Fri Jan 2 2004 Dries Verachtert <dries@ulyssis.org> 5.6.0-2
- fixed the desktop icon

* Sat Dec 20 2003 Dries Verachtert <dries@ulyssis.org> 5.6.0-1
- first packaging for Fedora Core 1
