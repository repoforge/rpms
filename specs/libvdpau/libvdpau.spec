# $Id$
# Authority: cheusov
# Upstream: NVIDIA

Summary: Video Decode and Presentation API for Unix
Name: libvdpau
Version: 0.4.1
Release: 1%{?dist}
License: MIT
Group: System Environment/Libraries
URL: http://http.download.nvidia.com/XFree86/vdpau/doxygen/html/

Source: http://people.freedesktop.org/~aplattner/vdpau/libvdpau-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libX11-devel
BuildRequires: libXext-devel
BuildRequires: libtool
BuildRequires: make

%description
The Video Decode and Presentation API for Unix (VDPAU) provides a
complete solution for decoding, post-processing, compositing, and
displaying compressed or uncompressed video streams. These video
streams may be combined (composited) with bitmap content, to implement
OSDs and other application user interfaces.  This VDPAU API allows
video programs to offload portions of the video decoding process and
video post-processing to the GPU video-hardware.

%package devel
Summary: Header files, libraries and development documentation for %{name}
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
%configure \
    --disable-documentation \
    --disable-static
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
%doc AUTHORS COPYING NEWS README
%doc doc/vdpau_data_flow.png
%{_libdir}/libvdpau.so.*
%dir %{_libdir}/vdpau/
%{_libdir}/vdpau/libvdpau_trace.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/vdpau/
%{_libdir}/libvdpau.so
%{_libdir}/pkgconfig/vdpau.pc
%dir %{_libdir}/vdpau/
%{_libdir}/vdpau/libvdpau_trace.so
%exclude %{_libdir}/libvdpau.la
%exclude %{_libdir}/vdpau/libvdpau_trace.la

%changelog
* Wed Oct 11 2011 Aleksey Cheusov <vle@gmx.net> - 0.4.1-1
- Initial package.
