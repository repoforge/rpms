# $Id$
# Authority: shuff
# Upstream: <LScube-devel$lscube,org>

Summary: Netembryo network abstraction library
Name: netembryo
Version: 0.1.1
Release: 1
License: LGPL
Group: System Environment/Libraries
URL: http://lscube.org/projects/netembryo

Source: http://lscube.org/files/downloads/%{name}/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc >= 3.4, make >= 3.80, libtool >= 1.5.20
BuildRequires: lksctp-tools-devel
BuildRequires: openssl-devel
BuildRequires: autoconf, automake
BuildRequires: gawk

Requires: openssl

%description
Netembryo is a network abstraction library  plus some misc utility
functions used as foundation for feng, libnemesi, felix.

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
%configure --disable-static --disable-dependency-tracking
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%doc README COPYING AUTHORS ChangeLog TODO
%{_libdir}/libnetembryo.so.*

%files devel
%defattr(-, root, root, 0755)
%doc README COPYING AUTHORS ChangeLog TODO
%{_includedir}/netembryo/*.h
%exclude %{_libdir}/libnetembryo.la
%{_libdir}/libnetembryo.so
%{_libdir}/pkgconfig/libnetembryo*.pc

%changelog
* Tue Sep 08 2009 Steve Huff <shuff_@_hmdc.harvard.edu> - 0.1.1-1
- initial package
