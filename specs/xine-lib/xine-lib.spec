# $Id$
# Authority: matthias
# Upstream: <xine-user$lists,sf,net>

%{?dtag: %{expand: %%define %dtag 1}}
%{?fedora: %{expand: %%define fc%{fedora} 1}}

%{!?dtag:%define _with_modxorg 1}
%{?el5: %define _with_modxorg 1}
%{?fc6: %define _with_modxorg 1}
%{?fc5: %define _with_modxorg 1}

%{?el4:%define _with_speex104 1}

%{?fc2:%define _without_gettextdevel 1}

%{?fc1:%define _without_alsa 1}
%{?fc1:%define _without_gettextdevel 1}
%{?fc1:%define _without_theora 1}
%{?fc1:%define _without_xvmc 1}

%{?el3:%define _without_alsa 1}
%{?el3:%define _without_freetype2_pc 1}
%{?el3:%define _without_fribidi 1}
%{?el3:%define _without_gettextdevel 1}
%{?el3:%define _without_theora 1}
%{?el3:%define _without_xvmc 1}

%{?rh9:%define _without_alsa 1}
%{?rh9:%define _without_freetype2_pc 1}
%{?rh9:%define _without_fribidi 1}
%{?rh9:%define _without_gettextdevel 1}
%{?rh9:%define _without_theora 1}
%{?rh9:%define _without_xvmc 1}

%{?rh8:%define _without_alsa 1}
%{?rh8:%define _without_freetype2_pc 1}
%{?rh8:%define _without_fribidi 1}
%{?rh8:%define _without_gettextdevel 1}
%{?rh8:%define _without_theora 1}
%{?rh8:%define _without_xvmc 1}

%{?rh7:%define _without_alsa 1}
%{?rh7:%define _without_freetype2_pc 1}
%{?rh7:%define _without_fribidi 1}
%{?rh7:%define _without_gettextdevel 1}
%{?rh7:%define _without_theora 1}
%{?rh7:%define _without_gnomevfs2 1}
%{?rh7:%define _without_xvmc 1}

%{?yd3:%define _without_alsa 1}
%{?yd3:%define _without_freetype2_pc 1}
%{?yd3:%define _without_fribidi 1}
%{?yd3:%define _without_gettextdevel 1}
%{?yd3:%define _without_theora 1}
%{?yd3:%define _without_xvmc 1}

%define libname libxine1

Summary: Core library of the xine multimedia player
Name: xine-lib
Version: 1.1.11
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://xinehq.de/

Source: http://downloads.sf.net/xine/xine-lib-%{version}.tar.bz2
Patch0: xine-lib-1.1.9-speex104.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, pkgconfig, zlib-devel, libtiff-devel
BuildRequires: libvorbis-devel, SDL-devel, bzip2-devel
# BUG : libmng-devel should apparently require libjpeg-devel for includes
BuildRequires: libpng-devel, libmng-devel, libjpeg-devel, freetype-devel
BuildRequires: gtk2-devel
BuildRequires: libcdio-devel, vcdimager-devel, a52dec-devel, libmad-devel
%{?_with_modxorg:BuildRequires: libXt-devel, libXv-devel, libGL-devel, libGLU-devel, libXinerama-devel, libXvMC-devel}
%{!?_with_modxorg:BuildRequires: XFree86-devel}
%{!?_with_modxorg:%{!?_without_xvmc:BuildRequires: libXvMCW-devel}}
%{?_with_rte:BuildRequires: rte-devel}
%{?_with_extdvdnav:BuildRequires: libdvdnav-devel >= 0.1.4}
%{?_with_extffmpeg:BuildRequires: ffmpeg-devel}
%{!?_without_alsa:BuildRequires: alsa-lib-devel}
%{!?_without_esound:BuildRequires: esound-devel}
%{!?_without_aalib:BuildRequires: aalib-devel}
%{!?_without_directfb:BuildRequires: directfb-devel}
%{!?_without_flac:BuildRequires: flac-devel}
%{!?_without_libfame:BuildRequires: libfame-devel}
%{!?_without_arts:BuildRequires: arts-devel}
%{!?_without_gnomevfs2:BuildRequires: gnome-vfs2-devel}
%{!?_without_speex:BuildRequires: speex-devel}
%{!?_without_caca:BuildRequires: libcaca-devel}
%{!?_without_theora:BuildRequires: libtheora-devel}
%{!?_without_samba:BuildRequires: samba-common}
%{!?_without_modplug:BuildRequires: libmodplug-devel}
%{!?_without_magick:BuildRequires: ImageMagick-devel}
%{!?_without_gettextdevel:BuildRequires: gettext-devel}
%{?_without_gettextdevel:BuildRequires: gettext}
%{!?dtag:BuildRequires: freeglut-devel}
%{?fc6:BuildRequires: freeglut-devel}
%{?fc5:BuildRequires: freeglut-devel}
%{?fc4:BuildRequires: freeglut-devel}
%{?fc3:BuildRequires: freeglut-devel}
%{?fc2:BuildRequires: freeglut-devel}
%{?fc1:BuildRequires: freeglut-devel}
%{?rh9:BuildRequires: glut-devel}
Requires: libdvdcss
Obsoletes: xine-libs <= 1.0.0
Obsoletes: libxine <= %{version}-%{release}
Obsoletes: xine-libs-moles <= %{version}-%{release}
Obsoletes: xine-arts <= %{version}-%{release}
Obsoletes: xine-extras <= %{version}-%{release}

