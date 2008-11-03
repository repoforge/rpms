# $Id$
# Authority: dag

Summary: Netfilter conntrack userspace library
Name: libnetfilter_conntrack
Version: 0.0.97
Release: 1
License: GPL
Group: System Environment/Libraries
URL: http://netfilter.org/

Source: http://netfilter.org/projects/libnetfilter_conntrack/files/libnetfilter_conntrack-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libnfnetlink-devel
BuildRequires: pkgconfig

%description
libnetfilter_conntrack is a userspace library providing a programming 
interface (API) to the in-kernel connection tracking state table.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: libnfnetlink-devel

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
%configure \
    --disable-rpath \
    --disable-static
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
%doc COPYING
#%{_libdir}/libnetfilter_conntrack.so.*
#%{_libdir}/libnetfilter_conntrack/nfct_*.so

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/libnetfilter_conntrack/libnetfilter_conntrack*.h
%{_includedir}/libnetfilter_conntrack/linux_nfnetlink_conntrack.h
%{_libdir}/libnetfilter_conntrack.so
%{_libdir}/libnetfilter_conntrack.so.1
%{_libdir}/libnetfilter_conntrack.so.1.2.0
%exclude %{_libdir}/libnetfilter_conntrack.la
%{_libdir}/pkgconfig/libnetfilter_conntrack.pc

%changelog
* Sat Oct 18 2008 Christoph Maser <cmr@financial.com> 0.0.97-1
- update version 0.0.97

* Thu Mar 22 2007 Dag Wieers <dag@wieers.com> - 0.0.50-1
- Initial package. (using DAR)
