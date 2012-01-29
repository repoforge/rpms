# $Id$
# Authority: matthias

%define _default_patch_fuzz 2

%define desktop_vendor rpmforge

%define _without_directfb 1
%define _without_ivtv 1
%define _without_jack 1
%define _without_live 1
%define _without_nas 1
%define _without_nemesi 1
%define _without_openal 1
%define _without_xmms 1
%define _without_xss 1

### Use internal/ffmpeg libraries
%define _without_dvdnav 1
%define _without_dvdread 1
%define _without_faac 1
%define _without_faad2 1

%{?el6:%define _without_lirc 1}

### Disable internal ASS for RHEL5 (and older) as it requires fontconfig >= 2.4.2 :-/
%{?el5:%define _without_ass 1}
%{?el5:%define _without_internal_ass 1}
%{?el5:%define _without_pulseaudio 1}
%{?el5:%define _without_schroedinger 1}
%{?el5:%define _without_speex 1}
%{?el4:%define _without_ass 1}

%{?el4:%define _without_giflib 1}
%{?el4:%define _without_internal_ass 1}
%{?el4:%define _without_modxorg 1}
%{?el4:%define _without_pulseaudio 1}
%{?el4:%define _without_sdl 1}
%{?el4:%define _without_samba 1}
%{?el4:%define _without_speex 1}
%{?el4:%define _without_vdpau 1}

%{?el3:%define _without_ass 1}
%{?el3:%define _without_alsa 1}
%{?el3:%define _without_binutils214 1}
%{?el3:%define _without_fribidi 1}
%{?el3:%define _without_giflib 1}
%{?el3:%define _without_hicolortheme 1}
%{?el3:%define _without_internal_ass 1}
%{?el3:%define _without_modxorg 1}
%{?el3:%define _without_pulseaudio 1}
%{?el3:%define _without_samba 1}
%{?el3:%define _without_schroedinger 1}
%{?el3:%define _without_sdl 1}
%{?el3:%define _without_speex 1}
%{?el3:%define _without_theora 1}
%{?el3:%define _without_v4l2 1}
%{?el3:%define _without_vdpau 1}
%{?el3:%define _without_xvmc 1}

%define real_name MPlayer

Summary: MPlayer, the Movie Player for Linux
Name: mplayer
Version: 1.0
%define real_version 2010-07-03
Release: 0.47.svn20100703%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://mplayerhq.hu/

