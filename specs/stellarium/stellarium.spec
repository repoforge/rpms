# $Id$
# Authority: dries
# Screenshot: http://stellarium.free.fr/gfx/pleiades.jpg
# ScreenshotURL: http://stellarium.free.fr/

# TODO: mail author about template problems with gcc 4
# also warnings about non virtual constructors in the classes in orbit.h

%{?dist: %{expand: %%define %dist 1}}

%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}

%{?fc1:%define _without_xorg 1}
%{?el3:%define _without_xorg 1}
%{?rh9:%define _without_xorg 1}
%{?rh8:%define _without_xorg 1}
%{?rh7:%define _without_xorg 1}
%{?el2:%define _without_xorg 1}
%{?rh6:%define _without_xorg 1}

Summary: Stellarium renders 3D photo-realistic skies in real time
Name: stellarium
Version: 0.7.1
Release: 1
License: GPL
Group: Amusements/Graphics
URL: http://stellarium.free.fr/

Source: http://dl.sf.net/stellarium/%{name}-%{version}.tar.gz
#Patch: gcc4-fix.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: dos2unix, gcc-c++, SDL-devel, libpng-devel
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}
%{?_without_xorg:BuildRequires: XFree86-devel}
%{!?_without_xorg:BuildRequires: xorg-x11-devel}

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
 
%prep
%setup
#%patch -p1
%{__cat} > stellarium.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Encoding=UTF-8
Name=Stellarium
Exec=/usr/bin/stellarium
Categories=Application;Graphics;X-Red-Hat-Extra;
EOF

%build
dos2unix configure
%{__chmod} +x configure
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
# {__make} DESTDIR=%{buildroot} install-strip
%{__mv} %{buildroot}/%{_bindir}/stellarium %{buildroot}/%{_bindir}/run-stellarium
%{__mkdir_p} %{buildroot}%{_datadir}/applications
%{__cat} > %{buildroot}%{_bindir}/stellarium <<EOF
#!/bin/bash
mkdir -p ~/.stellarium/%{version}
run-stellarium
EOF
%{__chmod} +x %{buildroot}%{_bindir}/stellarium

%if %{?_without_freedesktop:1}0
        %{__install} -Dp -m0644 stellarium.desktop %{buildroot}%{_datadir}/gnome/apps/Applications/stellarium.desktop
%else
        %{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
        desktop-file-install --vendor net                  \
                --add-category X-Red-Hat-Base              \
                --dir %{buildroot}%{_datadir}/applications \
                stellarium.desktop
%endif
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc README
%doc %{_mandir}/man?/*
%{_bindir}/run-stellarium
%{_bindir}/stellarium
%{_datadir}/stellarium
%{_datadir}/applications/*.desktop

%changelog
* Tue Sep 20 2005 Dries Verachtert <dries@ulyssis.org> - 0.7.1-1
- Update to release 0.7.1.

* Fri Sep 09 2005 Dries Verachtert <dries@ulyssis.org> - 0.7.0-1
- Update to release 0.7.0.

* Sun Jun 25 2005 Dries Verachtert <dries@ulyssis.org> - 0.6.2-1
- Update to release 0.6.2.

* Mon Oct 18 2004 Dries Verachtert <dries@ulyssis.org> 0.6.1-1
- Update to version 0.6.1.

* Fri Jul 30 2004 Dries Verachtert <dries@ulyssis.org> 0.6.0-1
- Update to version 0.6.0.

* Mon May 24 2004 Dries Verachtert <dries@ulyssis.org> 0.5.2-5
- renamed the original program to run-stellarium 
- renamed the wrapper to stellarium

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
