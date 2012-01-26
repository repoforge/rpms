# $Id$
# Authority: dag

### EL6 ships with hwloc-1.1-0.1.el6
%{?el6:# Tag: rfx}

Summary: Hardware Locality Library
Name: hwloc
Version: 1.4
Release: 1%{?dist}
License: BSD
Group: System Environment/Libraries
URL: http://www.open-mpi.org/projects/hwloc/

Source: http://www.open-mpi.org/software/hwloc/v1.4/downloads/hwloc-%{version}.tar.bz2
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
%doc %{_mandir}/man1/hwloc-assembler.1*
%doc %{_mandir}/man1/hwloc-assembler-remote.1*
%doc %{_mandir}/man1/hwloc-bind.1*
%doc %{_mandir}/man1/hwloc-calc.1*
%doc %{_mandir}/man1/hwloc-distances.1*
%doc %{_mandir}/man1/hwloc-distrib.1*
%doc %{_mandir}/man1/hwloc-gather-topology.1*
%doc %{_mandir}/man1/hwloc-info.1*
%doc %{_mandir}/man1/hwloc-ls.1*
%doc %{_mandir}/man1/hwloc-mask.1*
%doc %{_mandir}/man1/hwloc-ps.1*
%doc %{_mandir}/man1/lstopo.1*
%doc %{_mandir}/man7/hwloc.7*
%{_bindir}/hwloc-assembler
%{_bindir}/hwloc-assembler-remote
%{_bindir}/hwloc-bind
%{_bindir}/hwloc-calc
%{_bindir}/hwloc-distances
%{_bindir}/hwloc-distrib
%{_bindir}/hwloc-gather-topology
%{_bindir}/hwloc-info
%{_bindir}/hwloc-ls
%{_bindir}/hwloc-mask
%{_bindir}/hwloc-ps
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
* Thu Jan 26 2012 Dag Wieers <dag@wieers.com> - 1.4-1
- Updated to release 1.4.

* Wed Dec 21 2011 Dag Wieers <dag@wieers.com> - 1.3.1-1
- Updated to release 1.3.1.

* Mon Oct 24 2011 Dag Wieers <dag@wieers.com> - 1.3-1
- Updated to release 1.3.

* Mon Sep 05 2011 Dag Wieers <dag@wieers.com> - 1.2.1-1
- Updated to release 1.2.1.

* Tue Jul 26 2011 Yury V. Zaytsev <yury@shurup.com> - 1.2-2
- RFX'ed on RHEL6.

* Wed Apr 20 2011 Dag Wieers <dag@wieers.com> - 1.2-1
- Updated to release 1.2.

* Fri Apr 08 2011 Dag Wieers <dag@wieers.com> - 1.1.2-1
- Updated to release 1.1.2.

* Thu Jul 22 2010 Dag Wieers <dag@wieers.com> - 1.0.2-1
- Updated to release 1.0.2.

* Thu Jun 10 2010 Dag Wieers <dag@wieers.com> - 1.0.1-1
- Initial package. (using DAR)
