%define         _glib2          2.0.0
%define         hermes_version  1.3.3

Summary: GStreamer Streaming-media framework plugins
Name: gstreamer-plugins
Version: 0.8.5
%define majmin 0.8
%define po_package gst-plugins-%{majmin}
Release: 0%{?dist}
License: LGPL
Group: Applications/Multimedia
Source: gst-plugins-%{version}.tar.bz2
#Source2: patch-tarball.sh
#Source3: removed-sources.txt
Source4: http://clanlib.org/download/files/Hermes-%{hermes_version}.tar.bz2
#Source5: gst-fionread.m4
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Patch1: gstreamer-plugins-0.7.5-alsa.patch
Patch2: gstreamer-plugins-0.8.4-vorbis-seek-workaround.patch
Patch3: gstreamer-plugins-0.8.5-dv.patch

Requires: glib2 >= %_glib2
Requires: gstreamer >= %{version}
PreReq: /usr/bin/gst-register-%{majmin}
PreReq: GConf2
PreReq: /usr/bin/gconftool-2
Requires: arts
Requires: cdparanoia-libs >= alpha9.7
BuildRequires: glib2-devel >= %_glib2
BuildRequires: GConf2-devel
BuildRequires: gstreamer-devel >= %{version}
BuildRequires: arts-devel
BuildRequires: audiofile-devel >= 0.2.1
BuildRequires: cdparanoia-devel >= alpha9.7
BuildRequires: esound-devel >= 0.2.8
BuildRequires: alsa-lib-devel
BuildRequires: gnome-vfs2-devel >= 2.1.3
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
# don't buildrequires it; silly patents :(
#BuildRequires: libmad
BuildRequires: mikmod
BuildRequires: gstreamer-devel >= 0.5.2-8
BuildRequires: SDL-devel >= 1.2.0
BuildRequires: libogg-devel >= 1.0
BuildRequires: libvorbis-devel >= 0:1.0beta4
BuildRequires: libtheora-devel >= 1.0
BuildRequires: xmms-devel
BuildRequires: autoconf automake libtool
BuildRequires: libraw1394-devel
BuildRequires: libghttp-devel
BuildRequires: speex-devel
BuildRequires: flac-devel
%ifnarch s390 s390x
BuildRequires: libdv-devel
%endif

BuildRequires: gdk-pixbuf-devel, gtk2-devel, libmng-devel, libmusicbrainz-devel
BuildRequires: libavc1394-devel

%description
GStreamer is a streaming-media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new
plugins.

%package devel
Summary: Libraries/include files for GStreamer plugins.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: gstreamer-devel >= %{version}

%description devel
GStreamer is a streaming-media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new
plugins.

This package contains the libraries and includes files necessary to develop
applications and plugins for GStreamer.

%prep
%setup -q -n gst-plugins-%{version} -a 4
%patch1 -p1 -b .alsa
%patch2 -p1 -b .vorbis-seek-workaround
%patch3 -p1 -b .dv

#mkdir gst-libs/ext/ffmpeg

for docfile in AUTHORS COPYING README ; do
	cp Hermes-%{hermes_version}/${docfile} ${docfile}.Hermes
done

%build
hermes_top=`pwd`/Hermes-install

pushd Hermes-%{hermes_version}
#aclocal
#libtoolize --force --copy
#automake
#autoconf
CFLAGS="$RPM_OPT_FLAGS -fPIC"; export CFLAGS
./configure --disable-shared --enable-static \
	--prefix=${hermes_top} \
	--includedir=${hermes_top}/include \
	--libdir=${hermes_top}/%{_lib}
make all install
popd

#cp %{SOURCE5} m4/
#aclocal -I m4  -I common/m4
#libtoolize --force --copy
#automake
#autoconf

CFLAGS="$RPM_OPT_FLAGS -I${hermes_top}/include"; export CFLAGS
CPPFLAGS="-I${hermes_top}/include"; export CPPFLAGS
LDFLAGS="-L${hermes_top}/%{_lib}"; export LDFLAGS

