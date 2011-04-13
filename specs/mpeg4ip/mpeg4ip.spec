# $Id$
# Authority: dag
# Upstream: <mpeg4ip-discussion@lists.sourceforge.net>

Summary: Open MPEG-4 streaming tools
Name: mpeg4ip
Version: 1.5.0.1
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://mpeg4ip.net/

Source: http://dl.sf.net/mpeg4ip/mpeg4ip-%{version}.tar.gz
Patch0: mpeg4ip-1.5.0.1-nowerror.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: a52dec-devel
BuildRequires: arts-devel
BuildRequires: esound-devel
BuildRequires: faac-devel
BuildRequires: ffmpeg-devel
BuildRequires: gcc-c++
BuildRequires: gtk2-devel
BuildRequires: id3lib-devel
BuildRequires: lame-devel
BuildRequires: libmad-devel
BuildRequires: libtool
BuildRequires: libvorbis-devel
BuildRequires: mpeg2dec-devel
BuildRequires: nasm
BuildRequires: SDL-devel
BuildRequires: x264-devel
BuildRequires: xvidcore-devel

%description
MPEG4IP provides an end-to-end system to explore streaming multimedia. The
package includes many existing open source packages and the "glue" to
integrate them together. This is a tool for streaming video and audio that
is standards-oriented and free from proprietary protocols and extensions.

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
%patch0 -p1 -b .nowerror

%{__perl} -pi.orig -e 's|ffmpeg/avcodec.h|libavcodec/avcodec.h|' configure* \
    player/plugin/audio/ffmpeg/*.h server/mp4live/*

%build
sh bootstrap --disable-warns-as-err
%configure \
    --disable-static \
    --disable-warns-as-err
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

# Remove all *.la files
find %{buildroot} -name '*.la' -exec rm -f {} \;

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING FEATURES.html README* TODO
%doc %{_mandir}/man1/*.1*
%{_bindir}/*
%{_libdir}/*.so.*
%{_libdir}/mp4player_plugin/

%files devel
%defattr(-, root, root, 0755)
%doc %{_mandir}/man3/*.3*
%doc %{_mandir}/manm/*
%{_includedir}/*.h
%{_libdir}/*.so

%changelog
* Tue Jul 11 2006 Matthias Saou <http://freshrpms.net/> 1.5.0.1-1
- Update to 1.5.0.1.
- Move man3 files to devel package.
- Add missing ldconfig calls.

* Sat Jan 01 2004 Dag Wieers <dag@wieers.com> - 1.2-1
- Initial package. (using DAR)
