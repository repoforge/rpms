# $Id$
# Authority: dag

Summary: Universal Plug and Play (UPnP) SDK
Name: libupnp
Version: 1.4.2
Release: 1%{?dist}
License: BSD
Group: System Environment/Libraries
URL: http://pupnp.sourceforge.net/

Source: http://dl.sf.net/pupnp/libupnp-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
The Universal Plug and Play (UPnP) SDK for Linux provides 
support for building UPnP-compliant control points, devices, 
and bridges on Linux.

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
%configure \
    --disable-static \
    --with-documentation="/rpm-doc"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

### Clean up buildroot
%{__mv} -f %{buildroot}/rpm-doc/ .

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL LICENSE NEWS README THANKS TODO
%{_libdir}/libixml.so.*
%{_libdir}/libthreadutil.so.*
%{_libdir}/libupnp.so.*

%files devel
%defattr(-, root, root, 0755)
%doc rpm-doc/*
%{_includedir}/upnp/
%{_libdir}/libixml.so
%{_libdir}/libthreadutil.so
%{_libdir}/libupnp.so
%{_libdir}/pkgconfig/libupnp.pc
%exclude %{_libdir}/libixml.la
%exclude %{_libdir}/libthreadutil.la
%exclude %{_libdir}/libupnp.la

%changelog
* Wed Feb 21 2007 Dag Wieers <dag@wieers.com> - 1.4.2-1
- Initial package. (using DAR)
