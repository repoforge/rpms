# Authority: freshrpms
#$Id: xine-lib.spec,v 1.1 2004/02/25 00:07:30 dag- Exp $

%define libname libxine1
%define libver  1-rc0a
%define apiver  1.0.0

%define __libtoolize :

Summary: Core library for the xine video player.
Name: xine-lib
Version: %{apiver}
Release: 0.1.rc0a
License: GPL
Group: Applications/Multimedia
URL: http://xinehq.de/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://prdownloads.sourceforge.net/xine/%{name}-%{libver}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

Requires: zlib, libvorbis, SDL, glut, libmng
%{?_with_rte:Requires: rte}
%{?_with_ext-dvdnav:Requires: libdvdnav >= 0.1.4}
%{?_with_alsa:Requires: alsa-lib}
%{!?_without_esound:Requires: esound}
%{!?_without_aalib:Requires: aalib}
%{!?_without_libfame:Requires: libfame}
%{!?_without_flac:Requires: flac}
%{!?_without_arts:Requires: arts}
%{!?_without_gnomevfs2:Requires: gnome-vfs2}
%{!?_without_xvid:Requires: xvidcore}
%{!?_without_speex:Requires: speex}
BuildRequires: pkgconfig, XFree86-devel, zlib-devel
BuildRequires: libvorbis-devel, SDL-devel, glut-devel, libmng-devel
%{?_with_rte:BuildRequires: rte-devel}
%{?_with_ext-dvdnav:BuildRequires: libdvdnav-devel >= 0.1.4}
%{?_with_alsa:BuildRequires: alsa-lib-devel}
%{!?_without_esound:BuildRequires: esound-devel}
%{!?_without_aalib:BuildRequires: aalib-devel}
%{!?_without_libfame:BuildRequires: libfame-devel}
%{!?_without_flac:BuildRequires: flac-devel}
%{!?_without_arts:BuildRequires: arts-devel}
%{!?_without_gnomevfs2:BuildRequires: gnome-vfs2-devel}
%{!?_without_xvid:BuildRequires: xvidcore-devel}
%{!?_without_speex:BuildRequires: speex-devel}
Obsoletes: xine-libs <= 1.0.0

%description
Xine is a free multimedia player. It plays back CDs, DVDs, and VCDs. It also
decodes multimedia files like AVI, MOV, WMV, and MP3 from local disk drives,
and displays multimedia streamed over the Internet. It interprets many of the
most common multimedia formats available - and some of the most uncommon
formats, too.

This package contains the backend files for the Xine multimedia player.

