# $Id$
# Authority: dries
# Upstream: Russ Rew <russ$unidata,ucar,edu>

Summary: Libraries for the Unidata network Common Data Form (NetCDF)
Name: netcdf
Version: 4.1.2
Release: 1%{?dist}
License: BSD-like
Group: Development/Libraries
URL: http://www.unidata.ucar.edu/software/netcdf/

Source: ftp://ftp.unidata.ucar.edu/pub/netcdf/netcdf-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: binutils
BuildRequires: gcc-c++
BuildRequires: gcc-gfortran
BuildRequires: libcurl-devel
BuildRequires: make

%description
The Unidata network Common Data Form (netCDF) is an interface for
scientific data access and a freely-distributed software library that
provides an implementation of the interface.  The netCDF library also
defines a machine-independent format for representing scientific data.
Together, the interface, library, and format support the creation,
access, and sharing of scientific data.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build   
# need to package HDF5 library before we can enable netcdf-4 features
%configure \
    --disable-netcdf-4 \
    --enable-shared \
    --with-pic \
    --with-udunits
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%{__rm} -f %{buildroot}%{_infodir}/dir

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc INSTALL README
%doc %{_mandir}/man?/*
%doc %{_infodir}/*.gz
%{_bindir}/nccopy
%{_bindir}/ncdump
%{_bindir}/ncgen
%{_bindir}/ncgen3
%{_bindir}/udunits2
%{_libdir}/libnetcdf.so.*
%{_libdir}/libnetcdff.so.*
%{_libdir}/libnetcdf_c++.so.*
%{_libdir}/libudunits2.so.*
%{_datadir}/udunits

%files devel
%{_bindir}/nc-config
%{_includedir}/converter.h
%{_includedir}/ncvalues.h
%{_includedir}/netcdf.*
%{_includedir}/typesizes.mod
%{_includedir}/netcdfcpp.h
%{_includedir}/udunits.h
%{_includedir}/udunits2.h
%{_libdir}/libnetcdf.so
%{_libdir}/libnetcdff.so
%{_libdir}/libnetcdf_c++.so
%{_libdir}/libudunits2.so
%{_libdir}/pkgconfig/*.pc
%exclude %{_libdir}/*.a
%exclude %{_libdir}/*.la

%changelog
* Mon May 02 2011 Steve Huff <shuff@vecna.org> - 4.1.2-1
- Updated to release 4.1.2.
- Enabled building of udunits.
- Disabled some netCDF-4 features due to lack of packaged HDF5 library.

* Sun Jun 29 2008 Dries Verachtert <dries@ulyssis.org> - 3.6.3-1
- Updated to release 3.6.3.

* Wed Jul 25 2007 Dries Verachtert <dries@ulyssis.org> - 3.6.2-1
- Initial package, based on the the spec file from Mapping Hacks.
