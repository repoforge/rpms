Name: 		gstreamer-plugins-extra
Version: 	0.6.5
Release: 	0.lvn.1
Summary: 	GStreamer extra streaming media framework plugins.

Group: 		Applications/Multimedia
License: 	LGPL
URL:		http://gstreamer.net/
Source: 	http://freedesktop.org/~gstreamer/src/gst-plugins/gst-plugins-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%define		_gst		0.6.5
%define		majorminor	0.6
%define		register %{_bindir}/gst-register-%{majorminor} > /dev/null 2>&1

Provides:	gstreamer-plugins-extra = %{version}-%{release}

BuildRequires: 	gstreamer-devel >= %{_gst}
# libtool needs this, sigh
BuildRequires: 	gcc-c++
# so gst-libs can build
BuildRequires:	XFree86-devel

%description
GStreamer is a streaming-media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new 
plugins.

This package provides extra plugins currently hosted on http://rpm.livna.org/

%package audio
Summary: 	extra audio plugins for GStreamer.
Group: 		Applications/Multimedia

BuildRequires:  gsm-devel >= 1.0.10
BuildRequires:	lame-devel >= 3.89
BuildRequires:	libid3tag-devel >= 0.15.0
BuildRequires:	libmad-devel >= 0.13.0
Requires:	gstreamer-plugins = %{version}

Provides:	gstreamer-gsm = %{version}-%{release}
Provides:	gstreamer-lame = %{version}-%{release}
Provides:	gstreamer-mad = %{version}-%{release}

%description audio
This package contains extra audio plugins for GStreamer, including
- gsm decoding
- mad mp3 decoding
- lame mp3 encoding

%post audio
%{_bindir}/gst-register-%{majorminor} >/dev/null 2>&1
%postun audio
%{_bindir}/gst-register-%{majorminor} >/dev/null 2>&1

%files audio
%defattr(-, root, root, -)
%{_libdir}/gstreamer-%{majorminor}/libgstgsm.so
%{_libdir}/gstreamer-%{majorminor}/libgstlame.so
%{_libdir}/gstreamer-%{majorminor}/libgstmad.so
%{_libdir}/gstreamer-%{majorminor}/libgstmp3types.so

%package dvd
Summary: 	DVD plugins for GStreamer.
Group: 		Applications/Multimedia

BuildRequires:	a52dec-devel >= 0.7.3
BuildRequires:	libdvdnav-devel >= 0.1.3
BuildRequires:	libdvdread-devel >= 0.9.0
Requires:	gstreamer-plugins = %{version}
Provides:	gstreamer-dvd = %{version}-%{release}
Provides:	gstreamer-a52dec = %{version}-%{release}
Provides:	gstreamer-dvdnavsrc = %{version}-%{release}
Provides:	gstreamer-dvdreadsrc = %{version}-%{release}

%description dvd
This package contains dvd plugins for GStreamer, including
- libdvdnav
- libdvdread
- a52 decoding

%post dvd
%{register}
%postun dvd
%{register}

%files dvd
%defattr(-, root, root, -)
%{_libdir}/gstreamer-%{majorminor}/libgsta52dec.so
%{_libdir}/gstreamer-%{majorminor}/libgstdvdnavsrc.so
%{_libdir}/gstreamer-%{majorminor}/libgstdvdreadsrc.so

%package video
Summary: 	extra video plugins for GStreamer.
Group: 		Applications/Multimedia

BuildRequires:	libfame-devel >= 0.9.0
BuildRequires:	mpeg2dec-devel >= 0.3.2
BuildRequires:	swfdec-devel
Requires:	gstreamer-plugins = %{version}
Requires:	gstreamer-plugins-extra-audio = %{version}-%{release}

Provides:	gstreamer-libfame = %{version}-%{release}
Provides:	gstreamer-mpeg2dec = %{version}-%{release}
Provides:	gstreamer-swfdec = %{version}-%{release}

%description video
This package contains extra video plugins for GStreamer, including
- libfame MPEG video encoding
- mpeg2dec MPEG-2 decoding
- swfdec Flash decoding

%post video
%{register}
%postun video
%{register}

%files video
%defattr(-, root, root, -)
%{_libdir}/gstreamer-%{majorminor}/libgstlibfame.so
%{_libdir}/gstreamer-%{majorminor}/libgstmpeg2dec.so
%{_libdir}/gstreamer-%{majorminor}/libgstmp1videoparse.so
%{_libdir}/gstreamer-%{majorminor}/libgstmpeg1systemencode.so
%{_libdir}/gstreamer-%{majorminor}/libgstmpeg2subt.so
%{_libdir}/gstreamer-%{majorminor}/libgstmpegaudio.so
%{_libdir}/gstreamer-%{majorminor}/libgstmpegaudioparse.so
%{_libdir}/gstreamer-%{majorminor}/libgstmpegstream.so
%{_libdir}/gstreamer-%{majorminor}/libgstswfdec.so

%package -n gstreamer-ffmpeg
Summary:	GStreamer FFmpeg-based streaming media framework plugins.
Group: 		Applications/Multimedia

BuildRequires:  freetype-devel
BuildRequires:  imlib2-devel
BuildRequires:  SDL-devel

%description -n gstreamer-ffmpeg
GStreamer is a streaming-media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new
plugins.
                                                                                
This package provides FFmpeg plugins currently hosted on http://rpm.livna.org/
                                                                                
%post -n gstreamer-ffmpeg
%{register}
%postun -n gstreamer-ffmpeg
%{register}

%files -n gstreamer-ffmpeg
%defattr(-, root, root, -)
%{_libdir}/gstreamer-%{majorminor}/libgstffmpeg.so
%{_libdir}/gstreamer-%{majorminor}/libgstffmpegall.so

%prep
%setup -n gst-plugins-%{version}

%build
%configure \
  --with-plugins=\
mpeg1sys,mpeg1videoparse,mpeg2sub,mpegaudio,mpegaudioparse,mpegstream \
  --enable-debug \
  --enable-DEBUG \
  --disable-tests --disable-examples

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

# we're better off manually installing the plugins we want to package

cd gst
for p in mpeg1sys mpeg1videoparse mpeg2sub mpegaudio mpegaudioparse mpegstream
do
  cd $p
  %makeinstall
  cd ..
done
cd ..

cd ext
for p in a52dec dvdnav dvdread ffmpeg gsm lame libfame mad mpeg2dec swfdec
do
  cd $p
  %makeinstall
  cd ..
done
cd ..

# Clean out files that should not be part of the rpm.
rm -f $RPM_BUILD_ROOT%{_libdir}/gstreamer-%{majorminor}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/gstreamer-%{majorminor}/*.a

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Thu Mar 04 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.6.5-0.lvn.1: First package for rpm.livna.org
