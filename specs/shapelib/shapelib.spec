# $Id$
# Authority: dries

Summary: Read and write ESRI shapefiles and their related DBF files
Name: shapelib
Version: 1.2.10
Release: 1.2%{?dist}
License: MIT/X
Group: Development/Libraries
URL: http://shapelib.maptools.org/

Source: http://dl.maptools.org/dl/shapelib/shapelib-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

#BuildRequires:

%description
Shapefile C Library is a C library for reading and writing ESRI Shapefiles
and their related DBF files. All geometry types are supported, with robust
DBF support. Shapelib is widely used for commercial and free projects.
Shapelib includes command line utilities for dumping, subsetting, clipping,
shifting, scaling, and reprojecting shapefiles.

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
%{__make} %{?_smp_mflags}
%{__make} %{?_smp_mflags} lib

%install
%{__rm} -rf %{buildroot}
%{__install} -d %{buildroot}%{_bindir} %{buildroot}%{_libdir} %{buildroot}%{_includedir}
%{__perl} -pi -e "s|/usr/local|%{buildroot}%{_prefix}|g;" Makefile
%{__make} lib_install
%{__install} dbfcreate %{buildroot}%{_bindir}/shapelib-dbfcreate
%{__install} dbfadd %{buildroot}%{_bindir}/shapelib-dbfadd
%{__install} dbfdump %{buildroot}%{_bindir}/shapelib-dbfdump

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog README
%{_bindir}/shapelib-dbfadd
%{_bindir}/shapelib-dbfcreate
%{_bindir}/shapelib-dbfdump
%{_libdir}/libshp.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/libshp/
%{_libdir}/libshp.a
%{_libdir}/libshp.so
%exclude %{_libdir}/*.la

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.2.10-1.2
- Rebuild for Fedora Core 5.

* Sat Jan 14 2006 Dries Verachtert <dries@ulyssis.org> - 1.2.10-1
- Initial package.
