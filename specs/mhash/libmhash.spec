# $Id$
# Authority: dag
# Upstream: <mhash-dev$lists,sf,net>

%define real_name mhash

Summary: Thread-safe hash library
Name: libmhash
Version: 0.9.1
Release: 1.2%{?dist}
License: LGPL
Group: System Environment/Libraries
URL: http://mhash.sourceforge.net/

Source: http://dl.sf.net/mhash/mhash-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Provides: %{real_name}
Obsoletes: %{real_name}

%description
mhash is a thread-safe hash library, implemented in C, and provides a
uniform interface to a large number of hash algorithms (MD5, SHA-1,
HAVAL, RIPEMD128, RIPEMD160, TIGER, GOST). These algorithms can be
used to compute checksums, message digests, and other signatures.
The HMAC support implements the basics for message authentication,
following RFC 2104.

%package devel
Summary: Header files and libraries for developing apps which will use mhash
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

Provides: %{real_name}-devel
Obsoletes: %{real_name}-devel

%description devel
The mhash-devel package contains the header files and libraries needed
to develop programs that use the mhash library.

Install the mhash-devel package if you want to develop applications that
will use the mhash library.

%prep
%setup -n %{real_name}-%{version}

%build
%configure \
	--disable-dependency-tracking \
	--enable-static \
	--enable-shared
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README THANKS TODO
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%doc doc/example.c doc/md5-rfc1321.txt doc/mhash.html doc/skid2-authentication
%doc %{_mandir}/man?/*
%{_libdir}/*.a
%{_libdir}/*.so
%{_includedir}/*.h
%exclude %{_libdir}/*.la

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.9.1-1.2
- Rebuild for Fedora Core 5.

* Sun Apr 18 2004 Dag Wieers <dag@wieers.com> - 0.9.1-1
- Updated to release 0.9.1.

* Thu Apr 17 2003 Dag Wieers <dag@wieers.com> - 0.8.18-0
- Updated to release 0.8.18.

* Fri Feb 21 2003 Dag Wieers <dag@wieers.com> - 0.8.17-0
- Renamed package from mhash to libmhash.

* Tue Jan 07 2003 Dag Wieers <dag@wieers.com> - 0.8.17-0
- Initial package. (using DAR)

