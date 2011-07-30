# $Id$
# Authority: dag
# Upstream: <mhash-dev$lists,sf,net>

Summary: Thread-safe hash library
Name: mhash
Version: 0.9.9
Release: 1%{?dist}
License: LGPL
Group: System Environment/Libraries
URL: http://mhash.sourceforge.net/

Source: http://dl.sf.net/mhash/mhash-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Provides: libmhash = %{version}-%{release}
Obsoletes: libmhash <= %{version}-%{release}

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

Provides: libmhash-devel = %{version}-%{release}
Obsoletes: libmhash-devel <= %{version}-%{release}

%description devel
The mhash-devel package contains the header files and libraries needed
to develop programs that use the mhash library.

Install the mhash-devel package if you want to develop applications that
will use the mhash library.

%prep
%setup

%build
%configure \
    --program-prefix="%{?_program_prefix}" \
    --disable-dependency-tracking \
    --disable-static \
    --enable-shared
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README THANKS TODO
%{_libdir}/libmhash.so.*

%files devel
%defattr(-, root, root, 0755)
%doc doc/example.c doc/skid2-authentication
%doc %{_mandir}/man3/mhash.3*
%{_includedir}/mhash.h
%{_includedir}/mutils/
%{_libdir}/libmhash.so
%exclude %{_libdir}/libmhash.la

%changelog
* Wed Jul 20 2011 Dag Wieers <dag@wieers.com> - 0.9.9-1
- Rename package back from libmhash to mhash since it is in CentOS Extras.

* Sun Apr 18 2004 Dag Wieers <dag@wieers.com> - 0.9.1-1
- Updated to release 0.9.1.

* Thu Apr 17 2003 Dag Wieers <dag@wieers.com> - 0.8.18-0
- Updated to release 0.8.18.

* Fri Feb 21 2003 Dag Wieers <dag@wieers.com> - 0.8.17-0
- Renamed package from mhash to libmhash.

* Tue Jan 07 2003 Dag Wieers <dag@wieers.com> - 0.8.17-0
- Initial package. (using DAR)

