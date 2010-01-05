# $Id: vlc.spec 6047 2007-12-19 11:20:08Z dag $
# Authority: matthias
# Upstream: <vlc-devel$videolan,org>

%define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")

%{?fedora: %{expand: %%define fc%{fedora} 1}}

%{!?dtag:%define _with_avahi 1}

### Problems with dirac
%define _without_dirac 1

%ifarch %{ix86}
%define _with_loader 1
%endif

%{?fc7:%define _with_avahi 1}
%{?el5:%define _with_avahi 1}
%{?fc6:%define _with_avahi 1}
%{?fc5:%define _with_avahi 1}

%{?el5:%define mozilla xulrunner-devel nspr-devel}
%{?el5:%define _without_jack 1}

%{?el4:%define mozilla seamonkey-devel}
%{?el4:%define _without_jack 1}
%{?el4:%define _without_modxorg 1}
%{?el4:%define _without_sysfs 1}
%{?el4:%define _without_upnp 1}

%{?el3:%define mozilla seamonkey-devel}
%{?el3:%define _without_alsa 1}
%{?el3:%define _without_fribidi 1}
%{?el3:%define _without_hal 1}
%{?el3:%define _without_jack 1}
%{?el3:%define _without_modxorg 1}
%{?el3:%define _without_sysfs 1}
%{?el3:%define _without_theora 1}
#{?el3:#define _without_upnp 1}
#{?el3:#define _without_wxwidgets 1}

%define desktop_vendor rpmforge
%define ffmpeg_date 20061215
%define live_date 2006.12.08

Summary: The VideoLAN client, also a very good standalone video player
Name: vlc
Version: 0.8.6i
Release: 2%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://www.videolan.org/

