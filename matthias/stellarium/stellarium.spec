# $Id: stellarium.spec,v 1.3 2004/02/27 17:08:22 driesve Exp $

# Authority: dries

Summary: Stellarium renders 3D photo-realistic skies in real time.
Summary(nl): Stellarium toont 3D fotorealistische hemels in real time.
Name: stellarium
Version: 0.5.2
Release: 4
License: GPL
Group: Amusements/Graphics
URL: http://stellarium.free.fr/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://dl.sf.net/stellarium/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
BuildRequires: dos2unix, gcc-c++, XFree86-devel, SDL-devel

#(d) primscreenshot: http://stellarium.free.fr/gfx/pleiades.jpg
#(d) screenshotsurl: http://stellarium.free.fr/

%description
Stellarium renders 3D photo-realistic skies in real time. Most important
features:
* Over 120000 stars from the Hipparcos Catalogue with name and infos for the
brightest ones.
* Planets in real time, with a powerfull zoom mode to see them like in a
telescope.
* Drawing of the 88 constellations with their names.
* Drawing of more than 40 messiers objects (Orion, M31 etc..).
* Photorealistic Milky Way.
* Ground, fog, and landscape.
* Star twinkling.
* Grids in Equatorial and Azimuthal coordinates.
* Time control (real time and accelered time modes).
* Graphical menu for simple utilisation.
* Clikable stars, planets and nebulas with informations.
* Ecliptic and celestrial equator lines.
* Smooth real time navigation.
* Windowed and fullscreen modes.
 
%description -l nl
Stellarium toont 3D fotorealistische hemels in real time. De belangrijkste
features zijn:
* Meer dan 120000 sterren van de Hipparcos catalogus met naam en info voor
de helderste sterren.
* Planeten in real time, met een zoom mode zodat u ze ziet zoals met een
telescoop
* Tonen van de 88 constellaties met hun namen
* Tonen van meer dan 40 'messiers' objecten (Orion, M32, enz)
* Fotorealistische melkweg
* Grond, mist en landschap
* Schitteren van sterren
* Een grid met de coordinaten
* Een eenvoudig grafisch menu
* Informatie met een muisklik bij sterren, planeten en nebula's
* Ecliptische en 'celestrial' equator lijnen
* vloeiende real time navigatie
* fullscreen en venster modus

%prep
%{__rm} -rf "${RPM_BUILD_ROOT}"
%setup

%build
dos2unix configure
chmod +x configure
%configure
%{__make} %{?_smp_mflags}

%install
%{__make} DESTDIR=$RPM_BUILD_ROOT install-strip
mkdir -p $RPM_BUILD_ROOT/usr/share/applications
cat > $RPM_BUILD_ROOT/usr/share/applications/stellarium.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Encoding=UTF-8
Name=Stellarium
Exec=/usr/bin/stellarium-wrapper
Categories=Application;Graphics;X-Red-Hat-Extra;
EOF
cat > $RPM_BUILD_ROOT/usr/bin/stellarium-wrapper <<EOF
#!/bin/bash
mkdir -p ~/.stellarium/0.5.2
stellarium
EOF
chmod +x $RPM_BUILD_ROOT/usr/bin/stellarium-wrapper

%files
%defattr(-,root,root,0755)
%doc README
%{_bindir}/stellarium
%{_bindir}/stellarium-wrapper
/usr/share/stellarium
/usr/share/applications/stellarium.desktop

%changelog
* Tue Feb 24 2004 Dries Verachtert <dries@ulyssis.org> 0.5.2-4
- fixed the BuildRequires
- fixed the location of the stellarium icon
- added a small wrapper which creates a ~/stellarium/0.5.2 directory
  bug reported by Stefan Ekman, thanks Stefan!

* Sun Jan 11 2004 Dries Verachtert <dries@ulyssis.org> 0.5.2-3
- cleanup of spec file

* Fri Jan 2 2004 Dries Verachtert <dries@ulyssis.org> 0.5.2-2
- added a desktop file

* Sat Dec 20 2003 Dries Verachtert <dries@ulyssis.org> 0.5.2-1
- first packaging for Fedora Core 1
