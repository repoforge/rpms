# $Id$
# Authority: dries

Summary: C++  web services client library
Name: wsdlpull
Version: 1.24
Release: 2%{?dist}
License: LGPL
Group: Applications/Internet
URL: http://wsdlpull.sourceforge.net/

Source: http://downloads.sourceforge.net/project/wsdlpull/wsdlpull/wsdlpull%20%{version}/wsdlpull-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libcurl-devel
BuildRequires: gcc-c++
BuildRequires: doxygen

%description
wsdlpull is a C++ web services client library. It includes a WSDL
Parser,a XSD Schema Parser and Validator and XML Parser and serializer
and an API and command line tool for dynamic WSDL inspection and
invocation.

wsdlpull comes with a generic web service client.Using wsdlpull's /wsdl/
tool you can invoke most web services from command line without writing
any code.

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
#makeinstall
%{__make} install DESTDIR="%{buildroot}"

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog CHANGES COPYING INSTALL NEWS README
%{_bindir}/wsdlpull-schema
%{_bindir}/wsdlpull
%{_datadir}/wsdlpull/
%{_libdir}/libwsdlpullschema.so.*
%{_libdir}/libwsdlpull.so.*
%{_libdir}/libwsdlpullxml.so.*
%{_mandir}/man1/wsdlpull*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/wsdlpull/
%{_libdir}/libwsdlpullschema.so
%{_libdir}/libwsdlpull.so
%{_libdir}/libwsdlpullxml.so
%exclude %{_libdir}/*.la

%changelog
* Sun Jun 16 2013 Denis Fateyev <denis@fateyev.com> - 1.24-2
- Some spec cleanup

* Wed Apr 17 2013 Dries Verachtert <dries.verachtert@dries.eu> - 1.24-1
- Updated to release 1.24.

* Mon Aug 11 2008 Dries Verachtert <dries@ulyssis.org> - 1.20-1
- Updated to release 1.20.

* Tue Jan  1 2008 Dries Verachtert <dries@ulyssis.org> - 1.16-1
- Updated to release 1.16.

* Mon Jul 06 2007 Dries Verachtert <dries@ulyssis.org> - 1.14-1
- Updated to release 1.14.

* Wed Apr 18 2007 Dries Verachtert <dries@ulyssis.org> - 1.13-1
- Updated to release 1.13.

* Sun Nov 26 2006 Dries Verachtert <dries@ulyssis.org> - 1.12-1
- Updated to release 1.12.

* Sun Apr 23 2006 Dries Verachtert <dries@ulyssis.org> - 1.11-1
- Updated to release 1.11.

* Mon Apr 03 2006 Dries Verachtert <dries@ulyssis.org> - 1.10-1
- Updated to release 1.10.

* Tue Feb 07 2006 Dries Verachtert <dries@ulyssis.org> - 1.9.8-1
- Updated to release 1.9.8.

* Wed Jan 25 2006 Dries Verachtert <dries@ulyssis.org> - 1.9.7-1
- Updated to release 1.9.7.

* Mon Dec 12 2005 Dries Verachtert <dries@ulyssis.org> - 1.9.6-1
- Updated to release 1.9.6.

* Wed Nov 09 2005 Dries Verachtert <dries@ulyssis.org> - 1.9.5-1
- Initial package.