Source0: http://downloads.videolan.org/pub/videolan/vlc/%{version}/vlc-%{version}.tar.bz2
Source1: http://downloads.videolan.org/pub/videolan/vlc/%{version}/contrib/ffmpeg-%{ffmpeg_date}.tar.bz2
Source2: http://www.live555.com/liveMedia/public/live.%{live_date}.tar.gz
Patch0: vlc-0.8.6-ffmpegX11.patch
Patch1: vlc-0.8.6-wx28.patch
#Patch2: vlc-0.8.6a-faad2.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, libpng-devel, libxml2-devel, libtiff-devel
BuildRequires: libgcrypt-devel, gnutls-devel, libtar-devel
BuildRequires: libjpeg-devel
Buildrequires: autoconf, automake, libtool
%{?_with_avahi:BuildRequires: avahi-devel}
%{?_with_cddax:BuildRequires: cdparanoia-devel}
%{?_with_glide:BuildRequires: Glide3-devel}
%{?_with_hal:BuildRequires: hal-devel}
%{!?_without_modxorg:BuildRequires: libGLU-devel, libXt-devel, libXv-devel, libXinerama-devel, libXxf86vm-devel}
%{?_without_modxorg:BuildRequires: XFree86-devel}
%{?_with_mozilla:BuildRequires: %{mozilla}}
%{?_with_portaudio:BuildRequires: portaudio-devel}
%{!?_without_a52:BuildRequires: a52dec-devel}
%{!?_without_aa:BuildRequires: aalib-devel}
%{!?_without_alsa:BuildRequires: alsa-lib-devel}
%{!?_without_amr:BuildRequires: amrnb-devel amrwb-devel}
%{!?_without_arts:BuildRequires: arts-devel}
%{!?_without_caca:BuildRequires: libcaca-devel}
%{!?_without_cddb:BuildRequires: libcddb-devel}
%{!?_without_cdio:BuildRequires: libcdio-devel}
%{!?_without_daap:BuildRequires: libopendaap-devel}
#{!?_without_dc1394:BuildRequires: libdc1394-devel}
%{!?_without_dca:BuildRequires: libdca-devel}
%{!?_without_dirac:BuildRequires: dirac-devel >= 0.6.0}
%{!?_without_directfb:BuildRequires: directfb-devel >= 1.0.0}
%{!?_without_dvbpsi:BuildRequires: libdvbpsi-devel}
%{!?_without_dvdnav:BuildRequires: libdvdnav-devel}
%{!?_without_dvdread:BuildRequires: libdvdread-devel}
%{!?_without_esd:BuildRequires: esound-devel}
%{!?_without_faad2:BuildRequires: faad2-devel >= 2.5}
%{!?_without_ffmpeg:BuildRequires: lame-devel, faac-devel}
%{!?_without_flac:BuildRequires: flac-devel}
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}
%{!?_without_fribidi:BuildRequires: fribidi-devel}
%{!?_without_gnomevfs:BuildRequires: gnome-vfs2-devel}
#{!?_without_goom:BuildRequires: goom-devel}
%{!?_without_gsm:BuildRequires: gsm-devel}
%{!?_without_hal:BuildRequires: hal-devel}
%{!?_without_id3tag:BuildRequires: libid3tag-devel}
%{!?_without_jack:BuildRequires: jack-audio-connection-kit-devel}
%{!?_without_lirc:BuildRequires: lirc-devel}
%{!?_without_mad:BuildRequires: libmad-devel}
%{!?_without_mkv:BuildRequires: libebml-devel >= 0.7.6, libmatroska-devel}
%{!?_without_modplug:BuildRequires: libmodplug-devel}
%{!?_without_mpcdec:BuildRequires: libmpcdec-devel}
%{!?_without_mpeg2dec:BuildRequires: mpeg2dec-devel}
%{!?_without_ncurses:BuildRequires: ncurses-devel}
%{!?_without_ogg:BuildRequires: libogg-devel}
%{!?_without_sdl:BuildRequires: SDL-devel, SDL_image-devel}
%{!?_without_shout:BuildRequires: libshout-devel >= 2.2.2}
%{!?_without_smb:BuildRequires: samba-common}
%{!?_without_speex:BuildRequires: speex-devel}
%{!?_without_svgalib:BuildRequires: svgalib-devel}
%{!?_without_sysfs:BuildRequires: libsysfs-devel}
%{!?_without_theora:BuildRequires: libtheora-devel}
%{!?_without_twolame:BuildRequires: twolame-devel}
%{!?_without_upnp:BuildRequires: libupnp-devel}
%{!?_without_upnp:BuildRequires: libupnp-devel}
%{!?_without_vcd:BuildRequires: vcdimager-devel}
%{!?_without_vorbis:BuildRequires: libvorbis-devel}
%{!?_without_wxwidgets:BuildRequires: wxGTK-devel}
%{!?_without_x264:BuildRequires: x264-devel}
%{!?_without_xosd:BuildRequires: xosd-devel}
Obsoletes: videolan-client < 0.8.5-4
Provides: videolan-client = %{version}-%{release}

%description
VideoLAN Client (VLC) is a highly portable multimedia player for various
audio and video formats (MPEG-1, MPEG-2, MPEG-4, DivX, mp3, ogg, ...) as
well as DVDs, VCDs, and various streaming protocols.

Available rpmbuild rebuild options :
--with mga ncurses glide pth mozilla portaudio avahi hal
--without dvdread dvdnav dvbpsi v4l avi asf aac ogg mad ffmpeg cdio
          a52 vorbis mpeg2dec flac aa caca esd arts alsa wxwidgets xosd
          lsp lirc id3tag faad2 theora mkv modplug smb speex glx x264
          gnomevfs vcd daap upnp pvr live

Options that would need not yet existing add-on packages :
--with tremor tarkin svgalib ggi

%package devel
Summary: Header files and static library from the Videolan Client
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
VideoLAN Client (VLC) is a highly portable multimedia player for various
audio and video formats (MPEG-1, MPEG-2, MPEG-4, DivX, mp3, ogg, ...) as
well as DVDs, VCDs, and various streaming protocols.

Install this package if you need to build Videolan Client plugins or intend
to link statically to it.

%package -n mozilla-vlc
Summary: VLC Media Player plugin for Mozilla compatible web browsers
Group: Applications/Multimedia
Requires: %{name} = %{version}-%{release}

%description -n mozilla-vlc
This package contains a VLC Media Player plugin for Mozilla compatible
web browsers.

VLC (initially VideoLAN Client) is a highly portable multimedia player
for various audio and video formats (MPEG-1, MPEG-2, MPEG-4, DivX,
mp3, ogg, ...) as well as DVDs, VCDs, and various streaming protocols.
It can also be used as a server to stream in unicast or multicast in
IPv4 or IPv6 on a high-bandwidth network.

