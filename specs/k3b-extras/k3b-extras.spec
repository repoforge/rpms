# $Id$
# Authority: dag

# ExclusiveDist: el5


%{?el4:%define _without_modxorg 1}

%{?el3:%define _without_kde32 1}
%{?el3:%define _without_modxorg 1}

Summary: Additional codec plugins for the k3b CD/DVD burning application
Name: k3b-extras
Version: 0.12.17
Release: 4%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://www.k3b.org/

Source: http://dl.sf.net/k3b/k3b-%{version}.tar.bz2
Patch0: k3b-extras-0.12.17-ffmpeg-0.5.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

ExcludeArch: s390 s390x
BuildRequires: arts-devel
BuildRequires: ffmpeg-devel
BuildRequires: gettext
BuildRequires: k3b
BuildRequires: kdelibs-devel >= 6:3.1
BuildRequires: lame-devel
BuildRequires: libart_lgpl-devel
BuildRequires: libjpeg-devel
BuildRequires: libmad-devel
BuildRequires: libmpcdec-devel
BuildRequires: libmusicbrainz-devel
BuildRequires: libpng-devel
BuildRequires: libsndfile-devel
BuildRequires: taglib-devel
BuildRequires: zlib-devel
%{!?_without_kde32:BuildRequires: libmng-devel fam-devel glib2-devel alsa-lib-devel esound-devel}
%{!?_without_modxorg:BuildRequires: libX11-devel}
%{?_without_modxorg:BuildRequires: XFree86-devel}

Requires: k3b = %{version}

Obsoletes: k3b-mp3 <= %{version}-%{release}
Provides: k3b-mp3 = %{version}-%{release}
Obsoletes: k3b-extras-nonfree <= %{version}-%{release}
Provides: k3b-extras-nonfree = %{version}-%{release}

%description
Additional decoder/encoder plugins for k3b, a feature-rich and easy to
handle CD/DVD burning application.

%prep
%setup -n k3b-%{version}
%patch0 -p1 -b .ffmpeg

%{__perl} -pi.orig -e '
        s|<ffmpeg/avformat.h>|<libavformat/avformat.h>|g;
        s|<ffmpeg/avcodec.h>|<libavcodec/avcodec.h>|g;
    ' configure* plugins/decoder/ffmpeg/*

%build
source /etc/profile.d/qt.sh
export CPPFLAGS="-I%{_includedir}/ffmpeg"
%configure \
    --disable-rpath \
    --without-flac \
    --without-oggvorbis \
    --with-external-libsamplerate="no" \
    --with-k3bsetup="no" \
    --with-musepack \
    --with-qt-libraries="$QTDIR/lib" \
    --with-sndfile

%{__make} -C libk3bdevice %{?_smp_mflags}
%{__make} -C libk3b %{?_smp_mflags}

%{__make} -C plugins/decoder/ffmpeg %{?_smp_mflags}
%{__make} -C plugins/decoder/libsndfile %{?_smp_mflags}
%{__make} -C plugins/decoder/mp3 %{?_smp_mflags}
%{__make} -C plugins/decoder/musepack %{?_smp_mflags}
%{__make} -C plugins/encoder/lame %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} -C plugins/decoder/ffmpeg install DESTDIR="%{buildroot}"
%{__make} -C plugins/decoder/libsndfile install DESTDIR="%{buildroot}"
%{__make} -C plugins/decoder/mp3 install DESTDIR="%{buildroot}"
%{__make} -C plugins/decoder/musepack install DESTDIR="%{buildroot}"
%{__make} -C plugins/encoder/lame install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%dir %{_libdir}/kde3/
%{_libdir}/kde3/libk3bffmpegdecoder.*
%{_libdir}/kde3/libk3blameencoder.*
%{_libdir}/kde3/libk3blibsndfiledecoder.*
%{_libdir}/kde3/libk3bmaddecoder.*
%{_libdir}/kde3/libk3bmpcdecoder.*
%dir %{_datadir}/apps/
%dir %{_datadir}/apps/k3b/
%dir %{_datadir}/apps/k3b/plugins/
%{_datadir}/apps/k3b/plugins/k3bffmpegdecoder.plugin
%{_datadir}/apps/k3b/plugins/k3blameencoder.plugin
%{_datadir}/apps/k3b/plugins/k3blibsndfiledecoder.plugin
%{_datadir}/apps/k3b/plugins/k3bmaddecoder.plugin
%{_datadir}/apps/k3b/plugins/k3bmpcdecoder.plugin

%changelog
* Sun Jul 12 2009 Dag Wieers <dag@wieers.com> - 0.12.17-4
- Rebuild against ffmpeg-0.5.
- Fixed build system & patched against the new FFMPEG API. (Yury V. Zaytsev)

* Mon Dec 17 2007 Dag Wieers <dag@wieers.com> - 0.12.17-3
- Rebuild against libmpcdec 1.2.6.

* Fri Mar 30 2007 Dag Wieers <dag@wieers.com> - 0.12.17-2
- Added ffmpeg, libsndfile and mpcdec codecs.

* Sun Mar 05 2006 Dag Wieers <dag@wieers.com> - 0.12.17-1
- Imported based on Livna SPEC file.
- Initial package. (using DAR)
