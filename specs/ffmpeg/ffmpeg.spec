# $Id$
# Authority: matthias

#define date   2003-11-07
#define sqdate %(echo %{date} | tr -d '-')

Summary: Hyper fast MPEG1/MPEG4/H263/RV and AC3/MPEG audio encoder and decoder
Name: ffmpeg
Version: 0.4.8
Release: 2%{?date:.%{sqdate}}
License: GPL
Group: System Environment/Libraries
%if %{?date:0}%{!?date:1}
Source: http://dl.sf.net/ffmpeg/%{name}-%{version}.tar.gz
%else
Source: http://ffmpeg.sourceforge.net/cvs/%{name}-cvs-%{date}.tar.gz
%endif
URL: http://ffmpeg.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-root
Requires: imlib2, SDL, freetype, zlib
%{!?_without_lame:Requires: lame}
%{!?_without_vorbis:Requires: libogg, libvorbis}
%{!?_without_faad:Requires: faad2}
%{!?_without_faac:Requires: faac}
BuildRequires: imlib2-devel, SDL-devel, freetype-devel, zlib-devel
%{!?_without_lame:BuildRequires: lame-devel}
%{!?_without_vorbis:BuildRequires: libogg-devel, libvorbis-devel}
%{!?_without_faad:BuildRequires: faad2-devel}
%{!?_without_faac:BuildRequires: faac-devel}
%{!?_without_a52dec:BuildRequires: a52dec-devel}
Provides: libavcodec.so, libavformat.so

%description
FFmpeg is a very fast video and audio converter. It can also grab from a
live audio/video source.
The command line interface is designed to be intuitive, in the sense that
ffmpeg tries to figure out all the parameters, when possible. You have
usually to give only the target bitrate you want. FFmpeg can also convert
from any sample rate to any other, and resize video on the fly with a high
quality polyphase filter.

Available rpmbuild rebuild options :
--without : lame vorbis faad a52dec altivec


%package devel
Summary: Header files and static library for the ffmpeg codec library.
Group: Development/Libraries
Requires: %{name} = %{version}

%description devel
FFmpeg is a very fast video and audio converter. It can also grab from a
live audio/video source.
The command line interface is designed to be intuitive, in the sense that
ffmpeg tries to figure out all the parameters, when possible. You have
usually to give only the target bitrate you want. FFmpeg can also convert
from any sample rate to any other, and resize video on the fly with a high
quality polyphase filter.

Install this package if you want to compile apps with ffmpeg support.


%prep
%setup -n %{name}-%{?date:cvs-%{date}}%{!?date:%{version}}

%build
%configure \
    --enable-shared \
    --enable-pp \
%ifarch %{ix86}
     --disable-mmx \
%endif
%ifarch ppc
    %{?_without_altivec: --disable-altivec} \
%endif
    %{!?_without_lame: --enable-mp3lame} \
    %{!?_without_vorbis: --enable-vorbis} \
    %{!?_without_faad: --enable-faad} \
    %{!?_without_faac: --enable-faac} \
    %{!?_without_a52dec: --enable-a52}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

# Make installlib is broken in 0.4.6-8, so we do it by hand
%{__install} -m 644 libavcodec/libavcodec.a %{buildroot}%{_libdir}/
%{__install} -m 644 libavformat/libavformat.a %{buildroot}%{_libdir}/

# Create compat symlink
mkdir %{buildroot}%{_libdir}/{libavcodec,libavformat}
ln -s ../libavcodec.a %{buildroot}%{_libdir}/libavcodec/libavcodec.a
ln -s ../libavformat.a %{buildroot}%{_libdir}/libavformat/libavformat.a

# Remove from the included docs
%{__rm} -f doc/Makefile doc/*.1

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-, root, root, 0755)
%doc COPYING CREDITS Changelog README doc/
%{_bindir}/*
%{_libdir}/libavcodec-*.so
%{_libdir}/libavcodec.so
%{_libdir}/libavformat-*.so
%{_libdir}/libavformat.so
%{_libdir}/vhook
%{_mandir}/man1/*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/%{name}
%{_libdir}/libavcodec
%{_libdir}/libavcodec.a
%{_libdir}/libavformat
%{_libdir}/libavformat.a


%changelog
* Sat Feb 21 2004 Matthias Saou <http://freshrpms.net/> 0.4.8-2.fr
- Add faac support.
- Enable pp.
- Remove unneeded explicit main a52dec dependency.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 0.4.8-1.fr
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

