# $Id$
# Authority: matthias

%define date   2004-11-10
#define prever pre1
%{?date: %define sqdate %(echo %{date} | tr -d '-')}

Summary: Hyper fast MPEG1/MPEG4/H263/RV and AC3/MPEG audio encoder and decoder
Name: ffmpeg
Version: 0.4.9
Release: %{?date:0.%{sqdate}.}%{?prever:0.%{prever}.}1
License: GPL
Group: System Environment/Libraries
URL: http://ffmpeg.sourceforge.net/
%if %{?date:0}%{!?date:1}
Source: http://dl.sf.net/ffmpeg/ffmpeg-%{version}%{?prever:-%{prever}}.tar.gz
%else
Source: http://ffmpeg.sourceforge.net/cvs/%{name}-cvs-%{date}.tar.gz
%endif
Patch0: ffmpeg-0.4.9-pre1-sharedppfix.patch
Patch2: ffmpeg-0.4.9-pre1-pic.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: imlib2-devel, SDL-devel, freetype-devel, zlib-devel
BuildRequires: tetex
%{!?_without_lame:BuildRequires: lame-devel}
%{!?_without_vorbis:BuildRequires: libogg-devel, libvorbis-devel}
%{!?_without_faad:BuildRequires: faad2-devel}
%{!?_without_faac:BuildRequires: faac-devel}
%{!?_without_xvid:BuildRequires: xvidcore-devel}
%{!?_without_a52dec:BuildRequires: a52dec-devel}
# We need those as autoreqprov adds them as a requirement to the package
# (0.4.8, still true in 0.4.9-pre1)
Provides: libavcodec.so
Provides: libavformat.so
%ifarch x86_64
Provides: libavcodec.so()(64bit)
Provides: libavformat.so()(64bit)
%endif

%description
FFmpeg is a very fast video and audio converter. It can also grab from a
live audio/video source.
The command line interface is designed to be intuitive, in the sense that
ffmpeg tries to figure out all the parameters, when possible. You have
usually to give only the target bitrate you want. FFmpeg can also convert
from any sample rate to any other, and resize video on the fly with a high
quality polyphase filter.

Available rpmbuild rebuild options :
--without : lame vorbis faad faac xvid a52dec altivec


%package devel
Summary: Header files and static library for the ffmpeg codec library
Group: Development/Libraries
Requires: %{name} = %{version}
Requires: imlib2-devel, SDL-devel, freetype-devel, zlib-devel
%{!?_without_lame:Requires: lame-devel}
%{!?_without_vorbis:Requires: libogg-devel, libvorbis-devel}
%{!?_without_faad:Requires: faad2-devel}
%{!?_without_faac:Requires: faac-devel}
%{!?_without_xvid:Requires: xvidcore-devel}
%{!?_without_a52dec:Requires: a52dec-devel}

%description devel
FFmpeg is a very fast video and audio converter. It can also grab from a
live audio/video source.
The command line interface is designed to be intuitive, in the sense that
ffmpeg tries to figure out all the parameters, when possible. You have
usually to give only the target bitrate you want. FFmpeg can also convert
from any sample rate to any other, and resize video on the fly with a high
quality polyphase filter.

Install this package if you want to compile apps with ffmpeg support.


%package -n libpostproc
Summary: Video postprocessing library from ffmpeg
Group: System Environment/Libraries
# We need to override version here... when libpostproc was built from
# MPlayer, it got up to 1.0-0.11.x) - mach barfs! :-(
#Version: 1.0.1
Provides: libpostproc-devel = %{version}-%{release}

%description -n libpostproc
FFmpeg is a very fast video and audio converter. It can also grab from a
live audio/video source.

This package contains only ffmpeg's libpostproc post-processing library which
other projects such as transcode may use. Install this package if you intend
to use MPlayer, transcode or other similar programs.


%prep
%setup -n %{name}-%{?date:cvs-%{date}}%{!?date:%{version}%{?prever:-%{prever}}}
#patch0 -p1 -b .sharedpp
#patch2 -p1 -b .pic

### FIXME: Make Makefile use autotool directory standard. (Please fix upstream)
%{__perl} -pi -e 's|\$\(prefix\)/lib|\$(libdir)|g;
                  s|\$\(prefix\)/include|\$(includedir)|g' \
                  Makefile */Makefile */*/Makefile


%build
%configure \
%ifnarch %{ix86}
    --disable-mmx \
    --extra-cflags="%{optflags} -fPIC" \
%else
    --extra-cflags="%{optflags}" \
%endif
    %{!?_without_lame: --enable-mp3lame} \
    %{!?_without_vorbis: --enable-vorbis} \
    %{!?_without_faad: --enable-faad} \
    %{!?_without_faac: --enable-faac} \
    %{!?_without_xvid: --enable-xvid} \
    --enable-pp \
    --enable-shared-pp \
    --enable-shared \
    --enable-gpl \
    --disable-strip
