# $Id$
# Authority: dries
# Screenshot: http://www.ufoot.org/images/liquidwarshot5s.jpg
# ScreenshotURL: http://www.ufoot.org/liquidwar/screenshots.php3

Summary: Multiplayer wargame with liquid armies
Name: liquidwar
Version: 5.6.3
Release: 1.2%{?dist}
License: GPL
Group: Amusements/Games
URL: http://www.ufoot.org/liquidwar/

Source: http://www.ufoot.org/archive/liquidwar-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: allegro-devel, tetex-latex, python, texinfo
Requires: allegro

%description
Liquid War is a unique multiplayer wargame. You control an army of liquid
and have to try and eat your opponents. A single player mode is available,
but the game is definitely designed to be multiplayer, and has network
support.

%package doc
Summary: Documentation for the LiquidWar game
Group: Documentation
Requires: liquidwar = %{version}

%description doc
This package contains the documentation of LiquidWar in html, pdf, ps, txt
and info format.

%prep
%setup

%build
# little problem in Makefile.in
%{__perl} -pi.orig -e "s|\$.DESKTOPDIR.|\$\(DESTDIR\)\$\(DESKTOPDIR\)|g" Makefile.in
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}
## fix the desktop file
#%{__perl} -pi.orig -e 's|Exec=|Exec=%{_prefix}/games/|' \
#    %{buildroot}%{_datadir}/applications/liquidwar.desktop
%{__mv} %{buildroot}%{_datadir}/doc/liquidwar liquidwardocs

%clean
%{__rm} -rf %{buildroot}

%post doc
/sbin/install-info %{_infodir}/liquidwar.info.gz %{_datadir}/info/dir

%preun doc
/sbin/install-info %{_infodir}/liquidwar.info.gz --delete %{_datadir}/info/dir

%files
%defattr(-, root, root, 0755)
%doc COPYING
%{_bindir}/liquidwar
%{_bindir}/liquidwar-mapgen
%{_bindir}/liquidwar-server
%{_prefix}/games/liquidwar
%{_prefix}/games/liquidwar-mapgen
%{_prefix}/games/liquidwar-server
%{_datadir}/games/liquidwar/
%{_datadir}/pixmaps/liquidwar.xpm
%{_datadir}/applications/liquidwar.desktop
#%exclude %{_datadir}/applications/liquidwar.desktop.orig

%files doc
%defattr(-, root, root, 0755)
%doc liquidwardocs/*
%{_infodir}/liquidwar.*
%{_mandir}/man6/liquidwar-mapgen.6.gz
%{_mandir}/man6/liquidwar-server.6.gz
%{_mandir}/man6/liquidwar.6.gz

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 5.6.3-1.2
- Rebuild for Fedora Core 5.

* Tue Nov 29 2005 Dries Verachtert <dries@ulyssis.org> 5.6.3-1
- Updated to release 5.6.3.

* Fri Oct 29 2004 Dries Verachtert <dries@ulyssis.org> 5.6.2-3
- Some fixes in the spec file

* Fri Jul 16 2004 Matthias Saou <http://freshrpms.net/> 5.6.2-2
- Major spec cleanup, not sure why the docs are apart, though.
- Can't build... where is allegro??

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