%prep
%setup -a 1 -a 2
%patch0 -p1 -b .ffmpegX11
#patch1 -p1 -b .wx28

### Use regex to change FAAD2 interface
#patch2 -p1 -b .faad2
%{__perl} -pi -e 's|\bfaacDec\B|NeAACDec|g' modules/codec/faad.c

### Fix PLUGIN_PATH path for lib64
%{__perl} -pi -e 's|/lib\b|/%{_lib}|g' vlc-config.in.in configure*

### Fix ffmpeg to find libgsm
%{__perl} -pi -e 's|\bgsm.h|gsm/gsm.h|g' ffmpeg-%{ffmpeg_date}/configure ffmpeg-%{ffmpeg_date}/libavcodec/libgsm.c

%build
export CFLAGS="%{optflags}"

### Build bundeled ffmpeg first
%if %{!?_without_ffmpeg:1}0
pushd ffmpeg-%{ffmpeg_date}
    ./configure \
        --enable-faac \
        --enable-gpl \
        --enable-mp3lame \
        --enable-pp
    %{__make} %{?_smp_mflags}
popd

for pkgconfig in theora vorbis vorbisenc ogg ;do
    %{__ln_s} -f %{_libdir}/pkgconfig/$pkgconfig.pc
done
%endif

### Then bundled live555
%if %{!?_without_live:1}0
pushd live
    # Force the use of our CFLAGS
    %{__perl} -pi -e 's|-O2|%{optflags} -fPIC -DPIC|g' config.linux
    # Configure and build
    ./genMakefiles linux && %{__make}
popd
%endif

# Altivec compiler flags aren't set properly (0.8.2)
%ifarch ppc ppc64
export CFLAGS="%{optflags} -maltivec -mabi=altivec"
%endif

### Workaround to make -lX11 work on 64bit
export LDFLAGS="-L/usr/X11R6/%{_lib}"
%configure \
    --disable-dependency-tracking \
    --disable-rpath \
    --disable-static \
    --with-PIC \
    --enable-release \
%{?_without_a52:--disable-a52} \
%{!?_without_aa:--enable-aa} \
%{!?_without_alsa:--enable-alsa} \
%{!?_without_arts:--enable-arts} \
%{!?_without_caca:--enable-caca} \
%{?_with_cddax:--enable-cddax} \
%{?_without_cdio--disable-libcdio} \
%{!?_without_dirac:--enable-dirac} \
%{!?_without_directfb:--enable-directfb} \
%{!?_without_directfb:--with-directfb="%{_includedir}"} \
%{!?_without_dvbpsi:--enable-dvbpsi} \
%{?_without_dvdnav:--disable-dvdnav} \
%{!?_without_dvdread:--enable-dvdread} \
%{!?_without_esd:--enable-esd} \
%{!?_without_faad2:--enable-faad} \
    --enable-fbosd \
%{!?_without_ffmpeg:--enable-ffmpeg} \
%{!?_without_ffmpeg:--with-ffmpeg-tree="ffmpeg-%{ffmpeg_date}"} \
%{!?_without_ffmpeg:--with-ffmpeg-a52 --with-ffmpeg-faac --with-ffmpeg-mp3lame} \
%{!?_without_ffmpeg:--enable-libamr-nb --enable-libamr-wb --with-ffmpeg-ogg} \
%{!?_without_ffmpeg:--with-ffmpeg-theora --with-ffmpeg-vorbis --with--ffmpeg-zlib} \
%{!?_without_flac:--enable-flac} \
%{?_without_fribidi:--disable-fribidi} \
    --enable-galaktos \
%{?_with_ggi:--enable-ggi} \
%{?_with_glide:--enable-glide} \
%{?_without_glx:--disable-glx} \
%{!?_without_gnomevfs:--enable-gnomevfs} \
%{!?_without_jack:--enable-jack} \
%{!?_without_lirc:--enable-lirc} \
%{!?_without_live:--enable-live555 --with-live555-tree="$(pwd)/live"} \
%{?_with_loader:--enable-loader} \
%{?_without_mad:--disable-mad} \
%{?_with_mga:--enable-mga} \
%{?_without_mkv:--disable-mkv} \
%{?_without_modplug:--disable-mod} \
%{?_with_mozilla:--enable-mozilla} \
%{?_without_mpeg2dec:--disable-libmpeg2} \
    --enable-musicbrainz \
