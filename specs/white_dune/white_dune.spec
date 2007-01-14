# $Id$
# Authority: dries
# Screenshot: http://www.csv.ica.uni-stuttgart.de/vrml/dune/_gfx/screen02.jpg
# ScreenshotURL: http://www.csv.ica.uni-stuttgart.de/vrml/dune/screen.html

%{?dist: %{expand: %%define %dist 1}}

%{?fc4:%define _without_modxorg 1}
%{?el4:%define _without_modxorg 1}
%{?fc3:%define _without_modxorg 1}
%{?fc2:%define _without_modxorg 1}
%{?fc1:%define _without_modxorg 1}

%{?el3:%define _without_freeglut 1}
%{?el3:%define _without_modxorg 1}

%{?rh9:%define _without_freeglut 1}
%{?rh9:%define _without_modxorg 1}

%{?rh7:%define _without_modxorg 1}
%{?el2:%define _without_modxorg 1}
%{?yd3:%define _without_modxorg 1}

%define real_version 0.29beta534

Summary: Graphical VRML97 editor and animation tool
Name: white_dune
Version: 0.29
Release: 0.beta534
License: GPL
Group: Applications/Multimedia
URL: http://www.csv.ica.uni-stuttgart.de/vrml/dune/

Source: http://www.csv.ica.uni-stuttgart.de/vrml/dune/%{name}-%{real_version}.tar.gz
#Patch: gcc.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc-c++, flex, byacc, zlib-devel
BuildRequires: libjpeg-devel, libpng-devel, ImageMagick
%{!?_without_modxorg:BuildRequires: libX11-devel, xorg-x11-server-Xvfb, xorg-x11-proto-devel, libXi-devel, libXmu-devel}
%{?_without_modxorg:BuildRequires: XFree86-devel, /usr/X11R6/bin/Xvfb}
%{!?_without_freeglut:BuildRequires: freeglut-devel}
%{?_without_freeglut:BuildRequires: glut-devel}
%{?fc4:BuildRequires: openmotif-devel}
%{?fc5:BuildRequires: openmotif-devel}
%{?fc6:BuildRequires: lesstif-devel}

%description
The white_dune program is a graphical VRML97 editor and animation tool.
VRML97 (Virtual Reality Modelling Language) is the ISO standard for
displaying 3D data over the web. It has support for animation, realtime
interaction and multimedia (image, movie, sound). VRML97 can be written
by popular programs like maya, catia, 3D Studio MAX, cinema4D and others.
Dune can read VRML97 files, display and let the user change the
scenegraph/fields.
Some documentation how to use dune is included.

%description -l nl
Het programma white_dune is een grafische VRML97 editor en een animatie
tool. VRML97 (Virtual Reality Modelling Language) is de ISO standaard om 3D
data voor te stellen op het internet. Het heeft ondersteuning voor
animaties, realtime interactie en multimedia (beelden, films en geluid).
Populaire programma's zoals maya, catia, 3D Studio MAX en cinema4D kunnen
VML97 bestanden genereren. Dune kan VRML97 bestanden lezen, tonen en laat de
gebruiker toe om eigenschappen te wijzigen.
Documentatie over het gebruik van dune is ook beschikbaar.

%prep
%setup -n %{name}-%{real_version}
#%patch -p1

%build
%configure \
  --with-optimization \
  --with-buginlesstif \
  --without-devil \
  --with-vrmlbrowser=mozilla \
  --with-helpurl="%{_datadir}/doc/white_dune-%{real_version}/docs/index.html" \
  --with-nurbscurveprotourl="%{_datadir}/misc/white_dune/NurbsCurvePROTO.wrl" \
  --with-nurbsgroupprotourl="%{_datadir}/misc/white_dune/NurbsGroupPROTO.wrl" \
  --with-nurbssurfaceprotourl="%{_datadir}/misc/white_dune/NurbsSurfacePROTO.wrl"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 bin/dune %{buildroot}%{_bindir}/dune
%{__install} -Dp -m0755 bin/dune4kids %{buildroot}%{_bindir}/dune4kids
%{__install} -Dp -m0644 man/dune.1 %{buildroot}%{_mandir}/man1/dune.1
%{__install} -Dp -m0644 desktop/kde/redhat/dune.desktop %{buildroot}%{_datadir}/applications/dune.desktop
%{__install} -Dp -m0644 desktop/kde/dune.png %{buildroot}%{_datadir}/icons/Bluecurve/48x48/apps/dune.png
%{__install} -Dp -m0644 desktop/kde/redhat/dune4kids.desktop %{buildroot}%{_datadir}/applications/dune4kids.desktop
%{__install} -Dp -m0644 desktop/kde/dune4kids.png %{buildroot}%{_datadir}/icons/Bluecurve/48x48/apps/dune4kids.png
%{__install} -Dp -m0755 bin/illegal2vrml %{buildroot}/usr/bin/illegal2vrml
%{__install} -Dp -m0644 man/illegal2vrml.1 %{buildroot}%{_mandir}/man1/illegal2vrml.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING README docs
%{_bindir}/dune
%{_bindir}/dune4kids
%{_bindir}/illegal2vrml
%{_mandir}/man1/*
%{_datadir}/applications/dune.desktop
%{_datadir}/applications/dune4kids.desktop
%{_datadir}/icons/*/48x48/apps/dune.png
%{_datadir}/icons/*/48x48/apps/dune4kids.png


%changelog
* Sun Jan 14 2007 Dries Verachtert <dries@ulyssis.org> - 0.29-0.beta534
- Updated to release 0.29-0.beta534.

* Wed Dec 20 2006 Dries Verachtert <dries@ulyssis.org> - 0.29-0.beta506
- Updated to release 0.29-0.beta506.

* Sat Nov 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.29-0.beta473
- Updated to release 0.29-0.beta473.

* Mon Aug 07 2006 Dries Verachtert <dries@ulyssis.org> - 0.29-0.beta403
- Updated to release 0.29-0.beta403.

* Mon May 29 2006 Dries Verachtert <dries@ulyssis.org> - 0.29-0.beta345
- Updated to release 0.29-0.beta345.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.29-0.beta255.2
- Rebuild for Fedora Core 5.

* Sat Jan 14 2006 Dries Verachtert <dries@ulyssis.org> 0.29-0.beta255
- Updated to release 0.29-0.beta255.

* Fri Dec 16 2005 Dries Verachtert <dries@ulyssis.org> 0.29-0.beta240
- Updated to release 0.29-0.beta240.

* Mon Nov 14 2005 Dries Verachtert <dries@ulyssis.org> 0.29-0.beta221
- Updated to release 0.29-0.beta221.

* Thu Oct 28 2004 Dries Verachtert <dries@ulyssis.org> 0.27beta230-1
- Update to 0.27beta230.

* Thu Feb 26 2004 Dries Verachtert <dries@ulyssis.org> 0.26pl5-2
- added an icon for the desktop file

* Mon Feb 23 2004 Dries Verachtert <dries@ulyssis.org> 0.26pl5-1
- update to 0.26pl5
- cleanup of spec file
- build requirements tested with mach

* Fri Jan 2 2004 Dries Verachtert <dries@ulyssis.org> 0.26pl2-2
- added a desktop file

* Sat Dec 20 2003 Dries Verachtert <dries@ulyssis.org> 0.26pl2-1
- first packaging for Fedora Core 1, based on source rpm found on download site of white_dune
