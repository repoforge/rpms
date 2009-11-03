# $Id$
# Authority: dag

# ExclusiveDist: el2 rh7 rh9 el3 fc1

%define real_name liboil

Summary: Library of Optimized Inner Loops, CPU optimized functions
Name: liboil02
Version: 0.2.2
Release: 1%{?dist}
License: LGPL
Group: System Environment/Libraries
URL: http://www.schleef.org/liboil/

Source: http://www.schleef.org/liboil/download/liboil-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: glib2-devel, gcc-c++
Obsoletes: liboil <= %{version}

%description
Liboil is a library of simple functions that are optimized for various CPUs.
These functions are generally loops implementing simple algorithms, such as
converting an array of N integers to floating-poing numbers or multiplying
and summing an array of N numbers. Clearly such functions are candidates for
significant optimization using various techniques, especially by using
extended instructions provided by modern CPUs (Altivec, MMX, SSE, etc.).

%package devel
Summary: Development files and static library for liboil
Group: Development/Libraries
Requires: %{name} = %{version}, pkgconfig
Obsoletes: liboil-devel <= %{version}

%description devel
Liboil is a library of simple functions that are optimized for various CPUs.
These functions are generally loops implementing simple algorithms, such as
converting an array of N integers to floating-poing numbers or multiplying
and summing an array of N numbers. Clearly such functions are candidates for
significant optimization using various techniques, especially by using
extended instructions provided by modern CPUs (Altivec, MMX, SSE, etc.).

%prep
%setup -n %{real_name}-%{version}

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%doc ChangeLog
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/*
%{_libdir}/*.a
%exclude %{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
#%{_datadir}/gtk-doc/html/liboil/

%changelog
* Tue Apr 05 2005 Dag Wieers <dag@wieers.com> - 0.2.2-1
- Renamed to liboil02.

* Wed Nov 24 2004 Matthias Saou <http://freshrpms.net/> 0.2.2-1
- Update to 0.2.2.

* Thu Nov  4 2004 Matthias Saou <http://freshrpms.net/> 0.2.0-1
- Initial RPM release.
