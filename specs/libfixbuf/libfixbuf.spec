# $Id$
# Authority: dag

Summary: fixbuf IPFIX implementation library
Name: libfixbuf
Version: 0.9.0
Release: 1%{?dist}
License: LGPL
Group: Libraries
URL: http://tools.netsa.cert.org/fixbuf/

Source: http://tools.netsa.cert.org/releases/libfixbuf-%{version}.tar.gz
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
%configure
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
%doc AUTHORS COPYING ChangeLog NEWS README
%{_libdir}/libfixbuf-%{version}.so.*

%files devel
%defattr(-, root, root, 0755)
%doc doc/html
%{_includedir}/fixbuf/
%{_libdir}/libfixbuf.so
%{_libdir}/pkgconfig/libfixbuf.pc
%exclude %{_libdir}/libfixbuf.a
%exclude %{_libdir}/libfixbuf.la

%changelog
* Wed Feb 16 2011 Dag Wieers <dag@wieers.com> - 0.9.0-1
- Initial package. (using DAR)
