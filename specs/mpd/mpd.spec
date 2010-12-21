# $Id$
# Authority: shuff
# Upstream: Max Kellermann <max$duempel,org>
# ExcludeDist: el3 el4
# Rationale: 0.16 needs GLib 2.12

%define _without_cue 1
%define _without_sidplay 1

%{?el6:%define _without_mikmod 1}
%{?el6:%define _without_flac 1}

%{?el5:%define _without_inotify 1}
%{?el5:%define _without_pulseaudio 1}
%{?el5:%define _without_sqlite 1}

Summary: Music Player Daemon
Name: mpd
Version: 0.16
Release: 1%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://www.musicpd.org/

Source: http://downloads.sourceforge.net/project/musicpd/mpd/%{version}/mpd-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: audiofile-devel 
BuildRequires: bzip2-devel
BuildRequires: curl-devel
BuildRequires: faad2-devel
BuildRequires: ffmpeg-devel
BuildRequires: glib2-devel >= 2.12
# BuildRequires: jack-devel
BuildRequires: lame-devel
BuildRequires: libao-devel
BuildRequires: libcdio-devel
BuildRequires: libid3tag-devel
BuildRequires: libmad-devel
BuildRequires: libmodplug-devel
BuildRequires: libmpcdec-devel
BuildRequires: libogg-devel
BuildRequires: libsamplerate-devel
BuildRequires: libshout-devel >= 2.2.2
BuildRequires: libvorbis-devel
# BuildRequires: libwildmidi-devel
BuildRequires: mpg123-devel
BuildRequires: pkgconfig
BuildRequires: twolame-devel
BuildRequires: wavpack-devel
BuildRequires: zziplib-devel
%{!?_without_alsa:BuildRequires: alsa-lib-devel >= 1.0.16}
%{!?_without_avahi:BuildRequires: avahi-glib-devel}
%{!?_without_cue:BuildRequires: libcue-devel}
%{!?_without_flac:BuildRequires: flac-devel >= 1.1.2}
%{!?_without_libmms:BuildRequires: libmms-devel >= 0.4}
%{!?_without_sidplay:BuildRequires: libsidplay2-devel}
%{!?_without_mikmod:BuildRequires: mikmod-devel}
%{!?_without_sqlite:BuildRequires: sqlite-devel >= 3.0}
%{!?_without_pulseaudio:BuildRequires: pulseaudio-libs-devel}

%description
Music Player Daemon (MPD) allows remote access for playing music and managing
playlists. MPD is designed for integrating a computer into a stereo system
that provides control for music playback over a local network. It also makes
a great desktop music player, especially if you are a console junkie, like
frontend options, or restart X often.

%prep
%setup

%build
# packages without pkg-config files need to be configured manually
export FLAC_CFLAGS='-I%{_includedir}'
export FLAC_LIBS='-L%{_libdir}'
%configure --disable-dependency-tracking \
%{!?without_avahi:--with-zeroconf=avahi} \
%{?_without_cue:--disable-cue} \
%{?_without_flac:--disable-flac} \
%{?_without_inotify:--disable-inotify} \
%{?_without_libmms:--disable-mms} \
%{?_without_sidplay:--disable-sidplay} \
%{?_without_sqlite:--disable-sqlite} \
%{!?_without_alsa:--enable-alsa} \
    --enable-bzip2 \
    --enable-ffmpeg \
    --enable-httpd-output \
    --enable-iso9660 \
    --enable-lame-encoder \
    --enable-lastfm \
    --enable-libwrap \
    --enable-lsr \
    --enable-mad \
%{!?_without_mikmod:--enable-mikmod} \
    --enable-modplug \
    --enable-pipe-output \
%{!?_without_pulseaudio:--enable-pulseaudio} \
    --enable-recorder-output \
    --enable-shout \
    --enable-twolame-encoder \
    --enable-vorbis-encoder \
    --enable-zzip
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%{__rm} -rf %{buildroot}%{_datadir}/doc/mpd/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0775)
%doc AUTHORS COPYING README UPGRADING doc/mpdconf.example
%doc %{_mandir}/man1/mpd.1*
%doc %{_mandir}/man5/mpd.conf.5*
%{_bindir}/mpd

%changelog
* Tue Dec 21 2010 Steve Huff <shuff@vecna.org> - 0.16-1
- Update to 0.16.
- A few tweaks of requirements and configure options.

* Mon Dec 06 2010 Dag Wieers <dag@wieers.com> - 0.15.15-2
- Rebuild against ffmpeg-0.6.1.

* Tue Nov 09 2010 Steve Huff <shuff@vecna.org> - 0.15.15-1
- Update to 0.15.15.

* Wed Aug 04 2010 Steve Huff <shuff@vecna.org> - 0.15.12-1
- Update to 0.15.12.

* Fri Jun 11 2010 Steve Huff <shuff@vecna.org> - 0.15.10-1
- Update to 0.15.10.

* Tue Mar 23 2010 Steve Huff <shuff@vecna.org> - 0.15.9-1
- Update to 0.15.9.

* Fri Nov 06 2009 Dag Wieers <dag@wieers.com> - 0.13.0-3
- Rebuild against newer faad2 2.7.

* Mon Dec 17 2007 Dag Wieers <dag@wieers.com> - 0.13.0-2
- Rebuild against newer libmpcdec 1.2.6.

* Thu May 31 2007 Matthias Saou <http://freshrpms.net/> 0.13.0-1
- Update to 0.13.0.

* Wed Oct 18 2006 Matthias Saou <http://freshrpms.net/> 0.12.1-1
- Update to 0.12.1.

* Mon Oct  9 2006 Matthias Saou <http://freshrpms.net/> 0.12.0-1
- Initial RPM release.
