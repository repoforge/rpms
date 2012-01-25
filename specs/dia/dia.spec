# $Id$
# Authority: dag

### EL4 ships with dia-0.94-5.7.2
### EL2 ships with dia-0.88.1-3.3
# ExcludeDist: el2 el4

%{?el6:%define _default_patch_fuzz 2}

Summary: Diagram drawing program
Name: dia
Version: 0.97.2
Release: 1%{?dist}
Epoch: 1
License: GPL
Group: Applications/Multimedia
URL: http://www.gnome.org/projects/dia/

Source0: http://ftp.gnome.org/pub/gnome/sources/dia/0.97/dia-%{version}.tar.xz
Source11: http://dia-installer.de/shapes/central_data_processing/central_data_processing.zip
Source12: http://dia-installer.de/shapes/chemistry_lab/chemistry_lab.zip
Source13: http://dia-installer.de/shapes/cmos/cmos.zip
Source14: http://dia-installer.de/shapes/digital/digital.zip
Source15: http://dia-installer.de/shapes/edpc/edpc.zip
Source16: http://dia-installer.de/shapes/electronic/electronic.zip
Source17: http://dia-installer.de/shapes/lst/lst.zip
Source18: http://dia-installer.de/shapes/optics/optics.zip
Source19: http://dia-installer.de/shapes/Racks/Racks.zip
Source20: http://dia-installer.de/shapes/renewable_energy/renewable_energy.zip
Source21: http://dia-installer.de/shapes/scenegraph/scenegraph.zip
Patch1: dia-0.92.2-dtd.patch
Patch2: dia-0.95-pre6-help.patch
Patch3: dia-0.94-fallbacktoxpmicons.patch
Patch4: dia-0.96-python-detect.patch
Patch5: dia-0.96.1-64bit.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: docbook-style-xsl
BuildRequires: gcc-c++
BuildRequires: gettext
BuildRequires: glib2-devel >= 2.6
BuildRequires: gtk2-devel >= 2.6
BuildRequires: intltool
BuildRequires: libart_lgpl-devel >= 2.3.10
BuildRequires: libEMF-devel
BuildRequires: libgnome-devel >= 2.0
BuildRequires: libgnomeui-devel >= 2.0
BuildRequires: libpng-devel
BuildRequires: libxml2-devel >= 2.3.9
BuildRequires: libxslt-devel
BuildRequires: pango-devel >= 1.1.5
BuildRequires: perl(XML::Parser)
BuildRequires: pkgconfig >= 0.9
BuildRequires: python-devel >= 2.2.1
BuildRequires: pygtk2-devel
BuildRequires: PyXML
%{?el4:BuildRequires: gcc-g77}

%description
The Dia drawing program is designed to be like the Microsoft(R) Visio
program. Dia can be used to draw different types of diagrams, and
includes support for UML static structure diagrams (class diagrams),
entity relationship modeling, and network diagrams. Dia can load and
save diagrams to a custom file format, can load and save in .xml
format, and can export to PostScript(TM).

%prep
%setup
#patch1 -p1 -b .dtd
#patch2 -p1 -b .help
%patch3 -p1 -b .fallbacktoxpmicons
#patch4 -p1 -b .py-detect
#patch5 -p1 -b .64bit

%{__perl} -pi.orig -e 's|\(W32::HDC\)user_data;|(W32::HDC)(guint64)user_data;|g' plug-ins/wmf/wmf.cpp

# Change linking from static libpython${PYTHON_VERSION}.a to dynamic libpython${PYTHON_VERSION}.so
%{__perl} -pi -e 's|libpython\${PYTHON_VERSION}.a|libpython\${PYTHON_VERSION}.so|' configure

%build
#autoreconf --force --install --symlink
%configure \
    --enable-db2html \
    --enable-gnome \
    --with-python
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

unzip -n -d %{buildroot}%{_datadir}/dia %{SOURCE11}
unzip -n -d %{buildroot}%{_datadir}/dia %{SOURCE12}
unzip -n -d %{buildroot}%{_datadir}/dia %{SOURCE13}
unzip -n -d %{buildroot}%{_datadir}/dia %{SOURCE14}
unzip -n -d %{buildroot}%{_datadir}/dia %{SOURCE15}
unzip -n -d %{buildroot}%{_datadir}/dia %{SOURCE16}
unzip -n -d %{buildroot}%{_datadir}/dia %{SOURCE17}
unzip -n -d %{buildroot}%{_datadir}/dia %{SOURCE18}
unzip -n -d %{buildroot}%{_datadir}/dia %{SOURCE19}
unzip -n -d %{buildroot}%{_datadir}/dia %{SOURCE20}
unzip -n -d %{buildroot}%{_datadir}/dia %{SOURCE21}

### Conflicts with Assorted/square.shape
%{__perl} -pi -e "s|Square|Square2|" %{buildroot}%{_datadir}/dia/shapes/chemistry_lab/square.shape

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING doc/ KNOWN_BUGS NEWS README THANKS TODO
%doc %{_datadir}/gnome/help/dia/
%doc %{_mandir}/man1/dia.1*
%doc %lang(fr) %{_mandir}/fr/man1/dia.1*
%{_bindir}/dia
%{_datadir}/applications/dia.desktop
%{_datadir}/dia/
%{_datadir}/icons/hicolor/*/apps/dia.png
%{_datadir}/icons/hicolor/scalable/apps/dia.svg
%{_datadir}/mime-info/dia.keys
%{_datadir}/mime-info/dia.mime
%{_datadir}/omf/dia/
#%{_datadir}/pixmaps/dia-diagram.png
#%{_datadir}/pixmaps/dia_gnome_icon.png
%{_docdir}/dia/
%{_libdir}/dia/

%changelog
* Fri Jan 20 2012 Dag Wieers <dag@wieers.com> - 0.97.2-1
- Updated to release 0.97.2.

* Tue Mar 22 2011 Yury V. Zaytsev <yury@shurup.com> - 0.97-2
- Fixed EL6 build (thanks to Bjarne Saltbaek!)

* Tue Jul 14 2009 Dag Wieers <dag@wieers.com> - 0.97-1
- Updated to release 0.97.

* Mon Jun 25 2007 Dag Wieers <dag@wieers.com> - 0.96.1-1
- Updated to release 0.96.1.

* Sat May 06 2006 Dries Verachtert <dries@ulyssis.org> - 0.95-1
- Updated to release 0.95.

* Wed Aug 25 2004 Dag Wieers <dag@wieers.com> - 0.94-1
- Updated to release 0.94.

* Wed May 05 2004 Dag Wieers <dag@wieers.com> - 0.93-1
- Updated to release 0.93.

* Sun Nov 09 2003 Dag Wieers <dag@wieers.com> - 0.92.2-1
- Fixed the "Couldn't find standard objects..." error. (Krzysztof Leszczynski)

* Sat Nov 01 2003 Dag Wieers <dag@wieers.com> - 0.92.2-0
- Updated to release 0.92.2.

* Sun Oct 26 2003 Dag Wieers <dag@wieers.com> - 0.92.1-0
- Updated to release 0.92.1.

* Mon Oct 20 2003 Dag Wieers <dag@wieers.com> - 0.92-0
- Updated to release 0.92.

* Wed Sep 24 2003 Dag Wieers <dag@wieers.com> - 0.92-0-pre3
- Updated to release 0.92-pre3.

* Tue May 06 2003 Dag Wieers <dag@wieers.com> - 0.91-0
- Updated to release 0.91.

* Thu Jan 3 2003 Dag Wieers <dag@wieers.com> - 0.90.20030131-0
- Initial package. (using DAR)