Source0: http://www.mplayerhq.hu/MPlayer/releases/mplayer-export-%{real_version}.tar.bz2
Source1: http://www.mplayerhq.hu/MPlayer/skins/Blue-1.7.tar.bz2
Source10: mplayer-snapshot.sh
Patch2: mplayer-config.patch
Patch8: mplayer-manlinks.patch
Patch10: MPlayer-1.0pre6a-fribidi.patch
Patch14: mplayer-nodvdcss.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: desktop-file-utils
BuildRequires: flac-devel
BuildRequires: freetype-devel >= 2.0.9
BuildRequires: gcc-c++
BuildRequires: ImageMagick
BuildRequires: lame-devel
BuildRequires: libjpeg-devel
BuildRequires: libmad-devel
BuildRequires: libmatroska-devel
BuildRequires: libpng-devel
BuildRequires: libungif-devel
BuildRequires: lzo-devel >= 2.0
BuildRequires: yasm
%{!?_without_a52dec:BuildRequires: a52dec-devel}
%{!?_without_aalib:BuildRequires: aalib-devel}
%{!?_without_alsa:BuildRequires: alsa-lib-devel}
%{!?_without_amr:BuildRequires: opencore-amr-devel}
%{!?_without_arts:BuildRequires: arts-devel}
%{!?_without_ass:BuildRequires: libass-devel, freetype-devel >= 2.1.0}
%{!?_without_caca:BuildRequires: libcaca-devel}
%{!?_without_cdparanoia:BuildRequires: cdparanoia-devel}
%{!?_without_directfb:BuildRequires: directfb-devel >= 1.0.1}
%{!?_without_dts:BuildRequires: libdca-devel}
%{!?_without_dv:BuildRequires: libdv-devel}
%{!?_without_dvdnav:BuildRequires: libdvdnav-devel >= 4.1.3-1}
%{!?_without_dvdread:BuildRequires: libdvdread-devel}
%{!?_without_enca:BuildRequires: enca-devel}
%{!?_without_esound:BuildRequires: esound-devel}
%{!?_without_faac:BuildRequires: faac-devel}
%{!?_without_faad2:BuildRequires: faad2-devel >= 1:2.6.1}
%{!?_without_fame:BuildRequires: libfame-devel}
%{!?_without_fontconfig:BuildRequires: fontconfig-devel}
%{!?_without_fribidi:BuildRequires: fribidi-devel}
%{!?_without_giflib:BuildRequires: giflib-devel}
%{?_without_giflib:BuildRequires: libungif-devel}
%{!?_without_gtk2:BuildRequires: gtk2-devel}
%{!?_without_jack:BuildRequires: jack-audio-connection-kit-devel}
%{!?_without_ladspa:BuildRequires: ladspa-devel}
%{!?_without_lirc:BuildRequires: lirc-devel}
%{!?_without_live555:BuildRequires: live555-devel}
%{!?_without_lzo:BuildRequires: lzo-devel}
%{!?_without_modxorg:BuildRequires: libXv-devel, libXxf86vm-devel, libGL-devel, libXt-devel, xorg-x11-proto-devel, libXinerama-devel, libXScrnSaver-devel, libXv-devel, libXxf86dga-devel}
%{!?_without_modxorg:%{!?_without_xvmc:BuildRequires: libXvMC-devel}}
%{?_without_modxorg:%{!?_without_xvmc:BuildRequires: libXvMCW-devel}}
%{?_without_modxorg:BuildRequires: XFree86-devel}
%{!?_without_mpeg2:BuildRequires: libmpeg2-devel}
%{!?_without_musepack:BuildRequires: libmpcdec-devel >= 1.2.1}
%{!?_without_nas:BuildRequires: nas-devel}
%{!?_without_nemesi:BuildRequires: libnemesi-devel >= 0.6.3}
%{!?_without_openal:BuildRequires: openal-soft-devel}
%{!?_without_pulseaudio:BuildRequires: pulseaudio-lib-devel}
%{!?_without_samba:BuildRequires: samba-common, libsmbclient-devel}
%{!?_without_schroedinger:BuildRequires: schroedinger-devel}
%{!?_without_sdl:BuildRequires: SDL-devel}
%{!?_without_speex:BuildRequires: speex-devel >= 1.1}
%{!?_without_svgalib:BuildRequires: svgalib-devel}
%{!?_without_theora:BuildRequires: libtheora-devel}
%{!?_without_twolame:BuildRequires: twolame-devel}
%{!?_without_vdpau:BuildRequires: libvdpau-devel}
%{!?_without_vorbis:BuildRequires: libvorbis-devel}
%{!?_without_vstream:BuildRequires: vstream-client-devel}
%{!?_without_x264:BuildRequires: x264-devel}
%{!?_without_xmms:BuildRequires: xmms-devel}
%{!?_without_xvid:BuildRequires: xvidcore-devel}
Requires: mplayer-fonts
Requires: mplayer-common = %{version}-%{release}

%description
MPlayer is a multimedia player. It plays most video formats as well as DVDs.
Its big feature is the wide range of supported output drivers. There are also
nice antialiased shaded subtitles and OSD.

On x86, additional Win32 binary codecs should be added to %{_libdir}/codecs/.

Available rpmbuild rebuild options :
--with : dvdread
--without : aalib lirc cdparanoia arts xvid esd lzo fame caca dvb vstream
            theora osdmenu gcccheck fribidi xvmc x264 faac mpc live ladspa
            amrnb samba speex twolame

%package -n mencoder
Summary: MPlayer’s Movie Encoder
Group: Applications/Multimedia
Requires: mplayer-common = %{version}-%{release}

%description -n mencoder
MPlayer’s Movie Encoder is a simple movie encoder, designed to encode
MPlayer-playable movies to other MPlayer-playable formats. It encodes to
MPEG-4 (DivX/XviD), one of the libavcodec codecs and PCM/MP3/VBRMP3 audio
in 1, 2 or 3 passes.  Furthermore  it has stream copying abilities, a
powerful filter system (crop, expand, flip, postprocess, rotate, scale,
noise, rgb/yuv conversion) and more.

%package common
Summary: MPlayer common files
Group: Applications/Multimedia

%description common
This package contains common files for MPlayer packages.

%package gui
Summary: GUI for MPlayer
Group: Applications/Multimedia
Requires: mplayer-common = %{version}-%{release}
%{!?_without_hicolortheme:Requires: hicolor-icon-theme}

%description gui
This package contains a GUI for MPlayer and a default skin for it.

%package doc
Summary: Documentation for MPlayer, the Movie Player for Linux
Group: Applications/Multimedia
Obsoletes: mplayer-docs

%description doc
MPlayer is a movie player. It plays most video formats as well as DVDs.
Its big feature is the wide range of supported output drivers. There are also
nice antialiased shaded subtitles and OSD.

This package contains the end user documentation.

%package tools
Summary: Useful scripts for MPlayer
Group: Applications/Multimedia
Requires: mencoder = %{version}-%{release}
Requires: mplayer = %{version}-%{release}

%description tools
This package contains various scripts from MPlayer TOOLS directory.

