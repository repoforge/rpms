# $Id$
# Authority: dries

%define real_version 1.9.6

Summary: C++  web services client library
Name: wsdlpull
Version: 1.9.6
Release: 1
License: LGPL
Group: Applications/Internet
URL: http://wsdlpull.sourceforge.net/

Source: http://dl.sf.net/wsdlpull/wsdlpull-%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++

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
%setup -n %{name}-1.9

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS.txt CHANGES.txt COPYING.txt INSTALL.txt README.txt TODO.txt
%{_bindir}/schema
%{_bindir}/wsdl
%exclude %{_prefix}/docs/*
%{_libdir}/libschema.so.*
%{_libdir}/libwsdl.so.*
%{_libdir}/libxmlpull.so.*
%{_datadir}/wsdlpull/

%files devel
%{_includedir}/schemaparser/
%{_includedir}/wsdlparser/
%{_includedir}/xmlpull/
%{_libdir}/libschema.a
%{_libdir}/libwsdl.a
%{_libdir}/libxmlpull.a
%{_libdir}/libschema.so
%{_libdir}/libwsdl.so
%{_libdir}/libxmlpull.so
%exclude %{_libdir}/*.la

%changelog
* Mon Dec 12 2005 Dries Verachtert <dries@ulyssis.org> - 1.9.6-1
- Updated to release 1.9.6.

* Wed Nov 09 2005 Dries Verachtert <dries@ulyssis.org> - 1.9.5-1
- Initial package.
