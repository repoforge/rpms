# $Id$
# Authority: dag
# RFX: el6

%define real_name gc

Summary: Conservative garbage collector for C
Name: libgc
Version: 7.1
Release: 1%{?dist}
Epoch: 1
License: BSD
Group: System Environment/Libraries
URL: http://www.hpl.hp.com/personal/Hans_Boehm/gc/

Source: http://www.hpl.hp.com/personal/Hans_Boehm/gc/gc_source/gc-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Obsoletes: libgc6 <= %{epoch}:%{version}-%{release}
Provides: libgc6 <= %{epoch}:%{version}-%{release}
Obsoletes: gc <= %{epoch}:%{version}-%{release}
Provides: gc = %{epoch}:%{version}-%{release}
BuildRequires: gcc-c++

%description
Boehm's GC is a garbage collecting storage allocator that is
intended to be used as a plug-in replacement for C's malloc.

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{epoch}:%{version}-%{release}
Obsoletes: libgc6-devel <= %{epoch}:%{version}-%{release}
Provides: libgc6-devel = %{epoch}:%{version}-%{release}
Obsoletes: gc-devel <= %{epoch}:%{version}-%{release}
Provides: gc-devel = %{epoch}:%{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n %{real_name}-%{version}

%build
%configure \
	--enable-threads="pthreads" --enable-cplusplus
%{__make} %{?_smp_mflags} LIBS="-ldl"

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_libdir} \
			%{buildroot}%{_includedir}/libgc/ \
			%{buildroot}%{_mandir}/man1/
%makeinstall
#	DESTDIR="%{buildroot}"
#%{__install} -Dp -m0644 include/*.h %{buildroot}%{_includedir}/libgc/
%{__install} -Dp -m0655 doc/gc.man %{buildroot}%{_mandir}/man1/libgc.1

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/*.la
%{__rm} -rf %{buildroot}%{_datadir}/gc/

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README.QUICK
%{_libdir}/libgc.so.*
%{_libdir}/libgccpp.so.*
%{_libdir}/libcord.so.*

%files devel
%defattr(-, root, root, 0755)
%doc doc/*
%doc %{_mandir}/man1/libgc.1*
%{_libdir}/libgc.so
%{_libdir}/libgccpp.so
%{_libdir}/libcord.so
%{_includedir}/gc/
%{_includedir}/gc.h
%{_includedir}/gc_cpp.h
%{_includedir}/libgc/
%{_libdir}/pkgconfig/bdw-gc.pc
%exclude %{_libdir}/libgc.a
%exclude %{_libdir}/libgccpp.a
%exclude %{_libdir}/libcord.a
#exclude %{_libdir}/*.la

%changelog
* Mon Jun  9 2008 Dries Verachtert <dries@ulyssis.org> - 7.1-1
- Updated to release 7.1.

* Sun Jul 08 2007 Dries Verachtert <dries@ulyssis.org> - 7.0-1
- Updated to release 7.0.

* Fri Dec 15 2006 Dries Verachtert <dries@ulyssis.org> - 6.8-2
- Added --enable-cplusplus, thanks to Jens Hoelldampf.

* Wed Aug 09 2006 Dries Verachtert <dries@ulyssis.org> - 6.8-1
- Updated to release 6.8.

* Mon Apr 03 2006 Dries Verachtert <dries@ulyssis.org> - 6.7-1
- Updated to release 6.7.

* Sat Jan 14 2006 Dag Wieers <dag@wieers.com> - 6.6-1
- Excluded gc.1 manpage.

* Tue Sep 20 2005 Dries Verachtert <dries@ulyssis.org> - 6.6-0
- Updated to release 6.6.

* Sun Nov 23 2003 Dag Wieers <dag@wieers.com> - 6.2-0
- Updated to release 6.2.

* Mon Mar 17 2003 Dag Wieers <dag@wieers.com> - 6.1-0
- Initial package. (using DAR)
