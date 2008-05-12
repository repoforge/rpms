# $Id$
# Authority: dries

Name: navit
Summary: Open Source car navigation system
Version: 0.0.4
Release: 1
License: GPL
Group: Applications/Productivity
URL: http://navit.sourceforge.net/

Source:  http://dl.sf.net/navit/navit-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: gcc
BuildRequires: glib2-devel
BuildRequires: gtk2-devel 
BuildRequires: pango-devel
BuildRequires: cairo-devel
BuildRequires: atk-devel
BuildRequires: freetype-devel
BuildRequires: zlib-devel
BuildRequires: python-devel

# FIXME: Workaround for: http://trac.navit-project.org/ticket/126
%define _libdir /usr/lib

%description
Navit is a car navigation system with routing engine.

It's modular design is capable of using vector maps of various formats for routing and rendering of the displayed map. It's even possible to use multiple maps at a time.

The GTK+ or SDL user interfaces are designed to work well with touch screen displays. Points of Interest of various formats are displayed on the map.

The current vehicle position is either read from gpsd or directly from NMEA GPS sensors.

The routing engine not only calculates an optimal route to your destination, but also generates directions and even speaks to you using speechd.

%prep
%setup 

%build
%{__rm} -rf %{buildroot}
%configure \
  --disable-samplemap \
%{__make}

%install
%{__make} install \
  DESTDIR="%{buildroot}"

%files
%defattr(-, root, root, -)
%doc %{_datadir}/navit/README
%{_datadir}/navit/navit.xml
%{_datadir}/navit/xpm/
%{_datadir}/locale/
%{_bindir}/navit
%{_bindir}/osm2navit
%{_libdir}/navit/data/libdata_binfile.la
%{_libdir}/navit/data/libdata_binfile.so
%{_libdir}/navit/data/libdata_binfile.so.0
%{_libdir}/navit/data/libdata_binfile.so.0.0.0
%{_libdir}/navit/data/libdata_mg.la
%{_libdir}/navit/data/libdata_mg.so
%{_libdir}/navit/data/libdata_mg.so.0
%{_libdir}/navit/data/libdata_mg.so.0.0.0
%{_libdir}/navit/data/libdata_poi_geodownload.la
%{_libdir}/navit/data/libdata_poi_geodownload.so
%{_libdir}/navit/data/libdata_poi_geodownload.so.0
%{_libdir}/navit/data/libdata_poi_geodownload.so.0.0.0
%{_libdir}/navit/data/libdata_textfile.la
%{_libdir}/navit/data/libdata_textfile.so
%{_libdir}/navit/data/libdata_textfile.so.0
%{_libdir}/navit/data/libdata_textfile.so.0.0.0
%{_libdir}/navit/graphics/libgraphics_gtk_drawing_area.la
%{_libdir}/navit/graphics/libgraphics_gtk_drawing_area.so
%{_libdir}/navit/graphics/libgraphics_gtk_drawing_area.so.0
%{_libdir}/navit/graphics/libgraphics_gtk_drawing_area.so.0.0.0
%{_libdir}/navit/graphics/libgraphics_null.la
%{_libdir}/navit/graphics/libgraphics_null.so
%{_libdir}/navit/graphics/libgraphics_null.so.0
%{_libdir}/navit/graphics/libgraphics_null.so.0.0.0
%{_libdir}/navit/gui/libgui_gtk.la
%{_libdir}/navit/gui/libgui_gtk.so
%{_libdir}/navit/gui/libgui_gtk.so.0
%{_libdir}/navit/gui/libgui_gtk.so.0.0.0
%{_libdir}/navit/osd/libosd_core.la
%{_libdir}/navit/osd/libosd_core.so
%{_libdir}/navit/osd/libosd_core.so.0
%{_libdir}/navit/osd/libosd_core.so.0.0.0
%{_libdir}/navit/speech/libspeech_cmdline.la
%{_libdir}/navit/speech/libspeech_cmdline.so
%{_libdir}/navit/speech/libspeech_cmdline.so.0
%{_libdir}/navit/speech/libspeech_cmdline.so.0.0.0
%{_libdir}/navit/vehicle/libvehicle_demo.la
%{_libdir}/navit/vehicle/libvehicle_demo.so
%{_libdir}/navit/vehicle/libvehicle_demo.so.0
%{_libdir}/navit/vehicle/libvehicle_demo.so.0.0.0
%{_libdir}/navit/vehicle/libvehicle_file.la
%{_libdir}/navit/vehicle/libvehicle_file.so
%{_libdir}/navit/vehicle/libvehicle_file.so.0
%{_libdir}/navit/vehicle/libvehicle_file.so.0.0.0
%{_libdir}/navit/binding/libbinding_python.la
%{_libdir}/navit/binding/libbinding_python.so
%{_libdir}/navit/binding/libbinding_python.so.0
%{_libdir}/navit/binding/libbinding_python.so.0.0.0


%changelog
*Mon May 12 2008 Christoph Maser <cmr@financial.com> - 0.0.4-1
- Initial package.
