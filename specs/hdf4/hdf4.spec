# $Id$
# Authority: shuff
# Upstream: The HDF Group <help$hdfgroup,org>

%define real_name hdf

Summary: Multi-object file format for scientific data
Name: hdf4
Version: 4.2.6
Release: 1%{?dist}
License: GPL
Group: Applications/Engineering
URL: http://www.hdfgroup.org/products/hdf4/

Source: http://www.hdfgroup.org/ftp/HDF/HDF_Current/src/hdf-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: binutils
BuildRequires: gcc-c++
BuildRequires: libjpeg-devel
BuildRequires: make
BuildRequires: zlib-devel
BuildRequires: rpm-macros-rpmforge

%description
At its lowest level, HDF is a physical file format for storing scientific data.
At its highest level, HDF is a collection of utilities and applications for
manipulating, viewing, and analyzing data in HDF files. Between these levels,
HDF is a software library that provides high-level APIs and a low-level data
interface. 

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n %{real_name}-%{version}

%build
%configure \
    --disable-dependency-tracking \
    --enable-static=no \
    --enable-shared=yes \
    --enable-netcdf=no \
    --enable-fortran=no 
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

# do not leave the settings file behind
%{__mv} %{buildroot}%{_libdir}/libhdf4.settings .

# remove the files that conflict with netcdf
%{__rm} -f %{buildroot}%{_bindir}/ncdump
%{__rm} -f %{buildroot}%{_bindir}/ncgen
%{__rm} -f %{buildroot}%{_mandir}/man?/ncdump*
%{__rm} -f %{buildroot}%{_mandir}/man?/ncgen*

# fix for stupid strip issue
#%{__chmod} -R u+w %{buildroot}/*

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING README.txt release_notes/*
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%doc libhdf4.settings
%{_includedir}/*.h
%{_libdir}/*.so
%exclude %{_libdir}/*.la

%changelog
* Tue Aug 02 2011 Steve Huff <shuff@vecna.org> - 4.2.6-1
- Initial package.
- Disable NetCDF support because we already have a netcdf package.

