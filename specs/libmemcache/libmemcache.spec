# $Id$
# Authority: yury
# Upstream: Sean Chittenden <seanc$FreeBSD,org>

%define real_version 1.4.0.rc2

Summary: A client library for memcached
Name: libmemcache
Version: 1.4.0
Release: 0.1.rc2%{?dist}
License: BSD 3-Clause
Group: System Environment/Libraries
URL: http://people.freebsd.org/~seanc/libmemcache/

Source: http://people.freebsd.org/~seanc/libmemcache/%{name}-%{real_version}.tar.bz2
Patch0: libmemcache-1.4.0.rc2.patch

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
libmemcache implements a C client API for the superior memcached from Danga
Interactive.

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n %{name}-%{real_version}
%patch0 -p2 -b .cmemcache

%build
%configure
%{__make} %{?_smp_mflags} CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%doc COPYING ChangeLog
%{_libdir}/libmemcache.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/memcache*
%{_libdir}/libmemcache.so
%exclude %{_libdir}/libmemcache.a
%exclude %{_libdir}/libmemcache.la

%changelog
* Sun Dec 27 2009 Yury V. Zaytsev <yury@shurup.com> - 1.4.0-0.1.rc2
- Initial package.
- Thanks to Tom G. Christensen <swpkg@statsbiblioteket.dk>!
