# $Id$
# Authority: matthias
# Upstream: Thomas Östreich <ostreich$theorie,physik,uni-goettingen,de>
# Upstream: Tilmann Bitterberg <transcode$tibit,org>

%define prever pre1

%{?dist: %{expand: %%define %dist 1}}

%{?fc3:%define _without_mjpeg 1}

%{?fc1:%define _without_theora 1}

%{?el3:%define _without_theora 1}

%{?rh9:%define _without_theora 1}

%{?rh8:%define _without_theora 1}
%{?rh8:%define _without_magick 1}

%{?rh7:%define _without_theora 1}

%{?el2:%define _without_theora 1}

%{?rh6:%define _without_theora 1}

Summary: Linux video stream processing utility
Name: transcode
Version: 0.6.14
Release: %{?prever:0.%{prever}.}0
License: GPL
Group: Applications/Multimedia
URL: http://www.transcoding.org/
Source: http://www.jakemsr.com/transcode-%{version}%{?prever}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc-c++, gtk+-devel, SDL-devel, libxml2-devel, libjpeg-devel
BuildRequires: freetype-devel >= 2.0, libogg-devel, libvorbis-devel
BuildRequires: libdv-devel, bzip2-devel, ed, lzo-devel
# Seems like ImageMagick-devel should require this! (FC2 and higher)
BuildRequires: libexif-devel
%{!?_without_lame:BuildRequires: lame-devel >= 3.89}
%{!?_without_theora:BuildRequires: libtheora-devel}
%{!?_without_dvdread:BuildRequires: libdvdread-devel}
%{!?_without_quicktime:BuildRequires: libquicktime-devel}
%{!?_without_a52:BuildRequires: a52dec-devel >= 0.7.3}
%{!?_without_mpeg3:BuildRequires: libmpeg3}
%{!?_without_mjpeg:BuildRequires: mjpegtools-devel}
%{!?_without_libfame:BuildRequires: libfame-devel}
%{!?_without_magick:BuildRequires: ImageMagick-devel >= 5.4.3}
# Non configure options
%{!?_without_nasm:BuildRequires: nasm}
%{!?_without_postproc:BuildRequires: libpostproc}
%{!?_without_ffmpeg:BuildRequires: ffmpeg-devel}
%{!?_without_xvidcore:BuildRequires: xvidcore-devel}
Conflicts: perl-Video-DVDRip < 0.51.2

%description
Transcode is a linux text-console utility for video stream processing.
Decoding and encoding is done by loading modules that are responsible for
feeding transcode with raw video/audio streams (import modules) and
encoding the frames (export modules). It supports elementary video and
audio frame transformations, including de-interlacing or fast resizing of
video frames and loading of external filters.

Please see the included README file for more.

Available rpmbuild rebuild options :
--without : lame theora dvdread quicktime a52 mpeg3 mjpeg libfame magick
            nasm postproc ffmpeg xvidcore


%prep
%setup -n %{name}-%{version}%{?prever}

### FIXME: Use standard autotools directories (Fix upstream please)
#{__perl} -pi.orig -e 's|${prefix}/lib|%{_libdir}|g' configure


%build
%configure \
    --enable-netstream \
    --enable-v4l \
    %{?_without_lame:--disable-lame} \
    --enable-ogg \
    --enable-vorbis \
    %{!?_without_theora:--enable-theora} \
    %{?_without_dvdread:--disable-dvdread} \
    --enable-libdv \
    %{!?_without_quicktime:--enable-libquicktime} \
    --enable-lzo \
    %{!?_without_a52:--enable-a52} \
    %{!?_without_mpeg3:--enable-libmpeg3} \
    --enable-libxml2 \
    %{!?_without_mjpeg:--enable-mjpegtools} \
    --enable-sdl \
    --enable-gtk \
    %{!?_without_libfame:--enable-libfame} \
    %{!?_without_magick:--enable-imagemagick} \
    %{!?_without_ffmpeg:--enable-ffbin}
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot} _docs
%makeinstall \
    docsdir="../_docs/"


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING README TODO _docs/*
%{_bindir}/*
%{_libdir}/transcode/
%exclude %{_libdir}/transcode/*.la
%{_mandir}/man?/*


%changelog
* Thu Nov 11 2004 Matthias Saou <http://freshrpms.net/> 0.6.14-0.pre1.0
- Update to 0.6.14pre1.

* Fri Oct 29 2004 Matthias Saou <http://freshrpms.net/> 0.6.13-0
- Update to 0.6.13.
- Reworked the configure options, build reqs and rpmbuild conditionals.
- Remove gcc 2.96 patch, it doesn't apply anymore.
- Include bitstream patch to fix dvd::rip usage.
- Re-add ffmpeg-devel build dep, it builds shared again now.

* Fri Jul 30 2004 Dag Wieers <dag@wieers.com> - 0.6.12-6
- Added patch for building with gcc < 3. (Edward Rudd, ATbz #183)

* Fri Jul 23 2004 Matthias Saou <http://freshrpms.net/> 0.6.12-6
- Added ed build requirement for x86_64 build to succeed...
- Fix missing \ to configure lines.
- Remove explicit binary dependencies.

* Tue Jul 20 2004 Dag Wieers <dag@wieers.com> - 0.6.12-6
- Rebuild for x86_64 with quicktime support.

* Wed May 19 2004 Matthias Saou <http://freshrpms.net/> 0.6.12-5
- Rebuild for Fedora Core 2.
- Remove explicit stripping, it goes into the debuginfo package.
- Change some of the obvious conditional builds to be static (ogg...).
- Make xvid4 the default instead of xvid2.
- Added theora and libmpeg3 support.
- Added libexif-devel build requirement, although ImageMagick-devel should.

* Fri Apr 16 2004 Matthias Saou <http://freshrpms.net/> 0.6.12-3
- Rebuild against new libdv.

* Thu Mar 25 2004 Matthias Saou <http://freshrpms.net/> 0.6.12-2
- Fix bzip2-devel dependency.

* Sat Jan 10 2004 Matthias Saou <http://freshrpms.net/> 0.6.12-1
- Update to 0.6.12.

* Mon Nov 10 2003 Matthias Saou <http://freshrpms.net/> 0.6.11-1
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

