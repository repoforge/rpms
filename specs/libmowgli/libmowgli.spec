# $Id$
# Authority: dag

Summary: Development framework for C with high performance and flexible algorithms
Name: libmowgli
Version: 0.7.0
Release: 1%{?dist}
License: BSD
Group: Development/Libraries
URL: http://www.atheme.org/projects/mowgli.shtml

Source: http://distfiles.atheme.org/libmowgli-%{version}.tbz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
mowgli is a development framework for C (like GLib), which provides high
performance and highly flexible algorithms. It can be used as a suppliment
to GLib (to add additional functions (dictionaries, hashes), or replace
some of the slow GLib list manipulation functions), or stand alone.
It also provides a powerful hook system and convenient logging for your
code, as well as a high performance block allocator.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
%configure
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
%doc AUTHORS COPYING Mercurial-Access README doc/*
%{_libdir}/libmowgli.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/libmowgli/
%{_libdir}/libmowgli.so
%{_libdir}/pkgconfig/libmowgli.pc

%changelog
* Wed Jul 15 2009 Dag Wieers <dag@wieers.com> - 0.7.0-1
- Updated to release 0.7.0.

* Wed Oct 17 2007 Dag Wieers <dag@wieers.com> - 0.5.0-1
- Initial package. (using DAR)
