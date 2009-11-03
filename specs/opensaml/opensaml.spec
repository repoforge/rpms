# $Id$
# Authority: dries

%define real_version 1.1b

Summary: Toolkit form SAML 1.1 and 1.0
Name: opensaml
Version: 1.1
Release: 0.b.1%{?dist}
License: Apache 2.0
Group: Development/Libraries
URL: http://www.opensaml.org/

Source: http://shibboleth.internet2.edu/downloads/opensaml-%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: xml-security-c-devel, gcc-c++, xerces-c-devel, log4cpp-devel
BuildRequires: curl-devel >= 7.10

%description
OpenSAML 1.1 is an open source toolkit for implementing solutions using the 
SAML 1.1 and 1.0 specifications. It is a production quality release available 
for Java (1.4+) and C++ applications.

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
%{__mv} %{buildroot}/usr/doc/opensaml rpmdocs

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc rpmdocs/*
%{_bindir}/signtest
%{_libdir}/libsaml.so.*
%{_datadir}/xml/opensaml/

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/saml/
%{_libdir}/libsaml.so

%changelog
* Sat Nov 18 2006 Dries Verachtert <dries@ulyssis.org> - 1.1-0.b.1
- Initial package.
