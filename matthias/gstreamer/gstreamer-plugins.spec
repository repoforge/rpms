Name: 		gstreamer-plugins
Version: 	0.6.5
Release: 	0.fdr.1
Summary: 	GStreamer streaming media framework plugins.

Group: 		Applications/Multimedia
License: 	LGPL
URL:		http://gstreamer.net/
Source: 	http://freedesktop.org/~gstreamer/src/gst-plugins/gst-plugins-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%define		_gst		0.6.5
%define		majorminor	0.6
%define         register %{_bindir}/gst-register-%{majorminor} > /dev/null 2>&1

Provides:	gstreamer-plugins = %{version}-%{release}
PreReq:         %{_bindir}/gst-register-%{majorminor}

BuildRequires: 	gstreamer-devel >= %{_gst}
# libtool, sigh
BuildRequires:	gcc-c++

# dependency libraries for the main plugin package
BuildRequires: arts-devel
BuildRequires: audiofile-devel >= 0.2.1
BuildRequires: cdparanoia-devel >= alpha9.7
BuildRequires: esound-devel >= 0.2.8
BuildRequires: flac-devel
BuildRequires: gnome-vfs2-devel >= 2.1.3
BuildRequires: gtk2-devel
BuildRequires: Hermes-devel
BuildRequires: libjpeg-devel
BuildRequires: libogg-devel >= 1.0
BuildRequires: libpng-devel >= 1.2.0
BuildRequires: libraw1394-devel
BuildRequires: libvorbis-devel >= 0:1.0beta4
BuildRequires: mikmod
BuildRequires: pango-devel
BuildRequires: SDL-devel >= 1.2.0
BuildRequires: speex-devel

%description
GStreamer is a streaming-media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new 
plugins.

%package devel
Summary: 	Libraries/include files for GStreamer plugins.
Group: 		Development/Libraries

Requires: 	%{name} = %{version}-%{release}
Requires:	gstreamer-devel >= %{_gst}
Provides:	gstreamer-plugins-devel = %{version}-%{release}

%description devel
GStreamer is a streaming-media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new
plugins.

This package contains the libraries and includes files necessary to develop
applications and plugins for GStreamer.

%package alsa
Summary: 	ALSA plugin for GStreamer.
Group: 		Applications/Multimedia

BuildRequires:	alsa-lib-devel
Provides:	gstreamer-alsa = %{version}-%{release}

%description alsa
This package contains ALSA elements.

%package audio
Summary: 	Additional audio plugins for GStreamer.
Group: 		Applications/Multimedia

BuildRequires:	libsidplay-devel >= 1.36.0
BuildRequires:	libshout-devel >= 1.0.5
BuildRequires:	ladspa-devel
Provides:	gstreamer-ladspa = %{version}-%{release}
Provides:	gstreamer-sid = %{version}-%{release}
Provides:	gstreamer-shout = %{version}-%{release}

%description audio
This package contains additional audio plugins for GStreamer, including
- codec for sid (C64)
- a shout element to stream to icecast servers
- a ladspa elements wrapping LADSPA plugins

%package video
Summary: 	Additional video plugins for GStreamer.
Group: 		Applications/Multimedia

BuildRequires:	aalib-devel >= 1.3
BuildRequires:	libdv-devel >= 0.99
Provides:	gstreamer-aasink = %{version}-%{release}
Provides:	gstreamer-dvdec = %{version}-%{release}

%description video
This package contains additional video plugins for GStreamer, including
- an output sink based on aalib (ASCII art output)
- an element for decoding dv streams using libdv

%prep
%setup -q -n gst-plugins-%{version}

%build
%configure \
%ifnarch %{ix86}
  --disable-qcam \
%else
  --enable-qcam \
%endif
  --enable-debug \
  --enable-DEBUG \
  --disable-tests --disable-examples

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
# to make it easier to package, we only run make install in the subdirs
# that we want to have installed
for d in gst-libs gst sys tools gconf pkgconfig
do
  cd $d
%makeinstall
  cd ..
done
# now the stuff we want from ext
cd ext
for d in arts artsd audiofile cdparanoia esd flac gnomevfs hermes \
	jpeg libpng mikmod raw1394 sdl snapshot vorbis \
	alsa ladspa sidplay shout aalib dv
do
  cd $d
%makeinstall
  cd ..
done

cd ..
unset GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL

# Clean out files that should not be part of the rpm. 
rm -f $RPM_BUILD_ROOT%{_libdir}/gstreamer-%{majorminor}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/gstreamer-%{majorminor}/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
# these aren't stable yet
rm -rf $RPM_BUILD_ROOT%{_includedir}/gstreamer-%{majorminor}/gst/media-info
rm -rf $RPM_BUILD_ROOT%{_libdir}/libgstmedia-info*
# this is an upstream mistake
rm -f $RPM_BUILD_ROOT%{_libdir}/gstreamer-%{majorminor}/libgstxwindowlistener.so.0.0.0
# these we package somewhere else
rm -f $RPM_BUILD_ROOT%{_libdir}/gstreamer-%{majorminor}/libgstmp1video*
rm -f $RPM_BUILD_ROOT%{_libdir}/gstreamer-%{majorminor}/libgstmpeg*
rm -f $RPM_BUILD_ROOT%{_libdir}/gstreamer-%{majorminor}/libgstffmpeg*

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%{register}
export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
SCHEMAS="gstreamer-%{majorminor}.schemas"
for S in $SCHEMAS; do
  gconftool-2 --makefile-install-rule /etc/gconf/schemas/$S > /dev/null
