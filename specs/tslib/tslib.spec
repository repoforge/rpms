# $Id$
# Authority: dag

Summary: Abstraction layer for touchscreen panel event
Name: tslib
Version: 1.0
Release: 1
License: LGPL
Group: System Environment/Libraries
URL: http://tslib.berlios.de/

Source: http://download.berlios.de/tslib/tslib-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
tslib is an abstraction layer for touchscreen panel events, as well as
a filter stack for the manipulation of those events. It was created by
Russell King, of arm.linux.org.uk. Examples of implemented filters
include jitter smoothing and the calibration transform.

tslib is generally used on embedded devices to provide a common user
space interface to touchscreen functionality. It is supported by
Kdrive (aka TinyX) and OPIE as well as being used on a number of
commercial Linux devices including the Nokia 770.

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
autoreconf --force --install --symlink
%configure --disable-static
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
%doc AUTHORS ChangeLog README
%config(noreplace) %{_sysconfdir}/ts.conf
%{_bindir}/ts_*
%{_libdir}/libts-*.so.*
%{_libdir}/ts/
%exclude %{_libdir}/ts/*.la

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/tslib.h
%{_libdir}/libts.so
%{_libdir}/pkgconfig/tslib-*.pc
%exclude %{_libdir}/libts.la

%changelog
* Mon Sep 22 2008 Dag Wieers <dag@wieers.com> - 1.0-1
- Initial package. (using DAR)
