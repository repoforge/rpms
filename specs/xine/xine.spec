#$Id: xine.spec,v 1.1 2004/02/26 17:54:31 thias Exp $

%define desktop_vendor freshrpms

Summary: A free multimedia player
Name: xine
Version: 0.9.23
Release: 1.fr
License: GPL
Group: Applications/Multimedia
URL: http://xinehq.de/
Source: http://dl.sf.net/xine/xine-ui-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: xine-lib >= 1.0.0
%{!?_without_curl:Requires: curl >= 7.10.2}
BuildRequires: XFree86-devel, libpng-devel, xine-lib-devel >= 1.0.0
BuildRequires: libtermcap-devel, pkgconfig
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}
%{!?_without_curl:BuildRequires: curl-devel >= 7.10.2}
%{!?_without_aalib:BuildRequires: aalib-devel}
%{!?_without_lirc:BuildRequires: lirc}

%description
Xine is a free multimedia player. It plays back CDs, DVDs, and VCDs. It also
decodes multimedia files like AVI, MOV, WMV, and MP3 from local disk drives,
and displays multimedia streamed over the Internet. It interprets many of the
most common multimedia formats available - and some of the most uncommon
formats, too.
                                                                                
This package contains the GUI of the Xine multimedia player.

Available rpmbuild rebuild options :
--without : curl aalib lirc freedesktop

%prep
%setup -q -n xine-ui-%{version}

%build
%configure %{?_without_lirc:--disable-lirc}
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
%find_lang xine-ui

# Remove unpackaged files
find %{buildroot} -name "xitk*" | xargs rm -rf || :

# Move the docs back into place
mv %{buildroot}%{_docdir}/xine-ui xine-ui-doc

%if %{!?_without_freedesktop:1}%{?_without_freedesktop:0}
# Convert the menu entry
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install --vendor %{desktop_vendor} \
    --dir %{buildroot}%{_datadir}/applications  \
    --add-category X-Red-Hat-Base               \
    --add-category Application                  \
    --add-category AudioVideo                   \
    misc/desktops/xine.desktop
%else
install -D -m644 misc/desktops/xine.desktop \
    %{buildroot}/etc/X11/applnk/Multimedia/%{name}.desktop
%endif

%clean
rm -rf %{buildroot}

%files -f xine-ui.lang
%defattr(-, root, root)
%doc xine-ui-doc/*
#{!?_without_aalib:%{_bindir}/aaxine}
%{_bindir}/*
%{_datadir}/pixmaps/*
%{_datadir}/%{name}
%{!?_without_freedesktop:%{_datadir}/applications/%{desktop_vendor}-%{name}.desktop}
%{?_without_freedesktop:/etc/X11/applnk/Multimedia/%{name}.desktop}
%{_mandir}/man1/*
%lang(de)%{_mandir}/de/man1/*
%lang(es)%{_mandir}/es/man1/*
%lang(fr)%{_mandir}/fr/man1/*
%lang(pl)%{_mandir}/pl/man1/*

%changelog
* Sun Jan  4 2004 Matthias Saou <http://freshrpms.net/> 0.9.23-1.fr
- Update to 0.9.23.

* Tue Dec  9 2003 Matthias Saou <http://freshrpms.net/> 0.9.22-3.fr
- Fix a typo that made the package require curl-devel.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 0.9.22-2.fr
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