#   %{!?_without_a52: --enable-a52} \
# Make!
%{__make} %{?_smp_mflags} -C libavcodec/libpostproc
%{__make} %{?_smp_mflags}
%{__make} documentation
# Leftover, for reference :
# OPTFLAGS="-fPIC -fomit-frame-pointer %{optflags} -UUSE_FASTMEMCPY"


%install
%{__rm} -rf %{buildroot}
%makeinstall -C libavcodec/libpostproc
%makeinstall

### Make installlib is broken in 0.4.6-8, so we do it by hand
%{__install} -D -m0644 libavcodec/libavcodec.a \
    %{buildroot}%{_libdir}/libavcodec.a
%{__install} -D -m0644 libavformat/libavformat.a \
    %{buildroot}%{_libdir}/libavformat.a

### Remove from the included docs
%{__rm} -rf doc/{CVS,Makefile}


%clean
%{__rm} -rf %{buildroot}


%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%post -n libpostproc
/sbin/ldconfig

%postun -n libpostproc
/sbin/ldconfig


%files
%defattr(-, root, root, 0755)
%doc Changelog COPYING CREDITS README
%{_bindir}/*
%{_libdir}/*.so
%{_libdir}/vhook/
%{_mandir}/man1/*

%files devel
%defattr(-, root, root, 0755)
%doc doc/*
%{_includedir}/ffmpeg/
%{_libdir}/*.a

%files -n libpostproc
%defattr(-, root, root, 0755)
%{_includedir}/postproc/
%{_libdir}/libpostproc.so*


%changelog
* Tue Nov 16 2004 Matthias Saou <http://freshrpms.net/> 0.4.9-0.20041110.1
- Update to latest CVS snaphsot.
- Explicitely disable mmx on non-x86 to fix x86_64 build.
- Add -fPIC to --extra-cflags on non-x86 to fix x86_64 build, as it seems mmx
  and pic are mutually exclusive (build fails with both).

* Tue Nov  2 2004 Matthias Saou <http://freshrpms.net/> 0.4.9-0.20041102.1
- Update to 20040926 CVS to fix FC3 compilation problems... not!
- Moved OPTFLAGS to --extra-cflags configure option... no better!
- Add HAVE_LRINTF workaround to fix compile failure... yeah, one less.
- Disable -fPIC, libpostproc breaks with it enabled... argh :-(
- ...I give up, disable a52 for now.

* Mon Sep 27 2004 Matthias Saou <http://freshrpms.net/> 0.4.9-0.pre1.1
- Update to 0.4.9-pre1.
- Enable GPL, pp, shared and shared-pp!
- Add sharedpp and nostrip patches from livna.org rpm.
- Add PIC vs. __PIC__ patch.
- Re-enable MMX.
- Add mandatory -fomit-frame-pointer flag to not bomb on compile.
- Added man pages.
- Added -UUSE_FASTMEMCPY for libpostproc, otherwise we get :
  libpostproc.so.0: undefined reference to `fast_memcpy'

* Mon Aug  2 2004 Matthias Saou <http://freshrpms.net/> 0.4.8-3
- Removed explicit binary dependencies.
- Removed faac support, it doesn't exist.
- Seems like Imlib2 support is broken...
- Added missing -devel requirements for the -devel package.

* Thu Jun 03 2004 Dag Wieers <dag@wieers.com> - 0.4.8-3
- Fixes for building for x86_64 architecture.

* Tue May 18 2004 Matthias Saou <http://freshrpms.net/> 0.4.8-3
- Rebuilt for Fedora Core 2.

* Sat Feb 21 2004 Matthias Saou <http://freshrpms.net/> 0.4.8-2
- Add faac support.
- Enable pp.
- Remove unneeded explicit main a52dec dependency.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 0.4.8-1
- Update to 0.4.8.
- Steal some changes back from Troy Engel : Disabling mmx to make the build
  succeed and added man pages.
- Re-enabled auto provides but added explicit libavcodec.so and libavformat.so.
- Rebuild for Fedora Core 1.

* Mon Aug 25 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.4.7.

* Fri Aug  8 2003 Matthias Saou <http://freshrpms.net/>
- Update to todays's snapshot.

* Tue Jul  1 2003 Matthias Saou <http://freshrpms.net/>
- Update to a CVS snapshot as videolan-client 0.6.0 needs it.
- Enable faad, imlib2 and SDL support.
- Force OPTFLAGS to remove -mcpu, -march and -pipe that all prevent building!

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.
- Hardcode provides in order to get it right :-/

* Tue Feb 25 2002 Matthias Saou <http://freshrpms.net/>
- Moved libavcodec.so to the main package to fix dependency problems.

* Wed Feb 19 2002 Matthias Saou <http://freshrpms.net/>
- Major spec file updates, based on a very nice Mandrake spec.
- Revert to the 0.4.6 release as CVS snapshots don't build.

* Tue Feb  4 2002 Matthias Saou <http://freshrpms.net/>
- Initial RPM release.

