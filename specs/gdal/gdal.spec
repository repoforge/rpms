# $Id$
# Authority: shuff
# Upstream: Frank Warmerdam <warmerdam$pobox,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)
%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

Summary: Geospatial Data Abstraction Library
Name: gdal
Version: 1.8.1
Release: 1%{?dist}
License: MIT/X
Group: Applications/Engineering
URL: http://www.gdal.org/

Source: http://download.osgeo.org/gdal/gdal-%{version}.tar.gz
Patch0: gdal-1.8.0_perl-vendordir.patch
Patch1: gdal-1.8.0_python-distutils.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: curl-devel
BuildRequires: findutils
BuildRequires: gcc-c++
BuildRequires: expat-devel >= 1.95.0
BuildRequires: geos-devel >= 2.2.0
BuildRequires: giflib-devel
BuildRequires: hdf4-devel
BuildRequires: hdf5-devel
BuildRequires: jasper-devel
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: libtiff-devel
BuildRequires: mysql-devel
BuildRequires: netcdf-devel
BuildRequires: openjpeg-devel
BuildRequires: openssl-devel
BuildRequires: perl
BuildRequires: php-devel
BuildRequires: postgresql-devel
# BuildRequires: python-devel
# BuildRequires: ruby
# BuildRequires: ruby-devel
BuildRequires: swig
BuildRequires: xerces-c-devel

%description
The Geospatial Data Abstraction Library (GDAL) is a unifying C/C++ API for 
accessing raster geospatial data, and currently includes formats like 
GeoTIFF, Erdas Imagine, Arc/Info Binary, CEOS, DTED, GXF, and SDTS. It is 
intended to provide efficient access, suitable for use in viewer 
applications, and also attempts to preserve coordinate systems and 
metadata. Perl, C, and C++ interfaces are available.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%package -n perl-%{name}
Summary: Perl support for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: perl
Provides: perl(Geo::GDAL) = %{version}-%{release}
Provides: perl(Geo::GDAL::Const) = %{version}-%{release}
Provides: perl(Geo::OGR) = %{version}-%{release}
Provides: perl(Geo::OSR) = %{version}-%{release}

%description -n perl-%{name}
This package provides Perl bindings for %{name}.

# %package -n php-%{name}
# Summary: PHP support for %{name}.
# Group: Development/Libraries
# Requires: %{name} = %{version}-%{release}
# Requires: php
# 
# %description -n php-%{name}
# This package provides PHP bindings for %{name}.

# %package -n python-%{name}
# Summary: Python support for %{name}.
# Group: Development/Libraries
# Requires: %{name} = %{version}-%{release}
# Requires: python
# 
# %description -n python-%{name}
# This package provides Python bindings for %{name}.

# %package -n ruby-%{name}
# Summary: Ruby support for %{name}.
# Group: Development/Libraries
# Requires: %{name} = %{version}-%{release}
# Requires: ruby
# 
# %description -n ruby-%{name}
# This package provides Ruby bindings for %{name}.

%prep
%setup
%patch0 -p1
%patch1 -p1

%build
PY_HAVE_SETUPTOOLS=0 %configure \
    --datadir="%{_datadir}/gdal" \
    --disable-static \
    --with-mysql \
    --with-perl \
    --with-php
    # --with-python
    # --with-ruby

%{__make}
%{__make} docs

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%{__make} install-docs DESTDIR="%{buildroot}"

# put the docs in the right place
%{__mv} %{buildroot}%{_usr}/doc docs-to-install

# no .packlist files in the Perl module
find %{buildroot}%{perl_vendorarch} -name '.packlist' | xargs %{__rm} -f

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc NEWS docs-to-install/*
%{_bindir}/*
%{_datadir}/gdal/
%{_libdir}/libgdal.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/*.h
%{_libdir}/libgdal.so
%exclude %{_libdir}/*.la

%files -n perl-%{name}
%defattr(-, root, root, 0755)
%{perl_vendorarch}/Geo/*
%{perl_vendorarch}/auto/Geo/*
%exclude %{_libdir}/perl*/perllocal.pod

# %files -n php-%{name}
# %defattr(-, root, root, 0755)

# %files -n python-%{name}
# %defattr(-, root, root, 0755)

# %files -n ruby-%{name}
# %defattr(-, root, root, 0755)


%changelog
* Tue Aug 02 2011 Steve Huff <shuff@vecna.org> - 1.8.1-1
- Updated to release 1.8.1.
- Added HDF4 and HDF5 dependencies.

* Mon May 02 2011 Steve Huff <shuff@vecna.org> - 1.8.0-1
- Updated to release 1.8.0.
- Added SWIG bindings for Perl.

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
