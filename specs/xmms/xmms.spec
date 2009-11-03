# $Id$
# Authority: dag


%{?el5:%define _without_arts 1}

%{?fc2:%define _without_mikmod 1}

%{?fc1:%define _without_alsa 1}
%{?fc1:%define _without_mikmod 1}

%{?el3:%define _without_alsa 1}

%{?rh9:%define _without_alsa 1}
%{?rh9:%define _without_arts 1}
%{?rh9:%define _without_mikmod 1}

%{?rh7:%define _without_alsa 1}
%{?rh7:%define _without_arts 1}
%{?rh7:%define _without_freedesktop 1}
%{?rh7:%define _without_mikmod 1}
%{?rh7:%define _without_vorbis 1}

%{?el2:%define _without_alsa 1}
%{?el2:%define _without_arts 1}
%{?el2:%define _without_freedesktop 1}
%{?el2:%define _without_mikmod 1}
%{?el2:%define _without_vorbis 1}

%define artsplugin_ver 0.6.0

Summary: Media player for X which resembles Winamp
Name: xmms
Version: 1.2.10
Release: 14%{?dist}
Epoch: 1
License: GPL
Group: Applications/Multimedia
URL: http://www.xmms.org/

Source: http://www.xmms.org/files/1.2.x/xmms-%{version}.tar.bz2
Source4: arts_output-%{artsplugin_ver}.tar.gz
Source5: xmms.req
Source6: xmms.xpm
Source7: xmmsskins-1.0.tar.gz
#Source8: rh_mp3.c
Patch0: xmms-1.2.10-joycrash.patch
Patch1: xmms-1.2.6-audio.patch
Patch2: xmms-1.2.6-lazy.patch
Patch3: xmms-1.2.8-default-skin.patch
#Patch4: xmms-1.2.9-nomp3.patch
Patch5: xmms-1.2.8-arts.patch
Patch6: xmms-1.2.8-alsalib.patch
Patch7: xmms-cd-mountpoint.patch
# Patch8 on top of patch4
Patch8: xmms-1.2.10-multidevel.patch
Patch9: xmms-underquoted.patch
Patch10: xmms-alsa-backport.patch
Patch11: xmms-1.2.10-gcc4.patch
Patch12: xmms-1.2.10-crossfade-0.3.9.patch
Patch13: xmms-1.2.10-pls-188603.patch
Patch14: xmms-1.2.10-configfile-safe-write.patch
Patch15: xmms-1.2.10-reposition.patch
Patch16: xmms-1.2.10-ubuntu-CVE-2007-0653.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: glib2-devel, gtk+-devel, esound-devel
BuildRequires: /usr/bin/automake-1.4, /usr/bin/autoconf-2.13
%{!?_without_alsa:BuildRequires: alsa-lib-devel}
%{!?_without_arts:BuildRequires: arts-devel >= 1.0.1}
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}
%{!?_without_mikmod:BuildRequires: mikmod-devel}
%{?!_without_vorbis:BuildRequires: libvorbis-devel}

Requires: gtk+ >= 1:1.2.2, unzip
# the desktop file and redhat-menus are redundant requires really
Requires: /usr/share/desktop-menu-patches/redhat-audio-player.desktop
%{!?_without_freedesktop:Requires: desktop-file-utils}
Requires: redhat-menus >= 0.11

Obsoletes: x11amp0.7-1-1, x11amp, xmms-esd, xmms-gl, xmms-mikmod, xmms-gnome
Obsoletes: xmms-alsa, alsa-xmms, xmms-libs

#%{!?_without_arts:Conflicts: arts < 1.2.0-1.5}

%define _use_internal_dependency_generator 0
%define __find_requires %{SOURCE5}

%description
Xmms is a multimedia (Ogg Vorbis, CDs) player for the X Window System with
an interface similar to Winamp's. Xmms supports playlists and
streaming content and has a configurable interface.

%package devel
Summary: Static libraries and header files for Xmms plug-in development.
Group: Development/Libraries
Obsoletes: x11amp-devel
Requires: %{name} = %{epoch}:%{version}, gtk+-devel

