# $Id$
# Authority: dag
# Upstream: Dug Song <dugsong$monkey,org>
# Upstream: <libdnet-devel$lists,sf,net>

Summary: Non-blocking DNS resolver library
Name: libdnsres
Version: 0.1a
Release: 1
License: BSD-like
Group: System Environment/Libraries
URL: http://www.monkey.org/~provos/libdnsres/

Source: http://www.monkey.org/~provos/libdnsres-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libevent-devel

%description
ibdnsres provides a non-blocking thread-safe API for resolving DNS names.
It requires that your main application is built on top of libevent.
Libdnsres' API essentially mirrors the traditional gethostbyname and
getaddrinfo interfaces. All return values have been replaced by callbacks
instead.

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
%configure
%{__make} %{?_smp_mflags} \
	COPTFLAG="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_libdir}/libdnsres.so.*

%files devel
%defattr(-, root, root, 0755)
%doc %{_mandir}/man3/dnsres.3*
%{_includedir}/dnsres.h
%{_libdir}/libdnsres.a
%{_libdir}/libdnsres.so
%exclude %{_libdir}/libdnsres.la

%changelog
* Tue Feb 21 2006 Dag Wieers <dag@wieers.com> - 1.11-1
- Updated to release 1.11.

* Wed Oct 22 2003 Dag Wieers <dag@wieers.com> - 1.7-0
- Initial package. (using DAR)
