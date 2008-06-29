# $Id$
# Authority: dries
# Upstream: Russ Rew <russ$unidata,ucar,edu>

Summary: Libraries for the Unidata network Common Data Form (NetCDF)
Name: netcdf
Version: 3.6.3
Release: 1
License: BSD like
Group: Development/Libraries
URL: http://www.unidata.ucar.edu/software/netcdf/

Source: ftp://ftp.unidata.ucar.edu/pub/netcdf/netcdf-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, gcc-gfortran

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

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
%configure --enable-shared --with-pic
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
%doc INSTALL README
%doc %{_mandir}/man1/ncdump.1*
%doc %{_mandir}/man1/ncgen.1*
%doc %{_mandir}/man3/netcdf*.3*
%doc %{_infodir}/netcdf*.info*
%{_bindir}/ncdump
%{_bindir}/ncgen
%{_libdir}/libnetcdf.so.*
%{_libdir}/libnetcdff.so.*
%{_libdir}/libnetcdf_c++.so.*

%files devel
%{_includedir}/ncvalues.h
%{_includedir}/netcdf.*
%{_includedir}/typesizes.mod
%{_includedir}/netcdfcpp.h
%{_libdir}/libnetcdf.so
%{_libdir}/libnetcdff.so
%{_libdir}/libnetcdf_c++.so
%exclude %{_libdir}/*.a
%exclude %{_libdir}/*.la

%changelog
* Sun Jun 29 2008 Dries Verachtert <dries@ulyssis.org> - 3.6.3-1
- Updated to release 3.6.3.

* Wed Jul 25 2007 Dries Verachtert <dries@ulyssis.org> - 3.6.2-1
- Initial package, based on the the spec file from Mapping Hacks.
