# $Id$
# Authority: matthias

%{?dist: %{expand: %%define %dist 1}}

%{?fc1:%define _without_alsa 1}
%{?fc1:%define _without_theora 1}

%{?el3:%define _without_alsa 1}
%{?el3:%define _without_fribidi 1}
%{?el3:%define _without_theora 1}

%{?rh9:%define _without_alsa 1}
%{?rh9:%define _without_fribidi 1}
%{?rh9:%define _without_theora 1}

%{?rh8:%define _without_alsa 1}
%{?rh8:%define _without_fribidi 1}
%{?rh8:%define _without_theora 1}

%{?rh7:%define _without_alsa 1}
%{?rh7:%define _without_fribidi 1}
%{?rh7:%define _without_freedesktop 1}
%{?rh7:%define _without_theora 1}

%{?el2:%define _without_alsa 1}
%{?el2:%define _without_fribidi 1}
%{?el2:%define _without_freedesktop 1}
%{?el2:%define _without_theora 1}

%{?yd3:%define _without_alsa 1}
%{?yd3:%define _without_fribidi 1}
%{?yd3:%define _without_theora 1}

# Is this a daily build? If so, put the date like "20020808" otherwise put 0
%define date      20041025
#define rcver     pre5

%define xmms_plugindir %(xmms-config --input-plugin-dir || echo %{_libdir}/xmms/Input)

Summary: MPlayer, the Movie Player for Linux
Name: mplayer
Version: 1.0
Release: 0.12%{?rcver:.%{rcver}}%{?date:.%{date}}
License: GPL
Group: Applications/Multimedia
URL: http://mplayerhq.hu/
%if %{?date:1}0
Source0: http://www.mplayerhq.hu/MPlayer/cvs/MPlayer-%{date}.tar.bz2
%else
Source0: http://www.mplayerhq.hu/MPlayer/releases/MPlayer-%{version}%{?rcver}.tar.bz2
%endif
Source2: http://www.mplayerhq.hu/MPlayer/Skin/Blue-1.4.tar.bz2
Patch0: MPlayer-0.90pre9-runtimemsg.patch
Patch1: MPlayer-0.90-playlist.patch
Patch2: MPlayer-0.90pre10-redhat.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: mplayer-fonts
Requires: libpostproc = %{version}-%{release}
BuildRequires: gtk+-devel, SDL-devel
BuildRequires: libpng-devel, libjpeg-devel, libungif-devel
BuildRequires: lame-devel, libmad-devel, flac-devel
BuildRequires: libogg-devel, libvorbis-devel, libmatroska-devel
BuildRequires: libmad-devel, xmms-devel, libdv-devel
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}
%{?_with_samba:BuildRequires: samba-common}
%{?_with_dvb:BuildRequires: kernel-source}
%{!?_without_alsa:BuildRequires: alsa-lib-devel}
%{!?_without_fribidi:BuildRequires: fribidi-devel}
%{!?_without_aalib:BuildRequires: aalib-devel}
%{!?_without_lirc:BuildRequires: lirc}
%{!?_without_cdparanoia:BuildRequires: cdparanoia-devel}
%{!?_without_arts:BuildRequires: arts-devel}
%{!?_without_xvid:BuildRequires: xvidcore-devel}
%{!?_without_esd:BuildRequires: esound-devel}
%{!?_without_dvdread:BuildRequires: libdvdread-devel}
%{!?_without_faad2:BuildRequires: faad2-devel}
%{!?_without_lzo:BuildRequires: lzo-devel}
%{!?_without_fame:BuildRequires: libfame-devel}
%{!?_without_caca:BuildRequires: libcaca-devel}
%{!?_without_theora:BuildRequires: libtheora-devel}
#{!?_without_dvdnav:BuildRequires: libdvdnav-devel}

%description
MPlayer is a movie player. It plays most video formats as well as DVDs.
Its big feature is the wide range of supported output drivers. There are also
nice antialiased shaded subtitles and OSD.

Available rpmbuild rebuild options :
--with : samba dvb
--without : aalib lirc cdparanoia arts xvid esd dvdread faad2 lzo libfame caca
            theora osdmenu gcccheck freedesktop


%package -n libpostproc
Summary: Video postprocessing library from MPlayer
Group: System Environment/Libraries
Provides: libpostproc-devel = %{version}-%{release}

%description -n libpostproc
MPlayer is a movie player. It plays most video formats as well as DVDs.
Its big feature is the wide range of supported output drivers. There are also
nice antialiased shaded subtitles and OSD.

This package contains only MPlayer's libpostproc post-processing library which
other projects such as transcode may use. Install this package if you intend
to use MPlayer, transcode or other similar programs.


%prep
%if %{?date:1}0
%setup -n MPlayer-%{date}
%else
%setup -n MPlayer-%{version}%{?rcver}
%endif
%patch0 -p1 -b .runtimemsg
%patch1 -p1 -b .playlist
%patch2 -p0 -b .redhat

# Overwrite the system menu entry with ours
%{__cat} <<EOF > etc/mplayer.desktop
[Desktop Entry]
Name=Movie Player
Comment=Play multimedia files and media
Icon=mplayer.xpm
Exec=gmplayer %f
Terminal=false
MimeType=video/mpeg;video/x-msvideo;video/quicktime
Type=Application
Categories=Application;AudioVideo;
Encoding=UTF-8
EOF


