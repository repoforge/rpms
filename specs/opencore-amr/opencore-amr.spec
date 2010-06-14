# $Id$
# Authority: dag

Summary: Adaptive Multi-Rate Floating-point (AMR) Speech Codec
Name: opencore-amr
Version: 0.1.2
Release: 1%{?dist}
License: Apache License V2.0
Group: System Environment/Libraries
URL: http://opencore-amr.sourceforge.net/

Source: http://dl.sf.net/project/opencore-amr/opencore-amr/%{version}/opencore-amr-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++

%description
Library of OpenCORE Framework implementation of 3GPP Adaptive Multi-Rate
Floating-point (AMR) Speech Codec (3GPP TS 26.104 V 7.0.0) and 3GPP AMR
Adaptive Multi-Rate - Wideband (AMR-WB) Speech Codec (3GPP TS 26.204
V7.0.0).

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
%configure --disable-static
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
%doc AUTHORS ChangeLog COPYING LICENSE README
%{_libdir}/libopencore-amrnb.so.*
%{_libdir}/libopencore-amrwb.so.*

%files devel
%defattr(-, root, root, 0755)
%doc test/*
%{_includedir}/opencore-amrnb/
%{_includedir}/opencore-amrwb/
%{_libdir}/libopencore-amrnb.so
%{_libdir}/libopencore-amrwb.so
%{_libdir}/pkgconfig/opencore-amrnb.pc
%{_libdir}/pkgconfig/opencore-amrwb.pc
%exclude %{_libdir}/libopencore-amrnb.la
%exclude %{_libdir}/libopencore-amrwb.la

%changelog
* Sun Jun 13 2010 Dag Wieers <dag@wieers.com> - 0.1.2-1
- Updated to release 0.1.2.

* Fri Aug 07 2009 Bjarne Saltbaek <arnebjarne72@hotmail.com> - 0.1.1-0.git20090807
- Initial package.
