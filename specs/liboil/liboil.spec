# $Id$
# Authority: matthias

Summary: Library of Optimized Inner Loops, CPU optimized functions
Name: liboil
Version: 0.3.2
Release: 1
License: LGPL
Group: System Environment/Libraries
URL: http://www.schleef.org/liboil/
Source: http://www.schleef.org/liboil/download/liboil-%{version}.tar.gz
Patch: liboil-0.3.0-gccoptfixes.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: glib2-devel, gcc-c++

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

%description devel
Liboil is a library of simple functions that are optimized for various CPUs.
These functions are generally loops implementing simple algorithms, such as
converting an array of N integers to floating-poing numbers or multiplying
and summing an array of N numbers. Clearly such functions are candidates for
significant optimization using various techniques, especially by using
extended instructions provided by modern CPUs (Altivec, MMX, SSE, etc.).


%prep
%setup
%patch0 -p1


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall


%clean
%{__rm} -rf %{buildroot}


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-, root, root, 0755)
%doc ChangeLog
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%doc %{_datadir}/gtk-doc/html/liboil/
%{_includedir}/*
%{_libdir}/*.a
%exclude %{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%doc %{_datadir}/gtk-doc/html/liboil/


%changelog
* Wed May 25 2005 Matthias Saou <http://freshrpms.net/> 0.3.2-1
- Update to 0.3.2.
- Change ldconfig calls to be the program.
- Include new gtk-doc files in the devel package.

* Tue May 24 2005 Tom "spot" Callaway <tcallawa@redhat.com> - 0.3.0-4
- fix compilation error in FC-4 (bz #158641)
- use buildtime exported CFLAGS instead of making up its own

* Sat Apr  2 2005 Matthias Saou <http://freshrpms.net/> 0.3.1-1
- Update to 0.3.1.
- Include gtk-doc files.

* Fri Jan 28 2005 Matthias Saou <http://freshrpms.net/> 0.3.0-1
- Update to 0.3.0.

* Wed Nov 24 2004 Matthias Saou <http://freshrpms.net/> 0.2.2-1
- Update to 0.2.2.

* Thu Nov  4 2004 Matthias Saou <http://freshrpms.net/> 0.2.0-1
- Initial RPM release.

