# $Id$
# Authority: dag
# Upstream: John Smith <imipak$sf,net>

%define real_name mcrypt

Summary: Data encryption library
Name: libmcrypt
Version: 2.5.7
Release: 1.2%{?dist}
License: LGPL
Group: System Environment/Libraries
URL: http://mcrypt.sourceforge.net/

Source: http://dl.sf.net/mcrypt/libmcrypt-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libtool >= 1.3.4

%description
libmcrypt is a data encryption library. The library is thread safe
and provides encryption and decryption functions. This version of the
library supports many encryption algorithms and encryption modes. Some
algorithms which are supported:
SERPENT, RIJNDAEL, 3DES, GOST, SAFER+, CAST-256, RC2, XTEA, 3WAY,
TWOFISH, BLOWFISH, ARCFOUR, WAKE and more.

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
%configure \
	--program-prefix="%{?_program_prefix}" \
	--disable-dependency-tracking \
	--enable-static
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

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
%{_datadir}/aclocal/*.m4
%exclude %{_libdir}/*.la

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 2.5.7-1.2
- Rebuild for Fedora Core 5.

* Fri Apr 16 2004 ---
- Updated URL and Source tags. (Russ Herrold)

* Wed Jul 30 2003 Dag Wieers <dag@wieers.com> - 2.5.7-1
- Added static library.

* Thu Apr 17 2003 Dag Wieers <dag@wieers.com> - 2.5.7-0
- Updated to release 2.5.7.

* Fri Feb 21 2003 Dag Wieers <dag@wieers.com> - 2.5.6-0
- Updated to release 2.5.6.
- Fixed the --program-prefix problem.

* Tue Jan 07 2003 Dag Wieers <dag@wieers.com> - 2.5.5-0
- Initial package. (using DAR)
