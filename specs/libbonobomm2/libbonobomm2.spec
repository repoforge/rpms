# $Id$

# Authority: dag

%define rname libbonobomm

Summary: C++ wrappers for libbonobo, for use with gtkmm
Name: libbonobomm2
Version: 1.3.8
Release: 0
License: LGPL
Group: System Environment/Libraries
URL: http://gtkmm.sf.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/gtkmm/libbonobomm-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: gtkmm2-devel >= 2.0, libbonobo-devel >= 2.0, ORBit2-devel >= 2.0
BuildRequires: orbitcpp >= 1.3

%description
libgnomemm provides C++ wrappers for libbonobo, for use with gtkmm.

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n %{rname}-%{version}

%build
%configure \
	--enable-static \
	--enable-shared
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_libdir}/*.la

%post
/sbin/ldconfig &>/dev/null

%postun
/sbin/ldconfig &>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/libbonobomm-2.0/
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/gtkmm-2.0/proc/m4/*
%{_libdir}/libbonobomm-2.0/
%{_includedir}/libbonobomm-2.0/
%{_libdir}/pkgconfig/*.pc
#exclude %{_libdir}/*.la

%changelog
* Tue Nov 23 2003 Dag Wieers <dag@wieers.com> - 1.3.8-0
- Updated to release 1.3.8.

* Sat Mar 29 2003 Dag Wieers <dag@wieers.com> - 1.3.5-0
- Initial package. (using DAR)
