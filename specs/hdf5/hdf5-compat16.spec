# $Id$
# Authority: shuff
# Upstream: The HDF Group <help$hdfgroup,org>

%define real_name hdf5

Summary: Compatibility libraries for legacy HDF5 support
Name: hdf5-compat16
Version: 1.6.10
Release: 1%{?dist}
License: Distributable
Group: Development/Libraries
URL: http://hdfgroup.org/HDF5/

Source: http://www.hdfgroup.org/ftp/HDF5/prev-releases/hdf5-%{version}/src/hdf5-%{version}.tar.gz
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

Conflicts: hdf5 <= %{version}
Obsoletes: hdf5 <= %{version}

# don't scan the examples for autoreq/prov
%filter_requires_in %{_docdir}
%filter_provides_in %{_docdir}

%filter_setup

%description
HDF5 is a unique technology suite that makes possible the management of 
extremely large and complex data collections.

This package contains only runtime libraries to support applications compiled
agains HDF5 1.6.x.  If you need the full HDF5 utility suite, please install
Repoforge's "hdf5" package.

%prep
%setup -n %{real_name}-%{version}
%{__perl} -pi.orig -e 's|INSTALL\) h5cc \$\(bindir\)/\$\(H5CC_NAME\)|INSTALL) h5cc %{buildroot}\$(bindir)/\$(H5CC_NAME)|g;' tools/misc/Makefile*

%build
FC=/usr/bin/gfortran %configure \
    --disable-dependency-tracking \
    --disable-static \
    --enable-shared \
    --disable-cxx \
    --disable-fortran
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

# no binaries
%{__rm} -rf %{buildroot}%{_bindir}

# no devel
%{__rm} -rf %{buildroot}%{_includedir}
%{__rm} -rf %{buildroot}%{_libdir}/libhdf5*.so

# put the settings file in %doc
%{__mv} %{buildroot}%{_libdir}/libhdf5.settings .

# and the examples
%{__rm} -rf examples
%{__mv} %{buildroot}%{_usr}/doc/hdf5/examples .
%{__rm} -rf %{buildroot}%{_usr}/doc/hdf5/

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc *.txt release_docs/* examples/
%{_libdir}/libhdf5*.so.*
%exclude %{_libdir}/libhdf5*.la

%changelog
* Tue Aug 02 2011 Steve Huff <shuff@vecna.org> - 1.6.10-1
- Initial package.