%description
Xine is a free multimedia player. It plays back CDs, DVDs, and VCDs. It also
decodes multimedia files like AVI, MOV, WMV, and MP3 from local disk drives,
and displays multimedia streamed over the Internet. It interprets many of the
most common multimedia formats available - and some of the most uncommon
formats, too.

This package contains the backend files for the Xine multimedia player.

Available rpmbuild rebuild options :
--with : rte extdvdnav extffmpeg
--without : alsa aalib libfame flac esound arts gnomevfs2 speex caca xvmc samba
            modplug magick
(only alsa can be really disabled, others only remove explicit package
 dependency which won't make much difference if devel files are found)

%package devel
Summary: Development files for the xine library
Group: Development/Libraries
Requires: %{name} = %{version}, pkgconfig, zlib-devel
%{?_with_modxorg:Requires: libXt-devel, libXv-devel, libGL-devel, libGLU-devel, libXinerama-devel, libXvMC-devel}
%{!?_with_modxorg:Requires: XFree86-devel}
Obsoletes: xine-libs-devel <= 1.0.0

%description devel
Xine is a free multimedia player. It plays back CDs, DVDs, and VCDs. It also
decodes multimedia files like AVI, MOV, WMV, and MP3 from local disk drives,
and displays multimedia streamed over the Internet. It interprets many of the
most common multimedia formats available - and some of the most uncommon
formats, too.

This package contains the development files needed to build applications that
use the Xine library.

%prep
%setup

%{?_with_speex104:%patch0 -p0}

%{__perl} -pi -e 's|"/lib /usr/lib\b|"/%{_lib} %{_libdir}|' configure

%build
%{?_without_freetype2_pc:export FT2_CFLAGS="$(freetype-config --cflags)"}
%{?_without_freetype2_pc:export FT2_LIBS="$(freetype-config --libs)"}
export SDL_CFLAGS="$(sdl-config --cflags)" SDL_LIBS="$(sdl-config --libs)"
%configure \
%{?_without_alsa:--disable-alsa} \
    --enable-antialiasing \
%{!?_without_directfb:--enable-directfb} \
    --enable-ipv6 \
    --with-external-a52dec \
%{?_with_extffmpeg:--with-external-ffmpeg} \
    --with-external-libmad \
%{!?_with_extdvdnav:--with-included-dvdnav} \
    --with-fontconfig \
    --with-freetype \
    --with-pic \
%{?_with_modxorg:--with-xv-path="%{_libdir}"}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{libname}
# Remove all those unused docs
%{__rm} -rf %{buildroot}%{_docdir}/xine/ || :

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{libname}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%doc doc/README.* doc/faq/faq.txt doc/faq/faq.html
%doc %{_docdir}/xine-lib/hackersguide/
%doc %{_mandir}/man5/xine.5*
%{_datadir}/xine/
%{_libdir}/libxine.so.*
%{_libdir}/xine/
%exclude %{_docdir}/xine-lib/

%files devel
%defattr(-, root, root, 0755)
%doc doc/hackersguide/*.html doc/hackersguide/*.png
%doc %{_mandir}/man1/xine-config.1*
%{_bindir}/xine-config
%{_datadir}/aclocal/xine.m4
%{_includedir}/xine/
%{_includedir}/xine.h
%{_libdir}/libxine.so
%{_libdir}/pkgconfig/libxine.pc
%exclude %{_libdir}/libxine.la

%changelog
* Wed Mar 26 2008 Dag Wieers <dag@wieers.com> - 1.1.11-1
- Updated to release 1.1.11.

* Mon Feb 11 2008 Dag Wieers <dag@wieers.com> - 1.1.10.1-1
- Updated to release 1.1.10.1.

* Mon Jan 28 2008 Dag Wieers <dag@wieers.com> - 1.1.10-1
- Updated to release 1.1.10.

* Fri Jan 18 2008 Dag Wieers <dag@wieers.com> - 1.1.9.1-1
- Updated to release 1.1.9.1.

* Mon Jan 07 2008 Dag Wieers <dag@wieers.com> - 1.1.9-1
- Updated to release 1.1.9.

* Thu Oct 04 2007 Dag Wieers <dag@wieers.com> - 1.1.8-1
- Updated to release 1.1.8.

* Sat Apr 21 2007 Dag Wieers <dag@wieers.com> - 1.1.7-1
- Updated to release 1.1.7.

* Sat Apr 21 2007 Dag Wieers <dag@wieers.com> - 1.1.6-1
- Updated to release 1.1.6.

* Sun Apr 15 2007 Dag Wieers <dag@wieers.com> - 1.1.5-1
- Updated to release 1.1.5.

* Sun Mar 11 2007 Dag Wieers <dag@wieers.com> - 1.1.4-1
- Updated to release 1.1.4.
- Added Fedora Extras patches.

* Sun Sep 24 2006 Matthias Saou <http://freshrpms.net/> 1.1.2-2
- Rebuild against new libcdio.

* Tue Jul 11 2006 Matthias Saou <http://freshrpms.net/> 1.1.2-1
- Update to 1.1.2.
- Source is now a .bz2 file.
- Build require gettext-devel.
- Build require gtk2-devel (for gdk-pixbuf-2.0).
- Enable samba support by default.
- Enable modplug support by default.
- Enable ImageMagick support by default.
- Switch to external libcdio, vcdimager, a52dec and libmad. Keep internal
  dvdnav and libdts since those have extrnal development (mostly) stopped.
  (note that a52dec-devel seems to be missing a52_internal.h for now)

* Mon Mar  6 2006 Matthias Saou <http://freshrpms.net/> 1.1.1-2
- Add freetype support.
- Add many missing modular X build requirements.
- Force Xv path to prefix for modular X, otherwise it it not found.

* Tue Jan 10 2006 Matthias Saou <http://freshrpms.net/> 1.1.1-1
- Update to 1.1.1 (missed that one in Nov.!).
- Remove no longer needed faad patch.
- Don't use external ffmpeg (on FC4), as it's nearly never a good idea, so
  let only people who really want to do it... do it.

* Tue Aug  2 2005 Matthias Saou <http://freshrpms.net/> 1.1.0-1
- Move xine.5 man page from devel to the main package.
- Add some READMEs from doc/.
- Change the devel doc from sgml to html/png, makes more sense.

* Sat Jul 30 2005 Matthias Saou <http://freshrpms.net/> 1.1.0-1
- Update to 1.1.0, which includes gcc4 fixes.

* Tue May  3 2005 Matthias Saou <http://freshrpms.net/> 1.0.1-2
- Remove ffmpeg MMX disabling, it works, go figure.
- No longer run autogen.sh or libtool. Same, it works... confusing.
- Use external ffmpeg lib only for FC4, as there are issues (at least on FC3).

* Thu Apr 28 2005 Matthias Saou <http://freshrpms.net/> 1.0.1-1
- Update to 1.0.1.
- Add patch for GCC4 from Ville.
- Disable ffmpeg's MMX, build fails otherwise.
- Run autogen to fix lib linking problem.
- Add missing buildroot removal in %%install.

* Fri Feb  4 2005 Matthias Saou <http://freshrpms.net/> 1.0.0-2
- Added patch to fix faad on x86_64, thanks to Nicholas Miell.

* Mon Jan  3 2005 Matthias Saou <http://freshrpms.net/> 1.0.0-1
- Update to 1.0 final! (had to keep 1.0.0 as the version, though)
- Added libXvMCW support (for the VIA Unichrome, mostly).
- Change --enable-shared-xv to --disable-static-xv to keep x86_64 working.

* Thu Dec 16 2004 Matthias Saou <http://freshrpms.net/> 1.0.0-0.17.rc8
- Update to 1.0rc8 and remove obsolete memleak patch.
- Add --enable-shared-xv as compilation against static Xv fails on x86_64.

* Fri Dec  3 2004 Matthias Saou <http://freshrpms.net/> 1.0.0-0.17.rc7
- Added xine-lib-1-rc7-memleak.patch, thanks to Bastien Nocera.

* Wed Dec  1 2004 Matthias Saou <http://freshrpms.net/> 1.0.0-0.16.rc7
- Update to 1.0rc7.

* Fri Nov  5 2004 Matthias Saou <http://freshrpms.net/> 1.0.0-0.15.rc6a
- Removed most explicit deps, only libdvdcss is really needed.

* Tue Oct 12 2004 Dag Wieers <dag@wieers.com> - 1.0.0-0.15.rc6a
- Build against newer flac-1.1.1.

* Fri Sep 17 2004 Matthias Saou <http://freshrpms.net/> 1.0.0-0.14.rc6a
- Update to 1.0rc6a.
- Removed wrong "not x86 = 64bit" assumptions and build changes which seem
  properly autodetected now anyway.

* Wed Jun 30 2004 Matthias Saou <http://freshrpms.net/> 1.0.0-0.14.rc5
- Update to 1.0rc5.

* Tue Jun 15 2004 Matthias Saou <http://freshrpms.net/> 1.0.0-0.13.rc4a
- Remove explicit xvidcore dependencies, as they don't exist anymore.

* Wed May 19 2004 Matthias Saou <http://freshrpms.net/> 1.0.0-0.13.rc4a
- Update to 1.0rc4a.
- Remove the plugin stripping since now all goes into the debuginfo package.
- Added libtheora support by default.

* Tue May  4 2004 Matthias Saou <http://freshrpms.net/> 1.0.0-0.12.rc4
- Update to 1.0rc4.

* Thu Apr 15 2004 Matthias Saou <http://freshrpms.net/> 1.0.0-0.11.rc3c
- Update to 1.0rc3c.

* Thu Mar 25 2004 Matthias Saou <http://freshrpms.net/> 1.0.0-0.10.rc3b
- Removed explicit XFree86 dependency.

* Thu Mar 18 2004 Matthias Saou <http://freshrpms.net/> 1.0.0-0.9.rc3b
- Update to 1.0rc3b.

* Tue Feb 24 2004 Matthias Saou <http://freshrpms.net/> 1.0.0-0.8.rc3a
- Rebuild against new libfame.

* Tue Feb 24 2004 Matthias Saou <http://freshrpms.net/> 1.0.0-0.7.rc3a
- Rebuilt to get the debuginfo package.

* Sun Jan  4 2004 Matthias Saou <http://freshrpms.net/> 1.0.0-0.6.rc3a
- Update to 1.0rc3a.

* Thu Dec 18 2003 Matthias Saou <http://freshrpms.net/> 1.0.0-0.5.rc3
- Update to 1.0rc3.

* Tue Dec  2 2003 Matthias Saou <http://freshrpms.net/> 1.0.0-0.4.rc2
- Added an obsoletes tag for libxine.
- Added --with-pic configure option to allow prelinking.
- Added libdvdcss dependency to be sure it gets pulled in.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 1.0.0-0.3.rc2
- Update to 1.0rc2.
- Rebuild for Fedora Core 1.

* Tue Oct 21 2003 Matthias Saou <http://freshrpms.net/>
- Update to 1.0rc1.
- Disable ALSA by default for ppc, as it can't be supported with YDL kernels.

* Thu Aug  7 2003 Matthias Saou <http://freshrpms.net/>
- Update to 1.0rc0a.
- Added speex support.
- Removed all .la files of the plugins, not built by default anymore.

* Mon May 12 2003 Matthias Saou <http://freshrpms.net/>
- Update to 1.0beta12.

* Tue Apr 29 2003 Matthias Saou <http://freshrpms.net/>
- Update to 1.0beta11.

* Wed Apr  9 2003 Matthias Saou <http://freshrpms.net/>
- Update to 1.0beta10.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.
- Exclude .la files.

* Sun Mar 23 2003 Matthias Saou <http://freshrpms.net/>
- Update to 1.0beta9.

* Mon Mar 10 2003 Matthias Saou <http://freshrpms.net/>
- Update to 1.0beta8, no really, I mean it this time.
- Exclude vidix plugins for non x86 archs.

* Sun Mar  9 2003 Matthias Saou <http://freshrpms.net/>
- Update to 1.0beta8.

* Thu Feb 27 2003 Matthias Saou <http://freshrpms.net/>
- Update to 1.0beta6.

* Sat Feb 22 2003 Matthias Saou <http://freshrpms.net/>
- Update to 1.0beta5.

* Tue Feb  4 2003 Matthias Saou <http://freshrpms.net/>
- Rebuild now defaults to use the internal libdvdnav since many people
  reported problems using the external CVS snapshot.

* Thu Jan 30 2003 Matthias Saou <http://freshrpms.net/>
- Update to 1.0beta4 since beta3 had a build bug un mmx cpus.

* Wed Jan 29 2003 Matthias Saou <http://freshrpms.net/>
- Update to 1.0beta3.
- Added flac, libfame, rte and gnomevfs2 build options.

* Sun Jan 12 2003 Matthias Saou <http://freshrpms.net/>
- Repackage the latest 1.0beta2 at last, it's usable now.
- Split pack into xine/xine-lib instead of xine/xine-libs and two source
  packages.

* Sun Oct  6 2002 Matthias Saou <http://freshrpms.net/>
- Removed --without arts from %%description as it can't work if arts-devel
  is installed.
- Added vidix files.
- Delete unpackaged xitk related files.

* Mon Sep 30 2002 Matthias Saou <http://freshrpms.net/>
- Fixed ALSA support.
- Spec file cleanup.
- New --without aalib, lirc and arts options.

* Thu Sep 26 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 8.0.

* Tue Aug 27 2002 Matthias Saou <http://freshrpms.net/>
- Added new .desktop file support.
- Added alsa support.

* Sun Aug  4 2002 Matthias Saou <http://freshrpms.net/>
- Fixed plugins (new API version again).
- Rebuilt without the NVIDIA_GLX package :-/

* Sun Aug  4 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.9.13.
- Updated both d4d and d5d plugins.
- Now use %%find_lang.

* Tue Jun 25 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.9.12.

* Mon Jun 17 2002 Matthias Saou <http://freshrpms.net/>
- Split into xine (UI) and xine-libs to be able to install just the engine
  for other frontends.

* Mon May 27 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.9.10 final.
- Added a quick perl regexp hack for the d4d & d5d API versions.

* Thu May  9 2002 Matthias Saou <http://freshrpms.net/>
- Almost complete spec file rewrite to reflect improvements in the build
  process (simplifications were now possible).
- Updated the d5d plugin to 0.2.4.
- Moved everything from %%install to %%build as it seems more logical.
- Added %%{?_smp_mflags} and LIBRARY_PATH for the lib, thanks Ralf!
- Added the d4d plugin as well.

* Tue Apr 30 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.9.9.

* Wed Jan 16 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.9.8 with new all-in-one d5d css and menu support plugin.
- Cleaned up the docs.

* Tue Dec 11 2001 Matthias Saou <http://freshrpms.net/>
- Update to 0.9.7.

* Thu Nov 29 2001 Matthias Saou <http://freshrpms.net/>
- Update to 0.9.6.

* Sat Nov 24 2001 Matthias Saou <http://freshrpms.net/>
- Update to 0.9.5, added the new LC_MESSAGEs.

* Tue Nov  6 2001 Matthias Saou <http://freshrpms.net/>
- Update to 0.9.4 (0.9.3 had build problems).
- Update d4d plugin to 0.2.7.
- Put the menu navigation plugin back in and update it to 0.9.3beta
  (yeah, Fred, I'm doing that for you ;-)).

* Thu Nov  1 2001 Matthias Saou <http://freshrpms.net/>
- Added the missing xineshot to %files.
- Removed the menu navigation plugin : It's so buggy and not moving very
  fast. If you want menu support, try Ogle, it's worth it!
- Added new man pages translations.
- Cleaned-up the %doc section, lots were added recently.
- Modified the way the target cpu is forced, it should now be possible to
  rebuild for anything else than i686.

* Mon Oct 22 2001 Matthias Saou <http://freshrpms.net/>
- Removed the libdvdcss since it was making xine mutually exclusive with
  videolan... and moved it to a separate package instead.
- Removed the ugly hacks from libtool problems, I guess this spec won't
  be suited for 7.1 anymore.

* Sun Oct 21 2001 Matthias Saou <http://freshrpms.net/>
- Addedd libdvdcss library so that encrypted menus can now be played too.
- Updated lots of dependencies (ogg vorbis, arts, zlib, esd, libpng).

* Tue Oct 16 2001 Matthias Saou <http://freshrpms.net/>
- Update to 0.9.2 with updated CSS plugin and libvdvread.

* Mon Oct  8 2001 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat 7.2 with lirc support.

* Wed Sep 19 2001 Matthias Saou <http://freshrpms.net/>
- Updated the dvdnav plugin to the latest version.

* Tue Sep 18 2001 Matthias Saou <http://freshrpms.net/>
- Update to 0.9.1.
- Update libdvdread to 0.9.1 too :-)

* Fri Sep 14 2001 Matthias Saou <http://freshrpms.net/>
- Update to 0.9.0.
- Spec file cleanup, the configure scripts and the way they use macros
  are still too crappy to clean up more :-(
- Included the new menu plugin and libdvdcss...slurp!

* Thu Sep 13 2001 Matthias Saou <http://freshrpms.net/>
- Update to 0.5.3 and kept d4d plugin 0.2.2 (0.2.4 doesn't compile for me).

* Mon Sep  3 2001 Matthias Saou <http://freshrpms.net/>
- Update to 0.5.2.
- Removed the "aaxine" binary.

* Sat Aug 11 2001 Matthias Saou <http://freshrpms.net/>
- Update to 0.5.1.

* Fri Aug 10 2001 Matthias Saou <http://freshrpms.net/>
- Nothing weird with the package in one whole week, I'll release it :-)

* Mon Aug  6 2001 Matthias Saou <http://freshrpms.net/>
- Update to 0.5.0.
- Merged the new "lib" and "ui" sources in the same SRPM and split the
  binaries in a main and a "devel" package.

* Thu May 17 2001 Matthias Saou <http://freshrpms.net/>
- Update to 0.4.3.

* Thu May 10 2001 Matthias Saou <http://freshrpms.net/>
- Changed the spec file to now use XINE_BUILD to override the default
  build arch and use the compilation optimisations chosen by the xine
  authors in the configure script.
- Doesn't work with --arch=athlon though... I wonder why!

* Mon May  7 2001 Matthias Saou <http://freshrpms.net/>
- Update to 0.4.2.

* Fri Apr 20 2001 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat 7.1.

* Thu Mar  8 2001 Matthias Saou <http://freshrpms.net/>
- Update to 0.4.01.

* Thu Feb 15 2001 Matthias Saou <http://freshrpms.net/>
- Updated the DeCSS plugin to the latest 0.1.2 release.
- Added a menu entry since xine is now stable enough to not need to be
  launched in a terminal anymore.

* Wed Jan 31 2001 Matthias Saou <http://freshrpms.net/>
- Upgraded to 0.3.7 with the subtitles patch to the plugin

* Wed Jan 31 2001 Matthias Saou <http://freshrpms.net/>
- Upgraded to 0.3.6 with the same plugin

* Sat Jan 13 2001 Matthias Saou <http://freshrpms.net/>
- Included the DeCSS dvd plugin for 0.3.5

* Wed Jan 10 2001 Matthias Saou <http://freshrpms.net/>
- upgraded to 0.3.5

* Mon Jan  8 2001 Matthias Saou <http://freshrpms.net/>
- upgraded to 0.3.4
- tweak to configure.in to compile with gcc 2.96

* Tue Jan  2 2001 Matthias Saou <http://freshrpms.net/>
- upgraded to 0.3.3

* Sun Dec 17 2000 Matthias Saou <http://freshrpms.net/>
- upgraded to 0.3.2 "complete" :-)
- fixed my files section to include the new skin

* Mon Nov 20 2000 Matthias Saou <http://freshrpms.net/>
- cleaned-up the spec file for RedHat 7.0
- added stripping, changed prefix, added docs, added defattr

* Fri Oct 17 2000 Daniel Caujolle-Bert <f1rmb@users.sourceforge.net>
- first spec file.

