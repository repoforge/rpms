# $Id$
# Authority: matthias
# Upstream: <libdvdplay-devel$videolan,org>

Summary: Portable abstraction library for DVD menus support
Name: libdvdplay
Version: 1.0.1
Release: 0%{?dist}
License: GPL
Group: System Environment/Libraries
URL: http://www.videolan.org/libdvdplay/

Source: http://www.videolan.org/pub/libdvdplay/%{version}/libdvdplay-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Buildrequires: libdvdread-devel

%description
libdvdplay is a portable abstraction library for DVD menus support, it
provides a simple API to access a DVD device as a block device.

This package contains the libdbdplay runtime library.

%package devel
Summary: Development tools for programs which will use the %{name} library
Group: Development/Libraries
Requires: %{name} = %{version}

%description devel
The %{name}-devel package includes the header files and static libraries
necessary for developing programs which will manipulate DVDs files using
the %{name} library.

If you are going to develop programs which will manipulate DVDs, you
should install %{name}-devel.  You'll also need to have the %{name}
package installed.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/*.la

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README THANKS TODO
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_libdir}/*.a
%{_libdir}/*.so
%{_includedir}/dvdplay/
#exclude %{_libdir}/*.la

%changelog
* Tue Mar 11 2003 Dag Wieers <dag@wieers.com> - 1.0.1-0
- Updated to release 1.0.1.

* Mon Feb 17 2003 Dag Wieers <dag@wieers.com> - 1.0.0-1
- Rebuild against newer libdvdread-0.9.4.

* Wed Feb 05 2003 Dag Wieers <dag@wieers.com> - 1.0.0-0
- Initial package. (using DAR)