done

%postun
/sbin/ldconfig
%{register}

%post alsa
%{register}
%postun alsa
%{register}

%post audio
%{register}
%postun audio
%{register}

%post video
%{register}
%postun video
%{register}

%files
%defattr(-, root, root, -)
%doc AUTHORS COPYING NEWS README RELEASE

# helper programs
%{_bindir}/gst-launch-ext-%{majorminor}
%{_bindir}/gst-visualise-%{majorminor}
%{_mandir}/man1/gst-launch-ext-%{majorminor}.*
%{_mandir}/man1/gst-visualise-%{majorminor}*

# schema files
%{_sysconfdir}/gconf/schemas/gstreamer-%{majorminor}.schemas

# libraries
%{_libdir}/libgstplay-%{majorminor}.so.*
%{_libdir}/libgstgconf-%{majorminor}.so.*

# plugin helper libraries
%{_libdir}/gstreamer-%{majorminor}/libgstaudio.so
%{_libdir}/gstreamer-%{majorminor}/libgstidct.so
%{_libdir}/gstreamer-%{majorminor}/libgstriff.so
%{_libdir}/gstreamer-%{majorminor}/libgstvideo.so

# gstreamer-plugins
%{_libdir}/gstreamer-%{majorminor}/libgstac3parse.so
%{_libdir}/gstreamer-%{majorminor}/libgstadder.so
%{_libdir}/gstreamer-%{majorminor}/libgstalaw.so
%{_libdir}/gstreamer-%{majorminor}/libgstaudioscale.so
%{_libdir}/gstreamer-%{majorminor}/libgstauparse.so
%{_libdir}/gstreamer-%{majorminor}/libgstavidemux.so
%{_libdir}/gstreamer-%{majorminor}/libgstavimux.so
%{_libdir}/gstreamer-%{majorminor}/libgstcdplayer.so
%{_libdir}/gstreamer-%{majorminor}/libgstcdxaparse.so
%{_libdir}/gstreamer-%{majorminor}/libgstchart.so
%{_libdir}/gstreamer-%{majorminor}/libgstcolorspace.so
%{_libdir}/gstreamer-%{majorminor}/libgstcutter.so
%{_libdir}/gstreamer-%{majorminor}/libgstdeinterlace.so
%{_libdir}/gstreamer-%{majorminor}/libgsteffectv.so
%{_libdir}/gstreamer-%{majorminor}/libgstfestival.so
%{_libdir}/gstreamer-%{majorminor}/libgstfilter.so
%{_libdir}/gstreamer-%{majorminor}/libgstflxdec.so
%{_libdir}/gstreamer-%{majorminor}/libgstgoom.so
%{_libdir}/gstreamer-%{majorminor}/libgstintfloat.so
%{_libdir}/gstreamer-%{majorminor}/libgstlevel.so
%{_libdir}/gstreamer-%{majorminor}/libgstmedian.so
%{_libdir}/gstreamer-%{majorminor}/libgstmodplug.so
%{_libdir}/gstreamer-%{majorminor}/libgstmono2stereo.so
%{_libdir}/gstreamer-%{majorminor}/libgstmonoscope.so
%{_libdir}/gstreamer-%{majorminor}/libgstmp3types.so
%{_libdir}/gstreamer-%{majorminor}/libgstmulaw.so
%{_libdir}/gstreamer-%{majorminor}/libgstoneton.so
%{_libdir}/gstreamer-%{majorminor}/libgstpassthrough.so
%{_libdir}/gstreamer-%{majorminor}/libgstplayondemand.so
%ifarch %{ix86}
%{_libdir}/gstreamer-%{majorminor}/libgstqcam.so
%endif
%{_libdir}/gstreamer-%{majorminor}/libgstresample.so
%{_libdir}/gstreamer-%{majorminor}/libgstrtjpeg.so
%{_libdir}/gstreamer-%{majorminor}/libgstqtdemux.so
%{_libdir}/gstreamer-%{majorminor}/libgstsilence.so
%{_libdir}/gstreamer-%{majorminor}/libgstsinesrc.so
%{_libdir}/gstreamer-%{majorminor}/libgstsmooth.so
%{_libdir}/gstreamer-%{majorminor}/libgstsmpte.so
%{_libdir}/gstreamer-%{majorminor}/libgstspectrum.so
%{_libdir}/gstreamer-%{majorminor}/libgstspeed.so
%{_libdir}/gstreamer-%{majorminor}/libgststereo.so
%{_libdir}/gstreamer-%{majorminor}/libgststereosplit.so
%{_libdir}/gstreamer-%{majorminor}/libgststereo2mono.so
%{_libdir}/gstreamer-%{majorminor}/libgstsynaesthesia.so
%{_libdir}/gstreamer-%{majorminor}/libgstudp.so
%{_libdir}/gstreamer-%{majorminor}/libgstv4lelement.so
%{_libdir}/gstreamer-%{majorminor}/libgstv4lmjpegsink.so
%{_libdir}/gstreamer-%{majorminor}/libgstv4lmjpegsrc.so
%{_libdir}/gstreamer-%{majorminor}/libgstv4lsrc.so
%{_libdir}/gstreamer-%{majorminor}/libgstvbidec.so
%{_libdir}/gstreamer-%{majorminor}/libgstvcdsrc.so
%{_libdir}/gstreamer-%{majorminor}/libgstvideocrop.so
%{_libdir}/gstreamer-%{majorminor}/libgstvideoscale.so
%{_libdir}/gstreamer-%{majorminor}/libgstvideosink.so
%{_libdir}/gstreamer-%{majorminor}/libgstvideotestsrc.so
%{_libdir}/gstreamer-%{majorminor}/libgstvolenv.so
%{_libdir}/gstreamer-%{majorminor}/libgstvolume.so
%{_libdir}/gstreamer-%{majorminor}/libgstvumeter.so
%{_libdir}/gstreamer-%{majorminor}/libgstwavenc.so
%{_libdir}/gstreamer-%{majorminor}/libgstwavparse.so
%{_libdir}/gstreamer-%{majorminor}/libgsty4menc.so
%{_libdir}/gstreamer-%{majorminor}/libmixmatrix.so

