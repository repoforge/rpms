# $Id$
# Authority: dag

Summary: Implementation of the IPFIX Protocol
Name: libfixbuf
Version: 1.0.2
Release: 1%{?dist}
License: LGPLv2
Group: Development/Libraries
URL: http://tools.netsa.cert.org/fixbuf/

Source: http://tools.netsa.cert.org/releases/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: glib2-devel >= 2.4.7
#BuildRequires: libspread-devel
BuildRequires: lksctp-tools-devel
BuildRequires: pkgconfig

%description
libfixbuf aims to be a compliant implementation of the IPFIX Protocol
and message format, from which IPFIX Collecting Processes and
IPFIX Exporting Processes may be built.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig >= 0.8

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build

%configure \
    --disable-static

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
%doc AUTHORS COPYING NEWS README
%{_libdir}/libfixbuf-%{version}.so.*

%files devel
%defattr(-, root, root, 0755)
%doc doc/html
%{_includedir}/fixbuf/
%{_libdir}/libfixbuf.so
%{_libdir}/pkgconfig/libfixbuf.pc
%exclude %{_libdir}/libfixbuf.la

%changelog
* Tue Sep 13 2011 Yury V. Zaytsev <yury@shurup.com> - 1.0.2-1
- Fixed rpmlint warnings.
- Updated to release 1.0.2.

* Sun Aug 14 2011 Yury V. Zaytsev <yury@shurup.com> - 1.0.1-1
- Updated to release 1.0.1.

* Wed Feb 16 2011 Dag Wieers <dag@wieers.com> - 0.9.0-1
- Initial package. (using DAR)
