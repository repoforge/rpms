# $Id$
# Authority: dfateyev
# Upstream: Alon Bar-Lev <alon,barlev$gmail,com>

Name:           pkcs11-helper
Version:        1.08
Release:        1%{?dist}
Summary:        A library for using PKCS#11 providers

Group:          Development/Libraries
License:        GPLv2 or BSD
URL:            http://www.opensc-project.org/pkcs11-helper/
Source0:        http://www.opensc-project.org/files/%{name}/%{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:  doxygen
BuildRequires:  graphviz
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig


%description
pkcs11-helper is a library that simplifies the interaction with PKCS#11
providers for end-user applications using a simple API and optional OpenSSL
engine. The library allows using multiple PKCS#11 providers at the same time,
enumerating available token certificates, or selecting a certificate directly
by serialized id, handling card removal and card insert events, handling card
re-insert to a different slot, supporting session expiration and much more all
using a simple API.


%package        devel
Summary:        Development files for pkcs11-helper
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:       openssl-devel
Requires:       pkgconfig
# for /usr/share/aclocal
Requires:       automake


%description    devel
This package contains header files and documentation necessary for developing
programs using the pkcs11-helper library.


%prep
%setup

%build
%configure --disable-static --enable-doc
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}" INSTALL="%{__install} -p"

# Use %%doc to install documentation in a standard location
%{__mkdir} apidocdir
%{__mv} %{buildroot}/%{_datadir}/doc/%{name}/api/ apidocdir/
%{__rm} -rf %{buildroot}/%{_datadir}/doc/%{name}/

# Remove libtool .la files
%{__rm} -f %{buildroot}/%{_libdir}/*.la

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING* README THANKS
%{_libdir}/libpkcs11-helper.so.*


%files devel
%defattr(-,root,root,-)
%doc apidocdir/*
%{_includedir}/pkcs11-helper-1.0/
%{_libdir}/libpkcs11-helper.so
%{_libdir}/pkgconfig/libpkcs11-helper-1.pc
%{_datadir}/aclocal/pkcs11-helper-1.m4
%{_mandir}/man8/pkcs11-helper-1.8*


%changelog
* Tue Mar 01 2011 Denis Fateyev <denis@fateyev.com> - 1.08-1
- Updated to version 1.08.
- Rebuilt for RPMForge.

* Mon Jul 13 2009 Kalev Lember <kalev@smartlink.ee> - 1.07-2.1
- Fix EPEL-5 build by adding pkgconfig to BuildRequires.

* Sat Jul 11 2009 Kalev Lember <kalev@smartlink.ee> - 1.07-2
- Make devel package depend on automake for /usr/share/aclocal

* Tue Jun 23 2009 Kalev Lember <kalev@smartlink.ee> - 1.07-1
- Initial RPM release.
