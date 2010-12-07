# $Id$
# Authority: dag

Summary: Video Acceleration (VA) API for Linux
Name: libva
Version: 1.0.6
Release: 1%{?dist}
License: MIT
Group: System Environment/Libraries
URL: http://www.splitted-desktop.com/~gbeauchesne/libva/

Source0: http://cgit.freedesktop.org/libva/snapshot/libva-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libdrm-devel
BuildRequires: libtool
BuildRequires: libudev-devel
BuildRequires: libXext-devel
BuildRequires: libXfixes-devel
BuildRequires: mesa-libGL-devel

%description
Libva is a library providing the VA API video acceleration API.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
autoreconf -i
%configure \
    --disable-static \
    --enable-glx \
    --enable-i965-driver
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}" INSTALL="install -p"

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%doc COPYING
%{_bindir}/vainfo
%{_libdir}/libva.so.*
%{_libdir}/libva-glx.so.*
%{_libdir}/libva-tpi.so.*
%{_libdir}/libva-x11.so.*
%{_libdir}/dri/dummy_drv_video.so
%exclude %{_bindir}/h264encode
%exclude %{_bindir}/mpeg2vldemo
%exclude %{_bindir}/putsurface
%exclude %{_bindir}/test_*
%exclude %{_libdir}/dri/dummy_drv_video.la

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/va/
%{_libdir}/libva.so
%{_libdir}/libva-glx.so
%{_libdir}/libva-tpi.so
%{_libdir}/libva-x11.so
%{_libdir}/pkgconfig/libva.pc
%{_libdir}/pkgconfig/libva-glx.pc
%{_libdir}/pkgconfig/libva-tpi.pc
%{_libdir}/pkgconfig/libva-x11.pc
%exclude %{_libdir}/libva.la
%exclude %{_libdir}/libva-glx.la
%exclude %{_libdir}/libva-tpi.la
%exclude %{_libdir}/libva-x11.la

%changelog
* Mon Dec 06 2010 Dag Wieers <dag@wieers.com> - 1.0.6-1
- Initial package. (using DAR)
