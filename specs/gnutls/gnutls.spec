# $Id$
# Authority: matthias

### EL6 ships with gnutls-2.8.5-4.el6
### EL5 ships with gnutls-1.4.1-3.el5_4.8
### EL4 ships with gnutls-1.0.20-4.el4_8.7
# ExclusiveDist: el2 el3

Summary: The GNU Transport Layer Security library
Name: gnutls
Version: 1.0.13
Release: 1%{?dist}
License: LGPL/GPL
Group: System Environment/Libraries
URL: http://www.gnu.org/software/gnutls/

Source: ftp://ftp.gnutls.org/pub/gnutls/gnutls-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: zlib-devel, lzo-devel, opencdk-devel >= 0.5.2

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
%makeinstall

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING* doc/TODO NEWS README THANKS
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%doc doc/examples/ doc/README* doc/tex/gnutls.ps
%doc %{_mandir}/man1/*
%{_bindir}/*-config
%{_includedir}/*
%{_libdir}/*.a
%{_libdir}/*.la
%exclude %{_libdir}/*.so
%{_datadir}/aclocal/*.m4

%files utils
%defattr(-, root, root, 0755)
%{_bindir}/gnutls-*
%{_bindir}/*tool

%changelog
* Mon May 17 2004 Dag Wieers <dag@wieers.com> - 1.0.13-1
- Updated to release 1.0.13.

* Sat Feb 28 2004 Matthias Saou <http://freshrpms.net/> 1.0.7-1.fr
- Takeover the spec, update to 1.0.7.

* Wed Dec 31 2003 Dag Wieers <dag@wieers.com> - 0.8.10-0
- Initial package. (using DAR)
