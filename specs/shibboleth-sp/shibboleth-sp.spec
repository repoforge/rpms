# $Id$
# Authority: dries
# Upstream: <shib-info$internet2,edu>

%define real_version 1.3f

Summary: Web single signon middleware for service providers
Name: shibboleth-sp
Version: 1.3
Release: 0.f.1%{?dist}
License: Apache
Group: Applications/Internet
URL: http://shibboleth.internet2.edu/

Source: http://shibboleth.internet2.edu/downloads/shibboleth-sp-%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: log4cpp-devel, xml-security-c-devel, gcc-c++, xerces-c-devel, opensaml-devel
BuildRequires: openssl-devel

%description
The Shibboleth software implements the OASIS SAML v1.1 specification, 
providing a federated Single-SignOn and attribute exchange framework. 
Shibboleth also provides extended privacy functionality allowing the 
browser user and their home site to control the Attribute information 
being released to each Service Provider. Using Shibboleth-enabled 
access simplifies management of identity and access permissions for 
both Identity and Service Providers. Shibboleth is developed in an open 
and participatory environment, is freely available, and is released 
under the Apache Software License.

This package contains the software for the service providers.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n shibboleth-%{version}

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__mv} %{buildroot}/usr/doc/shibboleth rpmdocs

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc rpmdocs/*
%dir %{_sysconfdir}/shibboleth/
%config(noreplace) %{_sysconfdir}/shibboleth/*.xml
%config(noreplace) %{_sysconfdir}/shibboleth/*.logger
%config(noreplace) %{_sysconfdir}/shibboleth/*.html
%config(noreplace) %{_sysconfdir}/shibboleth/inqueue.pem
%config(noreplace) %{_sysconfdir}/shibboleth/shibd
%{_sysconfdir}/shibboleth/*.config
%{_sysconfdir}/shibboleth/sp-example.crt
%{_sysconfdir}/shibboleth/sp-example.key
%{_sysconfdir}/shibboleth/*.dist
%{_bindir}/posttest
%{_bindir}/shibtest
%{_bindir}/test-client
%{_sbindir}/shibd
%{_sbindir}/siterefresh
%{_libdir}/libshib-target.so.*
%{_libdir}/libshib.so.*
%{_libexecdir}/adfs.*
%{_libexecdir}/xmlproviders.*
%{_datadir}/xml/shibboleth/

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/shib/
%{_includedir}/shib-target/
%{_libdir}/libshib-target.so
%{_libdir}/libshib.so
#%exclude %{_libdir}/*.la

%changelog
* Sat Nov 18 2006 Dries Verachtert <dries@ulyssis.org> - 1.3-0.f.1
- Initial package.
