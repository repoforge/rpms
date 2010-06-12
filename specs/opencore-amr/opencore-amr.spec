# $Id$
# Authority: yury
# Upstream: http://opencore-amr.sourceforge.net

Summary: Adaptive Multi Rate speech codec
Name: opencore-amr
Version: 0.1.2
Release: 1%{?dist}
License: Apache License
Group: System Environment/Libraries
URL: http://opencore-amr.sourceforge.net/

Source: http://dl.sf.net/opencore-amr/opencore-amr-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
This library contains an implementation of the 3GPP TS 26.073
specification for the Adaptive Multi Rate (AMR) speech codec. The
implementation is derived from the OpenCORE framework, part of the
Google Android project.

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
%setup -n %{name}-%{version}

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
%{_includedir}/*
%{_libdir}/libopencore-amrnb.so
%{_libdir}/libopencore-amrwb.so
%{_libdir}/pkgconfig/opencore-amrnb.pc
%{_libdir}/pkgconfig/opencore-amrwb.pc
%exclude %{_libdir}/libopencore-amrnb.la
%exclude %{_libdir}/libopencore-amrwb.la

%changelog
* Sat Jun 12 2010 Yury V. Zaytsev <yury@shurup.com> - 0.1.2-1
- Salvaged from RPMForge SRPM by Bjarne Saltbaek.
- Minor fixes.
