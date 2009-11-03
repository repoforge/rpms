# $Id$
# Authority: dag

%define real_name libbonobouimm

Summary: C++ wrappers for libbonoboui, for use with gtkmm
Name: libbonobouimm2
Version: 1.3.5
Release: 0.dag%{?dist}
License: LGPL
Group: System Environment/Libraries
URL: http://gtkmm.sourceforge.net/

Source: http://dl.sf.net/gtkmm/libbonobouimm-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Prefix: %{_prefix}

BuildRequires: gtkmm2-devel >= 2.0, libbonobo-devel >= 2.0, libbonoboui-devel >= 2.0
BuildRequires: ORBit2-devel >= 2.0

%description
libbonobouimm provides C++ wrappers for libbonoboui, for use with gtkmm.

%package devel
Summary: Headers for developing programs that will use %{real_name}.
Group: Development/Libraries

%description devel
This package contains the static libraries and header files needed for
developing gtkmm applications.

%prep
%setup -n %{real_name}-%{version}

%build
%configure \
	--enable-static \
	--enable-shared
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
%doc AUTHORS ChangeLog COPYING NEWS README
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/libbonobouimm-2.0/
%{_libdir}/libgnomemm-2.0/proc/m4/*
%{_libdir}/pkgconfig/*.pc
%{_includedir}/libbonobouimm-2.0/
%{_includedir}/libgnomemm-2.0/
%exclude %{_libdir}/*.la

%changelog
* Sat Mar 29 2003 Dag Wieers <dag@wieers.com> - 1.3.5-0
- Initial package. (using DAR)
