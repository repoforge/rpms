# $Id$
# Authority: dag

### EL6 ships with openobex-1.4-7.el6
### EL5 ships with openobex-1.3-3.1
# ExclusiveDist: el2 el3 el4

### undefined reference to `usb_get_string_simple' in obexftp linking
%{?el3:%define _without_libusb018 1}
%{?rh9:%define _without_libusb018 1}
%{?rh7:%define _without_libusb018 1}
%{?el2:%define _without_libusb018 1}

Summary: Library for using OBEX
Name: openobex
### FC5 comes with openobex 1.1, we hope that RHEL5 will come with 1.3 so we can upgrade
Version: 1.1
Release: 1%{?dist}
License: LGPL
Group: System Environment/Libraries
#URL: http://openobex.sourceforge.net/
URL: http://openobex.triq.net/

Source: http://dl.sf.net/openobex/openobex-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: glib-devel >= 1.2.0, bluez-libs-devel
%{?!_without_libusb018:BuildRequires: libusb-devel >= 0.1.8}

%description
Open OBEX shared c-library.

%package devel
Summary: Header files, libraries and development documentation for %{name}
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
%{?_without_libusb18:--disable-usb}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall \
	includedir="%{buildroot}%{_includedir}/openobex"

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING* NEWS README
%{_libdir}/libopenobex.so.*

%files devel
%defattr(-, root, root, 0755)
%{_datadir}/aclocal/openobex.m4
%{_includedir}/openobex/
%{_libdir}/libopenobex.a
%exclude %{_libdir}/libopenobex.la
%{_libdir}/libopenobex.so
%{_libdir}/pkgconfig/openobex.pc

%changelog
* Sat Aug 19 2006 Dag Wieers <dag@wieers.com> - 1.1-1
- Updated to release 1.1.

* Wed Feb 04 2004 Dag Wieers <dag@wieers.com> - 1.0.1-1
- Rebuild against bluez-libs-devel (bluetooth support).

* Wed Oct 29 2003 Dag Wieers <dag@wieers.com> - 1.0.1-0
- Initial package. (using DAR)
