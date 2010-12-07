# $Id$
# Authority: matthias

%{?el6:%define _without_lirc 1}

%{?el4:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}

%define desktop_vendor rpmforge

Summary: Free multimedia player
Name: xine
Version: 0.99.6
Release: 1%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://www.xine-project.org/

Source0: http://dl.sf.net/xine/xine-ui-%{version}.tar.bz2
Source1: xine.png
Source2: http://www.bluebeamentertainment.com/xine/smokeyglass_splash.png
Source3: http://www.bluebeamentertainment.com/xine/smokeyglass_logo.m1v
Patch0: xine-ui-0.99.6-shared-lirc.patch
Patch1: xine-ui-0.99.6-fix-help-crash.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: aalib-devel
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: curl-devel
BuildRequires: desktop-file-utils
BuildRequires: gcc-c++
BuildRequires: gettext
### Required to overwrite the ugly icons
BuildRequires: ImageMagick
BuildRequires: libidn-devel
BuildRequires: libpng-devel >= 2:1.2.8
BuildRequires: libtermcap-devel
BuildRequires: libtool
BuildRequires: pkgconfig
BuildRequires: readline-devel
BuildRequires: xine-lib-devel >= 1.0.0
BuildRequires: /usr/bin/find
%{!?_with_moles:Requires: xine-lib >= 1.1.2}
%{?_with_moles:Requires: xine-lib-moles >= 1.1.2}
%{!?_without_modxorg:BuildRequires: libXt-devel, libXv-devel, libXinerama-devel, libXtst-devel, libXxf86vm-devel, libXext-devel, libXft-devel}
%{?_without_modxorg:BuildRequires: XFree86-devel}
%{!?_without_caca:BuildRequires: libcaca-devel}
%{!?_without_lirc:BuildRequires: lirc-devel}
%{!?_with_moles:Requires: xine-lib >= 1.1.2}
%{?_with_moles:Requires: xine-lib-moles >= 1.1.2}

%description
Xine is a free multimedia player. It plays back CDs, DVDs, and VCDs. It also
decodes multimedia files like AVI, MOV, WMV, and MP3 from local disk drives,
and displays multimedia streamed over the Internet. It interprets many of the
most common multimedia formats available - and some of the most uncommon
formats, too.

This package contains the GUI of the Xine multimedia player.

Available rpmbuild rebuild options :
--without : caca lirc freedesktop


%prep
%setup -n xine-ui-%{version}
%{!?_without_lirc:%patch0 -p1 -b .shared-lirc}
%patch1 -p0 -b .help

# Required by the shared-lirc patch
./autogen.sh

# Replace the default splash screen
%{__cp} -a -f %{SOURCE2} misc/xine_splash.png
# Replace the default window content with one matching the splash screen
%{__cp} -a -f %{SOURCE3} misc/xine-ui_logo.mpv

%{__cat} <<EOF >xine.desktop
[Desktop Entry]
Name=Xine
Comment=Versatile Multimedia Player
Exec=xine %U
MimeType=video/mpeg;video/quicktime;video/x-msvideo;audio/x-mp3;audio/x-mp2;audio/x-mpegurl
Icon=xine.png
Terminal=false
Type=Application
Encoding=UTF-8
Categories=Application;AudioVideo;
EOF

%{__cat} <<EOF >xine.applications
xine
    command=xine
    name=Xine
    can_open_multiple_files=true
    expects_uris=yes
    requires_terminal=false
    all_gnome_vfs_schemes_supported=yes
    uses_gnomevfs=true
    startup_notify=false
    supported_uri_schemes=rtp,mms,net,rtsp,pnm
    mime_types=video/mpeg,video/msvideo,video/quicktime,video/x-avi,video/x-ms-asf,video/x-ms-wmv,video/x-msvideo,application/x-ogg,application/ogg,audio/x-mp3,audio/x-mpeg,video/x-mpeg,video/x-fli,audio/x-wav,audio/x-mpegurl,audio/x-scpls,audio/x-ms-asx,application/vnd.rn-realmedia,audio/x-real-audio,audio/x-pn-realaudio,application/x-flac,audio/x-flac,application/x-shockwave-flash,audio/mpeg,audio/x-ms-asf,audio/x-m4a,audio/x-ms-wax,video/dv,video/x-anim,video/x-flc,misc/ultravox,application/x-matroska,audio/vnd.rn-realaudio,audio/x-pn-aiff,audio/x-pn-au,audio/x-pn-wav,audio/x-pn-windows-acm,image/vnd.rn-realpix,video/vnd.rn-realvideo
