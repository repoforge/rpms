# $Id$
# Authority: hadams

%define desktop_vendor rpmforge
%define audacity_version 1.4.6

Summary: Plugins for the Audacious media player
Name: audacious-plugins
Version: 1.4.5
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://audacious-media-player.org/

Source: http://distfiles.atheme.org/audacious-plugins-%{version}.tbz2
Patch0: audacious-plugins-1.2.2-cddb-buffer.patch
Patch1: audacious-plugins-1.4.1-neon-locking.patch
Patch2: audacious-plugins-1.4.4-gcc43.patch
Patch100: audacious-plugins-1.4.5-libvorbis_1.1.patch
Patch101: audacious-plugins-1.4.5-libmtp_0.3.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: alsa-lib-devel
BuildRequires: arts-devel
BuildRequires: audacious-devel >= %{audacious_version}
BuildRequires: curl-devel
BuildRequires: flac-devel >= 1.1.2
#BuildRequires: fluidsynth-devel
BuildRequires: gettext
#BuildRequires: jack-audio-connection-kit-devel
BuildRequires: libbinio-devel
BuildRequires: libmad-devel
BuildRequires: libmcs-devel >= 0.6.0
BuildRequires: libmms-devel
BuildRequires: libmodplug-devel
BuildRequires: libmpcdec-devel
BuildRequires: libmusicbrainz-devel
BuildRequires: libmowgli >= 0.5.0
BuildRequires: libmtp-devel
BuildRequires: libnotify-devel
BuildRequires: libogg-devel >= 1.0
BuildRequires: libsamplerate-devel
BuildRequires: libsidplay-devel
BuildRequires: libvisual-devel >= 0.2
BuildRequires: libXcomposite-devel
#BuildRequires: lirc-devel
BuildRequires: neon-devel >= 0.25
#BuildRequires: pulseaudio-devel
BuildRequires: SDL-devel >= 1.2.9
BuildRequires: taglib-devel >= 1.4
BuildRequires: wavpack-devel >= 4.31
BuildRequires: zlib-devel

Requires: audacious >= %{audacious_version}

Requires: desktop-file-utils >= 0.9
Requires: /sbin/ldconfig

%description
Audacious is a media player that currently uses a skinned
user interface based on Winamp 2.x skins. It is based on ("forked off")
BMP.
This package provides essential plugins for audio input, audio output
and visualization.

%package aac
Summary: AAC playback plugin for Audacious
Group: Applications/Multimedia
Requires: audacious >= %{audacious_version}
Requires: audacious-plugins >= %{version}

%description aac
Audacious is a media player that currently uses a skinned
user interface based on Winamp 2.x skins. It is based on ("forked off")
BMP.

This is the plugin needed to play AAC audio files.

%package alac
Summary: ALAC playback plugin for Audacious
Group: Applications/Multimedia
Requires: audacious >= %{audacious_version}
Requires: audacious-plugins >= %{version}

%description alac
Audacious is a media player that currently uses a skinned
user interface based on Winamp 2.x skins. It is based on ("forked off")

%package amidi
Summary: Audacious imput plugin for amidi
Group: Applications/Multimedia
Requires: audacious >= %{audacious_version}
Requires: audacious-plugins >= %{version}

%description amidi
This package provides an Audacious input plugin that uses the
amidi sound service.

%package arts
Summary: Audacious output plugin for KDE arts sound service
Group: Applications/Multimedia
Obsoletes: audacious-arts <= 1.1.2
Requires: audacious >= %{audacious_version}
Requires: audacious-plugins >= %{version}

%description arts
This package provides an Audacious output plugin that uses the
KDE arts sound server.

%package esd
Summary: Audacious output plugin for esd sound service
Group: Applications/Multimedia
Obsoletes: audacious-esd <= 1.1.2
Requires: audacious >= %{audacious_version}
Requires: audacious-plugins >= %{version}

%description esd
This package provides an Audacious output plugin that uses the
ESD sound server.

