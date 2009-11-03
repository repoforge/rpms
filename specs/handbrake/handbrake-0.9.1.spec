# $Id$
# Authority: dag

%define desktop_vendor rpmforge

%define real_name HandBrake

Summary: Multithreaded DVD to MPEG-4 converter
Name: HandBrake
Version: 0.9.1
Release: 1%{?dist}
Group: Applications/Multimedia
License: GPL
URL: http://handbrake.fr/

### FIXME: Try to build this without included ffmpeg/libdca/libmp4v2 !
Source: http://handbrake.fr/rotation.php?old=HandBrake-0.9.1.tar.gz
Source100: http://download.m0k.org/handbrake/contrib/ffmpeg-r15462.tar.gz
Source101: http://download.m0k.org/handbrake/contrib/libdca-r81-strapped.tar.gz
Source102: http://download.m0k.org/handbrake/contrib/libmp4v2-r45.tar.gz
Patch0: handbrake-0.9.1-disable-wget.patch
Patch1: handbrake-0.9.3-shared-libs.patch
Patch2: handbrake-0.9.3-ifoprint.patch
Patch3: handbrake-0.9.3-muxmkv.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: a52dec-devel >= 0.7.4
BuildRequires: bzip2-devel
BuildRequires: desktop-file-utils
BuildRequires: faac-devel >= 1.26
BuildRequires: faad2-devel >= 2.6.1
#BuildRequires: ffmpeg-devel >= 0.5
BuildRequires: glib2-devel
BuildRequires: gtk2-devel >= 2.8
BuildRequires: gtkhtml3-devel >= 3.14
BuildRequires: intltool
BuildRequires: jam
BuildRequires: lame-devel >= 3.98
#BuildRequires: libdca-devel >= rev81-strapped
BuildRequires: libdvdread-devel
BuildRequires: libmkv-devel
#BuildRequires: libmp4v2-devel >= rev45 ?
BuildRequires: libmpeg2-devel >= 0.5.1
BuildRequires: libogg-devel >= 1.1.3
BuildRequires: libsamplerate-devel >= 0.1.4
BuildRequires: libtheora-devel >= 1.0
BuildRequires: libtool
BuildRequires: libvorbis-devel
BuildRequires: wget
BuildRequires: x264-devel
BuildRequires: xvidcore-devel >= 1.2
BuildRequires: yasm
BuildRequires: zlib-devel
Requires: faac >= 1.26
Requires: xvidcore >= 1.2

Provides: HandBrake = %{version}-%{release}
Obsoletes: HandBrake <= %{version}-%{release}

Provides: ghb = %{version}-%{release}
Obsoletes: ghb <= %{version}-%{release}

%description
HandBrake is an open-source, GPL-licensed, multiplatform, multithreaded video
transcoder. It can convert any DVD like source and any multimedia format
supported by libavformat to MPEG4, MKV, AVI or OGM using MPEG4, H264 or Theora
codecs for video and AAC, MP3, Vorbis or AC-3 codecs for audio.

It features chapter selection, basic subtitle support, bitrate calculator,
picture deinterlacing, cropping and scaling and grayscale encoding.

%prep
%setup -n %{real_name}

%{__cp} -av %SOURCE100 ./contrib/ffmpeg.tar.gz
%{__cp} -av %SOURCE101 ./contrib/libdca.tar.gz
%{__cp} -av %SOURCE102 ./contrib/libmp4v2.tar.gz

%patch0 -p1 -b .disable-wget
%patch1 -p1 -b .shared-libs
%patch2 -p1 -b .ifoprint
%patch3 -p0 -b .orig

%build
%{__make} %{?_smp_mflags}

cd gtk
./autogen.sh --prefix="%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir}
%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
%{__install} -d -m0755 %{buildroot}%{_datadir}/icons/hicolor/
%{__make} -C gtk install DESTDIR="%{buildroot}"

desktop-file-install --delete-original \
  --vendor %{desktop_vendor} \
  --dir %{buildroot}%{_datadir}/applications \
  src/ghb.desktop

%clean
%{__rm} -rf %{buildroot}

%post
update-desktop-database &>/dev/null || :
touch --no-create %{_datadir}/icons/hicolor || :

%postun
update-desktop-database &>/dev/null || :
if [ $1 -eq 0 ]; then
  touch --no-create %{_datadir}/icons/hicolor &>/dev/null
  gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING CREDITS NEWS THANKS TRANSLATIONS
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/128x128/*
%exclude %{_docdir}/ghb
%exclude %{_datadir}/icons/hicolor/icon-theme.cache

%changelog
* Mon Jul 27 2009 Dag Wieers <dag@wieers.com> - 0.9.1-1
- Initial package. (based on fedora)