%build
find . -name "CVS" | xargs %{__rm} -rf
./configure \
    --prefix=%{_prefix} \
    --datadir=%{_datadir}/mplayer \
    --confdir=%{_sysconfdir}/mplayer \
    --mandir=%{_mandir} \
    --enable-gui \
    --enable-largefiles \
    --enable-dynamic-plugins \
    --enable-xmms \
    --with-xmmsplugindir=%{xmms_plugindir} \
%ifarch %{ix86}
    --enable-runtime-cpudetection \
    --enable-win32 \
    --with-win32libdir=%{_libdir}/win32 \
    --with-reallibdir=%{_libdir}/win32 \
%else
    --with-reallibdir=%{_libdir}/real \
%endif
    --enable-joystick \
    --disable-mpdvdkit \
    %{?_without_gcccheck:--disable-gcc-checking} \
    %{?_without_alsa:--disable-alsa} \
    %{?_without_aalib:--disable-aa} \
    %{?_without_lirc:--disable-lirc} \
    %{?_without_cdparanoia:--disable-cdparanoia} \
    %{!?_without_cdparanoia:--with-cdparanoiaincdir=%{_includedir}/cdda} \
    %{?_without_libdv:--disable-libdv} \
    %{?_without_arts:--disable-arts} \
    %{?_without_esd:--disable-esd} \
    %{?_without_dvdread:--disable-dvdread} \
    %{?_without_faad2:--disable-faad} \
    %{!?_without_faad2:--enable-external-faad} \
    %{?_without_libfame:--disable-libfame} \
    %{?_without_caca:--disable-caca} \
    %{?_without_theora:--disable-theora} \
    %{?_with_dvb:--enable-dvbhead} \
    %{?_with_dvb:--with-dvbincdir=/lib/modules/`uname -r`/build/include} \
    --enable-shared-pp \
    --enable-i18n \
    --language=all \
    %{!?_without_osdmenu:--enable-menu} \
    %{?_with_samba:--enable-smb}

    # "dvdnav disabled, it does not work" (1.0pre5, still the same)
    #{!?_without_dvdnav:--enable-dvdnav} \

# Fix some lib vs. lib64 issues
%{__perl} -pi.orig -e 's|/usr/lib/libxmms|%{_libdir}/libxmms|s' config.mak
%{__perl} -pi.orig -e 's|\$\(prefix\)/lib|\$(libdir)|g' \
    libavcodec/libpostproc/Makefile

%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}

### The default Skin
%{__mkdir_p} %{buildroot}%{_datadir}/mplayer/Skin/
%{__tar} -xjf %{SOURCE2} -C %{buildroot}%{_datadir}/mplayer/Skin/
%{__mv} -f %{buildroot}%{_datadir}/mplayer/Skin/* %{buildroot}%{_datadir}/mplayer/Skin/default

### Fix eventual skin permissions :-(
find %{buildroot}%{_datadir}/mplayer/Skin -type d -exec chmod 755 {} \;
find %{buildroot}%{_datadir}/mplayer/Skin -type f -exec chmod 644 {} \;

# The fonts are now in a separate package
%{__rm} -rf %{buildroot}%{_datadir}/mplayer/font || :

# The nicer icon used in the menu entry
%{__install} -D -m0644 Gui/mplayer/pixmaps/MPlayer_mini.xpm \
    %{buildroot}%{_datadir}/pixmaps/mplayer.xpm

### Install libpostproc if not already installed
if [ ! -e "%{buildroot}%{_libdir}/libpostproc.so" ]; then
    %makeinstall -C libavcodec/libpostproc
fi


%post
/sbin/ldconfig
update-desktop-database %{_datadir}/applications &>/dev/null || :

%postun
/sbin/ldconfig
update-desktop-database %{_datadir}/applications &>/dev/null || :

%post -n libpostproc
/sbin/ldconfig

%postun -n libpostproc
/sbin/ldconfig


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog DOCS/ README etc/*.conf
%dir %{_sysconfdir}/mplayer/
#config %{_sysconfdir}/mplayer/mplayer.conf
%{_bindir}/*
%ifarch %{ix86}
%{_libdir}/libdha.so*
%{_libdir}/mplayer/
%endif
%{_datadir}/applications/mplayer.desktop
%{_datadir}/mplayer/
%{_datadir}/pixmaps/*
%{_mandir}/man1/*.1*
%lang(cz) %{_mandir}/cz/man1/*.1*
%lang(de) %{_mandir}/de/man1/*.1*
%lang(es) %{_mandir}/es/man1/*.1*
%lang(fr) %{_mandir}/fr/man1/*.1*
%lang(hu) %{_mandir}/hu/man1/*.1*
%lang(it) %{_mandir}/it/man1/*.1*
%lang(pl) %{_mandir}/pl/man1/*.1*
%lang(sv) %{_mandir}/sv/man1/*.1*

%files -n libpostproc
%defattr(-, root, root, 0755)
%{_includedir}/postproc/
%{_libdir}/libpostproc.so*


%changelog
* Mon Nov 01 2004 Dag Wieers <dag@wieers.com> - 1.0-0.12.20042025
- Made the lack of update-desktop-database less dramatic.

* Mon Oct 25 2004 Matthias Saou <http://freshrpms.net/> 1.0-0.11.20042025
- Update to today's CVS snapshot.
- Simplify the desktop file install, as there is now one included.

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

