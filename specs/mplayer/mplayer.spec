# $Id$
# Authority: matthias

# Overridable kernel version, needed for the DVB includes
%{!?kversion: %define kversion %(uname -r)}

%{?dist: %{expand: %%define %dist 1}}
%{?fedora: %{expand: %%define fc%{fedora} 1}}

%{!?dist:%define _with_modxorg 1}
%{?fc6:  %define _with_modxorg 1}
%{?fc5:  %define _with_modxorg 1}

%{?fc1:%define _without_alsa 1}
%{?fc1:%define _without_theora 1}
%{?fc1:%define _without_xvmc 1}

%{?el3:%define _without_alsa 1}
%{?el3:%define _without_fribidi 1}
%{?el3:%define _without_theora 1}
%{?el3:%define _without_xvmc 1}

%{?rh9:%define _without_alsa 1}
%{?rh9:%define _without_fribidi 1}
%{?rh9:%define _without_theora 1}
%{?rh9:%define _without_xvmc 1}

%{?rh8:%define _without_alsa 1}
%{?rh8:%define _without_fribidi 1}
%{?rh8:%define _without_theora 1}
%{?rh8:%define _without_xvmc 1}

%{?rh7:%define _without_alsa 1}
%{?rh7:%define _without_fribidi 1}
%{?rh7:%define _without_freedesktop 1}
%{?rh7:%define _without_theora 1}
%{?rh7:%define _without_gcccheck 1}
%{?rh7:%define _without_xvmc 1}

%{?el2:%define _without_alsa 1}
%{?el2:%define _without_arts 1}
%{?el2:%define _without_caca 1}
%{?el2:%define _without_dv 1}
%{?el2:%define _without_fribidi 1}
%{?el2:%define _without_freedesktop 1}
%{?el2:%define _without_theora 1}
%{?el2:%define _without_xvmc 1}

%{?yd3:%define _without_alsa 1}
%{?yd3:%define _without_fribidi 1}
%{?yd3:%define _without_theora 1}

# Is this a daily build? If so, put the date like "20020808" otherwise put 0
#define date      20060314
%define rcver     pre8

Summary: MPlayer, the Movie Player for Linux
Name: mplayer
Version: 1.0
Release: 0.27%{?rcver:.%{rcver}}%{?date:.%{date}}
License: GPL
Group: Applications/Multimedia
URL: http://mplayerhq.hu/
%if %{?date:1}0
# cvs -z3 -d:pserver:anonymous@mplayerhq.hu:/cvsroot/mplayer co -P
# cvs -z3 -d:pserver:anonymous@mplayerhq.hu:/cvsroot/ffmpeg co -P
# cp -a mplayer MPlayer-%{date}
# cp -a ffmpeg/{libavcodec,libavformat,libavutil} MPlayer-%{date}/
# find MPlayer-%{date} -name CVS -o -name .cvsignore | xargs rm -rf
# tar cjvf MPlayer-%{date}.tar.bz2 MPlayer-%{date}/
Source0: http://www.mplayerhq.hu/MPlayer/cvs/MPlayer-%{date}.tar.bz2
%else
Source0: http://www.mplayerhq.hu/MPlayer/releases/MPlayer-%{version}%{?rcver}.tar.bz2
%endif
Source1: http://www.live555.com/liveMedia/public/live.2006.06.22.tar.gz
Source2: http://www.mplayerhq.hu/MPlayer/Skin/Blue-1.5.tar.bz2
Source3: mplayer.png
# Only for reference, required on YDL4 at least
Source10: uio.h-ppc.patch
Patch0: MPlayer-0.90pre9-runtimemsg.patch
Patch1: MPlayer-0.90-playlist.patch
Patch2: MPlayer-0.90pre10-redhat.patch
Patch10: MPlayer-1.0pre6a-fribidi.patch
Patch11: MPlayer-1.0pre8-udev.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: mplayer-fonts
BuildRequires: gtk2-devel, SDL-devel
BuildRequires: libpng-devel, libjpeg-devel, libungif-devel
BuildRequires: lame-devel, libmad-devel, flac-devel
BuildRequires: libmatroska-devel
BuildRequires: ImageMagick
%{?_with_dvdread:BuildRequires: libdvdread-devel}
%{!?_without_dvb:BuildRequires: kernel = %{kversion}, kernel-devel = %{kversion}}
%{!?_without_dv:BuildRequires: libdv-devel}
%{!?_without_ladspa:BuildRequires: ladspa-devel}
%{!?_without_alsa:BuildRequires: alsa-lib-devel}
%{!?_without_fribidi:BuildRequires: fribidi-devel}
%{!?_without_aalib:BuildRequires: aalib-devel}
%{!?_without_lirc:BuildRequires: lirc-devel}
%{!?_without_cdparanoia:BuildRequires: cdparanoia-devel}
%{!?_without_arts:BuildRequires: arts-devel}
%{!?_without_xvid:BuildRequires: xvidcore-devel}
%{!?_without_x264:BuildRequires: x264-devel}
%{!?_without_esd:BuildRequires: esound-devel}
%{!?_without_lzo:BuildRequires: lzo-devel}
%{!?_without_fame:BuildRequires: libfame-devel}
%{!?_without_caca:BuildRequires: libcaca-devel}
%{!?_without_theora:BuildRequires: libtheora-devel}
%{!?_without_dts:BuildRequires: libdca-devel}
%{!?_without_faac:BuildRequires: faac-devel}
%{!?_without_mpc:BuildRequires: libmpcdec-devel}
%{!?_without_vstream:BuildRequires: vstream-client-devel}
%{!?_without_amrnb:BuildRequires: amrnb-devel}
%{!?_without_samba:BuildRequires: samba-common}
%{!?_without_speex:BuildRequires: speex-devel}
%{?_with_modxorg:BuildRequires: libXv-devel, libXxf86vm-devel, libGL-devel}
%{!?_with_modxorg:%{!?_without_xvmc:BuildRequires: libXvMCW-devel}}
%{?_with_modxorg:%{!?_without_xvmc:BuildRequires: libXvMC-devel}}

