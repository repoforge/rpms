# $Id$
# Authority: dries
# Upstream: Bastiaan Bakker <freshmeat$deal,webcriminals,com>

### EL6 ships with log4cpp-1.0-13.el6
### EL5 ships with log4cpp-1.0-9.el5
# ExclusiveDist: el2 el3 el4

Summary: Logging library for c++
Name: log4cpp
Version: 1.0
Release: 1%{?dist}
License: LGPL
Group: Development/Libraries
URL: http://sourceforge.net/projects/log4cpp/

Source: http://dl.sf.net/log4cpp/log4cpp-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, doxygen

%description
A library of C++ classes for flexible logging to files, syslog, IDSA and 
other destinations. It is modeled after the Log for Java library 
(http://www.log4j.org), staying as close to their API as is reasonable.

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
%makeinstall
%{__mv} %{buildroot}/usr/doc/log4cpp-%{version} rpmdocs

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README THANKS TODO rpmdocs/*
%doc %{_mandir}/man3/log4cpp*
%{_libdir}/liblog4cpp.so.*

%files devel
%defattr(-, root, root, 0755)
%{_bindir}/log4cpp-config
%{_includedir}/log4cpp/
%{_libdir}/liblog4cpp.so
%{_libdir}/pkgconfig/log4cpp.pc
%{_datadir}/aclocal/log4cpp.m4
%exclude %{_libdir}/*.a
%exclude %{_libdir}/*.la

%changelog
* Mon Nov  5 2007 Dries Verachtert <dries@ulyssis.org> - 1.0-1
- Updated to release 1.0.

* Sat Nov 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.3.5-0.rc3
- Initial package.