%package jack
Summary: Audacious output plugin for JACK sound service
Group: Applications/Multimedia
Obsoletes: audacious-jack <= 1.1.2
Requires: audacious >= %{audacious_version}
Requires: audacious-plugins >= %{version}

%description jack
This package provides an Audacious output plugin that uses the
JACK sound service.

%package metronome
Summary: Audacious imput plugin simulating a metronome
Group: Applications/Multimedia
Requires: audacious >= %{audacious_version}
Requires: audacious-plugins >= %{version}

%description metronome
This package provides an Audacious input plugin that simulates
a metronome.

%package mms
Summary: MMS stream plugin for Audacious
Group: Applications/Multimedia
Requires: audacious >= %{audacious_version}
Requires: audacious-plugins >= %{version}

%description mms
Audacious is a media player that currently uses a skinned
user interface based on Winamp 2.x skins. It is based on ("forked off")
BMP.

This is the plugin needed to access MMS streams.

%package mp3
Summary: MP3 playback plugin for Audacious
Group: Applications/Multimedia
Requires: audacious >= %{audacious_version}
Requires: audacious-plugins >= %{version}

%description mp3
Audacious is a media player that currently uses a skinned
user interface based on Winamp 2.x skins. It is based on ("forked off")
BMP.

This is the plugin needed to play MP3 audio files.

%package pulseaudio
Summary: Audacious output plugin for PulseAudio
Group: Applications/Multimedia
Requires: audacious >= %{audacious_version}
Requires: audacious-plugins >= %{version}

%description pulseaudio
This package provides an Audacious output plugin that uses the
PulseAudio sound server.

%package tta
Summary: TTA playback plugin for Audacious
Group: Applications/Multimedia
Requires: audacious >= %{audacious_version}
Requires: audacious-plugins >= %{version}

%description tta
Audacious is a media player that currently uses a skinned
user interface based on Winamp 2.x skins. It is based on ("forked off")

This is the plugin needed to play TTA audio files.

%package vortex
Summary: Audacious imput plugin for vortex audio files
Group: Applications/Multimedia
Requires: audacious >= %{audacious_version}
Requires: audacious-plugins >= %{version}

%description vortex
This package provides an Audacious input plugin that reads
vortex compressed files.

%package wavpack
Summary: Audacious imput plugin for wavpack
Group: Applications/Multimedia
Requires: audacious >= %{audacious_version}
Requires: audacious-plugins >= %{version}

%description wavpack
This package provides an Audacious input plugin that reads WavPack
compressed files.

%package wma
Summary: WMA playback plugin for Audacious
Group: Applications/Multimedia
Requires: audacious >= %{audacious_version}
Requires: audacious-plugins >= %{version}

%description wma
Audacious is a media player that currently uses a skinned
user interface based on Winamp 2.x skins. It is based on ("forked off")
BMP.

This is the plugin needed to play WMA audio files.

%prep
%setup
# Fix regressions due to stricter GCC 4.3 checking
%patch2 -p1 -b .gcc43

%{__perl} -pi.orig -e 's|^\.SILENT:.*$||' buildsys.mk.in

%patch100 -p1 -b .vorbis_1.1
%patch101 -p1 -b .libmtp_0.3

%build
%configure \
    --disable-amidiplug-dummy \
    --disable-dependency-tracking \
    --disable-gnome-vfs \
    --disable-rpath \
    --disable-sndfile \
    --disable-sse2 \
    --enable-amidiplug \
    --enable-chardet \
    --enable-gconf \
    --enable-neon

%{__make} V=1 %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS
%{_datadir}/audacious/
%{_libdir}/audacious/
%exclude %{_libdir}/audacious/Input/aac.so
%exclude %{_libdir}/audacious/Input/alac.so
%exclude %{_libdir}/audacious/Input/madplug.so
%exclude %{_libdir}/audacious/Input/amidi-plug.so
%exclude %{_libdir}/audacious/Input/metronom.so
%exclude %{_libdir}/audacious/Input/tta.so
%exclude %{_libdir}/audacious/Input/vtx.so
%exclude %{_libdir}/audacious/Input/wavpack.so
%exclude %{_libdir}/audacious/Input/wma.so
%exclude %{_libdir}/audacious/Output/arts.so
%exclude %{_libdir}/audacious/Output/ESD.so
#%exclude %{_libdir}/audacious/Output/jackout.so
#%exclude %{_libdir}/audacious/Output/pulseaudio.so
%exclude %{_libdir}/audacious/Transport/mms.so

