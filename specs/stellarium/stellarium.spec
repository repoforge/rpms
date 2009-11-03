# $Id$
# Authority: dries
# Screenshot: http://stellarium.free.fr/gfx/pleiades.jpg
# ScreenshotURL: http://stellarium.free.fr/


%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}

%{?el4:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}
%{?el2:%define _without_modxorg 1}
%{?fc4:%define _without_modxorg 1}
%{?fc3:%define _without_modxorg 1}
%{?fc2:%define _without_modxorg 1}
%{?fc1:%define _without_modxorg 1}

Summary: Stellarium renders 3D photo-realistic skies in real time
Name: stellarium
Version: 0.10.2
Release: 1%{?dist}
License: GPL
Group: Amusements/Graphics
URL: http://stellarium.free.fr/

Source: http://dl.sf.net/stellarium/%{name}-%{version}.tar.gz
#Patch: gcc.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: dos2unix, gcc-c++, SDL-devel, libpng-devel, cmake
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}
%{!?_without_modxorg:BuildRequires: mesa-libGL-devel, mesa-libGLU-devel, freetype-devel}

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
#patch -p1
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
cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} .
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%{__mkdir_p} %{buildroot}%{_datadir}/applications

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
%find_lang %{name}-skycultures
%{__cat} %{name}-skycultures.lang >> %{name}.lang

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc README
%doc %{_mandir}/man1/stellarium.1*
%{_bindir}/stellarium
%{_datadir}/stellarium
%{_datadir}/applications/*.desktop

%changelog
* Thu Mar 12 2009 Dries Verachtert <dries@ulyssis.org> - 0.10.2-1
- Updated to release 0.10.2.

* Fri Jan  1 2008 Dries Verachtert <dries@ulyssis.org> - 0.9.1-1
- Updated to release 0.9.1.

* Sat May 06 2006 Dries Verachtert <dries@ulyssis.org> - 0.8.0-1
- Updated to release 0.8.0.

* Thu Mar 30 2006 Dries Verachtert <dries@ulyssis.org> - 0.7.1-2
- Simplify buildequirements: SDL-devel already requires xorg-x11-devel/XFree86-devel

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