%description devel
The static libraries and header files needed for building plug-ins for
the Xmms multimedia player.

%package mp3
Summary: XMMS plugin for mp3 playback.
Group: Applications/Multimedia
Requires: %{name} = %{epoch}:%{version}

%description mp3
This is the mp3 plugin for XMMS that was removed from Red Hat Linux because
the patented mp3 format itself is theoretically GPL incompatible.

%package skins
Summary: Skins for the xmms multimedia player.
Group: Applications/Multimedia
Obsoletes: xmmsskins
Requires: %{name}

%description skins
This is a collection of skins for the xmms multimedia player. The
skins were obtained from http://www.xmms.org/skins.html .

%prep
%setup -a 4
# Fix joystick plugin crashes
%patch0 -p1 -b .joycrash
# Set default output plugin to ALSA
%patch1 -p1 -b .audio
# Use RTLD_LAZY, not RTLD_NOW
%patch2 -p1 -b .lazy
# Change the default skin 
%patch3 -p1 -b .default-skin
# Don't build MP3 support, support bits for MP3 placeholder
#patch4 -p1 -b .nomp3
# Link arts dynamically and detect its presence for choosing output plugin
%patch5 -p1 -b .arts
# Don't link *everything* against alsa-lib
%patch6 -p1 -b .alsalib 
# Use something that's more likely to work as the default cdrom mountpoint
%patch7 -p0 -b .cd-mountpoint
# Avoid multilib devel conflicts
%patch8 -p1 -b .multidevel
# Fix m4 underquoted warning 
%patch9 -p1 -b .underquoted
# Backport for recent ALSA
%patch10 -p0 -b .alsa-backport
# Fix compilation with gcc4
%patch11 -p1 -b .gcc4
# Fix for crossfade >= 0.3.9 to work properly
%patch12 -p1 -b .crossfade
# Randomize playlists better
%patch13 -p1 -b .pls
%patch14 -p1
%patch15 -p1
%patch16 -p1

%{__perl} -pi.orig -e 's|/lib\b|/%{_lib}|g' configure

%{__cat} <<'EOF' >wmxmms.sh
#!/bin/sh
### http://bugs.xmms.org/show_bug.cgi?id=1907.
exec env XLIB_SKIP_ARGB_VISUALS=1 %{_libexecdir}/wmxmms "$@"
EOF

%{__cat} <<'EOF' >xmms.sh
#!/bin/sh
### http://bugs.xmms.org/show_bug.cgi?id=1907.
exec env XLIB_SKIP_ARGB_VISUALS=1 %{_libexecdir}/xmms "$@"
EOF

%build
%configure \
	--disable-dependency-tracking \
	--disable-rpath \
	--disable-static \
%{!?_without_arts:--enable-arts-shared} \
	--enable-ipv6 \
	--enable-kanji \
	--enable-texthack \
	--with-pic

