# $Id$


Summary:  The GNU Transport Layer Security library
Name: gnutls
Version: 1.0.7
Release: 1.fr
License: LGPL/GPL
Group: System Environment/Libraries
URL: http://www.gnu.org/software/gnutls/
Source: ftp://ftp.gnutls.org/pub/gnutls/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: zlib-devel, lzo-devel

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
%setup -q


%build
%configure --with-included-libtasn1
%{__make} %{?_smp_mflags}

%{__perl} -pi -e 's|^(\S.*[\s"])-L/usr/lib([\s"])|$1$2|g;
                  s|^(\S.*[\s"])-I/usr/include([\s"])|$1$2|g;' */*-config


%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -f %{buildroot}%{_libdir}/*.la


%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING* NEWS README THANKS doc/TODO
%{_libdir}/*.so.*


%files devel
%defattr(-, root, root, 0755)
%doc doc/tex/gnutls.ps doc/examples/ doc/README*
%{_bindir}/*-config
%{_includedir}/*
%{_libdir}/*.a
%{_libdir}/*.so
%{_datadir}/aclocal/*.m4


%files utils
%defattr(-, root, root, 0755)
%{_bindir}/gnutls-*


%changelog
* Sat Feb 28 2004 Matthias Saou <http://freshrpms.net/> 1.0.7-1.fr
- Takeover the spec, update to 1.0.7.

* Wed Dec 31 2003 Dag Wieers <dag@wieers.com> - 0.8.10-0
- Initial package. (using DAR)