%configure --disable-vorbistest \
%ifnarch %{ix86}
  --disable-qcam \
%else
  --enable-qcam \
%endif
  --disable-ffmpeg \
  --disable-faad \
  --disable-sndfile \
  --enable-DEBUG --disable-tests --disable-examples

make %{?_smp_mflags}

#cp %{SOURCE3} .

%install
rm -rf $RPM_BUILD_ROOT
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
%makeinstall
unset GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL

rm -f $RPM_BUILD_ROOT%{_libdir}/gstreamer-%{majmin}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/gstreamer-%{majmin}/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%find_lang %{po_package}

%clean
%{__rm} -rf %{buildroot}

%post
/sbin/ldconfig
env DISPLAY= %{_bindir}/gst-register-%{majmin} >/dev/null 2>&1
export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
SCHEMAS="gstreamer-%{majmin}.schemas"
for S in $SCHEMAS; do
  gconftool-2 --makefile-install-rule /etc/gconf/schemas/$S > /dev/null
done

%postun
/sbin/ldconfig
env DISPLAY= /usr/bin/gst-register-%{majmin} >/dev/null 2>&1 || true

%files -f %{po_package}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING README
%doc AUTHORS.Hermes COPYING.Hermes README.Hermes
%{_sysconfdir}/gconf/schemas/gstreamer-%{majmin}.schemas
%{_bindir}/*
%{_libdir}/*so.*
%dir %{_libdir}/gstreamer-%{majmin}
%ifarch %{ix86} ia64 ppc ppc64 x86_64
%{_libdir}/gstreamer-%{majmin}/libgst1394.*
%endif
%{_libdir}/gstreamer-%{majmin}/libgstac3parse.*
%{_libdir}/gstreamer-%{majmin}/libgstadder.*
%{_libdir}/gstreamer-%{majmin}/libgstalpha.*
%{_libdir}/gstreamer-%{majmin}/libgstalaw.*
%{_libdir}/gstreamer-%{majmin}/libgstalsa.*
%{_libdir}/gstreamer-%{majmin}/libgstalphacolor.*
%{_libdir}/gstreamer-%{majmin}/libgstarts.*
%{_libdir}/gstreamer-%{majmin}/libgstaudiorate.*
%{_libdir}/gstreamer-%{majmin}/libgstartsdsink.*
%{_libdir}/gstreamer-%{majmin}/libgstasf.*
%{_libdir}/gstreamer-%{majmin}/libgstaudio.*
%{_libdir}/gstreamer-%{majmin}/libgstaudioconvert.*
%{_libdir}/gstreamer-%{majmin}/libgstaudiofile.*
%{_libdir}/gstreamer-%{majmin}/libgstaudiofilter.*
%{_libdir}/gstreamer-%{majmin}/libgstaudioscale.*
%{_libdir}/gstreamer-%{majmin}/libgstauparse.*
%{_libdir}/gstreamer-%{majmin}/libgstavi.*
%{_libdir}/gstreamer-%{majmin}/libgstcdparanoia.*
%{_libdir}/gstreamer-%{majmin}/libgstcdplayer.*
%{_libdir}/gstreamer-%{majmin}/libgstcdxaparse.*
%{_libdir}/gstreamer-%{majmin}/libgstchart.*
%{_libdir}/gstreamer-%{majmin}/libgstcolorspace.*
%{_libdir}/gstreamer-%{majmin}/libgstcutter.*
%{_libdir}/gstreamer-%{majmin}/libgstdeinterlace.*
%{_libdir}/gstreamer-%{majmin}/libgstdebug.*
%{_libdir}/gstreamer-%{majmin}/libgstdecodebin.*
%ifnarch s390 s390x
%{_libdir}/gstreamer-%{majmin}/libgstdvdec.*
%endif
%{_libdir}/gstreamer-%{majmin}/libgstefence.*
%{_libdir}/gstreamer-%{majmin}/libgsteffectv.*
%{_libdir}/gstreamer-%{majmin}/libgstesd.*
%{_libdir}/gstreamer-%{majmin}/libgstfestival.*
%{_libdir}/gstreamer-%{majmin}/libgstfilter.*
%{_libdir}/gstreamer-%{majmin}/libgstflac.*
%{_libdir}/gstreamer-%{majmin}/libgstffmpegcolorspace.*
%{_libdir}/gstreamer-%{majmin}/libgstflxdec.*
%{_libdir}/gstreamer-%{majmin}/libgstgamma.*
%{_libdir}/gstreamer-%{majmin}/libgstgdkpixbuf.*
%{_libdir}/gstreamer-%{majmin}/libgstglimagesink.*
%{_libdir}/gstreamer-%{majmin}/libgstgnomevfs.*
%{_libdir}/gstreamer-%{majmin}/libgstgoom.*
%{_libdir}/gstreamer-%{majmin}/libgsthermescolorspace.*
%{_libdir}/gstreamer-%{majmin}/libgstidct.*
%{_libdir}/gstreamer-%{majmin}/libgstinterleave.*
%{_libdir}/gstreamer-%{majmin}/libgstjpeg.*
%{_libdir}/gstreamer-%{majmin}/libgstlevel.*
%{_libdir}/gstreamer-%{majmin}/libgstmatroska.*
%{_libdir}/gstreamer-%{majmin}/libgstmedian.*
%{_libdir}/gstreamer-%{majmin}/libgstmikmod.*
%{_libdir}/gstreamer-%{majmin}/libgstmng.*
%{_libdir}/gstreamer-%{majmin}/libgstmodplug.*
%{_libdir}/gstreamer-%{majmin}/libgstmonoscope.*
%{_libdir}/gstreamer-%{majmin}/libgstmultifilesink.*
%{_libdir}/gstreamer-%{majmin}/libgstmulaw.*
%{_libdir}/gstreamer-%{majmin}/libgstmultipart.*
%{_libdir}/gstreamer-%{majmin}/libgstnavigationtest.*
%{_libdir}/gstreamer-%{majmin}/libgstogg.*
%{_libdir}/gstreamer-%{majmin}/libgstossaudio.*
%{_libdir}/gstreamer-%{majmin}/libgstoverlay.*
%{_libdir}/gstreamer-%{majmin}/libgstpassthrough.*
%{_libdir}/gstreamer-%{majmin}/libgstplayondemand.*
%{_libdir}/gstreamer-%{majmin}/libgstplaybin.*
%{_libdir}/gstreamer-%{majmin}/libgstpng.*
%ifarch %{ix86}
%{_libdir}/gstreamer-%{majmin}/libgstqcam.*
%endif
%{_libdir}/gstreamer-%{majmin}/libgstqtdemux.*
%{_libdir}/gstreamer-%{majmin}/libgstresample.*
%{_libdir}/gstreamer-%{majmin}/libgstriff.*
%{_libdir}/gstreamer-%{majmin}/libgstrmdemux.*
%{_libdir}/gstreamer-%{majmin}/libgstrtjpeg.*
%{_libdir}/gstreamer-%{majmin}/libgstrtp.*
%{_libdir}/gstreamer-%{majmin}/libgstsdlvideosink.*
%{_libdir}/gstreamer-%{majmin}/libgstsilence.*
%{_libdir}/gstreamer-%{majmin}/libgstsinesrc.*
%{_libdir}/gstreamer-%{majmin}/libgstsmooth.*
%{_libdir}/gstreamer-%{majmin}/libgstsmoothwave.*
%{_libdir}/gstreamer-%{majmin}/libgstsmpte.*
%{_libdir}/gstreamer-%{majmin}/libgstsnapshot.*
%{_libdir}/gstreamer-%{majmin}/libgstspectrum.*
%{_libdir}/gstreamer-%{majmin}/libgstspeed.*
%{_libdir}/gstreamer-%{majmin}/libgststereo.*
%{_libdir}/gstreamer-%{majmin}/libgstswitch.*
%{_libdir}/gstreamer-%{majmin}/libgstsynaesthesia.*
%{_libdir}/gstreamer-%{majmin}/libgsttagedit.*
%{_libdir}/gstreamer-%{majmin}/libgsttcp.*
%{_libdir}/gstreamer-%{majmin}/libgsttrm.*
%{_libdir}/gstreamer-%{majmin}/libgsttextoverlay.*
%{_libdir}/gstreamer-%{majmin}/libgsttheora.*
%{_libdir}/gstreamer-%{majmin}/libgsttimeoverlay.*
%{_libdir}/gstreamer-%{majmin}/libgsttypefindfunctions.*
%{_libdir}/gstreamer-%{majmin}/libgstudp.*
%{_libdir}/gstreamer-%{majmin}/libgstvbidec.*
%{_libdir}/gstreamer-%{majmin}/libgstvcdsrc.*
%{_libdir}/gstreamer-%{majmin}/libgstvideo.*
%{_libdir}/gstreamer-%{majmin}/libgstvideo4linux.*
%{_libdir}/gstreamer-%{majmin}/libgstvideobalance.*
%{_libdir}/gstreamer-%{majmin}/libgstvideocrop.*
%{_libdir}/gstreamer-%{majmin}/libgstvideodrop.*
%{_libdir}/gstreamer-%{majmin}/libgstvideofilter.*
%{_libdir}/gstreamer-%{majmin}/libgstvideobox.*
%{_libdir}/gstreamer-%{majmin}/libgstvideomixer.*
%{_libdir}/gstreamer-%{majmin}/libgstvideorate.*
%{_libdir}/gstreamer-%{majmin}/libgstvideoflip.*
%{_libdir}/gstreamer-%{majmin}/libgstvideoscale.*
%{_libdir}/gstreamer-%{majmin}/libgstvideotestsrc.*
%{_libdir}/gstreamer-%{majmin}/libgstvolenv.*
%{_libdir}/gstreamer-%{majmin}/libgstvolume.*
%{_libdir}/gstreamer-%{majmin}/libgstvorbis.*
%{_libdir}/gstreamer-%{majmin}/libgstwavenc.*
%{_libdir}/gstreamer-%{majmin}/libgstwavparse.*
%{_libdir}/gstreamer-%{majmin}/libgstximagesink.*
%{_libdir}/gstreamer-%{majmin}/libgstxvimagesink.*
%{_libdir}/gstreamer-%{majmin}/libgstxwindowlistener.*
%{_libdir}/gstreamer-%{majmin}/libgsty4menc.*
%{_libdir}/gstreamer-%{majmin}/libgstmixmatrix.*
%{_mandir}/man*/*