%{!?_without_ncurses:--enable-ncurses} \
%{?_without_ogg:--disable-ogg} \
%{!?_without_opencv:--enable-opencv} \
%{?_with_portaudio:--enable-portaudio} \
%{?_with_pth:--enable-pth} \
    --enable-pulse \
%{!?_without_pvr:--enable-pvr} \
    --enable-real \
    --enable-realrtsp \
%{?_without_sdl:--disable-sdl} \
%{!?_without_shout:--enable-shout} \
%{?_without_slp:--disable-slp} \
%{?_without_smb:--disable-smb} \
    --enable-snapshot \
%{?_without_speex:--disable-speex} \
    --enable-svg \
%{!?_without_svgalib:--enable-svgalib} \
    --enable-switcher \
%{?_with_tarkin:--enable-tarkin} \
%{!?_without_theora:--enable-theora} \
%{?_with_tremor:--enable-tremor} \
%{!?_without_twolame:--enable-twolame} \
%{!?_without_upnp:--enable-upnp} \
%{!?_without_v4l:--enable-v4l} \
%{?_without_vorbis:--disable-vorbis} \
%{?_without_wxwidgets:--disable-wxwidgets --disable-skins2} \
%{?_without_x264:--disable-x264} \
%{!?_without_xosd:--enable-xosd} \
    --enable-xvmc
