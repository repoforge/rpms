# $Id$
# Authority: hadams

Summary: C++ unit testing framework
Name: cppunit
Version: 1.12.0
Release: 3%{?dist}
License: LGPL
Group: Development/Libraries
URL: http://cppunit.sourceforge.net/cppunit-wiki

Source: http://dl.sf.net/cppunit/cppunit-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%{!?_without_doxygen:BuildRequires: doxygen}
%{!?_without_graphviz:BuildRequires: graphviz}

%description
CppUnit is the C++ port of the famous JUnit framework for unit testing.
Test output is in XML for automatic testing and GUI based for supervised tests.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Provides: cppunit-doc = %{version}-%{release}
Obsoletes: cppunit-doc <= %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
%configure \
%{!?_without_doxygen:--enable-doxygen}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_datadir}/cppunit/

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%doc AUTHORS BUGS ChangeLog COPYING NEWS README THANKS TODO doc/FAQ
%{_bindir}/DllPlugInTester
%{_datadir}/aclocal/cppunit.m4
%{_libdir}/libcppunit*.so.*

%files devel
%defattr(-, root, root, 0755)
%doc doc/html/*
%doc %{_mandir}/man1/cppunit.1*
%{_bindir}/cppunit-config
%{_includedir}/cppunit/
%{_libdir}/libcppunit.a
%{_libdir}/libcppunit.so
%{_libdir}/pkgconfig/cppunit.pc
%exclude %{_libdir}/libcppunit.la

%changelog
* Thu Sep 11 2007 Heiko Adams <info@fedora-blog.de> - 1.12.0-3
- Rebuild for RPMforge.

* Sun Sep 10 2006 Patrice Dumas <pertusus@free.fr> 1.12.0-2
- rebuild for FC6

* Wed Jul  5 2006 Patrice Dumas <pertusus@free.fr> 1.12.0-1
- update to 1.12

* Sun May 21 2006 Patrice Dumas <pertusus@free.fr> 1.11.6-1
- update to 1.11.6

* Wed Dec 21 2005 Patrice Dumas <pertusus@free.fr> 1.11.4-1
- update

* Mon Aug 15 2005 Tom "spot" Callaway <tcallawa@redhat.com> 1.11.0-2
- various cleanups

* Mon Jul  4 2005 Patrice Dumas <pertusus@free.fr> 1.11.0-1
- update using the fedora template 
 
* Sat Apr 14 2001 Bastiaan Bakker <bastiaan.bakker@lifeline.nl>
- Initial release
