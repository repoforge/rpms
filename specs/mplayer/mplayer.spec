# $Id: mplayer.spec,v 1.1 2004/02/26 17:54:30 thias Exp $

# Is this a daily build? If so, put the date like "20020808" otherwise put 0
%define date      20040211
#define rcver     pre2

%define desktop_vendor freshrpms

Summary: MPlayer, the Movie Player for Linux
Name: mplayer
Version: 1.0
Release: 0.7%{?rcver:.%{rcver}}%{?date:.%{date}}.fr
License: GPL
Group: Applications/Multimedia
URL: http://mplayerhq.hu/
%if %{?date:1}%{!?date:0}
Source0: http://www.mplayerhq.hu/MPlayer/cvs/MPlayer-current.tar.bz2
%else
Source0: http://www.mplayerhq.hu/MPlayer/cvs/MPlayer-%{version}%{?rcver}.tar.bz2
%endif
Source2: http://www.mplayerhq.hu/MPlayer/Skin/Blue-1.0.tar.bz2
Patch0: MPlayer-0.90pre9-runtimemsg.patch
Patch1: MPlayer-0.90-playlist.patch
Patch2: MPlayer-0.90pre10-redhat.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: gtk+, SDL, libpng, lame, libogg, libvorbis
Requires: mplayer-fonts, libpostproc = %{version}-%{release}
#{?_with_dvdnav:Requires: libdvdnav}
%{?_with_samba:Requires: samba-common}
%{!?_without_alsa:Requires: alsa-lib}
%{!?_without_aalib:Requires: aalib}
%{!?_without_lirc:Requires: lirc}
%{!?_without_libdv:Requires: libdv}
%{!?_without_arts:Requires: arts}
%{!?_without_xvid:Requires: xvidcore}
%{!?_without_esd:Requires: esound}
%{!?_without_dvdread:Requires: libdvdread}
%{!?_without_faad2:Requires: faad2}
%{!?_without_lzo:Requires: lzo}
%{!?_without_fame:Requires: libfame}
BuildRequires: gtk+-devel, SDL-devel, libpng-devel, lame-devel, libogg-devel
BuildRequires: libvorbis-devel, libmad-devel
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}
#{?_with_dvdnav:BuildRequires: libdvdnav-devel}
%{?_with_samba:BuildRequires: samba-common}
%{!?_without_alsa:BuildRequires: alsa-lib-devel}
%{!?_without_aalib:BuildRequires: aalib-devel}
%{!?_without_lirc:BuildRequires: lirc}
%{!?_without_cdparanoia:BuildRequires: cdparanoia-devel}
%{!?_without_libdv:BuildRequires: libdv-devel}
%{!?_without_arts:BuildRequires: arts-devel}
%{!?_without_xvid:BuildRequires: xvidcore}
%{!?_without_esd:BuildRequires: esound-devel}
%{!?_without_dvdread:BuildRequires: libdvdread-devel}
%{!?_without_faad2:BuildRequires: faad2-devel}
%{!?_without_lzo:BuildRequires: lzo-devel}
%{!?_without_fame:BuildRequires: libfame-devel}
#{!?_without_caca:BuildRequires: libcaca-devel}

%description
MPlayer is a movie player. It plays most video formats as well as DVDs.
Its big feature is the wide range of supported output drivers. There are also
nice antialiased shaded subtitles and OSD.

Available rpmbuild rebuild options :
--with : samba
--without : alsa aalib lirc cdparanoia libdv arts xvid esd dvdread faad2 lzo
            libfame osdmenu gcccheck freedesktop


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
%if %{?date:1}%{!?date:0}
%setup -q -n MPlayer-%{date}
%else
%setup -q -n MPlayer-%{version}%{?rcver}
%endif
%patch0 -p1 -b .runtimemsg
%patch1 -p1 -b .playlist
%patch2 -p0 -b .redhat

%build
find . -name "CVS" | xargs rm -rf
#       %{?_with_dvdnav:--enable-dvdnav} \
./configure \
    --prefix=%{_prefix} \
    --datadir=%{_datadir}/mplayer \
    --confdir=%{_sysconfdir}/mplayer \
    --mandir=%{_mandir} \
    --enable-gui \
    --enable-largefiles \
%ifarch %ix86
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
%ifnarch ppc
    --enable-runtime-cpudetection \
%endif
    --enable-shared-pp \
    --enable-i18n \
    --language=all \
    %{!?_without_osdmenu:--enable-menu} \
    %{?_with_samba:--enable-smb} << EOF
EOF
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

# The default Skin
mkdir -p %{buildroot}%{_datadir}/mplayer/Skin
pushd %{buildroot}%{_datadir}/mplayer/Skin
    tar -xjf %{SOURCE2}
    mv * default || :
popd

# Fix eventual skin permissions :-(
find %{buildroot}%{_datadir}/mplayer/Skin -type d -exec chmod 755 {} \;
find %{buildroot}%{_datadir}/mplayer/Skin -type f -exec chmod 644 {} \;

# The fonts are not in a separate package
rm -rf %{buildroot}%{_datadir}/mplayer/font || :

# The icon used in the menu entry
install -D -m 644 Gui/mplayer/pixmaps/logo.xpm \
    %{buildroot}%{_datadir}/pixmaps/mplayer-logo.xpm

# Last, add system menu entries!
cat > %{name}.desktop << EOF
[Desktop Entry]
Name=Movie Player
Comment=Play DivX ;-), MPEG, DVDs and more
Icon=mplayer-logo.xpm
Exec=gmplayer %f
Terminal=false
MimeType=video/mpeg;video/x-msvideo;video/quicktime
Type=Application
Categories=Application;AudioVideo;X-Red-Hat-Extra;
EOF

%if %{!?_without_freedesktop:1}%{?_without_freedesktop:0}
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install --vendor %{desktop_vendor} --delete-original \
    --dir %{buildroot}%{_datadir}/applications \
    %{name}.desktop
%else
install -D -m644 %{name}.desktop \
    %{buildroot}/etc/X11/applnk/Multimedia/%{name}.desktop
%endif

# Install libpostproc if not already installed
test -e %{buildroot}%{_prefix}/lib/libpostproc.so || \
    make prefix=%{buildroot}%{_prefix} -C libavcodec/libpostproc install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%post -n libpostproc -p /sbin/ldconfig

%postun -n libpostproc -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, 755)
%doc AUTHORS ChangeLog DOCS/ README etc/*.conf
%dir %{_sysconfdir}/mplayer
#%config %{_sysconfdir}/mplayer/codecs.conf
%{_prefix}/bin/*
%{_prefix}/lib/libdha.so*
%{_prefix}/lib/%{name}
%{!?_without_freedesktop:%{_datadir}/applications/*%{name}.desktop}
%{?_without_freedesktop:/etc/X11/applnk/Multimedia/%{name}.desktop}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/Skin
%{_datadir}/pixmaps/mplayer-logo.xpm
%{_mandir}/man1/*.1*
%lang(de) %{_mandir}/de/man1/*.1*
%lang(es) %{_mandir}/es/man1/*.1*
%lang(fr) %{_mandir}/fr/man1/*.1*
%lang(hu) %{_mandir}/hu/man1/*.1*
%lang(pl) %{_mandir}/pl/man1/*.1*

%files -n libpostproc
%defattr(-, root, root, 755)
%{_prefix}/include/postproc
%{_prefix}/lib/libpostproc.so*

%changelog
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

