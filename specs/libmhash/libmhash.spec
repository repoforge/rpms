# $Id$

# Authority: dag

%define rname mhash

Summary: Thread-safe hash library
Name: libmhash
Version: 0.8.18
Release: 0
License: LGPL
Group: System Environment/Libraries
URL: http://mhash.sf.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://mhash.sf.net/dl/%{rname}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


Provides: %{rname}
Obsoletes: %{rname}

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

Provides: %{rname}-devel
Obsoletes: %{rname}-devel

%description devel
The mhash-devel package contains the header files and libraries needed
to develop programs that use the mhash library.

Install the mhash-devel package if you want to develop applications that
will use the mhash library.

%prep
%setup -n %{rname}-%{version}

%build
%configure \
	--disable-dependency-tracking \
	--enable-static \
	--enable-shared
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/*.la

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
%doc %{_mandir}/man3/*
%{_libdir}/*.a
%{_libdir}/*.so
%{_includedir}/*.h
#exclude %{_libdir}/*.la

%changelog
* Thu Apr 17 2003 Dag Wieers <dag@wieers.com> - 0.8.18-0
- Updated to release 0.8.18.

* Fri Feb 21 2003 Dag Wieers <dag@wieers.com> - 0.8.17-0
- Renamed package from mhash to libmhash.

* Tue Jan 07 2003 Dag Wieers <dag@wieers.com> - 0.8.17-0
- Initial package. (using DAR)