EOF

# Replace all of the ugly icons with ours
for size in 16 22 32 48; do
    convert -scale ${size}x${size} %{SOURCE1} \
        misc/desktops/icons/${size}/xine.png
done

# Convert all man pages to UTF-8
for manpage in doc/man/*/*.1*; do
    iconv -f iso8859-1 -t utf8 -o manpage.tmp ${manpage}
    %{__mv} -f manpage.tmp ${manpage}
done


%build

%configure \
    --x-libraries="%{_prefix}/X11R6/%{_lib}" \
    --with-aalib \
%{?_without_lirc:--disable-lirc} \
%{?_without_caca:--without-caca}

%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot} _doc
%{__make} install DESTDIR=%{buildroot}
%find_lang xine-ui

%{__install} -D -m 0644 xine.applications \
    %{buildroot}%{_datadir}/application-registry/xine.applications

# Replace (ugly) default icon with a nice one
%{__rm} -f %{buildroot}%{_datadir}/pixmaps/xine.xpm
%{__install} -p -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/

# Remove unpackaged files
find %{buildroot} -name 'xitk*' | xargs rm -rf || :

# Move the docs back into place
%{__mv} %{buildroot}%{_docdir}/xine-ui _doc

# Remove aaxine man pages, since we don't include it anymore
find %{buildroot} -name 'aaxine.1*' | xargs rm -f || :

%{__mkdir_p} %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor %{desktop_vendor} \
    --dir %{buildroot}%{_datadir}/applications  \
    xine.desktop

%clean
%{__rm} -rf %{buildroot}

%post
update-desktop-database %{_datadir}/applications &>/dev/null || :

%postun
update-desktop-database %{_datadir}/applications &>/dev/null || :

%files -f xine-ui.lang
%defattr(-, root, root, 0755)
%doc _doc/*
%doc %{_mandir}/man1/*.1*
%doc %lang(de)%{_mandir}/de/man1/*.1*
%doc %lang(es)%{_mandir}/es/man1/*.1*
%doc %lang(fr)%{_mandir}/fr/man1/*.1*
%doc %lang(pl)%{_mandir}/pl/man1/*.1*
%{!?_without_caca:%{_bindir}/cacaxine}
%{_bindir}/aaxine
%{_bindir}/fbxine
%{_bindir}/xine
%{_bindir}/xine-bugreport
%{_bindir}/xine-check
%{_bindir}/xine-remote
%{_datadir}/application-registry/xine.applications
%{_datadir}/applications/%{desktop_vendor}-xine.desktop
%{_datadir}/icons/hicolor/*/apps/xine.png
%{_datadir}/mime/packages/xine-ui.xml
%{_datadir}/pixmaps/xine.png
%{_datadir}/xine/

%changelog
* Mon Jun 14 2010 Yury V. Zaytsev <yury@shurup.com> - 0.99.6-1
- Rebuild against aalib.
- Rebuild against latest libcaca.
- Updated to xine 0.99.6.

* Fri May  4 2007 Matthias Saou <http://freshrpms.net/> 0.99.5-1
- Update to 0.99.5.
- Remove no longer needed patches.
- Remove aaxine and its man pages, no longer built and cacaxine is nicer.
- Include new hicolor icons, but create them from our own icon.
- Convert man pages to UTF-8.

* Mon Dec 18 2006 Matthias Saou <http://freshrpms.net/> 0.99.4-8
- Change name of requirement from xine-lib-extras to xine-lib-moles.

* Wed Nov  8 2006 Matthias Saou <http://freshrpms.net/> 0.99.4-7
- Require xine-lib-extras on FC5 too.

* Thu Nov  2 2006 Matthias Saou <http://freshrpms.net/> 0.99.4-6
- Require xine-lib-extras on FC6 in order to get the spash animation to work.

* Mon May 22 2006 Matthias Saou <http://freshrpms.net/> 0.99.4-5
- Replace old lirc workaround with patch from Ville to use the shared library,
  since the static library has been removed from the Extras lirc packages.

* Wed Mar 22 2006 Matthias Saou <http://freshrpms.net/> 0.99.4-4
- Make the aaxine and cacaxine %%files entries conditional too (thanks to
  John Robinson for spotting this).

