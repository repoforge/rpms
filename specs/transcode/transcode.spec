# $Id$
# Authority: matthias

Summary: Linux video stream processing utility
Name: transcode
Version: 0.6.12
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://zebra.fh-weingarten.de/~transcode/
Source: http://zebra.fh-weingarten.de/~transcode/pre/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
%{?_with_avifile6:Requires: avifile >= 0.6.0}
%{!?_without_text:Requires: freetype >= 2.0}
%{!?_without_lame:Requires: lame >= 3.89}
%{!?_without_ogg:Requires: libogg}
%{!?_without_vorbis:Requires: libvorbis}
%{!?_without_dvdread:Requires: libdvdread}
%{!?_without_xvidcore:Requires: xvidcore}
#{!?_without_postproc:Requires: libpostproc}
%{!?_without_quicktime:Requires: libquicktime}
%{!?_without_dv:Requires: libdv}
%{!?_without_lzo:Requires: lzo >= 1.08}
%{!?_without_libfame:Requires: libfame}
%{!?_without_magick:Requires: ImageMagick >= 5.4.3, bzip2-devel}
%{!?_without_mjpeg:Requires: mjpegtools}
Requires: SDL, libxml2, libjpeg
%{?_with_avifile6:BuildRequires: avifile-devel >= 0.6.0}
%{!?_without_text:BuildRequires: freetype-devel >= 2.0}
%{!?_without_lame:BuildRequires: lame-devel >= 3.89}
%{!?_without_ogg:BuildRequires: libogg-devel}
%{!?_without_vorbis:BuildRequires: libvorbis-devel}
%{!?_without_dvdread:BuildRequires: libdvdread-devel}
%{!?_without_xvidcore:BuildRequires: xvidcore-devel}
#{!?_without_postproc:BuildRequires: libpostproc}
%{!?_without_quicktime:BuildRequires: libquicktime-devel}
%{!?_without_dv:BuildRequires: libdv-devel}
%{!?_without_lzo:BuildRequires: lzo-devel >= 1.08}
%{!?_without_a52:BuildRequires: a52dec-devel >= 0.7.3}
%{!?_without_libfame:BuildRequires: libfame-devel}
%{!?_without_magick:BuildRequires: ImageMagick-devel >= 5.4.3, bzip2}
%{!?_without_mjpeg:BuildRequires: mjpegtools-devel}
BuildRequires: gcc-c++, glib-devel
BuildRequires: SDL-devel, libxml2-devel, libjpeg-devel
%ifarch %{ix86}
BuildRequires: nasm
%endif

%description
Transcode is a linux text-console utility for video stream processing.
Decoding and encoding is done by loading modules that are responsible for
feeding transcode with raw video/audio streams (import modules) and
encoding the frames (export modules). It supports elementary video and
audio frame transformations, including de-interlacing or fast resizing of
video frames and loading of external filters.

Please see the included README file for more.

Available rpmbuild rebuild options :
--with : avifile6
--without : text lame ogg vorbis dvdread xvidcore postproc quicktime dv lzo
            a52 libfame magick mjpeg

%prep
%setup

%build
%configure \
    %{!?_with_avifile6:--with-avifile-mods=no} \
    %{!?_without_lzo:--enable-text} \
    %{?_without_lzo:--with-lzo=no} \
    %{?_without_magick:--without-magick-mods} \
    %{?_without_lame:--without-lame} \
    %{?_without_ogg:--without-ogg} \
    %{?_without_vorbis:--without-vorbis} \
    %{?_without_dvdread:--without-dvdread} \
    %{?_without_xvidcore:--without-xvidcore} \
    %{!?_without_quicktime:--with-qt} \
    %{?_without_dv:--without-dv} \
    %{?_without_a52:--without-a52} \
    %{?_without_libfame:--without-libfame}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