Available rpmbuild rebuild options :
--with : rte ext-dvdnav
--without : alsa aalib libfame flac esound arts gnomevfs2 xvid speex
(only alsa can be really disabled, others only remove explicit package
 dependency which won't make much difference if devel files are found)


%package devel
Summary: Development files for the xine library.
Group: Development/Libraries
Requires: %{name} = %{version}
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
%setup -q -n %{name}-%{libver}

%build
%configure \
    %{!?_with_alsa:--disable-alsa} \
   %{!?_with_ext-dvdnav:--with-included-dvdnav}
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
%find_lang %{libname}

# Strip all those libs!
strip \
    %{buildroot}%{_libdir}/*.so* \
    %{buildroot}%{_libdir}/xine/plugins/%{apiver}/*.so \
    || :

# Remove all those unused docs
rm -rf %{buildroot}%{_docdir}/xine || :

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%clean
rm -rf %{buildroot}

%files -f %{libname}.lang
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%{_libdir}/*.so.*
%{_libdir}/xine
%{_datadir}/xine

%files devel
%defattr(-, root, root)
%doc doc/hackersguide/*.sgml
%{_bindir}/*
%{_includedir}/*
%exclude %{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_datadir}/aclocal/*
%{_mandir}/man1/*

%changelog
* Sun Aug 31 2003 Dag Wieers <dag@wieers.com> - 1.0-0.1.rc0a
- Taken from Matthias Saou (FreshRPMS) for compatibility.

* Thu Aug  7 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 1.0rc0a.
- Added speex support.
- Removed all .la files of the plugins, not built by default anymore.

* Mon May 12 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 1.0beta12.

* Tue Apr 29 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 1.0beta11.

* Wed Apr  9 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 1.0beta10.

* Mon Mar 31 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Rebuilt for Red Hat Linux 9.
- Exclude .la files.

* Sun Mar 23 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 1.0beta9.

* Mon Mar 10 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 1.0beta8, no really, I mean it this time.
- Exclude vidix plugins for non x86 archs.

* Sun Mar  9 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 1.0beta8.

* Thu Feb 27 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 1.0beta6.

* Sat Feb 22 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 1.0beta5.

* Tue Feb  4 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Rebuild now defaults to use the internal libdvdnav since many people
  reported problems using the external CVS snapshot.

* Thu Jan 30 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 1.0beta4 since beta3 had a build bug un mmx cpus.

* Wed Jan 29 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 1.0beta3.
- Added flac, libfame, rte and gnomevfs2 build options.

* Sun Jan 12 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Repackage the latest 1.0beta2 at last, it's usable now.
- Split pack into xine/xine-lib instead of xine/xine-libs and two source
  packages.

* Sun Oct  6 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Removed --without arts from %%description as it can't work if arts-devel
  is installed.
- Added vidix files.
- Delete unpackaged xitk related files.

* Mon Sep 30 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Fixed ALSA support.
- Spec file cleanup.
- New --without aalib, lirc and arts options.

* Thu Sep 26 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Rebuilt for Red Hat Linux 8.0.

* Tue Aug 27 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Added new .desktop file support.
- Added alsa support.

* Sun Aug  4 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Fixed plugins (new API version again).
- Rebuilt without the NVIDIA_GLX package :-/

* Sun Aug  4 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 0.9.13.
- Updated both d4d and d5d plugins.
- Now use %%find_lang.

* Tue Jun 25 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 0.9.12.

* Mon Jun 17 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Split into xine (UI) and xine-libs to be able to install just the engine
  for other frontends.

* Mon May 27 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 0.9.10 final.
- Added a quick perl regexp hack for the d4d & d5d API versions.

* Thu May  9 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Almost complete spec file rewrite to reflect improvements in the build
  process (simplifications were now possible).
- Updated the d5d plugin to 0.2.4.
- Moved everything from %%install to %%build as it seems more logical.
- Added %%{?_smp_mflags} and LIBRARY_PATH for the lib, thanks Ralf!
- Added the d4d plugin as well.

* Tue Apr 30 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 0.9.9.

* Wed Jan 16 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 0.9.8 with new all-in-one d5d css and menu support plugin.
- Cleaned up the docs.

* Tue Dec 11 2001 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 0.9.7.

* Thu Nov 29 2001 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 0.9.6.

* Sat Nov 24 2001 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 0.9.5, added the new LC_MESSAGEs.

* Tue Nov  6 2001 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 0.9.4 (0.9.3 had build problems).
- Update d4d plugin to 0.2.7.
- Put the menu navigation plugin back in and update it to 0.9.3beta
  (yeah, Fred, I'm doing that for you ;-)).

* Thu Nov  1 2001 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Added the missing xineshot to %files.
- Removed the menu navigation plugin : It's so buggy and not moving very
  fast. If you want menu support, try Ogle, it's worth it!
- Added new man pages translations.
- Cleaned-up the %doc section, lots were added recently.
- Modified the way the target cpu is forced, it should now be possible to
  rebuild for anything else than i686.

* Mon Oct 22 2001 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Removed the libdvdcss since it was making xine mutually exclusive with
  videolan... and moved it to a separate package instead.
- Removed the ugly hacks from libtool problems, I guess this spec won't
  be suited for 7.1 anymore.

* Sun Oct 21 2001 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Addedd libdvdcss library so that encrypted menus can now be played too.
- Updated lots of dependencies (ogg vorbis, arts, zlib, esd, libpng).

* Tue Oct 16 2001 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 0.9.2 with updated CSS plugin and libvdvread.

* Mon Oct  8 2001 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Rebuilt for Red Hat 7.2 with lirc support.

* Wed Sep 19 2001 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Updated the dvdnav plugin to the latest version.

* Tue Sep 18 2001 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 0.9.1.
- Update libdvdread to 0.9.1 too :-)

* Fri Sep 14 2001 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 0.9.0.
- Spec file cleanup, the configure scripts and the way they use macros
  are still too crappy to clean up more :-(
- Included the new menu plugin and libdvdcss...slurp!

* Thu Sep 13 2001 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 0.5.3 and kept d4d plugin 0.2.2 (0.2.4 doesn't compile for me).

* Mon Sep  3 2001 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 0.5.2.
- Removed the "aaxine" binary.

* Sat Aug 11 2001 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 0.5.1.

* Fri Aug 10 2001 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Nothing weird with the package in one whole week, I'll release it :-)

* Mon Aug  6 2001 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 0.5.0.
- Merged the new "lib" and "ui" sources in the same SRPM and split the
  binaries in a main and a "devel" package.

* Thu May 17 2001 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 0.4.3.

* Thu May 10 2001 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Changed the spec file to now use XINE_BUILD to override the default
  build arch and use the compilation optimisations chosen by the xine
  authors in the configure script.
- Doesn't work with --arch=athlon though... I wonder why!

* Mon May  7 2001 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 0.4.2.

* Fri Apr 20 2001 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Rebuilt for Red Hat 7.1.

* Thu Mar  8 2001 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 0.4.01.

* Thu Feb 15 2001 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Updated the DeCSS plugin to the latest 0.1.2 release.
- Added a menu entry since xine is now stable enough to not need to be
  launched in a terminal anymore.

* Wed Jan 31 2001 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Upgraded to 0.3.7 with the subtitles patch to the plugin

* Wed Jan 31 2001 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Upgraded to 0.3.6 with the same plugin

* Sat Jan 13 2001 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Included the DeCSS dvd plugin for 0.3.5

* Wed Jan 10 2001 Matthias Saou <matthias.saou@est.une.marmotte.net>
- upgraded to 0.3.5

* Mon Jan  8 2001 Matthias Saou <matthias.saou@est.une.marmotte.net>
- upgraded to 0.3.4
- tweak to configure.in to compile with gcc 2.96

* Tue Jan  2 2001 Matthias Saou <matthias.saou@est.une.marmotte.net>
- upgraded to 0.3.3

* Sun Dec 17 2000 Matthias Saou <matthias.saou@est.une.marmotte.net>
- upgraded to 0.3.2 "complete" :-)
- fixed my files section to include the new skin

* Mon Nov 20 2000 Matthias Saou <matthias.saou@est.une.marmotte.net>
- cleaned-up the spec file for RedHat 7.0
- added stripping, changed prefix, added docs, added defattr

* Fri Oct 17 2000 Daniel Caujolle-Bert <f1rmb@users.sourceforge.net>
- first spec file.

