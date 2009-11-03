# $Id$
# Authority: dag

%{?dtag: %{expand: %%define %dtag 1}}

%{?el4:%define _without_gstreamer10 1}
%{?el3:%define _without_gstreamer10 1}

Summary: Portable libraries for the high quality Dirac video codec
Name: schroedinger
Version: 1.0.7
Release: 1%{?dist}
License: GPL
Group: System Environment/Libraries
URL: http://www.diracvideo.org/

Source: http://www.diracvideo.org/download/schroedinger/schroedinger-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%{!?_without_gstreamer10:BuildRequires: gstreamer-devel >= 0.10}
%{!?_without_gstreamer10:BuildRequires: gstreamer-plugins-base-devel >= 0.10}
BuildRequires: gtk-doc
BuildRequires: liboil-devel >= 0.3.16

%description
The Schrödinger project will implement portable libraries for the high
quality Dirac video codec created by BBC Research and
Development. Dirac is a free and open source codec producing very high
image quality video.

The Schrödinger project is a project done by BBC R&D and Fluendo in
order to create a set of high quality decoder and encoder libraries
for the Dirac video codec.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig
Requires: liboil-devel >= 0.3.16

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%package -n gstreamer-plugins-schroedinger
Group: Applications/Multimedia
Summary: GStreamer Plugins that implement Dirac video encoding and decoding

%description -n gstreamer-plugins-schroedinger
GStreamer Plugins that implement Dirac video encoding and decoding

%prep
%setup

%build
%configure \
    --disable-gtk-doc \
    --disable-static \
%{?_without_gstreamer10:--disable-gstreamer}
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
%doc COPYING* NEWS TODO
%{_libdir}/libschroedinger-1.0.so.*

%files devel
%defattr(-, root, root, 0755)
%doc %{_datadir}/gtk-doc/html/schroedinger
%{_includedir}/schroedinger-1.0/
%{_libdir}/libschroedinger-1.0.so
%{_libdir}/pkgconfig/schroedinger-1.0.pc
%exclude %{_libdir}/libschroedinger-1.0.la

%if %{!?_without_gstreamer10:1}0
%files -n gstreamer-plugins-schroedinger
%defattr(-, root, root, 0755)
%dir %{_libdir}/gstreamer-0.10/
%{_libdir}/gstreamer-0.10/libgstschro.so
%exclude %{_libdir}/gstreamer-0.10/libgstschro.la
%endif

%changelog
* Tue Jul 14 2009 Dag Wieers <dag@wieers.com> - 1.0.7-1
- Initial packages. (using DAR)
