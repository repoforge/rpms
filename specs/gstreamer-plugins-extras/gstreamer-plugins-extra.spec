%define		gst_minver	0.7.6
%define		gstp_minver	0.7.6
%define		majorminor	0.8
%define		gstreamer	gstreamer
%define		register	%{_bindir}/gst-register-%{majorminor} > /dev/null 2>&1 || :

Name: 		%{gstreamer}-plugins-extra
Version: 	0.8.1
Release: 	1
Summary: 	GStreamer extra streaming media framework plugins

Group: 		Applications/Multimedia
License: 	LGPL
URL:		http://gstreamer.net/
Source: 	http://freedesktop.org/~gstreamer/src/gst-plugins/gst-plugins-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: 	%{gstreamer}-devel >= %{gst_minver}
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
Summary: 	extra audio plugins for GStreamer
Group: 		Applications/Multimedia

BuildRequires:	faad2-devel >= 2.0
BuildRequires:  gsm-devel >= 1.0.10
BuildRequires:	lame-devel >= 3.89
BuildRequires:	libid3tag-devel >= 0.15.0
BuildRequires:	libmad-devel >= 0.15.0

Requires:	%{gstreamer}-plugins >= %{gstp_minver}
Requires(pre):	%{_bindir}/gst-register-%{majorminor}
Requires(post):	%{_bindir}/gst-register-%{majorminor}

Provides:	%{gstreamer}-faad = %{version}-%{release}
Provides:	%{gstreamer}-gsm = %{version}-%{release}
Provides:	%{gstreamer}-lame = %{version}-%{release}
Provides:	%{gstreamer}-mad = %{version}-%{release}

%description audio
This package contains extra audio plugins for GStreamer, including
- gsm decoding
- faad2 decoding
- mad mp3 decoding
- lame mp3 encoding

%post audio
%{register}
%postun audio
%{register}

%files audio
%defattr(-, root, root, -)
%{_libdir}/gstreamer-%{majorminor}/libgstfaad.so
%{_libdir}/gstreamer-%{majorminor}/libgstgsm.so
%{_libdir}/gstreamer-%{majorminor}/libgstlame.so
%{_libdir}/gstreamer-%{majorminor}/libgstmad.so

%package dvd
Summary: 	DVD plugins for GStreamer
Group: 		Applications/Multimedia

BuildRequires:	a52dec-devel >= 0.7.3
BuildRequires:	libdvdnav-devel >= 0.1.3
BuildRequires:	libdvdread-devel >= 0.9.0

Requires:	%{gstreamer}-plugins >= %{gstp_minver}
Requires:	%{gstreamer}-plugins-extra-video >= %{gstp_minver}
Requires(pre):	%{_bindir}/gst-register-%{majorminor}
Requires(post):	%{_bindir}/gst-register-%{majorminor}

Provides:	%{gstreamer}-dvd = %{version}-%{release}
Provides:	%{gstreamer}-a52dec = %{version}-%{release}
Provides:	%{gstreamer}-dvdnavsrc = %{version}-%{release}
Provides:	%{gstreamer}-dvdreadsrc = %{version}-%{release}

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
Summary: 	extra video plugins for GStreamer
Group: 		Applications/Multimedia

BuildRequires:	libfame-devel >= 0.9.0
BuildRequires:	mpeg2dec-devel >= 0.4.0
BuildRequires:	swfdec-devel

Requires:	%{gstreamer}-plugins >= %{gstp_minver}
Requires:	%{gstreamer}-plugins-extra-audio >= %{gstp_minver}
Requires(pre):	%{_bindir}/gst-register-%{majorminor}
Requires(post):	%{_bindir}/gst-register-%{majorminor}

Provides:	%{gstreamer}-libfame = %{version}-%{release}
Provides:	%{gstreamer}-mpeg2dec = %{version}-%{release}
Provides:	%{gstreamer}-swfdec = %{version}-%{release}

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

%prep
%setup -n gst-plugins-%{version}

%build
%configure \
  --with-plugins=\
mpeg1sys,mpeg1videoparse,mpeg2sub,mpegaudio,mpegaudioparse,mpegstream \
  --enable-debug \
  --enable-DEBUG \
  --disable-tests \
  --disable-examples

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
for p in a52dec dvdnav dvdread faad gsm lame libfame mad mpeg2dec swfdec
do
  cd $p
  %makeinstall
  cd ..
done
cd ..

# Clean out files that should not be part of the rpm.
rm -f $RPM_BUILD_ROOT%{_libdir}/gstreamer-%{majorminor}/*.{a,la}

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Fri Jul 16 2004 Matthias Saou <http://freshrpms.net/> 0.8.1-1
- Bumped release for rebuild against newer libdvdnav.

* Thu Apr 15 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.8.1-0.lvn.1: new source release

* Tue Mar 16 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.8.0-0.lvn.1: new source release, change base name to gstreamer

* Tue Mar 09 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.7.6-0.lvn.1: new source release

* Fri Mar 05 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.7.5-0.lvn.2: sync with FreshRPMS

* Tue Mar 02 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.7.5-0.lvn.1: First package for rpm.livna.org
