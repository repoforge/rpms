# $Id$

# Authority: dag

%define real_name gc

Summary: Conservative garbage collector for C
Name: libgc
Version: 6.2
Release: 0
Epoch: 1
License: BSD
Group: System Environment/Libraries
URL: http://www.hpl.hp.com/personal/Hans_Boehm/gc/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.hpl.hp.com/personal/Hans_Boehm/%{real_name}/gc_source/%{real_name}%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Obsoletes: libgc-6, libgc-6.1alpha5, gc

%description
Boehm's GC is a garbage collecting storage allocator that is
intended to be used as a plug-in replacement for C's malloc.

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{epoch}:%{version}-%{release}
Obsoletes: libgc6-devel, gc-devel

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n %{real_name}%{version}

%build
%configure \
	--enable-threads="pthreads"
%{__make} %{?_smp_mflags} LIBS="-ldl"

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_libdir} \
			%{buildroot}%{_includedir}/%{real_name} \
			%{buildroot}%{_mandir}/man1/
%makeinstall \
	DESTDIR="%{buildroot}"
#%{__install} -m0644 include/*.h %{buildroot}%{_includedir}/%{real_name}
%{__install} -m0655 doc/gc.man %{buildroot}%{_mandir}/man1/gc.1

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/*.la
%{__rm} -rf %{buildroot}%{_datadir}/gc/

%post 
/sbin/ldconfig 2>/dev/null

%postun 
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README.QUICK
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%doc doc/*
%doc %{_mandir}/man?/*
%{_libdir}/*.a
%{_libdir}/*.so
%{_includedir}/*.h
%{_includedir}/%{real_name}/
#exclude %{_libdir}/*.la

%changelog
* Sun Nov 23 2003 Dag Wieers <dag@wieers.com> - 6.2-0
- Updated to release 6.2.

* Mon Mar 17 2003 Dag Wieers <dag@wieers.com> - 6.1-0
- Initial package. (using DAR)
