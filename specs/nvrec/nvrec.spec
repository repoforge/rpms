# $Id$
# Authority: dag
# Upstream: Iñaki García Etxebarria <garetxe$users,sf,net>

Summary: High quality, generic capture core
Name: nvrec
Version: 20030316
Release: 2.2
Group: Applications/Multimedia
License: GPL
URL: http://nvrec.sourceforge.net/

Source: http://nvrec.sf.net/downloads/nvrec-%{version}.tar.gz
#Source1: http://dl.sf.net/ffmpeg-0.4.6.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: avifile-devel
#BuildRequires: ffmpeg-devel
BuildRequires: lame-devel
BuildRequires: libmad-devel
BuildRequires: libquicktime-devel
BuildRequires: librte-devel
BuildRequires: SDL-devel >= 1.2
BuildRequires: xvidcore-devel

%description
nvrec supports v4l1 and v4l2 devices as video sources, and oss as an audio
source. It can output to quicktime (in RTjpeg, YUV2, or RAW format, and
most ffmpeg formats), AVI (in DivX format), NuppelVideo format, MPEG-1,
and streaming multicast/unsicast.

nvrec includes deep buffering to minimise frame drops, in high load
situations, and a smooth framedropping algorithm to keep the video as
smooth as possible if you do have to drop frames. It also has a audio
"stretcher" to make sure that exactly the right amount of audio is
written to the output file (this compensates for lack of clock synch
between video and audio cards).

nvrec is written in an extremely modular way, to make it easy to integrate
with existing applications, or add your own output formats.

%prep
%setup

%build
#ln -sf ffmpeg-0.4.6/ ffmpeg
#cd ffmpeg
#configure \
#   --enable-a52bin \
#   --enable-mp3lame \
#   --enable-vorbis \
#   --enable-shared
#%{__make}
#cd -

./bootstrap
%configure \
    --disable-dependency-tracking \
    --enable-v4l2 \
    --with-avifile \
    --with-divx4linux \
    --with-ffmpeg \
    --with-mad \
    --with-mp3lame \
    --with-quicktime \
    --with-rte \
    --with-sdl
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING CREDITS FAQ KNOWN_BUGS NEWS README* STATUS VERSION
%doc etc/nvrec.conf
%doc %{_mandir}/man1/*.1*
%{_bindir}/*

%changelog
* Mon Apr 07 2003 Dag Wieers <dag@wieers.com> - 20030316-2
- Build against new (renamed) libxvidcore package.

* Sun Mar 30 2003 Dag Wieers <dag@wieers.com> - 20030316-0
- Updated to release 20030316. (no ffmpeg support)

* Thu Feb 20 2003 Dag Wieers <dag@wieers.com> - 20030217-0
- Initial package. (using DAR)
