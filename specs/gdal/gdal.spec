# $Id$
# Authority: dries
# Upstream: Frank Warmerdam <warmerdam$pobox,com>

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

Summary: Geospatial Data Abstraction Library
Name: gdal
Version: 1.4.4
Release: 2
License: MIT/X
Group: Applications/Engineering
URL: http://www.gdal.org/

Source: http://download.osgeo.org/gdal/gdal-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: curl-devel
BuildRequires: gcc-c++
BuildRequires: geos-devel
BuildRequires: giflib-devel
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: libtiff-devel
BuildRequires: netcdf-devel
BuildRequires: openssl-devel
BuildRequires: postgresql-devel
BuildRequires: python-devel

%description
The Geospatial Data Abstraction Library (GDAL) is a unifying C/C++ API for 
accessing raster geospatial data, and currently includes formats like 
GeoTIFF, Erdas Imagine, Arc/Info Binary, CEOS, DTED, GXF, and SDTS. It is 
intended to provide efficient access, suitable for use in viewer 
applications, and also attempts to preserve coordinate systems and 
metadata. Python, C, and C++ interfaces are available.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
%configure \
    --datadir="%{_datadir}/gdal" \
    --disable-static
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc NEWS 
%doc %{_mandir}/man1/gdal*.1*
%doc %{_mandir}/man1/ogr*.1*
%doc %{_mandir}/man1/pct2rgb.1*
%doc %{_mandir}/man1/rgb2pct.1*
%{_bindir}/gdal*
%{_bindir}/ogr*
%{_bindir}/gcps*
%{_bindir}/epsg_tr.py*
%{_bindir}/pct2rgb.py*
%{_bindir}/rgb2pct.py*
%{_datadir}/gdal/
%{_libdir}/libgdal.so.*
%{python_sitearch}/_gdalmodule.*
%{python_sitearch}/gdal*.py*
%{python_sitearch}/ogr.py*
%{python_sitearch}/osr.py*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/cpl_*.h
%{_includedir}/gdal*.h
%{_includedir}/ogr*.h
%{_includedir}/*dataset.h
%{_includedir}/gvgcpfit.h
%{_includedir}/thinplatespline.h
%{_libdir}/libgdal.so
%exclude %{_libdir}/*.la

%changelog
* Tue Jul 14 2009 Dag Wieers <dag@wieers.com> - 1.4.4-2
- Rebuild against geos-3.1.0.

* Mon Dec  3 2007 Dries Verachtert <dries@ulyssis.org> - 1.4.4-1
- Updated to release 1.4.4.

* Mon Nov  5 2007 Dries Verachtert <dries@ulyssis.org> - 1.4.3-1
- Updated to release 1.4.3.

* Thu Jul 26 2007 Dries Verachtert <dries@ulyssis.org> - 1.4.2-1
- Updated to release 1.4.2.

* Sun Jan 07 2007 Dries Verachtert <dries@ulyssis.org> - 1.4.0-1
- Updated to release 1.4.0.

* Sun May 07 2006 Dries Verachtert <dries@ulyssis.org> - 1.3.2-1
- Updated to release 1.3.2.

* Tue Dec 13 2005 Dries Verachtert <dries@ulyssis.org> - 1.3.1-1
- Initial package.
