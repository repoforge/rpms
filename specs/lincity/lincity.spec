# $Id$

# Authority: dries

Summary: A city simulation game.
Summary(nl): Een stadsimulatie spel.
Name: lincity
Version: 1.12.0
Release: 3
License: GPL
Group: Amusements/Games
URL: http://lincity.sourceforge.net/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://dl.sf.net/lincity/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
#Requires:  
BuildRequires: gcc make

#(d) primscreenshot: http://lincity.sourceforge.net/screenshots/power.png
#(d) screenshotsurl: http://lincity.sourceforge.net/screenshots/index.html

%description
Lincity is a city simulation game. Build your city up from a primitive
village to an advanced civilization. Build a sustainable economy, or build
rockets to escape from a pollution ridden and resource starved planet.

%description -l nl
Lincity is een stad simulatie spel. Bouw een stad gaande van een primitief
dorp tot een zeer geavanceerde beschaving. Bouw een duurzame economie of
bouw raketten om de stervende planeet te verlaten.

%prep
%{__rm} -rf "${RPM_BUILD_ROOT}"
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
export DESTDIR=${RPM_BUILD_ROOT}
make install-strip
mkdir -p $RPM_BUILD_ROOT/usr/share/applications
cat > $RPM_BUILD_ROOT/usr/share/applications/lincity.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Encoding=UTF-8
Name=Lincity
Exec=/usr/bin/xlincity
Categories=Application;Game;ArcadeGame
EOF

%files
%defattr(-,root,root,0755)
%doc README CHANGES ABOUT-NLS COPYING COPYRIGHT TODO
%{_bindir}/xlincity
/usr/share/lincity
/usr/share/locale/*/LC_MESSAGES/lincity.mo
/usr/share/man/man6/lincity.6.gz
/usr/share/applications/lincity.desktop

%changelog
* Sun Jan 11 2004 Dries Verachtert <dries@ulyssis.org> 1.12.0-3
- cleanup of spec file

* Fri Jan 2 2004 Dries Verachtert <dries@ulyssis.org> 1.12.0-2
- added a desktop file

* Sat Dec 20 2003 Dries Verachtert <dries@ulyssis.org> 1.12.0-1
- first packaging for Fedora Core 1
