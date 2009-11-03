# $Id$
# Authority: dries

Summary: Platform independent generic unit testing framework for C++
Name: mockpp
Version: 1.16.4
Release: 1%{?dist}
License: LGPL
Group: Development/Libraries
URL: http://mockpp.sourceforge.net/

Source: http://dl.sf.net/mockpp/mockpp-%{version}-src.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++

%description
mockpp is a platform independent generic unit testing framework for C++. It's 
goal is to facilitate developing unit tests in the spirit of Mock Objects for 
Java, EasyMock and jMock.

Mock objects allow you to set up predictible behaviour to help you test your 
production code by emulating some functionality your code depends on. This 
might for example be a huge database which is too difficult and time consuming 
to maintain just for testing purposes.

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
%doc AUTHORS ChangeLog COPYING INSTALL README TODO
%{_bindir}/mockpp2xml
%{_bindir}/xml2mockpp
%{_libdir}/libmockpp.so.*
%{_libdir}/libmockpp_cxxtest.so.*
%{_libdir}/libmockpp_production.so.*
%{_libdir}/pkgconfig/mockpp.pc
%{_datadir}/mockpp/

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/mockpp/
%exclude %{_libdir}/*.a
%{_libdir}/libmockpp.so
%{_libdir}/libmockpp_cxxtest.so
%{_libdir}/libmockpp_production.so
%exclude %{_libdir}/*.la

%changelog
* Sat Dec  1 2007 Dries Verachtert <dries@ulyssis.org> - 1.16.4-1
- Updated to release 1.16.4.

* Mon Oct  1 2007 Dries Verachtert <dries@ulyssis.org> - 1.16.2-1
- Updated to release 1.16.2.

* Fri Aug 17 2007 Dries Verachtert <dries@ulyssis.org> - 1.16.1-1
- Updated to release 1.16.1.

* Sun Apr 15 2007 Dries Verachtert <dries@ulyssis.org> - 1.15.1-1
- Initial package.