#{!?_without_dc1394:--enable-dc1394} \
#{!?_without_goom:--enable-goom} \
#{!?_without_ffmpeg:--with-ffmpeg-mp3lame --with-ffmpeg-faac} \
#{!?_without_ffmpeg:--with-ffmpeg-tree=ffmpeg-%{ffmpeg_date}} \
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot} _docs
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}
# Include the docs below, our way
%{__mv} %{buildroot}%{_docdir}/vlc _docs
# So that the icon gets themable (still required in 0.8.6)
%{__mkdir_p} %{buildroot}%{_datadir}/pixmaps
%{__cp} -ap %{buildroot}%{_datadir}/vlc/vlc48x48.png %{buildroot}%{_datadir}/pixmaps/vlc.png

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING ChangeLog MAINTAINERS README THANKS
%doc _docs/*
%{_bindir}/svlc
%{_bindir}/vlc
%{_bindir}/wxvlc
%{_libdir}/vlc/
#exclude %{_libdir}/vlc/*.a
%{_datadir}/applications/vlc.desktop
%{_datadir}/pixmaps/vlc.png
%{_datadir}/vlc/

%files devel
%defattr(-, root, root, 0755)
%doc HACKING
%{_bindir}/vlc-config
%{_includedir}/vlc/
%exclude %{_libdir}/libvlc.a

%if %{?_with_mozilla:1}0
%files -n mozilla-vlc
%defattr(-, root, root, 0755)
%{_libdir}/mozilla/plugins/libvlcplugin.so
%endif

%changelog
* Fri Nov 06 2009 Dag Wieers <dag@wieers.com> - 0.8.6i-2
- Rebuild against newer faad2 2.7.

* Tue Sep 16 2008 Dag Wieers <dag@wieers.com> - 0.8.6i-1
- Updated to release 0.8.6i.

* Sun Jun 08 2008 Dag Wieers <dag@wieers.com> - 0.8.6h-1
- Updated to release 0.8.6h.

* Sat May 17 2008 Dag Wieers <dag@wieers.com> - 0.8.6g-1
- Updated to release 0.8.6g.

* Mon Dec 17 2007 Dag Wieers <dag@wieers.com> - 0.8.6d-2
- Rebuild against libmpcdec 1.2.6 and libupnp 1.6.x.

* Sat Dec 01 2007 Dag Wieers <dag@wieers.com> - 0.8.6d-1
- Updated to release 0.8.6d.

* Wed Jul 11 2007 Matthias Saou <http://freshrpms.net/> 0.8.6c-1
- Remove no longer needed flac patch.

* Mon Jun 18 2007 Dag Wieers <dag@wieers.com> - 0.8.6c-1
- Updated to release 0.8.6c.

* Mon Jun 04 2007 Dag Wieers <dag@wieers.com> - 0.8.6b-3
- Rebuild against x264-0.4.20070529 because I missed it.

* Thu May 31 2007 Matthias Saou <http://freshrpms.net/> 0.8.6b-2
- Still no dc1394 support.
- F7 rebuild.

* Sat Apr 21 2007 Dag Wieers <dag@wieers.com> - 0.8.6b-1
- Updated to release 0.8.6b.

* Wed Mar 28 2007 Matthias Saou <http://freshrpms.net/> 0.8.6a-4
- Enable upnp support (Paul Stewart).

* Wed Feb 14 2007 Matthias Saou <http://freshrpms.net/> 0.8.6a-3
- Add patch for (new) FLAC 1.1.3 support.

* Tue Jan 16 2007 Dag Wieers <dag@wieers.com> - 0.8.6a-2
- Build against wxGTK 2.6.3.

* Mon Jan  8 2007 Matthias Saou <http://freshrpms.net/> 0.8.6a-1
- Update to 0.8.6a.
- Add faad2 patch.

* Mon Jan  8 2007 Matthias Saou <http://freshrpms.net/> 0.8.6-2
- Add patch to fix wxGTK 2.8 build (FC devel).
- Revert many useless changes to the ffmpeg compilation since we use it as
  a statically linked library and don't need nor want most of its features.

* Fri Dec 15 2006 Matthias Saou <http://freshrpms.net/> 0.8.6-1
- Update to 0.8.6.
- Update ffmpeg to 20060710.
- Update live to 2006.12.08.
- Require faad2 >= 2.5 since vlc no longer builds with previous 2.0 release.
- No longer create our own desktop file, it's taken care of now.
- Rename deprecated livedotcom options to live555.
- Add libjpeg, libsysfs and libtar build requirements.
- Add libupnp support, enabled by default.
- Add autotools build requirements to make build output more silent and run
  configure only once :-/
- Include patch to fix final binary linking, where -lX11 was missing.
- Add jack support, and soon goom (lib required?).

* Tue Oct 24 2006 Matthias Saou <http://freshrpms.net/> 0.8.5-5
- Update live lib to 2006.10.18a.
- Try to update fffmpeg... but... nope, way too hard :-(
- Update x264 patch for it to work with latest x264.

* Mon Sep 25 2006 Matthias Saou <http://freshrpms.net/> 0.8.5-4
- Rename videolan-client to vlc to match upstream and what Ville asked before.
- Rebuild against new libcdio.
- Update to ffmpeg snapshot 20051207, more recent ones don't work.
- Update live lib to 2006.09.20.

* Tue Sep 19 2006 Matthias Saou <http://freshrpms.net/> 0.8.5-3
- Add patch for recent x264 versions (no more b_cbr).

* Thu Jun 15 2006 Matthias Saou <http://freshrpms.net/> 0.8.5-2
- Rebuild for FC development (gnutls update).
- Add -lX11 extra libs for ffmpeg to build with the latest xorg.

* Fri May 12 2006 Matthias Saou <http://freshrpms.net/> 0.8.5-1
- Update to 0.8.5.
- Update live lib to 2006.05.11.
- Remove no longer needed extraqualif patch.
- Added libXt-devel and libXxf86vm-devel to the modular X buil requirements.
- Added hal, mpcdec, cddb and dca support.

* Wed Mar 22 2006 Matthias Saou <http://freshrpms.net/> 0.8.4a-4
- Add missing modular X build requirements.
- Add libtiff-devel build requirement.
- Add avahi (bonjour) support.

* Fri Mar 17 2006 Matthias Saou <http://freshrpms.net/> 0.8.4a-3
- Fix modular X build requirement : libGLU-devel was missing.

* Fri Jan 13 2006 Matthias Saou <http://freshrpms.net/> 0.8.4a-2
- Add modular xorg build conditional.
- Include extraqualif patch to fix FC5 / gcc 4.1 errors.

* Sun Jan  8 2006 Matthias Saou <http://freshrpms.net/> 0.8.4a-1
- Update to 0.8.4a.
- Enable live555.

* Fri Dec  9 2005 Matthias Saou <http://freshrpms.net/> 0.8.4-3
- Add PVR option, enabled by default.
- Rebuild against new libdvbpsi.

* Tue Nov 29 2005 Matthias Saou <http://freshrpms.net/> 0.8.4-2
- Re-add --x-libraries prefix, as it's still required for x86_64 to build.

* Sun Nov 27 2005 Matthias Saou <http://freshrpms.net/> 0.8.4-1
- Update to 0.8.4.
- Remove no longer needed 64bit and asm patches.
- Exclude static libraries (from the devel package).
- Add SDL_image-devel to the sdl conditional build (now checked for).
- Add gnome-vfs, vcdimager, libopendaap support.
- Ready for bonjour support (avahi will be in FC5).
- Now enable x264 by default (there are freshrpms.net packages of it now).
- Add hal, but disable for now (build fails on FC4).

* Tue Jul 12 2005 Matthias Saou <http://freshrpms.net/> 0.8.2-3
- Force altivec gcc flags on ppc as configure doesn't set them properly.
- Fix PLUGIN_PATH path for lib64 (they got searched for in lib, not lib64).

* Tue Jul 12 2005 Matthias Saou <http://freshrpms.net/> 0.8.2-2
- Include vlc-0.8.2-asm.patch to fix build on x86_64, thanks to Sam Lau.

* Mon Jun 27 2005 Matthias Saou <http://freshrpms.net/> 0.8.2-1
- Update to 0.8.2, ffmpeg 20050513.
- Remove explicit stripping of the plugin libraries (14MB debuginfo now!).
- Change lirc build requirement to lirc-devel.
- FC4 speex package is too old, so it's disabled.
- Update DVD options : Remove dvd and dvdplay, add dvdnav.
- Add libxml2-devel, libgcrypt-devel and gnutls-devel build dependencies.
- Add smbclient support (--without smb to disable).
- Add libcdio support.
- Add libcaca support.
- Add portaudio support (disabled by default).
- Prepare for future x264 support (no package yet).
- Remove obsolete options (xvid, dv, rawdv, mp4, cinepack, gtk, gnome, qt, kde,
  ntfwin), unrelevant options (embedded, Windows) and defaults (X, oss...).
- Re-enable faac in ffmpeg.
- Don't enable pth by default, as it's not the default the developers chose.

* Wed Apr 06 2005 Dag Wieers <dag@wieers.com> - 0.8.1-3
- Added libmodplug support, enabled by default.

* Tue Mar  1 2005 Matthias Saou <http://freshrpms.net/> 0.8.1-2
- Update ffmpeg to 20050209.
- Added libmatroska (mkv) support, enabled by default.

* Tue Nov 16 2004 Matthias Saou <http://freshrpms.net/> 0.8.1-1
- Update to 0.8.1.

* Thu Nov  4 2004 Matthias Saou <http://freshrpms.net/> 0.8.0-1
- Update to 0.8.0 final and ffmpeg 20041101 snapshot.
- Move lib/vlc/*.a files to devel package.

* Fri Oct  1 2004 Matthias Saou <http://freshrpms.net/> 0.8.0-0.test2.1
- Update to 0.8.0-test2 and ffmpeg 20041001 snapshot.

* Tue Jun  1 2004 Matthias Saou <http://freshrpms.net/> 0.7.2-1
- Update to 0.7.2.
- Added fribidi support.
- Added --enable-gpl to ffmpeg for the postprocessing code to stay enabled.

* Mon May 17 2004 Matthias Saou <http://freshrpms.net/> 0.7.1-1
- Fix the desktop entry's description, make the icon themable.
- Add theora and faad2 support, enabled by default.

* Sat May 15 2004 Dag Wieers <dag@wieers.com> - 0.7.1-0.1
- Updated to release 0.7.1.

* Tue Feb 24 2004 Matthias Saou <http://freshrpms.net/> 0.7.0-0.3
- Rebuild against new libfame.

* Sat Feb 21 2004 Matthias Saou <http://freshrpms.net/> 0.7.0-0.1
- Update to 0.7.0.
- Bundle ffmpeg to avoid all the hassles of using the shared lib.
- Move the (now installed) docs to the proper location.
- Added wxWindows interface, the currently most maintained.

* Tue Nov 11 2003 Matthias Saou <http://freshrpms.net/> 0.6.2-0.2
- Rebuild for Fedora Core 1.

* Thu Aug 14 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.6.2.

* Tue Jul  1 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.6.0.
- Added libid3tag support.
- Added mpeg2dec dependency, cvs version, same for ffmpeg.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.

* Tue Mar 11 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.5.2.
- Fix the dv build dependency, thanks to Alan Hagge.
- Added flac support.
- Fixed the libdvbpsi requirements.

* Mon Feb 24 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt against the new xosd lib.

* Wed Feb 19 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.5.1.
- Major spec file update.

* Fri Nov 15 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.4.6.

* Tue Oct 22 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.4.5.
- Minor --with / --without adjustments.

* Sun Oct  6 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 8.0.
- New menu entry.
- Added all --without options and --with qt.

* Mon Aug 12 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.4.4.

* Fri Jul 26 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.4.3.

* Fri Jul 12 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.4.2.

* Wed Jun  5 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.4.1.

* Fri May 24 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.4.0.
- Disabled qt interface, it's hell to build with qt2/3!
- Use %%find_lang and %%{?_smp_mflags}.

* Fri Apr 19 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.3.1.

* Mon Apr  8 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.3.0.

* Sat Jan 12 2002 Matthias Saou <http://freshrpms.net/>
- Removed the dependency on libdvdcss package, use the built in one instead,
  because 1.x.x is not as good as 0.0.3.ogle3.

* Tue Jan  1 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.2.92.
- Build fails with libdvdcss < 1.0.1.

* Tue Nov 13 2001 Matthias Saou <http://freshrpms.net/>
- Update to 0.2.91 and now requires libdvdcss 1.0.0.

* Mon Oct 22 2001 Matthias Saou <http://freshrpms.net/>
- Split libdvdcss into a separate package since it's also needed by the
  xine menu plugin.

* Thu Oct 11 2001 Matthias Saou <http://freshrpms.net/>
- Updated to 0.2.90.
- Removed ggi, svgalib and aalib since they aren't included in Red Hat 7.2.

* Mon Aug 27 2001 Matthias Saou <http://freshrpms.net/>
- Updated to 0.2.83.

* Sat Aug 11 2001 Matthias Saou <http://freshrpms.net/>
- Updated to 0.2.82.

* Mon Jul 30 2001 Matthias Saou <http://freshrpms.net/>
- Updated to 0.2.81.
- Added all the new split libdvdcss.* files to the %%files section.

* Tue Jun  5 2001 Matthias Saou <http://freshrpms.net/>
- Updated to the latest release, 0.2.80.

* Wed May 30 2001 Matthias Saou <http://freshrpms.net/>
- Updated to today's CVS version, works great! :-)
- Fixed the desktop menu entry.

* Tue May 22 2001 Matthias Saou <http://freshrpms.net/>
- Spec file cleanup to make it look more like others do.
- Added the use of many macros.
- Disabled automatic requires and provides (the package always needed qt,
  gtk+, gnome etc. otherwise).
- Added a system desktop menu entry.

* Mon Apr 30 2001 Arnaud Gomes-do-Vale <arnaud@glou.org>
Added relocation support and compile fixes for Red Hat 7.x.

* Sat Apr 28 2001 Henri Fallon <henri@videolan.org>
New upstream release (0.2.73)

* Mon Apr 16 2001 Samuel Hocevar <sam@zoy.org>
New upstream release (0.2.72)

* Fri Apr 13 2001 Samuel Hocevar <sam@zoy.org>
New upstream release (0.2.71)

* Sun Apr 8 2001 Christophe Massiot <massiot@via.ecp.fr>
New upstream release (0.2.70)

* Fri Feb 16 2001 Samuel Hocevar <sam@via.ecp.fr>
New upstream release

* Tue Aug  8 2000 Samuel Hocevar <sam@via.ecp.fr>
Added framebuffer support

* Sun Jun 18 2000 Samuel Hocevar <sam@via.ecp.fr>
Took over the package

* Thu Jun 15 2000 Eric Doutreleau <Eric.Doutreleau@int-evry.fr>
Initial package

