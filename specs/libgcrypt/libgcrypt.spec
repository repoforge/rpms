# $Id$
# Authority: dag
# Upstream: <gnupg-devel$gnupg,org>

# ExcludeDist: fc1 fc2 fc3 el4

Summary: GNU cryptographic library
Name: libgcrypt
Version: 1.1.12
Release: 1.2%{?dist}
License: LGPL
Group: System Environment/Libraries
URL: http://www.gnupg.org/

Source: ftp://ftp.gnupg.org/gcrypt/alpha/libgcrypt/libgcrypt-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libgpg-error-devel

%description
libgcrypt is a general purpose cryptographic library based on the code
from GNU Privacy Guard. It provides functions for all cryptograhic
building blocks: symmetric ciphers (AES, DES, Blowfish, CAST5,
Twofish, Arcfour), hash algorithms (MD5, RIPE-MD160, SHA-1,
TIGER-192), MACs (HMAC for all hash algorithms), public key algorithms
(RSA, ElGamal, DSA), large integer functions, random numbers and a lot
of supporting functions.

%package devel
Summary: Header files, libraries and development documentation for %{name}
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
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%post devel
/sbin/install-info %{_infodir}/gcrypt.info.gz %{_infodir}/dir

%preun devel
/sbin/install-info --delete %{_infodir}/gcrypt.info.gz %{_infodir}/dir

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING* NEWS README* THANKS TODO VERSION
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%doc %{_infodir}/*.info*
%{_bindir}/*
%{_includedir}/*.h
%{_libdir}/*.a
%{_libdir}/*.so
%{_datadir}/aclocal/*.m4
%exclude %{_libdir}/*.la
#%exclude %{_infodir}/dir

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.1.12-1.2
- Rebuild for Fedora Core 5.

* Wed Dec 31 2003 Dag Wieers <dag@wieers.com> - 1.1.12-0
- Initial package. (using DAR)