%description
MPlayer is a multimedia player. It plays most video formats as well as DVDs.
Its big feature is the wide range of supported output drivers. There are also
nice antialiased shaded subtitles and OSD.

On x86, additional Win32 binary codecs should be added to %{_libdir}/win32/.

Available rpmbuild rebuild options :
--with : dvdread
--without : aalib lirc cdparanoia arts xvid esd lzo fame caca dvb vstream
            theora osdmenu gcccheck fribidi xvmc x264 faac mpc live ladspa
            amrnb samba speex


%package -n mencoder
Summary: MPlayer’s Movie Encoder
Group: Applications/Multimedia
Requires: %{name} = %{version}

%description -n mencoder
MPlayer’s Movie Encoder is a simple movie encoder, designed to encode
MPlayer-playable movies to other MPlayer-playable formats. It encodes to
MPEG-4 (DivX/XviD), one of the libavcodec codecs and PCM/MP3/VBRMP3 audio
in 1, 2 or 3 passes.  Furthermore  it has stream copying abilities, a
powerful filter system (crop, expand, flip, postprocess, rotate, scale,
noise, rgb/yuv conversion) and more.


%package docs
Summary: Documentation for MPlayer, the Movie Player for Linux
Group: Applications/Multimedia

%description docs
MPlayer is a movie player. It plays most video formats as well as DVDs.
Its big feature is the wide range of supported output drivers. There are also
nice antialiased shaded subtitles and OSD.

This package contains the end user documentation.


%prep
%if %{?date:1}0
%setup -n MPlayer-%{date} -a 1
%else
%setup -n MPlayer-%{version}%{?rcver} -a 1
%endif
%patch0 -p1 -b .runtimemsg
%patch1 -p1 -b .playlist
%patch2 -p0 -b .redhat
%patch10 -p1 -b .fribidi
%patch11 -p1 -b .udev

# Clean up the tarball contents (useful for the included docs)
find . -name "CVS" | xargs %{__rm} -rf

# Overwrite some of the details of the provided system menu entry
%{__perl} -pi -e 's|^Exec=gmplayer$|Exec=gmplayer %f|g;
                  s|^Categories=.*|Categories=Application;AudioVideo;|g;
                  s|^Icon=.*|Icon=mplayer.png|g' \
    etc/mplayer.desktop
echo "MimeType=video/dv;video/mpeg;video/x-mpeg;video/msvideo;video/quicktime;video/x-anim;video/x-avi;video/x-ms-asf;video/x-ms-wmv;video/x-msvideo;video/x-nsv;video/x-flc;video/x-fli;application/ogg;application/x-ogg;application/x-matroska;audio/x-mp3;audio/x-mpeg;audio/mpeg;audio/x-wav;audio/x-mpegurl;audio/x-scpls;audio/x-m4a;audio/x-ms-asf;audio/x-ms-asx;audio/x-ms-wax;application/vnd.rn-realmedia;audio/x-real-audio;audio/x-pn-realaudio;misc/ultravox;audio/vnd.rn-realaudio;audio/x-pn-aiff;audio/x-pn-au;audio/x-pn-wav;audio/x-pn-windows-acm;image/vnd.rn-realpix;video/vnd.rn-realvideo;audio/x-pn-realaudio-plugin;" >> etc/mplayer.desktop


%build
# Build statically linked live555 libraries
%if 0%{!?_without_live:1}
pushd live
    # Force the use of our CFLAGS
    %{__perl} -pi -e 's|-O2|%{optflags}|g' config.linux
    # Configure and build
    ./genMakefiles linux && %{__make}
popd
%endif

