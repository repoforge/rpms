# $Id$
# Authority: dag
# Upstream: Dug Song <dugsong$monkey,org>
# Upstream: <libdnet-devel$lists,sf,net>

Summary: Non-blocking DNS resolver library
Name: libdnsres
Version: 0.1a
Release: 4%{?dist}
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
%configure --with-pic
%{__make} %{?_smp_mflags}

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
%exclude %{_libdir}/libdnsres.la
%{_libdir}/libdnsres.so

%changelog
* Sun Mar 25 2007 Dag Wieers <dag@wieers.com> - 0.2-5
- Rebuild against libevent-1.1a on EL5.

* Wed Mar 07 2007 Dag Wieers <dag@wieers.com> - 0.2-4
- Rebuild against libevent-1.3b.

* Tue Feb 20 2007 Dag Wieers <dag@wieers.com> - 0.1a-2
- Rebuild against libevent-1.3a.

* Tue Feb 21 2006 Dag Wieers <dag@wieers.com> - 0.1a-1
- Initial package. (using DAR)
