# $Id$

# Authority: dries

Summary: A graphical VRML97 editor and animation tool.
Name: white_dune
Version: 0.26pl5
Release: 2
License: GPL
Group: Applications/Multimedia
URL: http://www.csv.ica.uni-stuttgart.de/vrml/dune/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://www.csv.ica.uni-stuttgart.de/vrml/dune/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
BuildRequires: gcc-c++, lesstif-devel, byacc, zlib-devel, libjpeg-devel, libpng-devel, XFree86, XFree86-Xvfb, flex, ImageMagick

#(d) primscreenshot: http://www.csv.ica.uni-stuttgart.de/vrml/dune/_gfx/screen02.jpg
#(d) screenshotsurl: http://www.csv.ica.uni-stuttgart.de/vrml/dune/screen.html

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
%setup -q

%build
%configure --with-optimization \
  --with-buginlesstif \
  --without-devil \
  --with-vrmlbrowser=mozilla \
  --with-helpurl="/usr/share/doc/white_dune-0.26pl2/docs/" \
  --with-nurbscurveprotourl="/usr/share/misc/white_dune/NurbsCurvePROTO.wrl" \
  --with-nurbsgroupprotourl="/usr/share/misc/white_dune/NurbsGroupPROTO.wrl" \
  --with-nurbssurfaceprotourl="/usr/share/misc/white_dune/NurbsSurfacePROTO.wrl"
%{__make} %{_smp_mflags} 
strip bin/dune
strip bin/dune4kids

%install
echo RPM_BUILD_ROOT is $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/usr/share/man/man1
mkdir -p $RPM_BUILD_ROOT/usr/share/misc/white_dune
install -s -m 755 bin/dune $RPM_BUILD_ROOT/usr/bin/dune
install -s -m 755 bin/dune4kids $RPM_BUILD_ROOT/usr/bin/dune4kids
install -m 644 man/dune.1 $RPM_BUILD_ROOT/usr/share/man/man1/dune.1
install -m 644 docs/vrml200x_nurbssurface/NurbsCurvePROTO.wrl $RPM_BUILD_ROOT/usr/share/misc/white_dune/NurbsCurvePROTO.wrl
install -m 644 docs/vrml200x_nurbssurface/NurbsGroupPROTO.wrl $RPM_BUILD_ROOT/usr/share/misc/white_dune/NurbsGroupPROTO.wrl
install -m 644 docs/vrml200x_nurbssurface/NurbsSurfacePROTO.wrl $RPM_BUILD_ROOT/usr/share/misc/white_dune/NurbsSurfacePROTO.wrl
mkdir -p $RPM_BUILD_ROOT/usr/share/applications
cat > $RPM_BUILD_ROOT/usr/share/applications/dune.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Encoding=UTF-8
Name=White Dune
Icon=dune
Exec=/usr/bin/dune
Categories=Application;Graphics;X-Red-Hat-Extra;
EOF
cat > $RPM_BUILD_ROOT/usr/share/applications/dune4kids.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Encoding=UTF-8
Icon=dune4kids
Name=White Dune 4 kids
Exec=/usr/bin/dune4kids
Categories=Application;Graphics;X-Red-Hat-Extra;
EOF
mkdir -p $RPM_BUILD_ROOT//usr/share/icons/hicolor/48x48/apps
/usr/bin/convert desktop/xfce/dune.xpm $RPM_BUILD_ROOT/usr/share/icons/hicolor/48x48/apps/dune.png
/usr/bin/convert desktop/xfce/dune4kids.xpm $RPM_BUILD_ROOT/usr/share/icons/hicolor/48x48/apps/dune4kids.png


%clean
# rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,0755)
%doc README COPYING docs
%{_bindir}/dune
%{_bindir}/dune4kids
%{_mandir}/man1/dune.1*
/usr/share/misc/white_dune/NurbsCurvePROTO.wrl
/usr/share/misc/white_dune/NurbsGroupPROTO.wrl
/usr/share/misc/white_dune/NurbsSurfacePROTO.wrl
/usr/share/applications/dune.desktop
/usr/share/applications/dune4kids.desktop
/usr/share/icons/hicolor/48x48/apps/dune.png
/usr/share/icons/hicolor/48x48/apps/dune4kids.png


%changelog
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