export CFLAGS="%{optflags}"
echo | ./configure \
    --prefix=%{_prefix} \
    --bindir=%{_bindir} \
    --datadir=%{_datadir}/mplayer \
    --mandir=%{_mandir} \
    --confdir=%{_sysconfdir}/mplayer \
    --libdir=%{_libdir} \
    --enable-gui \
    --enable-largefiles \
    --enable-joystick \
    %{!?_with_dvdread:--disable-dvdread} \
    %{!?_without_osdmenu:--enable-menu} \
    %{!?_with_modxorg:%{!?_without_xvmc:--enable-xvmc --with-xvmclib=XvMCW}} \
    %{?_with_modxorg:%{!?_without_xvmc:--enable-xvmc}} \
%ifarch %{ix86}
    --enable-runtime-cpudetection \
    --enable-win32 \
    --with-win32libdir=%{_libdir}/win32 \
    --with-xanimlibdir=%{_libdir}/win32 \
    --with-reallibdir=%{_libdir}/win32 \
%else
    --with-reallibdir=%{_libdir}/real \
%endif
    --language=all \
    --enable-debug \
    --enable-dynamic-plugins \
    %{?_without_gcccheck:--disable-gcc-checking} \
    %{!?_without_dvb:--with-dvbincdir=/lib/modules/%{kversion}/build/include} \
    %{!?_without_live:--with-livelibdir=`pwd`/live}

%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
# The libdir override is required for libpostproc when _libdir is /usr/lib64
%{__make} install \
    STRIPBINARIES="no" \
    DESTDIR=%{buildroot} \
    libdir=%{buildroot}%{_libdir}

# The default Skin
%{__mkdir_p} %{buildroot}%{_datadir}/mplayer/Skin/
%{__tar} -xjf %{SOURCE2} -C %{buildroot}%{_datadir}/mplayer/Skin/
%{__mv} -f %{buildroot}%{_datadir}/mplayer/Skin/* %{buildroot}%{_datadir}/mplayer/Skin/default

# The fonts are now in a separate package
%{__rm} -rf %{buildroot}%{_datadir}/mplayer/font || :

# Remove unwanted stuff from the docs to be included
%{__rm} -rf DOCS/{man,xml}

# Create empty Win32 binary codec directory
%ifarch %{ix86}
%{__mkdir_p} %{buildroot}%{_libdir}/win32
%else
%{__mkdir_p} %{buildroot}%{_libdir}/real
%endif

# Install our own nicer icon
%{__rm} -f %{buildroot}%{_datadir}/pixmaps/mplayer.xpm
%{__install} -p -m 0644 %{SOURCE3} \
           %{buildroot}%{_datadir}/pixmaps/mplayer.png


%post
/sbin/ldconfig
update-desktop-database %{_datadir}/applications &>/dev/null || :

%postun
/sbin/ldconfig
update-desktop-database %{_datadir}/applications &>/dev/null || :


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog Copyright LICENSE README etc/*.conf
%dir %{_sysconfdir}/mplayer/
#ghost %config %{_sysconfdir}/mplayer/codecs.conf
#ghost %config %{_sysconfdir}/mplayer/input.conf
#ghost %config %{_sysconfdir}/mplayer/menu.conf
#ghost %config %{_sysconfdir}/mplayer/mplayer.conf
%{_bindir}/gmplayer
%{_bindir}/mplayer
%ifarch %{ix86}
%dir %{_libdir}/win32/
%else
%dir %{_libdir}/real/
%endif
%{_libdir}/libdha.so*
%{_libdir}/mplayer/
%{!?_without_freedesktop:%{_datadir}/applications/mplayer.desktop}
%{_datadir}/mplayer/
%{_datadir}/pixmaps/mplayer.png
%{_mandir}/man1/mplayer.1*
%lang(cs) %{_mandir}/cs/man1/mplayer.1*
%lang(de) %{_mandir}/de/man1/mplayer.1*
%lang(es) %{_mandir}/es/man1/mplayer.1*
%lang(fr) %{_mandir}/fr/man1/mplayer.1*
%lang(hu) %{_mandir}/hu/man1/mplayer.1*
%lang(it) %{_mandir}/it/man1/mplayer.1*
%lang(pl) %{_mandir}/pl/man1/mplayer.1*
%lang(sv) %{_mandir}/sv/man1/mplayer.1*

%files -n mencoder
%defattr(-, root, root, 0755)
%{_bindir}/mencoder
%{_mandir}/man1/mencoder.1*
%lang(cs) %{_mandir}/cs/man1/mencoder.1*
%lang(de) %{_mandir}/de/man1/mencoder.1*
%lang(es) %{_mandir}/es/man1/mencoder.1*
%lang(fr) %{_mandir}/fr/man1/mencoder.1*
%lang(hu) %{_mandir}/hu/man1/mencoder.1*
%lang(it) %{_mandir}/it/man1/mencoder.1*
%lang(pl) %{_mandir}/pl/man1/mencoder.1*
%lang(sv) %{_mandir}/sv/man1/mencoder.1*

%files docs
%defattr(-, root, root, 0755)
%doc DOCS/*


%changelog
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
- Changed %pre / %post to -p.
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
- %doc cleanup and update to today's build.
- Modified for the new CONFDIR stuff.

* Wed Dec 12 2001 Matthias Saou <http://freshrpms.net/>
- Initial RPM release.

