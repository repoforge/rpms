# $Id$
# Authority: shuff
# Upstream: The HDF Group <help$hdfgroup,org>

Summary: Manages extremely large and complex data collections
Name: hdf5
Version: 1.8.7
Release: 1%{?dist}
License: Distributable
Group: Development/Libraries
URL: http://hdfgroup.org/HDF5/

Source: ftp://ftp.hdfgroup.org/HDF5/current/src/hdf5-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: binutils
BuildRequires: bison
BuildRequires: flex
BuildRequires: gcc-c++
BuildRequires: gcc-gfortran
BuildRequires: libjpeg-devel
BuildRequires: make
BuildRequires: zlib-devel >= 1.1.2
BuildRequires: rpm-macros-rpmforge

# don't scan the examples for autoreq/prov
%filter_requires_in %{_docdir}
%filter_provides_in %{_docdir}

%filter_setup

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
FC=/usr/bin/gfortran %configure \
    --disable-dependency-tracking \
    --disable-static \
    --enable-shared \
    --enable-cxx \
    --enable-fortran
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

# put the settings file in %doc
%{__mv} %{buildroot}%{_libdir}/libhdf5.settings .

# and the examples
%{__mv} %{buildroot}%{_datadir}/hdf5_examples .

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc *.txt release_docs/*
%{_bindir}/*
%{_libdir}/libhdf5*.so.*

%files devel
%doc libhdf5.settings hdf5_examples
%{_includedir}/H5*.h
%{_includedir}/hdf5*.h
%{_includedir}/*.mod
%{_libdir}/libhdf5*.so
%exclude %{_libdir}/libhdf5*.la

%changelog
* Tue Aug 02 2011 Steve Huff <shuff@vecna.org> - 1.8.7-1
- Updated to release 1.8.7.
- Added additional compile-time options.
- Captured missing dependencies.

* Thu May 15 2008 Dries Verachtert <dries@ulyssis.org> - 1.8.0-1
- Initial package.
