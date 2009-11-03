# $Id$
# Authority: matthias


%{?fc4:%define _without_modxorg 1}
%{?el4:%define _without_modxorg 1}
%{?fc3:%define _without_modxorg 1}
%{?fc2:%define _without_modxorg 1}
%{?fc1:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}
%{?rh9:%define _without_modxorg 1}
%{?rh7:%define _without_modxorg 1}
%{?el2:%define _without_modxorg 1}
%{?rh6:%define _without_modxorg 1}
%{?yd3:%define _without_modxorg 1}

%{?fc1:%define _without_xorg 1}
%{?el3:%define _without_xorg 1}
%{?rh9:%define _without_xorg 1}
%{?rh8:%define _without_xorg 1}
%{?rh7:%define _without_xorg 1}
%{?el2:%define _without_xorg 1}
%{?rh6:%define _without_xorg 1}
%{?yd3:%define _without_xorg 1}

%define desktop_vendor rpmforge

Summary: The Open Racing Car Simulator
Name: torcs
Version: 1.2.4
Release: 1%{?dist}
License: GPL
Group: Amusements/Games
URL: http://torcs.org/
Source: http://dl.sf.net/torcs/TORCS-%{version}-src.tgz
Source1: http://dl.sf.net/torcs/TORCS-%{version}-src-robots-base.tgz
Source2: http://dl.sf.net/torcs/TORCS-%{version}-src-robots-berniw.tgz
Source3: http://dl.sf.net/torcs/TORCS-%{version}-src-robots-bt.tgz
Source4: http://dl.sf.net/torcs/TORCS-%{version}-src-robots-olethros.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: torcs-data, torcs-data-tracks-road, torcs-data-cars-extra
%if 0%{?_without_modxorg:1}
%{?_without_xorg:BuildRequires: XFree86-devel, XFree86-Mesa-libGLU}
%{!?_without_xorg:BuildRequires: xorg-x11-devel, xorg-x11-Mesa-libGLU}
%else
BuildRequires: mesa-libGLU-devel
%endif
BuildRequires: gcc-c++, freeglut-devel, plib-devel >= 1.8.3
BuildRequires: libpng-devel, libjpeg-devel, zlib-devel, openal-devel
BuildRequires: desktop-file-utils

%description
TORCS is a 3D racing cars simulator using OpenGL.  The goal is to have
programmed robots drivers racing against each others.  You can also drive
yourself with either a wheel, keyboard or mouse.


%package robots
Summary: The Open Racing Car Simulator robots
Group: Amusements/Games
Requires: %{name} = %{version}

%description robots
TORCS is a 3D racing cars simulator using OpenGL.  The goal is to have
programmed robots drivers racing against each others.  You can also drive
yourself with either a wheel, keyboard or mouse.

This package contains the robots who can race on their own.


