# $Id$
# Authority: dries

Summary: Graphical VRML97 editor and animation tool
Name: white_dune
Version: 0.26pl5
Release: 2
License: GPL
Group: Applications/Multimedia
URL: http://www.csv.ica.uni-stuttgart.de/vrml/dune/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://www.csv.ica.uni-stuttgart.de/vrml/dune/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc-c++, lesstif-devel, flex, byacc, zlib-devel
BuildRequires: libjpeg-devel, libpng-devel, XFree86, XFree86-Xvfb, ImageMagick

# Screenshot: http://www.csv.ica.uni-stuttgart.de/vrml/dune/_gfx/screen02.jpg
# ScreenshotURL: http://www.csv.ica.uni-stuttgart.de/vrml/dune/screen.html

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
%configure \
  --with-optimization \
  --with-buginlesstif \
  --without-devil \
  --with-vrmlbrowser=mozilla \
  --with-helpurl="%{_datadir}/doc/white_dune-0.26pl2/docs/" \
  --with-nurbscurveprotourl="%{_datadir}/misc/white_dune/NurbsCurvePROTO.wrl" \
  --with-nurbsgroupprotourl="%{_datadir}/misc/white_dune/NurbsGroupPROTO.wrl" \
  --with-nurbssurfaceprotourl="%{_datadir}/misc/white_dune/NurbsSurfacePROTO.wrl"
%{__make} %{?_smp_mflags} 

%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}%{_bindir}
%{__mkdir_p} %{buildroot}%{_mandir}/man1
%{__mkdir_p} %{buildroot}%{_datadir}/misc/white_dune
%{__install} -m 0755 bin/dune %{buildroot}%{_bindir}/dune
%{__install} -m 0755 bin/dune4kids %{buildroot}%{_bindir}/dune4kids
%{__install} -m 0644 man/dune.1 %{buildroot}%{_mandir}/man1/dune.1
%{__install} -m 0644 docs/vrml200x_nurbssurface/NurbsCurvePROTO.wrl %{buildroot}%{_datadir}/misc/white_dune/NurbsCurvePROTO.wrl
%{__install} -m 0644 docs/vrml200x_nurbssurface/NurbsGroupPROTO.wrl %{buildroot}%{_datadir}/misc/white_dune/NurbsGroupPROTO.wrl
%{__install} -m 0644 docs/vrml200x_nurbssurface/NurbsSurfacePROTO.wrl %{buildroot}%{_datadir}/misc/white_dune/NurbsSurfacePROTO.wrl

%{__mkdir_p} %{buildroot}%{_datadir}/applications
%{__cat} > %{buildroot}%{_datadir}/applications/dune.desktop << EOF
[Desktop Entry]
Name=White Dune
Exec=dune
Icon=dune
Terminal=false
Type=Application
Categories=Application;Graphics;
Encoding=UTF-8
EOF
%{__cat} > %{buildroot}%{_datadir}/applications/dune4kids.desktop << EOF
[Desktop Entry]
Name=White Dune 4 kids
Exec=dune4kids
Icon=dune4kids
Terminal=false
Type=Application
Categories=Application;Graphics;
Encoding=UTF-8
EOF

%{__mkdir_p} %{buildroot}/%{_datadir}/icons/hicolor/48x48/apps
convert desktop/xfce/dune.xpm %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/dune.png
convert desktop/xfce/dune4kids.xpm %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/dune4kids.png


%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,0755)
%doc README COPYING docs
%{_bindir}/dune
%{_bindir}/dune4kids
%{_mandir}/man1/dune.1*
%{_datadir}/misc/white_dune/NurbsCurvePROTO.wrl
%{_datadir}/misc/white_dune/NurbsGroupPROTO.wrl
%{_datadir}/misc/white_dune/NurbsSurfacePROTO.wrl
%{_datadir}/applications/dune.desktop
%{_datadir}/applications/dune4kids.desktop
%{_datadir}/icons/hicolor/48x48/apps/dune.png
%{_datadir}/icons/hicolor/48x48/apps/dune4kids.png


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
