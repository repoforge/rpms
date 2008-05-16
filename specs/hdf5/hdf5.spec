# $Id$
# Authority: dries

Summary: Manages extremely large and complex data collections
Name: hdf5
Version: 1.8.0
Release: 1
License: Distributable
Group: Development/Libraries
URL: http://hdfgroup.org/HDF5/

Source: ftp://ftp.hdfgroup.org/HDF5/current/src/hdf5-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, gcc-gfortran

%description
HDF5 is a unique technology suite that makes possible the management of 
extremely large and complex data collections.
The HDF5 technology suite includes:
* A versatile data model that can represent very complex data objects and 
a wide variety of metadata.
* A completely portable file format with no limit on the number or size of 
data objects in the collection.
* A software library that runs on a range of computational platforms, from 
laptops to massively parallel systems, and implements a high-level API with 
C, C++, Fortran 90, and Java interfaces.
* A rich set of integrated performance features that allow for access time 
and storage space optimizations.
* Tools and applications for managing, manipulating, viewing, and analyzing 
the data in the collection.

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
%{__perl} -pi.orig -e 's|INSTALL\) h5cc \$\(bindir\)/\$\(H5CC_NAME\)|INSTALL) h5cc %{buildroot}\$(bindir)/\$(H5CC_NAME)|g;' tools/misc/Makefile*

%build
%configure
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
%doc COPYING *.txt
%{_bindir}/gif2h5
%{_bindir}/h52gif
%{_bindir}/h52gifgentst
%{_bindir}/h5copy
%{_bindir}/h5debug
%{_bindir}/h5diff
%{_bindir}/h5dump
%{_bindir}/h5import
%{_bindir}/h5jam
%{_bindir}/h5ls
%{_bindir}/h5mkgrp
%{_bindir}/h5redeploy
%{_bindir}/h5repack
%{_bindir}/h5repart
%{_bindir}/h5stat
%{_bindir}/h5unjam
%{_bindir}/h5cc
%{_libdir}/libhdf5*.so.*
%{_libdir}/libhdf5.settings

%files devel
%{_includedir}/H5*.h
%{_includedir}/hdf5*.h
%{_libdir}/libhdf5*.so
%exclude %{_libdir}/libhdf5*.a
%exclude %{_libdir}/libhdf5*.la

%changelog
* Thu May 15 2008 Dries Verachtert <dries@ulyssis.org> - 1.8.0-1
- Initial package.