%prep
%setup -a 1 -a 2 -a 3 -a 4
# Put the drivers back where they belong
%{__mv} %{name}-%{version}/src/drivers/* src/drivers/


%build
%configure
# Having %{?_smp_mflags} makes the build fail with 1.2.3
%{__make}


%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}

%{__install} -D -p -m 0644 Ticon.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

%{__cat} > %{name}.desktop << EOF
[Desktop Entry]
Name=TORCS
Comment=The Open Racing Car Simulator
Exec=torcs
Icon=%{name}.png
Terminal=false
Type=Application
Encoding=UTF-8
Categories=Application;Game;
EOF

%{__mkdir_p} %{buildroot}%{_datadir}/applications
desktop-file-install --vendor %{desktop_vendor} \
    --dir %{buildroot}%{_datadir}/applications \
    %{name}.desktop

# We need this for proper automatic stripping to take place (still in 1.2.3)
find %{buildroot}%{_libdir}/%{name}/ -name '*.so' | xargs %{__chmod} +x


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc CHANGELOG.html COPYING README.linux TODO.html
%{_bindir}/*
%dir %{_libdir}/%{name}/
%dir %{_libdir}/%{name}/drivers/
# From main
%{_libdir}/%{name}/drivers/human/
# From robots-base
%{_libdir}/%{name}/drivers/cylos1/
%{_libdir}/%{name}/drivers/damned/
%{_libdir}/%{name}/drivers/inferno/
%{_libdir}/%{name}/drivers/inferno2/
%{_libdir}/%{name}/drivers/lliaw/
%{_libdir}/%{name}/drivers/tanhoj/
%{_libdir}/%{name}/drivers/tita/
%{_libdir}/%{name}/lib/
%{_libdir}/%{name}/modules/
%{_libdir}/%{name}/setup_linux.sh
%{_libdir}/%{name}/*-bin
%{_datadir}/applications/%{desktop_vendor}-%{name}.desktop
%dir %{_datadir}/games/%{name}/
%{_datadir}/games/%{name}/config/
%dir %{_datadir}/games/%{name}/drivers/
# From main
%{_datadir}/games/%{name}/drivers/human/
# From robots-base
%{_datadir}/games/%{name}/drivers/cylos1/
%{_datadir}/games/%{name}/drivers/damned/
%{_datadir}/games/%{name}/drivers/inferno/
%{_datadir}/games/%{name}/drivers/inferno2/
%{_datadir}/games/%{name}/drivers/lliaw/
%{_datadir}/games/%{name}/drivers/tanhoj/
%{_datadir}/games/%{name}/drivers/tita/
%{_datadir}/games/%{name}/results/
%{_datadir}/games/%{name}/telemetry/
%{_datadir}/pixmaps/%{name}.png

%files robots
%defattr(-, root, root, 0755)
%dir %{_libdir}/%{name}/
%dir %{_libdir}/%{name}/drivers/
# From robots-berniw
%{_libdir}/%{name}/drivers/berniw/
%{_libdir}/%{name}/drivers/berniw2/
%{_libdir}/%{name}/drivers/berniw3/
%{_libdir}/%{name}/drivers/sparkle/
# From robots-bt
%{_libdir}/%{name}/drivers/bt/
# From robots-olethros
%{_libdir}/%{name}/drivers/olethros/
%dir %{_datadir}/games/%{name}/
%dir %{_datadir}/games/%{name}/drivers/
# From robots-berniw
%{_datadir}/games/%{name}/drivers/berniw/
%{_datadir}/games/%{name}/drivers/berniw2/
%{_datadir}/games/%{name}/drivers/berniw3/
%{_datadir}/games/%{name}/drivers/sparkle/
# From robots-bt
%{_datadir}/games/%{name}/drivers/bt/
# From robots-olethros
%{_datadir}/games/%{name}/drivers/olethros/


%changelog
* Wed Oct 12 2005 Matthias Saou <http://freshrpms.net/> 1.2.4-1
- Update to 1.2.4.
- Add torcs-data-tracks-road requirement directly to main torcs.
- Drop no longer needed TORCS-1.2.3-64bit.patch.
- Add openal-devel build dependency.

* Wed Aug  3 2005 Matthias Saou <http://freshrpms.net/> 1.2.3-5
- Move base robots from the sub-package to the main one to have the default
  quick race work. Hopefully this will change in later versions if the game
  checks which drivers are available before starting the default quick race.
- Add torcs-data-cars-extra requirement for the same reason as above : Without,
  none of the drivers of the default quick race have a car and the game exits.
- Add olethros robots.
- Change %%files section to explicitly list all robots since the above change
  moved many of them to the main package, not just "human".
- Renamed 64bit patch to TORCS-1.2.3-64bit.patch.

* Mon Feb  7 2005 Matthias Saou <http://freshrpms.net/> 1.2.3-1
- Update to 1.2.3.
- Remove billy and K1999 robot packages (no longer upstream).
- Update plib requirement from plib16 to plib (1.8.x).
- Remove %%{?_smp_mflags} as the build fails with -jN.

* Fri Nov  5 2004 Matthias Saou <http://freshrpms.net/> 1.2.2-4
- Add +x chmod'ing to .so files in order to get them stripped properly.

* Mon Oct 25 2004 Matthias Saou <http://freshrpms.net/> 1.2.2-3
- Remove un-needed /sbin/ldconfig calls.

* Fri Jul 23 2004 Matthias Saou <http://freshrpms.net/> 1.2.2-3
- Change build dependency of plib to compat package plib16-devel as
  rebuilding against 1.8 is not currently possible.
- Add patch for -fPIC to fix x86_64 build (hmm, doesn't work).

* Thu May 20 2004 Matthias Saou <http://freshrpms.net/> 1.2.2-2
- Rebuild for Fedora Core 2.
- Change XFree86 deps to xorg-x11 and glut to freeglut.

* Thu Feb 26 2004 Matthias Saou <http://freshrpms.net/> 1.2.2-1
- Update to 1.2.2.
- No longer require compat-libstdc++-devel for building.
- This version broke %%makeinstall, so switch to DESTDIR method.
- Re-enabled K1999 build, it works again.
- Added new robots : billy and bt.

* Tue Jan 13 2004 Matthias Saou <http://freshrpms.net/> 1.2.1-4
- Work around the XFree86 dependency problem by adding XFree86-Mesa-libGLU.

* Tue Dec  2 2003 Matthias Saou <http://freshrpms.net/> 1.2.1-3
- Rebuild for Fedora Core 1.
- Disabled build of the K1999 driver (strstream.h seems obsolete).

* Tue May 27 2003 Matthias Saou <http://freshrpms.net/>
- Added a torcs requirement to the robots package.

* Wed Apr 23 2003 Matthias Saou <http://freshrpms.net/>
- Initial RPM release.