%prep
%setup -n mplayer-export-%{real_version} -a 1
%patch2 -p1 -b .config
%patch8 -p1 -b .manlinks
%patch10 -p1 -b .fribidi
%patch14 -p1 -b .nodvdcss

%build
export LDFLAGS="%{!?_without_fontconfig:$(pkg-config --libs fontconfig)} %{!?_without_fribidi:$(pkg-config --libs fribidi)}"
export CFLAGS="%{optflags} -fomit-frame-pointer"
echo | ./configure \
    --prefix="%{_prefix}" \
    --bindir="%{_bindir}" \
    --confdir="%{_sysconfdir}/mplayer" \
    --datadir="%{_datadir}/mplayer" \
    --libdir="%{_libdir}" \
    --mandir="%{_mandir}" \
    --codecsdir="%{_libdir}/codecs" \
    --extra-cflags="%{optflags}%{!?_without_live: -I/usr/include/liveMedia}" \
%{?_without_binutils214:--disable-ssse3} \
    --disable-bitmap-font \
%{?_without_gcccheck:--disable-gcc-check} \
%{?_without_internal_ass:--disable-ass-internal} \
%{?_without_sdl:--disable-sdl} \
    --disable-termcap \
%{!?_without_amr:--enable-libopencore_amrnb --enable-libopencore_amrwb} \
%{!?_without_arts:--enable-arts} \
%{!?_without_ass:--enable-ass} \
%{!?_without_directfb:--enable-directfb} \
%{!?_without_dvdread:--enable-dvdread} \
    --enable-dynamic-plugins \
%{!?_without_esound:--enable-esd} \
%{!?_without_faac:--enable-faac} \
    --enable-fbdev \
%{!?_without_fontconfig:--enable-fontconfig} \
%{!?_without_fribidi:--enable-fribidi} \
    --enable-gui \
%{!?_without_ivtv:--enable-ivtv} \
%{!?_without_jack:--enable-jack} \
    --enable-joystick \
    --enable-largefiles \
%{!?_without_lirc:--enable-lirc} \
%{!?_without_live:--enable-live} \
%{!?_without_openal:--enable-openal} \
%{!?_without_osdmenu:--enable-menu} \
%{!?_without_musepack:--enable-musepack} \
%{!?_without_nemesi:--enable-nemesi} \
    --enable-radio \
    --enable-radio-capture \
    --enable-runtime-cpudetection \
%{!?_without_samba:--enable-smb} \
%{!?_without_sdl:--enable-sdl} \
%{!?_without_svgalib:--enable-svga} \
    --enable-tv-v4l1 \
%{!?_without_v4l2:--enable-tv-v4l2} \
    --enable-unrarexec \
%{!?_without_xmms:--enable-xmms --with-xmmslibdir="%{_libdir}"} \
%{!?_without_xss:--enable-xss} \
%{?_without_modxorg:%{!?_without_xvmc:--enable-xvmc --with-xvmclib="XvMCW"}} \
%{!?_without_modxorg:%{!?_without_xvmc:--enable-xvmc}} \
%ifarch %{ix86}
    --enable-qtx \
    --enable-win32dll \
%endif
    --language="all"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}" INSTALLSTRIP=""

# The default Skin
%{__install} -d -m0755 %{buildroot}%{_datadir}/mplayer/skins/
%{__tar} -xjf %{SOURCE1} --exclude=".svn" -C %{buildroot}%{_datadir}/mplayer/skins/
%{__ln_s} Blue %{buildroot}%{_datadir}/mplayer/skins/default

# The fonts are now in a separate package
%{__rm} -rf %{buildroot}%{_datadir}/mplayer/font || :

# Remove unwanted stuff from the docs to be included
%{__rm} -rf DOCS/{man,xml}/

# Create empty binary codecs directory
%{__install} -d -m0755 %{buildroot}%{_libdir}/codecs

# Default config files
%{__install} -Dp -m0644 etc/example.conf %{buildroot}%{_sysconfdir}/mplayer/mplayer.conf
%{__install} -Dp -m0644 etc/input.conf %{buildroot}%{_sysconfdir}/mplayer/input.conf
%{__install} -Dp -m0644 etc/menu.conf %{buildroot}%{_sysconfdir}/mplayer/menu.conf