%files aac
%defattr(-, root, root, 0755)
%{_libdir}/audacious/Input/aac.so

%files alac
%defattr(-, root, root, 0755)
%{_libdir}/audacious/Input/alac.so

%files amidi
%defattr(-, root, root, 0755)
%{_libdir}/audacious/Input/amidi-plug.so
# %{_libdir}/audacious/amidi-plug

%files arts
%defattr(-, root, root, 0755)
%{_bindir}/audacious-arts-helper
%{_libdir}/audacious/Output/arts.so

%files esd
%defattr(-, root, root, 0755)
%{_libdir}/audacious/Output/ESD.so

#%files jack
#%defattr(-, root, root, 0755)
#%{_libdir}/audacious/Output/libjackout.so

%files metronome
%defattr(-, root, root, 0755)
%{_libdir}/audacious/Input/metronom.so

%files mms
%defattr(-, root, root, 0755)
%{_libdir}/audacious/Transport/mms.so

%files mp3
%defattr(-, root, root, 0755)
%{_libdir}/audacious/Input/madplug.so

#%files pulseaudio
#%defattr(-, root, root, 0755)
#%{_libdir}/audacious/Output/pulseaudio.so

%files tta
%defattr(-, root, root, 0755)
%{_libdir}/audacious/Input/tta.so

%files vortex
%defattr(-, root, root, 0755)
%{_libdir}/audacious/Input/vtx.so

%files wavpack
%defattr(-, root, root, 0755)
%{_libdir}/audacious/Input/wavpack.so

%files wma
%defattr(-, root, root, 0755)
%{_libdir}/audacious/Input/wma.so

%changelog
* Wed Jul 15 2009 Dag Wieers <dag@wieers.com> - 1.4.5-1
- Updated to release 1.4.5.

* Mon Mar 24 2008 Heiko Adams <info-2007@fedora-blog.de> 1.3.5-5
- Added more dependencies to BuildRequires.

* Mon Mar 24 2008 Heiko Adams <info-2007@fedora-blog.de> 1.3.5-4
- Added libmms-devel and libogg-devel to BuildRequires.

* Sat Mar 22 2008 Heiko Adams <info-2007@fedora-blog.de> 1.3.5-3
- Rebuild for rpmforge.

* Sat Jun 16 2007 Ralf Ertzinger <ralf@skytale.net> 1.3.5-2.fc6
- Update to 1.3.5

* Sat May 26 2007 Ralf Ertzinger <ralf@skytale.net> 1.3.4-2.fc6
- Update to 1.3.4

* Sun Apr 22 2007 Ralf Ertzinger <ralf@skytale.net> 1.3.3-1.fc6
- Update to 1.3.3
- Introduce aud_ver variable into specfile

* Mon Apr 16 2007 Ralf Ertzinger <ralf@skytale.net> 1.3.2-1.fc6
- Update to 1.3.2

* Mon Jan 15 2007 Ralf Ertzinger <ralf@skytale.net> 1.2.5-3.fc6
- Fix a BuildRequires typo

* Sat Dec 16 2006 Ralf Ertzinger <ralf@skytale.net> 1.2.5-2.fc6
- Rebuild for new wavpack
- Do not build against sndfile, it causes an unpausable wav plugin
  to be built

* Thu Nov 30 2006 Ralf Ertzinger <ralf@skytale.net> 1.2.5-1.fc6
- Update to 1.2.5
- Add audacious-plugins-wavpack for WavPack input plugin
- Drop cddb patch, included upstream

* Sun Nov 26 2006 Ralf Ertzinger <ralf@skytale.net> 1.2.2-1.fc6
- Initial RPM build for FE
