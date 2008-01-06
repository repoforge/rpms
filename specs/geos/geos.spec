# $Id$
# Authority: dries
# Upstream: Paul Ramsey <pramsey$refractions,net>

Summary: GEOS (Geometry Engine, Open Source) topology library
Name: geos
Version: 3.0.0
Release: 1
License: LGPL
Group: System Environment/Libraries
URL: http://geos.refractions.net/

Source: http://geos.refractions.net/downloads/geos-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++

%description
GEOS is a complete C++ implementation of the functions and predicates defined 
in the OpenGIS "Simple Features for SQL" specification. It includes high 
quality implementations of all the important spatial relationships and 
operations, robust versions of all functions in the dimensionally extended 
9 intersection predicate model, implementations of the operators, Buffer(), 
Union(), and Intersection(), and all other SFSQL functions including Area(), 
Length(), Centroid(), etc.

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
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%{_libdir}/libgeos*.so.*

%files devel
%{_bindir}/geos-config
%{_bindir}/XMLTester
%{_includedir}/geos*.h
%{_includedir}/geos/
%{_libdir}/libgeos*.so
%exclude %{_libdir}/libgeos*.a
%exclude %{_libdir}/libgeos*.la

%changelog
* Sun Jan  6 2008 Dries Verachtert <dries@ulyssis.org> - 3.0.0-1
- Updated to release 3.0.0.

* Mon Jul 23 2007 Dayne Broderson <dayne@alaska.edu> - 2.2.3-1
- Initial package, based on a spec file made by Mapping Hacks.