* Mon Mar  6 2006 Matthias Saou <http://freshrpms.net/> 0.99.4-4
- Remove setting of the X libs location, as it breaks with modular X.

* Mon Jan 30 2006 Matthias Saou <http://freshrpms.net/> 0.99.4-3
- Fix modular xorg requirements since the "xine" binary wasn't being built.
- List all bindir entries in %%files so that the above makes the build fail.

* Fri Jan 13 2006 Matthias Saou <http://freshrpms.net/> 0.99.4-2
- Add modular xorg build conditional.

* Sat Jul 30 2005 Matthias Saou <http://freshrpms.net/> 0.99.4-1
- Update to 0.99.4, which includes gcc4 fixes.

* Wed Jul 13 2005 Matthias Saou <http://freshrpms.net/> 0.99.3-6
- More patches from Alex Stewart : sprintf, xftfontsize and uifixups. These
  should fix many bugs, including broken dialog boxes and broken menus.

* Tue Jul  5 2005 Matthias Saou <http://freshrpms.net/> 0.99.3-5
- Add menucrash patch from Alex Stewart, at last! :-) (for x86_64)

* Fri Apr 29 2005 Matthias Saou <http://freshrpms.net/> 0.99.3-4
- Replace Christmas splash screen with another one.
- Add gcc4 patch.
- Replace default icons with a nicer home made one.

* Tue Apr  5 2005 Matthias Saou <http://freshrpms.net/> 0.99.3-3
- Fix Exec line in desktop file to get drag and drop to work properly (%%U).

* Fri Jan  7 2005 Matthias Saou <http://freshrpms.net/> 0.99.3-2
- Add a quick lib vs. lib64 replace for lirc static lib detection to work on
  x86_64.

* Mon Jan  3 2005 Matthias Saou <http://freshrpms.net/> 0.99.3-1
- Update to 0.99.3.
- Re-enable lirc on x86_64, don't even know why it was disabled.
- Added readline dep for the network interface.
- Added new caca support.
- Added libidn-devel build dep to fix libcurl support.

* Sat Oct 16 2004 Matthias Saou <http://freshrpms.net/> 0.99.2-1
- Added update-desktop-database scriplet calls.

* Sun Aug 01 2004 Dag Wieers <dag@wieers.com> - 0.99.2-1
- Added xine.applications to application-registry.

* Mon Jul 05 2004 Dag Wieers <dag@wieers.com>> - 0.99.2-1
- Added an improved desktop file.
- Updated to release 0.99.2

* Wed May  5 2004 Matthias Saou <http://freshrpms.net/> 0.99.1-1
- Update to 0.99.1.
- Have curl enabled by default, if it's too old, it'll be disabled anyway.

* Sun Jan  4 2004 Matthias Saou <http://freshrpms.net/> 0.9.23-1
- Update to 0.9.23.

* Tue Dec  9 2003 Matthias Saou <http://freshrpms.net/> 0.9.22-3
- Fix a typo that made the package require curl-devel.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 0.9.22-2
- Rebuild for Fedora Core 1.

* Fri Aug  8 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.9.22.

* Tue May 20 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.9.21.
- Removed explicit aaxine from %%files to avoid listing twice.
- Removed some obsolete xitk stuff.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.

* Wed Mar 26 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.9.20.

* Sat Mar 15 2003 Matthias Saou <http://freshrpms.net/>
- Added freedesktop build option.

* Mon Mar 10 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.9.19.

* Mon Feb  3 2003 Matthias Saou <http://freshrpms.net/>
- Rebuild to hopefully fix an unexplained problem.
- Fixed the aalib-devel build dependency.

* Fri Jan 31 2003 Matthias Saou <http://freshrpms.net/>
- Update to ui 0.9.18.
- Removed binary lirc dependency as it's statically linked.
- Modified man pages list to tag languages (no more aaxine exception though).

* Sun Jan 12 2003 Matthias Saou <http://freshrpms.net/>
- Update to ui 0.9.17.
- This main xine package now only contains the ui source, thus needs the
  now separate xine-lib.

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
- Added the missing xineshot to %%files.
- Removed the menu navigation plugin : It's so buggy and not moving very
  fast. If you want menu support, try Ogle, it's worth it!
- Added new man pages translations.
- Cleaned-up the %%doc section, lots were added recently.
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