# Added when using pristine sources
%{_libdir}/gstreamer-%{majmin}/libgstmp1videoparse.*
%{_libdir}/gstreamer-%{majmin}/libgstmpeg1systemencode.*
%{_libdir}/gstreamer-%{majmin}/libgstmpeg2subt.*
%{_libdir}/gstreamer-%{majmin}/libgstmpegaudio.*
%{_libdir}/gstreamer-%{majmin}/libgstmpegaudioparse.*
%{_libdir}/gstreamer-%{majmin}/libgstmpegstream.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/gstreamer-%{majmin}/gst/*
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*so

%changelog
* Wed Oct 06 2004 Colin Walters <walters@redhat.com> - 0.8.5-1
- Update to 0.8.5
- Add mngsink
- Remove speex for now, configure check is buggy

* Fri Sep 24 2004 Colin Walters <walters@redhat.com> - 0.8.4-2
- Add gstreamer-plugins-0.8.4-vorbis-seek-workaround.patch for 133411

* Mon Aug 31 2004 Colin Walters <walters@redhat.com> - 0.8.4-1
- Update to 0.8.4
- Add gstglimagesink

* Mon Aug 07 2004 Colin Walters <walters@redhat.com> - 0.8.3-2
- Restore media-info, which was not shipped for some unknown reason (#129392)

* Mon Aug 02 2004 Colin Walters <walters@redhat.com> - 0.8.3-1
- Update to 0.8.3
- Remove alsa fixes
- Kill off lame plugin
- Add alphacolor, decodebin, multifilesink, and playbin.

* Wed Jul 28 2004 Colin Walters <walters@redhat.com> - 0.8.2-6
- Really restore ffmpegcolorspace
- Reinstate checks for exact plugins installed, i was a
  bit shortsighted in removing it
- BuildRequire libtheora-devel
- Ensure we disable faad and sndfile even if they are installed

* Tue Jul 27 2004 Colin Walters <walters@redhat.com> - 0.8.2-5
- Re-add ffmpegcolorspace, since it does not have patent issues
- Restore smp_mflags

* Fri Jul 16 2004 Colin Walters <walters@redhat.com> - 0.8.2-4
- Backported ALSA fixes from CVS HEAD

* Tue Jul 05 2004 Colin Walters <walters@redhat.com> - 0.8.2-3
- Another rebuild to placate beehive!

* Tue Jul 05 2004 Colin Walters <walters@redhat.com> - 0.8.2-2
- Rebuild to placate beehive

* Wed Jun 23 2004 Colin Walters <walters@redhat.com> - 0.8.2-1
- Update to 0.8.2, fixes numerous bugs
- Remove upstreamed memleaks patch

* Sun Jun 20 2004 Jeremy Katz <katzj@redhat.com> - 0.8.1-5
- rebuild to lose gtk+ 1.2 dependency

* Wed Jun 15 2004 Colin Walters <walters@redhat.com> 0.8.1-4
- BuildRequire libghttp-devel

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed May 19 2004 Colin Walters <walters@redhat.com> 0.8.1-3
- Don't lose if gst-register isn't installed

* Fri May 07 2004 Colin Walters <walters@redhat.com> 0.8.1-2
- Apply patch to fix memleaks

* Wed Apr 15 2004 Colin Walters <walters@redhat.com> 0.8.1-1
- Update to 0.8.1

* Wed Mar 31 2004 Colin Walters <walters@redhat.com> 0.8.0-3
- Second attempt at rebuild to pick up new libdv

* Tue Mar 30 2004 Colin Walters <walters@redhat.com> 0.8.0-2
- Rebuild to pick up new libdv (hopefully).
- Use one big glob to capture all plugins.  No GStreamer
  plugin that's included directly in the tarball that I am
  aware of besides ffmpeg includes patented code directly,
  so this should be safe.

* Tue Mar 16 2004 Alex Larsson <alexl@redhat.com> 0.8.0-1
- update to 0.8.0

* Thu Mar 11 2004 Alex Larsson <alexl@redhat.com> 0.7.6-2
- correct plugin names

* Wed Mar 10 2004 Alex Larsson <alexl@redhat.com> 0.7.6-1
- update to 0.7.6

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Mar  1 2004 Alexander Larsson <alexl@redhat.com> 0.7.5-2
- Make alsa default sink/source instead of oss.

* Fri Feb 27 2004 Alexander Larsson <alexl@redhat.com> 0.7.5-1
- update to 0.7.5

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 28 2004 Alexander Larsson <alexl@redhat.com> 0.7.3-2
- Use versioned gst-register

* Wed Jan 28 2004 Alexander Larsson <alexl@redhat.com> 0.7.3-1
- update to 0.7.3

* Thu Nov 27 2003 Thomas Woerner <twoerner@redhat.com> 0.6.3-4
- added BuildRequires for libraw1394-devel

* Wed Sep 17 2003 Bill Nottingham <notting@redhat.com> 0.6.3-3
- more cleanups

* Fri Sep 12 2003 Nalin Dahyabhai <nalin@redhat.com> 0.6.3-2
- build gstcolorspace against a static bundled libHermes, which might want
  to move into its own package at some point
- explicitly list the plugins which are built in the files manifest so that
  we get errors if there are some which don't get built or get added between
  releases
- disable qcam on amd64 -- configure disables it on non-i386 arches
- limit 1394 support to amd64,ia64,ppc,ppc64,x86

* Thu Sep 11 2003 Alexander Larsson <alexl@redhat.com> 0.6.3-1
- Update to 0.6.3 (gnome 2.4 final)
- remove all mpeg plugins

* Tue Aug 19 2003 Alexander Larsson <alexl@redhat.com> 0.6.2-1
- 0.6.2

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed May 21 2003 Jeremy Katz <katzj@redhat.com> 0.6.0-7
- use automake 1.6

* Mon Feb 17 2003 Florian La Roche <Florian.LaRoche@redhat.de>
- rebuild to get sane s390x requires

* Tue Feb 11 2003 Jonathan Blandford <jrb@redhat.com> 0.6.0-4
- unset the DISPLAY when running gst-register

* Sat Feb  8 2003 Bill Nottingham <notting@redhat.com> 0.6.0-4
- move libgst*.so.X.X to main package; things require them (#80518, #83805)
- gstreamer-plugins-devel requires gstreamer-devel (#82506)

* Tue Feb  4 2003 Jonathan Blandford <jrb@redhat.com> 0.6.0-3
- remove ffmpeg for now.  It doesn't build -fPIC

* Tue Feb 04 2003 Phil Knirsch <pknirsch@redhat.com> 0.6.0-2
- Bump release and rebuild.

* Thu Jan 30 2003 Jonathan Blandford <jrb@redhat.com>
- new version.  Requires new gstreamer.

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Wed Jan 15 2003 Matt Wilson <msw@redhat.com> 0.5.0-18
- disable qcam on all non x86 and x86_64 platforms

* Mon Dec 30 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- fix spec file to better remove libgstmedia-info
- exclude for mainframe

* Thu Dec 19 2002 Elliot Lee <sopwith@redhat.com> 0.5.0-15
- Include ia64
- Add BuildRequires: autoconf automake

* Wed Dec 18 2002 Jonathan Blandford <jrb@redhat.com>
- rebuild

* Tue Dec 17 2002 Jonathan Blandford <jrb@redhat.com> 0.5.0-12
- rebuild

* Mon Dec 16 2002 Jonathan Blandford <jrb@redhat.com> 0.5.0-10
- rebuild
- disable tests

* Mon Dec 16 2002 Tim Powers <timp@redhat.com> 0.5.0-9
- rebuild

* Wed Dec 11 2002 Jonathan Blandford <jrb@redhat.com> 0.5.0-7
- fix libdir for ia64.

* Wed Dec 11 2002 Jonathan Blandford <jrb@redhat.com> 0.5.0-3
- ExcludeArch: ia64.   Random assembler errors that I have no hope of fixing
- Add devel package

* Wed Dec 11 2002 Jonathan Blandford <jrb@redhat.com> 0.5.0-1
- 0.5.0
- apparently, festival-devel isn't needed.

* Tue Dec 10 2002 Tim Powers <timp@redhat.com> 0.4.2-3
- rebuild to fix broken dep on libgstreamer-0.4.2.so.0

* Tue Dec  3 2002 Havoc Pennington <hp@redhat.com>
- excludearch the arches that can't build gstreamer cothreads
- well it isn't really SMP-safe
- add patch for including pthread.h when required
- prereq gconftool
- fix typo that broke schema installation in post

* Mon Dec  2 2002 Havoc Pennington <hp@redhat.com>
- initial "official" import
- munge tarball for legal cleanliness

* Thu Nov  7 2002 Jeremy Katz <katzj@redhat.com>
- 0.4.2

* Mon Sep 23 2002 Jeremy Katz <katzj@redhat.com>
- 0.4.1
- install the gconf schema
- use %%configure

* Sun Sep 22 2002 Jeremy Katz <katzj@redhat.com>
- update to 0.4.0
- give explicit vorbis include path, don't run vorbis test

* Sun Aug 11 2002 Jeremy Katz <katzj@redhat.com>
- collapse into one package to preserve some sanity

* Wed Mar 13 2002 Thomas Vander Stichele <thomas@apestaart.org>
- added more BuildRequires and Requires
- rearranged some plugins
- added changelog ;)
