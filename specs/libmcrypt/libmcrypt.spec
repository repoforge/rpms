# Authority: dag

%define rname mcrypt

Summary: libmcrypt is a data encryption library.
Name: libmcrypt
Version: 2.5.7
Release: 1
License: LGPL
Group: System Environment/Libraries
URL: http://mcrypt.hellug.gr/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: ftp://mcrypt.hellug.gr/pub/crypto/mcrypt/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: libtool >= 1.3.4

%description
libmcrypt is a data encryption library. The library is thread safe
and provides encryption and decryption functions. This version of the
library supports many encryption algorithms and encryption modes. Some
algorithms which are supported:
SERPENT, RIJNDAEL, 3DES, GOST, SAFER+, CAST-256, RC2, XTEA, 3WAY,
TWOFISH, BLOWFISH, ARCFOUR, WAKE and more.

%package devel
Summary: Development files of the libmcrypt data encryption library.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
Header file and static libraries of libmcrypt data encryption library.

%prep
%setup

%build
%configure \
	--program-prefix="%{?_program_prefix}" \
	--disable-dependency-tracking \
	--enable-static
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/*.la

%clean
%{__rm} -rf %{buildroot}

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING.LIB KNOWN-BUGS NEWS README THANKS TODO
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%doc doc/README* doc/example.c
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_libdir}/*.a
%{_libdir}/*.so
%{_includedir}/*.h
%{_datadir}/aclocal/*
#exclude %{_libdir}/*.la

%changelog
* Wed Jul 30 2003 Dag Wieers <dag@wieers.com> - 2.5.7-1
- Added static library.

* Thu Apr 17 2003 Dag Wieers <dag@wieers.com> - 2.5.7-0
- Updated to release 2.5.7.

* Fri Feb 21 2003 Dag Wieers <dag@wieers.com> - 2.5.6-0
- Updated to release 2.5.6.
- Fixed the --program-prefix problem.

* Tue Jan 07 2003 Dag Wieers <dag@wieers.com> - 2.5.5-0
- Initial package. (using DAR)
