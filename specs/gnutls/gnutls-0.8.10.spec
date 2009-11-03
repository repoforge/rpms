# $Id$
# Authority: dag

Summary: The GNU Transport Layer Security library
Name: gnutls
Version: 0.8.10
Release: 2%{?dist}
License: LGPL/GPL
Group: System Environment/Libraries
URL: http://www.gnu.org/software/gnutls/

Source: ftp://ftp.gnutls.org/pub/gnutls/attic/gnutls-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: zlib-devel, lzo-devel, opencdk-devel

%description
GnuTLS is a project that aims to develop a library which provides a secure
layer, over a reliable transport layer. Currently the GnuTLS library
implements the proposed standards by the IETF's TLS working group.

Quoting from RFC2246 - the TLS 1.0 protocol specification:
"The TLS protocol provides communications privacy over the Internet.
 The protocol allows client/server applications to communicate in a way that

%package devel
Summary: Header files, libraries and development documentation for GnuTLS
Group: Development/Libraries
Requires: %{name} = %{version}

%description devel
GnuTLS is a project that aims to develop a library which provides a secure
layer, over a reliable transport layer. Currently the GnuTLS library
implements the proposed standards by the IETF's TLS working group.

This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%package utils
Summary: Utilities for the GNU Transport Layer Security library
Group: Applications/System
Requires: %{name} = %{version}

%description utils
GnuTLS is a project that aims to develop a library which provides a secure
layer, over a reliable transport layer. Currently the GnuTLS library
implements the proposed standards by the IETF's TLS working group.

This package contains some tools using for GnuTLS.

%prep
%setup

%build
%configure --with-included-libtasn1
%{__make} %{?_smp_mflags}

%{__perl} -pi -e 's|^(\S.*[\s"])-L/usr/lib([\s"])|$1$2|g;
                  s|^(\S.*[\s"])-I/usr/include([\s"])|$1$2|g;' */*-config

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING* NEWS README THANKS doc/TODO
%{_libdir}/libgnutls.so.*
%{_libdir}/libgnutls-extra.so.*

%files devel
%defattr(-, root, root, 0755)
%doc doc/tex/gnutls.ps doc/examples/ doc/README*
#%doc %{_mandir}/man1/*
%{_bindir}/libgnutls-config
%{_bindir}/libgnutls-extra-config
%{_datadir}/aclocal/libgnutls.m4
%{_datadir}/aclocal/libgnutls-extra.m4
%{_includedir}/gnutls/
%{_libdir}/libgnutls.so
%{_libdir}/libgnutls-extra.so
%exclude %{_libdir}/libgnutls.a
%exclude %{_libdir}/libgnutls.la
%exclude %{_libdir}/libgnutls-extra.a
%exclude %{_libdir}/libgnutls-extra.la

%files utils
%defattr(-, root, root, 0755)
%{_bindir}/gnutls-*
#%{_bindir}/*tool

%changelog
* Wed Dec 31 2003 Dag Wieers <dag@wieers.com> - 0.8.10-2
- Cosmetic cleanup.
- Added .so files to libgnutls-devel.

* Wed Dec 31 2003 Dag Wieers <dag@wieers.com> - 0.8.10-1
- Initial package. (using DAR)