%{__perl} -pi.orig -e 's|-lpthread|-lpthread -L/%{_lib}|g' Makefile */Makefile */*/Makefile */*/*/Makefile

%{__make}

%{__ln_s} -nf ../libxmms/configfile.h xmms/configfile.h

%if %{!?_without_arts:1}0
export XMMS_CONFIG="env PKG_CONFIG_PATH=$(pwd) $(pwd)/xmms-config"
cd arts_output-%{artsplugin_ver}
CFLAGS="%{optflags} -I.." %configure --disable-rpath
%{__make}
cd ..
%endif

#gcc -fPIC $RPM_OPT_FLAGS -shared -Wl,-soname -Wl,librh_mp3.so -o librh_mp3.so \
#     %{SOURCE8} -I. `gtk-config --cflags gtk`

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

%if %{!?_without_arts:1}0
%{__make} install -C arts_output-%{artsplugin_ver} DESTDIR="%{buildroot}"
%endif

### https://bugzilla.redhat.com/213172
%{__install} -Dp -m0755 %{buildroot}%{_bindir}/wmxmms %{buildroot}%{_libexecdir}/wmxmms
%{__install} -Dp -m0755 wmxmms.sh %{buildroot}%{_bindir}/wmxmms
%{__install} -Dp -m0755 %{buildroot}%{_bindir}/xmms %{buildroot}%{_libexecdir}/xmms
%{__install} -Dp -m0755 xmms.sh %{buildroot}%{_bindir}/xmms

#install -m 755 librh_mp3.so %{buildroot}%{_libdir}/xmms/Input

mkdir -p %{buildroot}%{_datadir}/xmms/Skins
pushd %{buildroot}%{_datadir}/xmms/Skins
  tar xvfz %{SOURCE7}
popd

mkdir -pv %{buildroot}%{_datadir}/applications
(cd $RPM_BUILD_ROOT%{_datadir}/applications && ln -sf \
  %{_datadir}/desktop-menu-patches/redhat-audio-player.desktop)

%{__install} -Dp -m0644 xmms/xmms_logo.xpm %{buildroot}%{_datadir}/pixmaps/xmms_logo.xpm
%{__install} -Dp -m0644 xmms/xmms_mini.xpm %{buildroot}%{_datadir}/pixmaps/mini/xmms_mini.xpm
%{__install} -Dp -m0644 $RPM_SOURCE_DIR/xmms.xpm %{buildroot}%{_datadir}/pixmaps/xmms.xpm
%{__install} -Dp -m0644 xmms.pc %{buildroot}%{_libdir}/pkgconfig/xmms.pc

# unpackaged files
rm -f %{buildroot}%{_datadir}/xmms/*/lib*.{a,la} \
      %{buildroot}%{_libdir}/libxmms.la \
      %{buildroot}%{_libdir}/xmms/*/*.la \
      %{buildroot}%{_mandir}/man1/gnomexmms*

%post
/sbin/ldconfig
gtk-update-icon-cache -qf %{_datadir}/icons/hicolor &>/dev/null || :
update-desktop-database %{_datadir}/desktop-menu-patches &>/dev/null || :

%postun
/sbin/ldconfig
gtk-update-icon-cache -qf %{_datadir}/icons/hicolor &>/dev/null || :
update-desktop-database %{_datadir}/desktop-menu-patches &>/dev/null || :

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING FAQ INSTALL NEWS README TODO
%{_bindir}/wmxmms
%{_bindir}/xmms
%{_libdir}/libxmms.so.1*
%dir %{_libdir}/xmms/
%{_libdir}/xmms/Effect/
%{_libdir}/xmms/General/
%dir %{_libdir}/xmms/Input/
%{_libdir}/xmms/Input/libcdaudio.so
%{_libdir}/xmms/Input/libmikmod.so
%{_libdir}/xmms/Input/libtonegen.so
%{!?_without_vorbis:%{_libdir}/xmms/Input/libvorbis.so}
%{_libdir}/xmms/Input/libwav.so
%{_libdir}/xmms/Output/
%{_libdir}/xmms/Visualization/
%{_libexecdir}/wmxmms
%{_libexecdir}/xmms
%{_datadir}/applications/redhat-audio-player.desktop
%{_datadir}/pixmaps/xmms.xpm
%{_datadir}/pixmaps/xmms_logo.xpm
%{_datadir}/pixmaps/mini/xmms_mini.xpm
%dir %{_datadir}/xmms/
%{_datadir}/xmms/*.xpm
%{_mandir}/man1/[wx]*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/xmms
%{_bindir}/xmms-config
%{_datadir}/aclocal/xmms.m4
#%{_libdir}/lib*.a
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/xmms.pc 

%files mp3
%defattr(-, root, root, 0755)
%dir %{_libdir}/xmms/Input/
%{_libdir}/xmms/Input/libmpg123.so

%files skins
%defattr(-, root, root, 0755)
%{_datadir}/xmms/Skins/

%changelog
* Sat May 05 2007 Dag Wieers <dag@wieers.com> - 1:1.2.10-14
- Workaround for http://bugs.xmms.org/show_bug.cgi?id=1907.
- Fixed build again on anything older than EL5.

* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 1:1.2.10-13
- Added xmms.pc for building software against xmms. (Chris Tracy)

* Wed Mar 21 2007 Dag Wieers <dag@wieers.com> - 1:1.2.10-12
- Fixed gcc4 compilation with patch from Fedora.

* Tue Jan 11 2005 Dag Wieers <dag@wieers.com> - 1:1.2.10-9.2
- Disable arts for el3.

* Tue Jan 04 2005 Dag Wieers <dag@wieers.com> - 1:1.2.10-9.2
- Added _without_arts macros. (Tres Seaver)

* Mon Jan 03 2005 Dag Wieers <dag@wieers.com> - 1:1.2.10-9.2
- Fix a problem with update-desktop-database on older dists. (Erik Kjær Pedersen)

* Thu Nov  4 2004 Matthias Saou <http://freshrpms.net/> 1:1.2.10-9.1
- Put back pristine sources.
- Added the usual mp3 sub-package.
- Removed nomp3 patch and commented out rh_mp3 plugin build/install.
- Added xmms-alsa obsoletes.
- No longer fix the missing gtk+-devel dep of the devel package, yeah!

* Wed Oct 13 2004 Colin Walters <walters@redhat.com> 1:1.2.10-9
- Correct update-desktop-database correction for postun

* Wed Oct 13 2004 Colin Walters <walters@redhat.com> 1:1.2.10-8
- Call update-desktop-database on correct directory

* Mon Oct 04 2004 Colin Walters <walters@redhat.com> 1:1.2.10-7
- PreReq desktop-file-utils 0.9
- Run update-desktop-database

* Sun Aug 15 2004 Tim Waugh <twaugh@redhat.com> 1:1.2.10-6
- Fixed another underquoted m4 definition.

* Thu Jul 15 2004 Tim Waugh <twaugh@redhat.com> 1:1.2.10-5
- Fixed warnings in shipped m4 file.

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon May 31 2004 Warren Togami <wtogami@redhat.com> 1:1.2.10-3.p
- #124701 -devel req gtk+-devel

* Thu Mar 11 2004 Bill Nottingham <notting@redhat.com> 1:1.2.10-2.p
- update to 1.2.10
- fix buildreqs (#114857)
- switch default output plugin to ALSA

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Feb 23 2004 Than Ngo <than@redhat.com> 1:1.2.9-5.p
- enable arts plugin, it should work with arts-1.2.0-1.5 or newer.

* Sat Feb 14 2004 Than Ngo <than@redhat.com> 1:1.2.9-4.p
- disable xmms-1.2.8-arts.patch

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 28 2004 Bill Nottingham <notting@redhat.com> 1:1.2.9-2.p
- enable ipv6 (#105774)

* Wed Jan 28 2004 Bill Nottingham <notting@redhat.com> 1:1.2.9-1.p
- update to 1.2.9

* Fri Dec 12 2003 Bill Nottingham <notting@redhat.com> 1:1.2.8-4.p
- rebuild, pick up alsa plugin

* Wed Oct 22 2003 Bill Nottingham <notting@redhat.com> 1:1.2.8-3.p
- fix dependency blacklisting (corollary of #100917)

* Mon Oct 13 2003 Than Ngo <than@redhat.com> 1:1.2.8-2.p
- workaround to fix arts crash

* Mon Sep  8 2003 Bill Nottingham <notting@redhat.com> 1:1.2.8-1.p
- update to 1.2.8
- clean out now-upstream stuff (Welsh po file, other patches)
- switch to Håvard's arts plugin, tweak it's default buffer size
- don't explicitly require trademarked skin name (#84554)

* Mon Jun 30 2003 Bill Nottingham <notting@redhat.com> 1:1.2.7-23.p
- add welsh po file (#98244)

* Sun Jun  8 2003 Tim Powers <timp@redhat.com> 1:1.2.7-22.1.p
- built for RHEL

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Jun  3 2003 Jeff Johnson <jbj@redhat.com>
- add explicit epoch's where needed.

* Mon Feb 24 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 21 2003 Havoc Pennington <hp@redhat.com> 1:1.2.7-20.p
- patch to fix session management which may prevent gnome-session hangs

* Wed Feb  5 2003 Bill Nottingham <notting@redhat.com> 1.2.7-19.p
- rename zz_mp3 to rh_mp3
- fix rh_mp3 taking precedence over other plugins (#81002)
- nuke .la files (#68341)

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Tue Jan 14 2003 Owen Taylor <otaylor@redhat.com> 1.2.7-17.p
- Add patch from havardk@netcom.no to fix problem with file browser not
  updating in CDROM directories (#65173)

* Tue Nov 12 2002 Bill Nottingham <notting@redhat.com> 1.2.7-16.p
- rebuild on more arches

* Wed Oct  2 2002 Bill Nottingham <notting@redhat.com> 1.2.7-15.p
- fix zz_mp3 plugin, tweak some buildprereqs

* Tue Oct  1 2002 Bill Nottingham <notting@redhat.com> 1.2.7-14.p
- fix arts config code (#72440, #74708, #74717)
- fix selection of 'no skin' (#73799)

* Mon Sep  2 2002 Bill Nottingham <notting@redhat.com> 1.2.7-13.p
- placeholder mp3 plugin

* Thu Aug 22 2002 Bill Nottingham <notting@redhat.com> 1.2.7-12.p
- absolute symlinks

* Wed Aug 21 2002 Bill Nottingham <notting@redhat.com> 1.2.7-11.p
- add mikmod buildprereq to insure plugin actually gets built (#70088)

* Tue Aug 20 2002 Bill Nottingham <notting@redhat.com> 1.2.7-10.p
- take out mpg123 plugin

* Sat Aug 10 2002 Than Ngo <than@redhat.com> 1.2.7-10
- Fix to use Bluecurve

* Sat Aug  3 2002 Havoc Pennington <hp@redhat.com>
- add a patch to default to redhat-artwork skin

* Wed Jul 31 2002 Havoc Pennington <hp@redhat.com> 1.2.7-8
- use override desktop file from redhat-menus so we can translate it
- desktop file is not a config file

* Tue Jul 30 2002 Bill Nottingham <notting@redhat.com> 1.2.7-7
- desktop file tweaks (#69549)

* Thu Jul 25 2002 Bill Nottingham <notting@redhat.com> 1.2.7-6
- desktop file tweaks (#69549)

* Fri Jul 18 2002 Bill Nottingham <notting@redhat.com> 1.2.7-5
- build against current libvorbis

* Wed Jun 27 2002 Karsten Hopp <karsten@redhat.de> 1.2.7-4
- fix buildprereq (arts-devel instead of kdelibs-sound-devel)
- added patch to avoid dynamic linkage against libarts (static libarts is no
  longer available), use dlopen instead

* Sun May 26 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 16 2002 Bill Nottingham <notting@redhat.com> 1.2.7-2
- kill -gnome subpackage

* Mon Mar  4 2002 Bill Nottingham <notting@redhat.com> 1.2.7-1
- update to 1.2.7

* Tue Feb 26 2002 Bill Nottingham <notting@redhat.com> 1.2.6-2
- don't strip libs

* Tue Jan 15 2002 Bill Nottingham <notting@redhat.com> 1.2.6-0.7
- update to 1.2.6

* Tue Sep  4 2001 Bill Nottingham <notting@redhat.com>
- ship man pages (#53095)

* Mon Aug 20 2001 Bill Nottingham <notting@redhat.com>
- add patch to fix vorbis on big-endian machines (<havardk@xmms.org>)
- fix double ownership of files that made xmms-skins irrelevant (#51581)

* Mon Jul 23 2001 Bill Nottingham <notting@redhat.com>
- buildrequire gnome-libs-devel (#44849)

* Tue Jul 17 2001 Bill Nottingham <notting@redhat.com>
- own %%{_datadir}/xmms
- take out the realtime patch for now
- remove other obsoleted patches

* Tue Jul 17 2001 Preston Brown <pbrown@redhat.com>
- add audio/mpegurl to list of acceptable MimeTypes

* Tue Jun 26 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- change filelist to include link from lib major version number

* Wed Jun 20 2001 Preston Brown <pbrown@redhat.com>
- 1.2.5
- italian i18n patch disabled until a newer one available
- japanese patch disabled until there is one available for 1.2.5
- add OGG mimetype to .desktop file

* Wed Jun  6 2001 Bill Nottingham <notting@redhat.com>
- make it build

* Mon May 21 2001 Tim Powers <timp@redhat.com>
- added skins subpackage

* Mon May 14 2001 Bill Nottingham <notting@redhat.com>
- remove extraneous printf in tmpdir patch
- add prototype for mpg123_munge_sample in downsample_vis patch

* Thu Apr 11 2001 Bill Nottingham <notting@redhat.com>
- rebuild to fix dependencies on ia64

* Tue Mar 20 2001 Bill Nottingham <notting@redhat.com>
- remove a couple of patches that are no longer needed (<havardk@xmms.org>)

* Tue Mar 20 2001 Harald Hoyer <harald@redhat.de>
- added euro patch to fix font loading

* Tue Mar 13 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Fix arts plugin installation

* Mon Mar 05 2001 Owen Taylor <otaylor@redhat.com>
- Rebuild for GTK+-1.2.9 include dirs

* Thu Mar  1 2001 Bill Nottingham <notting@redhat.com>
- fix arts pluging build to be self hosting (#30049)

* Thu Feb 22 2001 Bill Nottingham <notting@redhat.com>
- add recommended bugfixes from the XMMS team (<havardk@xmms.org>)

* Thu Feb  8 2001 Bill Nottingham <notting@redhat.com>
- fix tmpdir patch & skin saving (#26494)

* Thu Feb  1 2001 Bill Nottingham <notting@redhat.com>
- hack to fix visualization scope when downsampling (#19642)
- install xmms.xpm and fix icon entry in desktop,
  add some #include fixes (#20944, <tothwolf@concentric.net>)
- make realtime not make xmms perform *worse* (#23951)

* Thu Jan 18 2001 Bill Nottingham <notting@redhat.com>
- don't segfault on skin change (#24284)

* Mon Jan  8 2001 Bill Nottingham <notting@redhat.com>
- kill separate kde package

* Mon Jan  8 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Add arts backend (new kde subpackage)
- Add a hack to determine whether arts, esd or oss should be used
- Fix requires
- Mark locale files

* Tue Jan  2 2001 Bill Nottingham <notting@redhat.com>
- clean up japanese support patch some
- don't enable transparenthack; it's broken
- fix possible temp race

* Mon Dec 25 2000 Yukihiro Nakai <ynakai@redhat.com>
- Add Japanese resources.

* Tue Nov 28 2000 Bill Nottingham <notting@redhat.com>
- update to 1.2.4

* Mon Nov 13 2000 Bill Nottingham <notting@redhat.com>
- fix some compiler warnings (#20135)
- add Ogg Vorbis plugin

* Mon Oct 30 2000 Preston Brown <pbrown@redhat.com>
- even better .desktop file handling streaming MP3 types

* Mon Oct 16 2000 Bill Nottingham <notting@redhat.com>
- um, if we're going to ship a japanese translation, we should probably
  ship the .mo files
- add a patch for small files from Thomas Woller
- add alpha patches (#19141)

* Fri Oct 13 2000 Preston Brown <pbrown@redhat.com>
- improved .desktop file
- 1.2.3

* Thu Aug 31 2000 Satoru Sato <ssato@redhat.com>
- fix SPEC

* Wed Aug 30 2000 Satoru Sato <ssato@redhat.com>
- apply nls patch (by Hiroshi Takekawa <sian@big.or.jp>)

* Fri Aug 11 2000 Jonathan Blandford <jrb@redhat.com>
- Up Epoch and release

* Mon Aug  7 2000 Bill Nottingham <notting@redhat.com>
- rebuild against new DGA

* Fri Aug  4 2000 Bill Nottingham <notting@redhat.com>
- add translation to desktop entry

* Wed Jul 19 2000 Bill Nottingham <notting@redhat.com>
- version 1.2.2

* Thu Jul 13 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Fri Jul  7 2000 Bill Nottingham <notting@redhat.com>
- use lazy symbol resolution in the plugin loader

* Mon Jun 18 2000 Bill Nottingham <notting@redhat.com>
- 1.2.1

* Fri Jun 16 2000 Preston Brown <pbrown@redhat.com>
- some fixes to the .desktop entry

* Mon Jun 12 2000 Preston Brown <pbrown@redhat.com>
- 1.2.0
- use rpm macros
- fix gnomexmms buildroot breakage

* Sun Jun 11 2000 Bill Nottingham <notting@redhat.com>
- rebuild in new environment
- work around some toolchain madness

* Mon Mar 27 2000 Bill Nottingham <notting@redhat.com>
- include /usr/share/xmmms/wmxmms.xpm

* Tue Feb 22 2000 Bill Nottingham <notting@redhat.com>
- use /usr prefix to be consistent with xmms.org (why not?)
- find something more appropriate than the disk writer to use
  as output plugin if configured one doesn't exist

* Wed Feb 16 2000 Matt Wilson <msw@redhat.com>
- include /usr/X11R6/bin/wmxmms

* Thu Feb  3 2000 Bill Nottingham <notting@redhat.com>
- some cleanups

* Mon Jan 31 2000 Bill Nottingham <notting@redhat.com>
- update to 1.0.1

* Fri Jan 28 2000 Bill Nottingham <notting@redhat.com>
- update to 1.0.0

* Tue Sep 28 1999 Bill Nottingham <notting@redhat.com>
- update to 0.9.5.1

* Wed Sep 23 1999 Preston Brown <pbrown@redhat.com>
- latest stable release (0.9.5)

* Wed Sep 22 1999 Bill Nottingham <notting@redhat.com>
- open in non-blocking mode, then reset
- make esd the default

* Mon Sep 13 1999 Bill Nottingham <notting@redhat.com>
- fix binaries

* Thu Sep  9 1999 Bill Nottingham <notting@redhat.com>
- fix gtk+ requirements

* Wed Aug 18 1999 Bill Nottingham <notting@redhat.com>
- fix a /0 in the disk writer

* Tue Jul 20 1999 Bill Nottingham <notting@redhat.com>
- 0.9.1

* Mon Jun 21 1999 Bill Nottingham <notting@redhat.com>
- use other fallback patch
- obsolete x11amp-devel

* Fri Jun 11 1999 Matt Wilson <msw@redhat.com>
- updated to xmms 0.9 final

* Thu Apr 8 1999 The Rasterman <raster@redhat.com>
- patched to have plugin fallback to other plugins for output if plugin fails.

* Mon Mar 29 1999 Michael Maher <mike@redhat.com>
- added desktop entry.

* Mon Mar 22 1999 Michael Maher <mike@redhat.com>
- made some changes to the spec file.
- has 'esd' support now.
- stripped executables.

* Mon Feb 15 1999 Michael Maher <mike@redhat.com>
- built pacakge for 6.0
- changed spec file, added mp3 licenses.

* Mon Feb 15 1999 Ryan Weaver <ryanw@infohwy.com>
  [x11amp-0.9-alpha3-1]
- Updated to alpha3 see ChangLog for changes.

* Wed Jan 13 1999 Ryan Weaver <ryanw@infohwy.com>
  [x11amp-0.9-alpha2-1]
- fixed close button in PL/EQ windows
- fixed shuffel/randomize functions
- removed imlib, no need for imlib anymore
- mpg123 plugin now works on SMP machines, also reduced cpu usage
- fixed so mainwindow will be positioned correct at startup in some windowmanagers
- fixed the playlistwindow buttons that ended up behind the window
- added mikmod plugin into the source tree
- now you can configure the OSS drivers and mpg123 plugin
- SKINSDIR variable can be used again
- added bars as analyzer mode
- in playlistwindow the player control buttons now work, also time window works
