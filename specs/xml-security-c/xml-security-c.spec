# $Id$
# Authority: dries

Summary: Implementation of security standards for XML
Name: xml-security-c
Version: 1.3.0
Release: 1%{?dist}
License: Apache
Group: Development/Libraries
URL: http://xml.apache.org/security/

Source: http://xml.apache.org/security/dist/c-library/xml-security-c-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, xerces-c-devel

%description
The XML Security project is aimed at providing implementation of 
security standards for XML.

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
cd src
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
cd src
%makeinstall

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc LICENSE *.txt
%{_libdir}/libxml-security-c.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/xsec/
%{_libdir}/libxml-security-c.so

%changelog
* Sat Nov 18 2006 Dries Verachtert <dries@ulyssis.org> - 1.3.0-1
- Initial package.
