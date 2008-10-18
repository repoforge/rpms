# $Id$
# Authority: dag

Summary: Netfilter netlink userspace library
Name: libnfnetlink
Version: 0.0.39
Release: 1
License: GPL
Group: System Environment/Libraries
URL: http://netfilter.org/

Source: http://netfilter.org/projects/libnfnetlink/files/libnfnetlink-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
libnfnetlink is a userspace library that provides some low-level
nfnetlink handling functions. It is used as a foundation for other, netfilter
subsystem specific libraries such as libnfnetlink_conntrack, libnfnetlink_log
and libnfnetlink_queue.

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
%doc README
%{_libdir}/libnfnetlink.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/libnfnetlink/libnfnetlink.h
%{_includedir}/libnfnetlink/linux_nfnetlink.h
%{_includedir}/libnfnetlink/linux_nfnetlink_compat.h
%exclude %{_libdir}/libnfnetlink.la
%{_libdir}/libnfnetlink.so
%{_libdir}/pkgconfig/libnfnetlink.pc

%changelog
* Sat Oct 18 2008 Christoph Maser <cmr@financial.com> - 0.0.39-1
- Update to version 0.0.39

* Thu Mar 22 2007 Dag Wieers <dag@wieers.com> - 0.0.25-1
- Initial package. (using DAR)
