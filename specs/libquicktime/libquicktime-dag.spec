# $Id$
# Authority: matthias
# Upstream: <libquicktime-devel@lists.sf.net>

%{?dist: %{expand: %%define %dist 1}}

Summary: Library for reading and writing quicktime files
Name: libquicktime
Version: 0.9.2
Release: 1
License: GPL
Group: System Environment/Libraries
URL: http://libquicktime.sf.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/libquicktime/libquicktime-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

### When MMX is enabled
BuildArch: i586
BuildRequires: autoconf, automake, libpng-devel >= 1.0.8, libjpeg-devel
BuildRequires: libdv-devel, libogg-devel, libvorbis-devel
BuildRequires: glib-devel
%{?fc2:BuildRequires: libraw1394-devel, libavc1394-devel}
%{?fc1:BuildRequires: libraw1394-devel, libavc1394-devel}
%{?el3:BuildRequires: libraw1394-devel, libavc1394-devel}
%{?rh9:BuildRequires: libraw1394-devel, libavc1394-devel}
%{?rh8:BuildRequires: libraw1394-devel, libavc1394-devel}

%description
Libquicktime is a library for reading and writing QuickTime files
on UNIX systems. Video CODECs supported by this library are OpenDivX, MJPA,
JPEG Photo, PNG, RGB, YUV 4:2:2, and YUV 4:2:0 compression.  Supported
audio CODECs are Ogg Vorbis, IMA4, ulaw, and any linear PCM format.

Libquicktime is based on the quicktime4linux library.  Libquicktime add
features such as a GNU build tools-based build process and dynamically
loadable CODECs.

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

### FIXME: Fix plugin compilation
#%{__perl} -pi.orig -e 's|^(LDFLAGS) = |$1 = -L../../src/.libs |' plugins/*/Makefile
#%{__perl} -pi.orig -e 's|^(LQT_LIBS) = |$1 = -L../../src/.libs |g' plugins/Makefile plugins/*/Makefile

%build
%configure \
	--disable-dependency-tracking

### FIXME: Disabled ffmpeg build (fails)
%{__perl} -pi.orig -e 's|^libavcodec_subdirs = ffmpeg|libavcodec_subdirs = |' plugins/Makefile

%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%doc %{_mandir}/man?/*
%dir %{_libdir}/libquicktime/
%{_bindir}/lqtplay
%{_bindir}/qt*
%{_libdir}/*.so.*
%{_libdir}/libquicktime/*.so

%files devel
%defattr(-, root, root, 0755)
%dir %{_libdir}/libquicktime/
%{_bindir}/*config
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/libquicktime/
%{_includedir}/quicktime/*.h
%{_datadir}/aclocal/*.m4
%exclude %{_libdir}/*.la
%exclude %{_libdir}/libquicktime/*.la

%changelog
* Sun Apr 11 2004 Dag Wieers <dag@wieers.com> - 0.9.2-1
- Rebuild against libdv 0.102.

* Mon Feb 10 2003 Dag Wieers <dag@wieers.com> - 0.9.1.91-0
- Initial package. (using DAR)
