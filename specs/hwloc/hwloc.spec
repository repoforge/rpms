# $Id$
# Authority: dag

Summary: Hardware Locality Library
Name: hwloc
Version: 1.0.1
Release: 1%{?dist}
License: BSD
Group: System Environment/Libraries
URL: http://www.open-mpi.org/

Source: http://www.open-mpi.org/software/hwloc/v1.0/downloads/hwloc-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
The Portable Hardware Locality (hwloc) software package provides a portable
abstraction (across OS, versions, architectures, ...) of the hierarchical
topology of modern architectures, including NUMA memory nodes, sockets, shared
caches, cores and simultaneous multithreading. It also gathers various system
attributes such as cache and memory information. It primarily aims at helping
applications with gathering information about modern computing hardware so as
to exploit it accordingly and efficiently.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

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

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING NEWS README
%doc %{_mandir}/man1/hwloc-bind.1*
%doc %{_mandir}/man1/hwloc-calc.1*
%doc %{_mandir}/man1/hwloc-distrib.1*
%doc %{_mandir}/man1/hwloc-info.1*
%doc %{_mandir}/man1/hwloc-ls.1*
%doc %{_mandir}/man1/hwloc-mask.1*
%doc %{_mandir}/man1/lstopo.1*
%doc %{_mandir}/man7/hwloc.7*
%{_bindir}/hwloc-bind
%{_bindir}/hwloc-calc
%{_bindir}/hwloc-distrib
%{_bindir}/hwloc-info
%{_bindir}/hwloc-ls
%{_bindir}/hwloc-mask
%{_bindir}/lstopo
%{_datadir}/hwloc/
%{_libdir}/libhwloc.so.*
%exclude %{_docdir}/hwloc/

%files devel
%defattr(-, root, root, 0755)
%doc %{_mandir}/man3/HWLOC_*.3*
%doc %{_mandir}/man3/hwloc_*.3*
%doc %{_mandir}/man3/hwlocality_*.3*
%{_includedir}/hwloc/
%{_includedir}/hwloc.h
%{_libdir}/libhwloc.so
%{_libdir}/pkgconfig/hwloc.pc
%exclude %{_libdir}/libhwloc.la

%changelog
* Thu Jun 10 2010 Dag Wieers <dag@wieers.com> - 1.0.1-1
- Initial package. (using DAR)