# Install tools
for file in TOOLS/*.sh; do
    %{__install} -Dp -m0755 $file %{buildroot}%{_bindir}/$(basename $file .sh)
done
for file in TOOLS/*.pl; do
    %{__install} -Dp -m0755 $file %{buildroot}%{_bindir}/$(basename $file .pl)
done
for file in TOOLS/*.py; do
    %{__install} -Dp -m0755 $file %{buildroot}%{_bindir}/$(basename $file .py)
done
%{__install} -d -m0755 %{buildroot}%{_datadir}/mplayer/
%{__install} -p -m0644 TOOLS/*.fp %{buildroot}%{_datadir}/mplayer/

%{__install} -Dp -m0644 etc/mplayer.xpm %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/mplayer.xpm
desktop-file-install \
    --vendor %{desktop_vendor} \
    --dir %{buildroot}%{_datadir}/applications/ \
    etc/mplayer.desktop

%post gui
/usr/bin/update-mime-database %{_datadir}/mime &>/dev/null || :
/usr/bin/update-desktop-database -q %{_datadir}/applications &>/dev/null || :
/usr/bin/gtk-update-icon-cache -qf %{_datadir}/icons/hicolor &> /dev/null || :

%postun gui
/usr/bin/update-mime-database %{_datadir}/mime &>/dev/null || :
/usr/bin/update-desktop-database -q %{_datadir}/applications &>/dev/null || :
/usr/bin/gtk-update-icon-cache -qf %{_datadir}/icons/hicolor &> /dev/null || :

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_bindir}/mplayer

%files common
%defattr(-, root, root, 0755)
%doc AUTHORS Changelog Copyright LICENSE README etc/*.conf
%doc %{_mandir}/man1/mplayer.1*
%doc %lang(cs) %{_mandir}/cs/man1/mplayer.1*
%doc %lang(de) %{_mandir}/de/man1/mplayer.1*
%doc %lang(es) %{_mandir}/es/man1/mplayer.1*
%doc %lang(fr) %{_mandir}/fr/man1/mplayer.1*
%doc %lang(hu) %{_mandir}/hu/man1/mplayer.1*
%doc %lang(it) %{_mandir}/it/man1/mplayer.1*
%doc %lang(pl) %{_mandir}/pl/man1/mplayer.1*
%doc %lang(ru) %{_mandir}/ru/man1/mplayer.1*
%doc %lang(zh_CN) %{_mandir}/zh_CN/man1/mplayer.1*
%dir %{_sysconfdir}/mplayer/
%config(noreplace) %{_sysconfdir}/mplayer/input.conf
%config(noreplace) %{_sysconfdir}/mplayer/menu.conf
%config(noreplace) %{_sysconfdir}/mplayer/mplayer.conf
%{_datadir}/mplayer/
%dir %{_libdir}/codecs/

%files gui
%defattr(-, root, root, 0755)
%{_bindir}/gmplayer
%{_datadir}/applications/%{desktop_vendor}-mplayer.desktop
%{_datadir}/icons/hicolor/32x32/apps/mplayer.xpm
%{_datadir}/mplayer/skins/
%{_datadir}/pixmaps/mplayer.xpm
%exclude %{_datadir}/applications/mplayer.desktop

%files -n mencoder
%defattr(-, root, root, 0755)
%doc %{_mandir}/man1/mencoder.1*
%doc %lang(cs) %{_mandir}/cs/man1/mencoder.1*
%doc %lang(de) %{_mandir}/de/man1/mencoder.1*
%doc %lang(es) %{_mandir}/es/man1/mencoder.1*
%doc %lang(fr) %{_mandir}/fr/man1/mencoder.1*
%doc %lang(hu) %{_mandir}/hu/man1/mencoder.1*
%doc %lang(it) %{_mandir}/it/man1/mencoder.1*
%doc %lang(pl) %{_mandir}/pl/man1/mencoder.1*
%doc %lang(ru) %{_mandir}/ru/man1/mencoder.1*
%doc %lang(zh_CN) %{_mandir}/zh_CN/man1/mencoder.1*
%{_bindir}/mencoder

%files doc
%defattr(-, root, root, 0755)
%doc DOCS/*

%files tools
%defattr(-, root, root, 0755)
%{_bindir}/aconvert
%{_bindir}/binary_codecs
%{_bindir}/calcbpp
%{_bindir}/checktree
%{_bindir}/countquant
%{_bindir}/divx2svcd
%{_bindir}/dvd2divxscript
%{_bindir}/mencvcd
%{_bindir}/midentify
%{_bindir}/mpconsole
%{_bindir}/mphelp_check
%{_bindir}/mplmult
%{_bindir}/plotpsnr
%{_bindir}/psnr-video
%{_bindir}/qepdvcd
%{_bindir}/subedit
%{_bindir}/subsearch
%{_bindir}/vobshift
%{_bindir}/w32codec_dl
%{_bindir}/wma2ogg
%{_datadir}/mplayer/*.fp

%changelog
* Tue Oct 11 2011 Aleksey Cheusov <vle@gmx.net> - 1.0-0.47.svn20100703
- Enable support for VDPAU.

* Tue Dec 07 2010 Dag Wieers <dag@wieers.com> - 1.0-0.46.svn20100703
- Fix issue with fontconfig on RHEL5, RHEL4 and RHEL3.

* Mon Dec 06 2010 Dag Wieers <dag@wieers.com> - 1.0-0.45.svn20100703
- Rebuild against libmatroska-1.0.0.

* Sat Dec 04 2010 Dag Wieers <dag@wieers.com> - 1.0-0.44.svn20100703
- Rebuild against newer x264.

* Tue Jun 15 2010 Dag Wieers <dag@wieers.com> - 1.0-0.44.svn20090711
- Rebuild RHEL4 against libcaca-0.99-0.1.beta17. (Jaroslaw Polok)

* Mon Jun 14 2010 Dag Wieers <dag@wieers.com> - 1.0-0.43.svn20090711
- Revert back to subversion snapshot 20090711. (Yury V. Zaytsev)

* Sun Jun 13 2010 Dag Wieers <dag@wieers.com> - 1.0-0.43.rc3
- Updated to release 1.0rc3.

* Sun Jun 13 2010 Dag Wieers <dag@wieers.com> - 1.0-0.42.svn20090711
- Rebuild against libdvbpsi-0.1.7.

* Fri Nov 06 2009 Dag Wieers <dag@wieers.com> - 1.0-0.41.svn20090711
- Rebuild against faad2-2.7.

* Tue Jul 14 2009 Dag Wieers <dag@wieers.com> - 1.0-0.40.svn20090711
- Updated to subversion snapshot 20090711.
- Updated live to version 2009.07.09.

* Wed Jul 08 2009 Dag Wieers <dag@wieers.com> - 1.0-0.40.rc2
- Updated to release 1.0rc2.

* Wed Sep 24 2008 Dag Wieers <dag@wieers.com> - 1.0-0.40.rc1tr2
- Rebuild against directfb-1.2.4.

* Wed Jul 09 2008 Dag Wieers <dag@wieers.com> - 1.0-0.39.rc1try2
- Rebuild against directfb-1.0.1.

* Mon Dec 17 2007 Dag Wieers <dag@wieers.com> - 1.0-0.38.rc1try2
- Build against libmpcdec 1.2.6 and libupnp 1.6.x.

* Tue Nov 20 2007 Tom G. Christensen <swpkg@statsbiblioteket.dk> - 1.0-0.37.rc1try2
- Build with twolame support.

* Thu Oct 11 2007 Matthias Saou <http://freshrpms.net/> 1.0-0.36.rc1try2
- Rebuild freshrpms package to fix lame detection on i386.

* Mon Jun 04 2007 Dag Wieers <dag@wieers.com> - 1.0-0.35.rc1try2
- Rebuild against x264-0.4.20070529 because I missed it.

* Tue Jan  9 2007 Matthias Saou <http://freshrpms.net/> 1.0-0.34.rc1try2
- Include patch to fix mp3 playback on AMD CPUs.
- Include patch to fix buffer overflow in asmrp.c.

* Tue Oct 24 2006 Matthias Saou <http://freshrpms.net/> 1.0-0.33.rc1
- Update to 1.0rc1.
- Update live library to 2006.10.18a.
- Remove udev patch as lirc is now properly detected (lib, not the /dev entry).
- Try to add patch for lzo, but it requires lzo1 while we only have lzo2 now.
- No longer use --enable-debug since all it did was pass -g but it was now
  forcing CFLAGS to something different from our optflags too.
- Force use of -fomit-frame-pointer for now, as i386 build fails otherwise.

* Tue Oct 17 2006 Matthias Saou <http://freshrpms.net/> 1.0-0.32.20060919
- Revert to 20060919 snapshot since 20061017 doesn't build on i386.

* Tue Oct 17 2006 Matthias Saou <http://freshrpms.net/> 1.0-0.31.20061017
- Update to today's SVN code.
- Update live library to 2006.10.12a.

* Tue Sep 19 2006 Matthias Saou <http://freshrpms.net/> 1.0-0.31.20060919
- Update to today's SVN code.
- Remove kversion since it's not needed anymore (only dvbhead enabled).

* Mon Sep  4 2006 Matthias Saou <http://freshrpms.net/> 1.0-0.30.pre8
- Add nas support by default.
- Add libXt-devel build requirement if modxorg since the nas check requires it.

* Mon Jul 31 2006 Matthias Saou <http://freshrpms.net/> 1.0-0.29.pre8
- Update Blue skin to 1.6.
- Update live library to 2006.07.04.

* Fri Jun 23 2006 Matthias Saou <http://freshrpms.net/> 1.0-0.28.pre8
- Move location where binary codecs are searched for from %%{_libdir}/win32/ to
  %%{_libdir}/codecs/ since "win32" is considered obsolete by MPlayer. Looks
  like codecs in the old location are still picked up automatically!

* Thu Jun 22 2006 Matthias Saou <http://freshrpms.net/> 1.0-0.27.pre8
- Update to 1.0pre8.
- Update live555 to 2006.06.22.
- Use our own nicer png icon for the desktop file (created from the original
  xcf file from the MPlayer FTP archive).
- Remove old --enable-i18n parameter.
- Update mplayer-desktop.xpm that got renamed to mplayer.xpm.
- Clean up autodetected configure options, let us assume we build on minimal
  systems when we poke around --with and --without build options.
- Remove --disable-fastmemcpy, assuming runtime cpudetection takes care of
  support for < i686 CPUs...
- Enable samba support by default.
- Remove no longer needed explicit path to cdparanoia includes.
- Add speex support, enabled by default (but >= 1.1 is required).
- Pass --with-xanimlibdir= for x86 to find xanim libs in /usr/lib/win32.
- Rename the kernel macro to kversion to keep more consistent with Extras.
- Seems like amr_nb support is disabled because of the included libavcodec.
- Seems like libfame support is disabled because there are none of dxr2, dxr3
  and dvb enabled.

* Wed Mar 22 2006 Matthias Saou <http://freshrpms.net/> 1.0-0.26.20060314
- Add missing modular X build requirements.
- Re-enable libXvMC with modular X.

* Tue Mar 14 2006 Matthias Saou <http://freshrpms.net/> 1.0-0.25.20060314
- Update to current CVS which fixes the heap overflow in demuxer.h issue.
- Update live555 library to 2006.03.03.

* Thu Feb 23 2006 Matthias Saou <http://freshrpms.net/> 1.0-0.24.20060223
- Update to current CVS.
- Update live555 library to 2006.02.15.
- Add support for amrnb.

* Fri Jan 13 2006 Matthias Saou <http://freshrpms.net/> 1.0-0.24.20060113
- Update to a Friday the 13th snapshot! :-)
- Update live555 library to 2006.01.05.
- Remove XFree86-devel build requirement, gtk2-devel takes care of the
  required X stuff.
- Remove no longer needed nostrip patch, use STRIPBINARIES now.
- Disable "xvmc" (the old wrapper) on FC5, and use the xorg libXvMC instead.

* Mon Dec 19 2005 Matthias Saou <http://freshrpms.net/> 1.0-0.23.20051211
- Enable vstream support (TiVo vserver stream).

* Tue Dec 13 2005 Matthias Saou <http://freshrpms.net/> 1.0-0.22.20051211
- Force _libdir since libdha and vidix modules are now built on x86_64.
- Include empty _libdir/real/ for non-x86 archs.

* Sun Dec 11 2005 Matthias Saou <http://freshrpms.net/> 1.0-0.21.20051211
- Update to CVS code.
- Update Blue skin to 1.5.
- Update udev patch (v4l detection no longer uses test on /dev files, but lirc
  still does).
- Remove all obsolete patches.
- Change gtk+ build requirement to gtk2.
- Enable x264 again.
- Add faac, ladspa and musepack (mpc) support (enabled).
- Add live555 support, include latest snapshot : live.2005.12.09.
- Enable dvb by default, and make overriding the kernel version possible.
- Switch from external libdvdread to mpdvdkit, since the streaming part fails
  to build otherwise.
- Remove disabled dvdnav support, as it's no longer available.

* Sun Dec 11 2005 Matthias Saou <http://freshrpms.net/> 1.0-0.20.pre7
- Enable DTS (libdca).
- Try to enable x264, fix configure check (libpthread), but compile fails.

* Fri Dec  9 2005 Matthias Saou <http://freshrpms.net/> 1.0-0.19.pre7
- Include patch to fix PPC compilation on FC4 at last.

* Thu Dec  8 2005 Matthias Saou <http://freshrpms.net/> 1.0-0.18.pre7
- Disabled shared libpostprocess, let the original ffmpeg package take
  care of that once and for all.
- Include ad_pcm_fix patch.

* Tue Jul 19 2005 Matthias Saou <http://freshrpms.net/> 1.0-0.17.pre7
- Added x86_64 patch from Ryo Dairiki.
- Remove gtk-update-icon-cache calls, at least until icon changes place.

* Tue Jun 28 2005 Matthias Saou <http://freshrpms.net/> 1.0-0.16.pre7
- Fix "libfame" to "fame" rebuild option listed in the description.

* Sun May  1 2005 Matthias Saou <http://freshrpms.net/> 1.0-0.16.pre7
- Include gcc4 patches from Gentoo portage, to build on FC4..
- Split off docs sub-package, as it represents 7MB of data!
- Split off mencoder sub-package too, not everyone uses it.
- Add gtk-update-icon-cache calls in post and postun.
- Add debug option (it only adds -g and disabled stripping) + patch.

* Sun Apr 17 2005 Matthias Saou <http://freshrpms.net/> 1.0-0.16.pre7
- Update to 1.0pre7.
- No longer overwrite the entire desktop file, just replace a few fields.
- Remove libogg and libvorbis deps, ogg/vorbis now uses Tremor internally.
- Disable xmms support, as it's been moved to Extras.
- Disable external faad2, it changes too much, using the internal is safer.
- Add Copyright and LICENSE files to %%doc.
- Remove .cvsignore file removal from DOCS, there are none leftover anymore.
- Remove manual libpostproc install, it seems fixed now.
- Add same MimeType as totem, except flac and flash types.
- Remove lib64 hacks, problems have been fixed.

* Thu Jan 13 2005 Matthias Saou <http://freshrpms.net/> 1.0-0.15.pre6a
- Change lirc patch into more generic udev one to avoid /dev/video* detection.
- Enable v4l again (from the above patch).

* Fri Jan  7 2005 Matthias Saou <http://freshrpms.net/> 1.0-0.14.pre6a
- Added quick patch to skip /dev/lirc* file presence check, since this doesn't
  work as expected with udev.
- Add ppc to the ifarch for libdha and vidix modules inclusion as configure
  enables it for "ppc && linux" (not x86_64, though, probably a good reason?).
- Include uio.h-ppc.patch as source, as this is a required change on YDL4 (ppc)
  to get MPlayer's x11 vo to compile properly (VECTOR vs. IOVEC).
- Added libXvMCW support for Unichrome and others, even though a comment in the
  configure script seems to suggest it's not entirely ready yet.

* Mon Jan  3 2005 Matthias Saou <http://freshrpms.net/> 1.0-0.13.pre6a
- Update to 1.0pre6a.
- Remove cz man pages, add cs ones.
- Fix fribidi support and include patch from Nir Misgav.

* Wed Nov  3 2004 Matthias Saou <http://freshrpms.net/> 1.0-0.12.20042025
- Merge Dag's scriplet changes.

* Mon Oct 25 2004 Matthias Saou <http://freshrpms.net/> 1.0-0.11.20042025
- Update to today's CVS snapshot.
- Simplify the desktop file install, as there is now one included.
- Add --disable-fastmemcpy to fix broken libpostproc.

* Sat Oct 16 2004 Matthias Saou <http://freshrpms.net/> 1.0-0.11.pre5
- Added update-desktop-database scriplet calls.

* Fri Jul 23 2004 Matthias Saou <http://freshrpms.net/> 1.0-0.11.pre5
- Add fixes for x86_64, it now builds and works.
- Added external libmatroska support.
- Added optional DVB conditional build.

* Fri Jul 16 2004 Matthias Saou <http://freshrpms.net/> 1.0-0.10.pre5
- Update to 1.0pre5.
- Updated Blue skin to 1.4.
- Now use the MPlayer_mini.xpm icon to fix the transparent vs. white problem.

* Thu May 20 2004 Matthias Saou <http://freshrpms.net/> 1.0-0.10.pre4
- Rebuild for Fedora Core 2.
- Update to 1.0pre4... why doesn't drag'n drop work anymore? :-(
- Updated Blue skin to 1.2.
- Added caca and theora support.
- Un-conditionalized alsa and libdv, which are now part of Fedora Core 2.

* Thu Apr 15 2004 Matthias Saou <http://freshrpms.net/> 1.0-0.9.20040415
- Updated to today's CVS snapshot to fix http vulnerability.

* Wed Feb 11 2004 Matthias Saou <http://freshrpms.net/> 1.0-0.8.20040325
- Updated to today's CVS snapshot.
- Updated Blue skin to 1.1.
- Added xmms support to mencoder.
- Added it man page.

* Wed Feb 11 2004 Matthias Saou <http://freshrpms.net/> 1.0-0.7.20040211.fr
- Updated to today's CVS snapshot.

* Fri Dec  5 2003 Matthias Saou <http://freshrpms.net/> 1.0-0.6.20031205.fr
- Updated to today's CVS snapshot.
- Removed the ffmpeg CVS stuff, as it's now part of the snapshots again.
- Rebuild against a modified libfame to have libfame/fame.h found.
- Change back xvidcore-static build dep to xvidcore-devel, as it seems to
  build against the shared lib again.
- Fix libmad to libmad-devel build dep.

* Mon Nov 17 2003 Matthias Saou <http://freshrpms.net/> 1.0-0.5.pre2.20031107.fr
- Rebuild with proper faad2 (external) support.

* Sun Oct  5 2003 Matthias Saou <http://freshrpms.net/>
- Update to 1.0rc2.

* Thu Oct  2 2003 Matthias Saou <http://freshrpms.net/>
- Update to today's CVS snapshot.
- Fixed menu entry (missing trailing ";" to Categories=!).

* Wed Sep  3 2003 Matthias Saou <http://freshrpms.net/>
- Update to 1.0pre1.

* Fri Aug  8 2003 Matthias Saou <http://freshrpms.net/>
- Update to today's cvs snapshot.
- Added libfame support.
- Enabled translated man pages.
- Added osdmenu and samba build switches.
- Disabled codecs.conf, as it's not installed anymore.
- Fixed xvidcore build requirement, as link is static.
- Removed explicit /sbin/ldconfig dep, picked up automatically.

* Mon Jun 16 2003 Matthias Saou <http://freshrpms.net/>
- Update to today's cvs snapshot.
- Reverted Requires(...) to plain Requires.
- Changed %%pre / %%post to -p.
- Added libpostproc install workaround since it seems broken.

* Mon Apr 28 2003 Matthias Saou <http://freshrpms.net/>
- Added libpng dependencies.

* Tue Apr  8 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.90 final.
- Changed the default skin to Blue.
- Moved the fonts into a separate package.
- Split libpostproc (to remove mplayer dep from transcode).
- Added faad2 support and explicit lzo dep.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.

* Mon Mar 24 2003 Matthias Saou <http://freshrpms.net/>
- Fix ppc build.

* Wed Mar 19 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.90rc5.

* Sat Mar 15 2003 Matthias Saou <http://freshrpms.net/>
- Added gcccheck build option.
- Added freedesktop build option.

* Sun Feb 16 2003 Matthias Saou <http://freshrpms.net/>
- Rebuild against new libdvdread.

* Wed Feb 12 2003 Matthias Saou <http://freshrpms.net/>
- Add a workaround for the default skin's permission problem.

* Mon Feb 10 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.90rc4.
- Updated default skin to 1.7.

* Wed Jan 22 2003 Matthias Saou <http://freshrpms.net/>
- Added --without dvdnav build option.

* Mon Jan 20 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.90rc3.
- Added "--without esd" build option.

* Sat Jan 11 2003 Matthias Saou <http://freshrpms.net/>
- Update to today's snapshot as it fixes many bugs (fullscreen for ex).
- Replace all divx4linux stuff with xvid.
- Rebuilt with libavcodec from ffmpeg, doh!

* Thu Jan  2 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.90rc2, updated the cdda patch too.
- Removed the Epoch... yes, upgrade manually by erasing and installing again.

* Mon Dec  9 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.90rc1.

* Fri Nov 15 2002 Matthias Saou <http://freshrpms.net/>
- Re-enabled the auto req/prov.

* Tue Nov 12 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.90pre10.
- Added CDDA support through cdparanoia + include fix.
- Enabled shared postproc library.
- Fixed VCD support by having redhat -> linux (probably fixes joystick too).
- Removed CFLAGS overwriting.

* Sat Oct 26 2002 Matthias Saou <http://freshrpms.net/>
- Fixed aa with --disable-aa instead of --disable-aalib.

* Fri Oct 25 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.90pre9.
- Enable ALSA by default now.
- Added patch to remove that awful startup message about runtime cpudetection.
- Added libdvdnav support for rebuild.

* Wed Oct  3 2002 Matthias Saou <http://freshrpms.net/>
- Enforced --without libdv, lirc options to disable even if libs are present.

* Sat Sep 28 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 8.0.
- Added new menu entry.
- New --with and --without rebuild options.

* Fri Sep 20 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.90pre8.
- Added some files to the %%doc section.

* Thu Sep  5 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.90pre7.
- Removed obsolete prefix.
- Explicitely disable ALSA for now.

* Mon Aug 20 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt with libdvdnav... but removed, just too experimental :-(
- Added direct DVD menu entry.

* Mon Aug 13 2002 Matthias Saou <http://freshrpms.net/>
- Added arts dependency.

* Tue Aug  6 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.90pre6.
- Added aalib and lirc build dependencies to get a full-featured binary.
- Updated %%description.
- Added iso-8859-2 font in the package.
- Cleaned up old unuseful hacks.

* Mon Jun 10 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.90pre5.

* Tue May 14 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.90pre4.
- Overwrite the absolute link for the mencoder.1 man page.

* Sat May 11 2002 Matthias Saou <http://freshrpms.net/>
- Added the mime types for the menu entry.

* Thu May  2 2002 Matthias Saou <http://freshrpms.net/>
- Added CFLAGS for configure and i18n.
- Rebuilt against Red Hat Linux 7.3.
- Added the %%{?_smp_mflags} expansion.

* Tue Apr 30 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.90pre2.
- Fixed the libGLcore.so.1 and lirc dependencies.
- Build with gcc 2.96 instead of gcc3.

* Fri Apr 26 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.90pre1, fully GPL at last! Here come the binary packages :-)

* Fri Feb  1 2002 Matthias Saou <http://freshrpms.net/>
- Update to today's current version.
- Added 3 skins + removed workaround since skin archives are fixed.

* Wed Jan  2 2002 Matthias Saou <http://freshrpms.net/>
- %%doc cleanup and update to today's build.
- Modified for the new CONFDIR stuff.

* Wed Dec 12 2001 Matthias Saou <http://freshrpms.net/>
- Initial RPM release.

