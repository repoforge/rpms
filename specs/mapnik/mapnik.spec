# $Id$
# Authority: dries

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')

Summary: Toolkit for developing GIS applications
Name: mapnik
Version: 0.6.0
Release: 1
License: GPL
Group: Development/Libraries
URL: http://mapnik.org/

Source: http://download.berlios.de/mapnik/mapnik-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: scons, libtool-ltdl-devel, proj-devel, python

%description
Mapnik is a toolkit for developing GIS applications. At the core is a C++ 
shared library providing algorithms/patterns for spatial data access and 
visualization. Essentially a collection of geographic objects (map, layer, 
datasource, feature, and geometry), the library doesn't rely on "windowing 
systems" and can be deployed in any server environment. It is intended to 
play fair in a multi-threaded environment and is aimed primarily, but not 
exclusively, at Web-based development. High-level Python bindings 
(boost.python) facilitate rapid application development, targeting zope3, 
django, etc.

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
scons PREFIX="%{_prefix}"

%install
%{__rm} -rf %{buildroot}
scons install DESTDIR=%{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
# -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING INSTALL README
%{_bindir}/shapeindex
%{_libdir}/libmapnik.so.*
%{_libdir}/mapnik/
%{python_sitelib}/mapnik/

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/mapnik/
%{_libdir}/libmapnik.so

%changelog
* Tue Apr  7 2009 Dries Verachtert <dries@ulyssis.org> - 0.6.0-1
- Updated to release 0.6.0.

* Sun Apr 20 2008 Dries Verachtert <dries@ulyssis.org> - 0.5.1-1
- Updated to release 0.5.1.

* Tue Apr 17 2007 Dries Verachtert <dries@ulyssis.org> - 0.4.0-1
- Updated to release 0.4.0.

* Tue May 24 2006 Dries Verachtert <dries@ulyssis.org> - 0.3.0-1
- Initial package.
