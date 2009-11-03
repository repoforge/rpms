# $Id$
# Authority: dag

Summary: Provides basic parts of the OpenPGP message format.
Name: opencdk
Version: 0.5.8
Release: 1.2%{?dist}
License: GPL
Group: System Environment/Libraries
URL: http://www.gnu.org/software/gnutls/download.html

Source: ftp://ftp.gnutls.org/pub/gnutls/opencdk/opencdk-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libgcrypt-devel >= 1.2, zlib-devel, perl, gcc-c++

%description
This library provides basic parts of the OpenPGP message format.  For
reference, please read RFC2440. Due to some possible security problems,
the library also implements parts of draft-ietf-openpgp-rfc2440bis-06.txt.

The aim of the library is *not* to replace any available OpenPGP version.
There will be no real support for key management (sign, revoke, alter
preferences, ...) and some other parts are only rudimentary available. The
main purpose is to handle and understand OpenPGP packets and to use basic
operations. For example to encrypt/decrypt or to sign/verify and packet
routines.

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
%configure
%{__make} %{?_smp_mflags}

%{__perl} -pi.orig -e '
		s|^(\S.*[\s"])-L/usr/lib([\s"])|$1$2|g;
		s|^(\S.*[\s"])-I/usr/include([\s"])|$1$2|g;
	' src/opencdk-config

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
%doc AUTHORS ChangeLog COPYING NEWS README* THANKS TODO
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%doc doc/*.html doc/DETAILS
%{_bindir}/*
%{_includedir}/*
%{_libdir}/*.a
%exclude %{_libdir}/*.la
%{_libdir}/*.so

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.5.8-1.2
- Rebuild for Fedora Core 5.

* Fri Nov 11 2005 Dries Verachtert <dries@ulyssis.org> - 0.5.8-1
- Updated to release 0.5.8.

* Wed Dec 31 2003 Dag Wieers <dag@wieers.com> - 0.4.5-0
- Initial package. (using DAR)
