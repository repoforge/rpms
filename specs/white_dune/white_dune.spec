# $Id$
# Authority: dries
# Screenshot: http://www.csv.ica.uni-stuttgart.de/vrml/dune/_gfx/screen02.jpg
# ScreenshotURL: http://www.csv.ica.uni-stuttgart.de/vrml/dune/screen.html

%{?dtag: %{expand: %%define %dtag 1}}

%{?fc4:%define _without_modxorg 1}
%{?el4:%define _without_modxorg 1}
%{?fc3:%define _without_modxorg 1}
%{?fc2:%define _without_modxorg 1}
%{?fc1:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}
%{?rh9:%define _without_modxorg 1}
%{?rh7:%define _without_modxorg 1}
%{?el2:%define _without_modxorg 1}
%{?yd3:%define _without_modxorg 1}

%{?el3:%define _without_freeglut 1}
%{?rh9:%define _without_freeglut 1}
%{?rh7:%define _without_freeglut 1}
%{?el2:%define _without_freeglut 1}


%{!?dtag:%define _with_lesstif 1}
%{?el5:%define _with_openmotif 1}
%{?fc6:%define _with_lesstif 1}
%{?fc5:%define _with_openmotif 1}
%{?fc4:%define _with_openmotif 1}
%{?fc3:%define _with_lesstif 1}
%{?el4:%define _with_openmotif 1}
%{?el3:%define _with_openmotif 1}
%{?el2:%define _with_lesstif 1}

%define real_version 0.29beta851

Summary: Graphical VRML97 editor and animation tool
Name: white_dune
Version: 0.29
Release: 0.beta851
License: GPL
Group: Applications/Multimedia
URL: http://www.csv.ica.uni-stuttgart.de/vrml/dune/

Source: http://www.csv.ica.uni-stuttgart.de/vrml/dune/white_dune-%{real_version}.tar.gz
#Patch: gcc.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc-c++, flex, byacc, zlib-devel, bison
BuildRequires: libjpeg-devel, libpng-devel, ImageMagick
%{!?_without_modxorg:BuildRequires: libX11-devel, xorg-x11-server-Xvfb, xorg-x11-proto-devel, libXi-devel, libXmu-devel}
%{?_without_modxorg:BuildRequires: XFree86-devel, /usr/X11R6/bin/Xvfb}
%{!?_without_freeglut:BuildRequires: freeglut-devel}
%{?_without_freeglut:BuildRequires: glut-devel}
%{?_with_lesstif:BuildRequires: lesstif-devel}
%{?_with_openmotif:BuildRequires: openmotif-devel}

%description
The white_dune program is a graphical VRML97 editor and animation tool.
VRML97 (Virtual Reality Modelling Language) is the ISO standard for
displaying 3D data over the web. It has support for animation, realtime
interaction and multimedia (image, movie, sound). VRML97 can be written
by popular programs like maya, catia, 3D Studio MAX, cinema4D and others.
Dune can read VRML97 files, display and let the user change the
scenegraph/fields.
Some documentation how to use dune is included.

%prep
%setup -n %{name}-%{real_version}
#%patch -p1

%build
%configure \
  --with-optimization \
  --with-buginlesstif \
  --without-devil \
  --with-vrmlbrowser="mozilla" \
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
%doc %{_mandir}/man1/dune.1*
%doc %{_mandir}/man1/illegal2vrml.1*
%{_bindir}/dune
%{_bindir}/dune4kids
%{_bindir}/illegal2vrml
%{_datadir}/applications/dune.desktop
%{_datadir}/applications/dune4kids.desktop
%{_datadir}/icons/Bluecurve/48x48/apps/dune.png
%{_datadir}/icons/Bluecurve/48x48/apps/dune4kids.png

%changelog
* Tue Feb  5 2008 Dries Verachtert <dries@ulyssis.org> - 0.29-0.beta851
- Updated to release 0.29-0.beta851.

* Sun Jan 27 2008 Dries Verachtert <dries@ulyssis.org> - 0.29-0.beta834
- Updated to release 0.29-0.beta834.

* Sun Jan  6 2008 Dries Verachtert <dries@ulyssis.org> - 0.29-0.beta796
- Updated to release 0.29-0.beta796.

* Sat Dec  1 2007 Dries Verachtert <dries@ulyssis.org> - 0.29-0.beta777
- Updated to release 0.29-0.beta777.

* Fri Nov 30 2007 Dries Verachtert <dries@ulyssis.org> - 0.29-0.beta775
- Updated to release 0.29-0.beta775.

* Tue Nov 20 2007 Dries Verachtert <dries@ulyssis.org> - 0.29-0.beta762
- Updated to release 0.29-0.beta762.

* Tue Nov  6 2007 Dries Verachtert <dries@ulyssis.org> - 0.29-0.beta745
- Updated to release 0.29-0.beta745.

* Tue Oct 16 2007 Dries Verachtert <dries@ulyssis.org> - 0.29-0.beta721
- Updated to release 0.29-0.beta721.

* Mon Oct  1 2007 Dries Verachtert <dries@ulyssis.org> - 0.29-0.beta698
- Updated to release 0.29-0.beta698.

* Sun Sep 16 2007 Dries Verachtert <dries@ulyssis.org> - 0.29-0.beta683
- Updated to release 0.29-0.beta683.

* Mon Sep 10 2007 Dries Verachtert <dries@ulyssis.org> - 0.29-0.beta678
- Updated to release 0.29-0.beta678.

* Mon Sep  3 2007 Dries Verachtert <dries@ulyssis.org> - 0.29-0.beta676
- Updated to release 0.29-0.beta676.

* Mon Aug 20 2007 Dries Verachtert <dries@ulyssis.org> - 0.29-0.beta667
- Updated to release 0.29-0.beta667.

* Mon Jul 23 2007 Dries Verachtert <dries@ulyssis.org> - 0.29-0.beta657
- Updated to release 0.29-0.beta657.

* Sun Jul 08 2007 Dries Verachtert <dries@ulyssis.org> - 0.29-0.beta651
- Updated to release 0.29-0.beta651.

* Fri Jun 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.29-0.beta647
- Updated to release 0.29-0.beta647.

* Sun Jun 17 2007 Dries Verachtert <dries@ulyssis.org> - 0.29-0.beta637
- Updated to release 0.29-0.beta637.

* Wed May 30 2007 Dries Verachtert <dries@ulyssis.org> - 0.29-0.beta634
- Updated to release 0.29-0.beta634.

* Thu May 17 2007 Dries Verachtert <dries@ulyssis.org> - 0.29-0.beta628
- Updated to release 0.29-0.beta628.

* Tue May 08 2007 Dries Verachtert <dries@ulyssis.org> - 0.29-0.beta622
- Updated to release 0.29-0.beta622.

* Mon Apr 16 2007 Dries Verachtert <dries@ulyssis.org> - 0.29-0.beta607
- Updated to release 0.29-0.beta607.

* Sun Apr 01 2007 Dries Verachtert <dries@ulyssis.org> - 0.29-0.beta596
- Updated to release 0.29-0.beta596.

* Mon Mar 19 2007 Dries Verachtert <dries@ulyssis.org> - 0.29-0.beta586
- Updated to release 0.29-0.beta586.

* Mon Mar 12 2007 Dries Verachtert <dries@ulyssis.org> - 0.29-0.beta581
- Updated to release 0.29-0.beta581.

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