mv %{buildroot}%{_docdir}/transcode installed-docs
strip %{buildroot}%{_libdir}/transcode/*.so

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING README TODO installed-docs/*
%{_bindir}/*
%{_libdir}/transcode
%exclude %{_libdir}/transcode/*.la
%{_mandir}/man1/*

%changelog
* Sat Jan 10 2004 Matthias Saou <http://freshrpms.net/> 0.6.12-1.fr
- Update to 0.6.12.

* Mon Nov 10 2003 Matthias Saou <http://freshrpms.net/> 0.6.11-1.fr
- Rebuild for Fedora Core 1.
- Update to 0.6.11.
- Remove ffmpeg, looks like a snapshot is included now.
- libpostproc is currently broken, "undefined reference to 'fast_memcpy'" :-(

* Tue Sep  9 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.6.10.

* Sun Aug 24 2003 Matthias Saou <http://freshrpms.net/>
- Added bzip2-devel ImageMagick dependency.

* Fri Aug  8 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.6.9.

* Tue Jul  8 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.6.8.

* Thu Jul  3 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.6.7.
- Removed obsolete lame patch.

* Fri May 23 2003 Matthias Saou <http://freshrpms.net/>
- Added aud_aux-lame-enoding-error-1.patch to fix lame encoding problems.

* Wed May 21 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.6.6.
- Removed the snapshot macro stuff, as future releases won't need it.
- Added "--without text" option for the new freetype2 support.

* Sat May 10 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.6.5.20030510.

* Fri May  2 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.6.4 final.

* Wed Apr  9 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.6.4.20030409.
- Change mplayer dep to libpostproc.
- Re-enabled ImageMagick support by default, as it's fixed in RHL9.
- Removed obsoleted ffmpeg & xvid fix.
- Added libquicktime support and explicit xvidcore.
- Enable lzo by default.

* Sat Apr  5 2003 Matthias Saou <http://freshrpms.net/>
- Exclude .la files.
- Added fix for xvid and ffmpeg export modules, thanks to Dag Wieers.
- Strip all libs by default.
- Add ffmpeg requirement.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.

* Tue Mar 25 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.6.4.20030325 in order to fix ppc build.

* Tue Feb 18 2003 Matthias Saou <http://freshrpms.net/>
- Added lzo support, thanks to José Romildo Malaquias.

* Sun Feb 16 2003 Matthias Saou <http://freshrpms.net/>
- Rebuild against new libdvdread.

* Fri Jan 31 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.6.3 final.

* Tue Jan 28 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.6.3.20030123 snapshot.

* Sat Jan 11 2003 Matthias Saou <http://freshrpms.net/>
- Fix the avifile dependency (disabled by default).

* Tue Dec 24 2002 Matthias Saou <http://freshrpms.net/>
- Added mjpegtools.

* Mon Dec  9 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.6.2 final.

* Sun Nov 17 2002 Matthias Saou <http://freshrpms.net/>
- Updated to latest snapshot, 20021114.
- Rebuilt to use mplayer's libpostproc.
- Added libfame support.

* Sun Oct  6 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 8.0.
- Added --with and --without build options.

* Mon Sep 23 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.6.1.

* Mon Aug 19 2002 Matthias Saou <http://freshrpms.net/>
- Added nasm dependency.

* Fri Aug  2 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.6.0 final!

* Thu Aug  1 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.6.0rc4... doesn't compile :-(
- Added libdv, libogg and libvorbis dependencies.

* Fri Jun 14 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.6.0rc1.
- Spec file updates and fixes.

* Mon Dec 24 2001 Matthias Saou <http://freshrpms.net/>
- Update to 0.5.3.

* Sun Dec  2 2001 Matthias Saou <http://freshrpms.net/>
- Update to 0.5.1.

* Sun Nov 25 2001 Matthias Saou <http://freshrpms.net/>
- Major spec file cleanup.

* Wed Jul 11 2001 Thomas Östreich
- update to transcode v0.3.3
- small changes suggested by VM

* Tue Jul 10 2001 Thomas Östreich
- update to transcode v0.3.2
- added pkgdir in install section

* Tue Jul 10 2001 Volker Moell <moell@gmx.de>
- Wrote this specfile; first build