# gstreamer-plugins with external dependencies but in the main package
%ifarch %{ix86} ia64 ppc ppc64 x86_64
%{_libdir}/gstreamer-%{majorminor}/libgst1394.so
%endif
%{_libdir}/gstreamer-%{majorminor}/libgstarts.so
%{_libdir}/gstreamer-%{majorminor}/libgstartsdsink.so
%{_libdir}/gstreamer-%{majorminor}/libgstaudiofile.so
%{_libdir}/gstreamer-%{majorminor}/libgstcdparanoia.so
%{_libdir}/gstreamer-%{majorminor}/libgstesdmon.so
%{_libdir}/gstreamer-%{majorminor}/libgstesdsink.so
%{_libdir}/gstreamer-%{majorminor}/libgstflac.so
%{_libdir}/gstreamer-%{majorminor}/libgstgnomevfssink.so
%{_libdir}/gstreamer-%{majorminor}/libgstgnomevfssrc.so
%{_libdir}/gstreamer-%{majorminor}/libgstjpeg.so
%{_libdir}/gstreamer-%{majorminor}/libgstmikmod.so
%{_libdir}/gstreamer-%{majorminor}/libgstossaudio.so
%{_libdir}/gstreamer-%{majorminor}/libgstpng.so
%{_libdir}/gstreamer-%{majorminor}/libgstsdlvideosink.so
%{_libdir}/gstreamer-%{majorminor}/libgstsnapshot.so
%{_libdir}/gstreamer-%{majorminor}/libgstvorbis.so
%{_libdir}/gstreamer-%{majorminor}/libgstxvideosink.so

%files devel
%defattr(-, root, root, -)
# plugin helper library headers
%{_includedir}/gstreamer-%{majorminor}/gst/audio/audio.h
%{_includedir}/gstreamer-%{majorminor}/gst/floatcast/floatcast.h
%{_includedir}/gstreamer-%{majorminor}/gst/idct/idct.h
%{_includedir}/gstreamer-%{majorminor}/gst/resample/resample.h
%{_includedir}/gstreamer-%{majorminor}/gst/riff/riff.h
%{_includedir}/gstreamer-%{majorminor}/gst/video/video.h
# library headers
%{_includedir}/gstreamer-%{majorminor}/gst/gconf/gconf.h
%{_includedir}/gstreamer-%{majorminor}/gst/play/play.h
# pkg-config files
%{_libdir}/pkgconfig/gstreamer-libs-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-play-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-gconf-%{majorminor}.pc
# .so files
%{_libdir}/libgstgconf-%{majorminor}.so
%{_libdir}/libgstplay-%{majorminor}.so

%files alsa
%defattr(-, root, root, -)
%{_libdir}/gstreamer-%{majorminor}/libgstalsa.so

%files audio
%defattr(-, root, root, -)
%{_libdir}/gstreamer-%{majorminor}/libgstladspa.so
%{_libdir}/gstreamer-%{majorminor}/libgstsid.so
%{_libdir}/gstreamer-%{majorminor}/libgstshout.so

%files video
%defattr(-, root, root, -)
%{_libdir}/gstreamer-%{majorminor}/libgstaasink.so
%{_libdir}/gstreamer-%{majorminor}/libgstdvdec.so

%changelog
* Wed Mar 03 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.6.5-0.fdr.1: First package for fedora.us
