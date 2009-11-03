# $Id$
# Authority: dag

Summary: Simple, secure, TCP communications library
Name: libsnet
Version: 0.0
%define real_version 20060320
Release: 20060320.1%{?dist}
License: BSD
Group: System Environment/Libraries
URL: http://sourceforge.net/projects/libsnet/

Source: libsnet-%{real_version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: openssl-devel, cyrus-sasl-devel, zlib-devel

%description
libsnet is a simple, secure, TCP communications library with support
for line & block IO, SSL, SASL, ZLIB.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n libsnet

%build
%configure \
    --enable-shared \
    --enable-static 
%{__make} %{?_smp_mflags} OPTOPTS="%{optflags} -fPIC -I/usr/kerberos/include"

%install
%{__rm} -rf %{buildroot}
#%{__make} install DESTDIR="%{buildroot}"
%makeinstall

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYRIGHT
%{_libdir}/libsnet.so.*
%{_libdir}/libsnet_p.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/snet.h
%{_libdir}/libsnet.a
%exclude %{_libdir}/libsnet.la
%{_libdir}/libsnet.so
%{_libdir}/libsnet_p.a
%exclude %{_libdir}/libsnet_p.la
%{_libdir}/libsnet_p.so

%changelog
* Sun Aug 06 2006 Dag Wieers <dag@wieers.com> - 0.0-20060320.1
- Initial package. (using DAR)
