# Authority: freshrpms
%define rversion 0.9.2pre1

Summary: A library for manipulating QuickTime files
Name: libquicktime
Version: 0.9.1.91
Release: 0
License: GPL
Group: System Environment/Libraries
URL: http://libquicktime.sourceforge.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: ftp://ftp.sourceforge.net/pub/sourceforge/%{name}/%{name}-%{rversion}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: autoconf, automake, libpng-devel >= 1.0.8, libjpeg-devel
BuildRequires: libdv-devel, libogg-devel, libvorbis-devel
BuildRequires: glib-devel %{?rh80:, libraw1394-devel, libavc1394-devel}

%description
Libquicktime is a library for reading and writing QuickTime files
on UNIX systems. Video CODECs supported by this library are OpenDivX, MJPA,
JPEG Photo, PNG, RGB, YUV 4:2:2, and YUV 4:2:0 compression.  Supported
audio CODECs are Ogg Vorbis, IMA4, ulaw, and any linear PCM format.

Libquicktime is based on the quicktime4linux library.  Libquicktime add
features such as a GNU build tools-based build process and dynamically
loadable CODECs.

%package devel
Summary: Header files and development documentation for libquicktime
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
Header files and development documentation for libquicktime.

%prep
%setup -n %{name}-%{rversion}

%build
%configure \
	--disable-dependency-tracking \
	--enable-static \
	--enable-shared
%{__perl} -pi.orig -e 's|^libavcodec_subdirs = ffmpeg|libavcodec_subdirs = |' plugins/Makefile
%{__perl} -pi.orig -e 's|^LDFLAGS = |LDFLAGS = -L../../src/.libs|' plugins/*/Makefile
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
#%{__make} DESTDIR="%{buildroot}" install

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/*.la %{buildroot}%{_libdir}/libquicktime/*.la

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%doc %{_mandir}/man1/*
%dir %{_libdir}/libquicktime/
%{_bindir}/lqtplay
%{_bindir}/qt*
%{_libdir}/*.so.*
%{_libdir}/libquicktime/*.so

%files devel
%defattr(-, root, root, 0755)
%dir %{_libdir}/libquicktime/
%dir %{_includedir}/quicktime/
%{_bindir}/*config
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/libquicktime/*.a
%{_includedir}/quicktime/*.h
%{_datadir}/aclocal/*.m4
#exclude %{_libdir}/*.la
#exclude %{_libdir}/libquicktime/*.la

%changelog
* Mon Feb 10 2003 Dag Wieers <dag@wieers.com> - 0.9.1.91-0
- Initial package. (using DAR)
