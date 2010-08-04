# $Id$
# Authority: shuff
# Upstream: Max Kellermann <max$duempel,org>

%{?el5:%define _without_pulseaudio 1}
%{?el4:%define _without_pulseaudio 1}
%{?el3:%define _without_pulseaudio 1}

Summary: Music Player Daemon
Name: mpd
Version: 0.15.12
Release: 1%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://www.musicpd.org/

Source: http://downloads.sourceforge.net/project/musicpd/mpd/%{version}/mpd-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: alsa-lib-devel >= 1.0.16
BuildRequires: audiofile-devel 
BuildRequires: avahi-glib-devel
BuildRequires: bzip2-devel
BuildRequires: curl-devel
BuildRequires: faad2-devel
BuildRequires: ffmpeg-devel
BuildRequires: flac-devel >= 1.1.2
BuildRequires: glib2-devel
# BuildRequires: jack-devel
BuildRequires: lame-devel
BuildRequires: libao-devel
# BuildRequires: libcue-devel
BuildRequires: libid3tag-devel
BuildRequires: libmad-devel
# BuildRequires: libmms-devel >= 0.4
BuildRequires: libmodplug-devel
BuildRequires: libmpcdec-devel
BuildRequires: libogg-devel
BuildRequires: libsamplerate-devel
BuildRequires: libshout-devel >= 2.2.2
# BuildRequires: libsidplay2-devel
BuildRequires: libvorbis-devel
# BuildRequires: libwildmidi-devel
BuildRequires: mikmod-devel
BuildRequires: pkgconfig
# BuildRequires: sqlite-devel
BuildRequires: zziplib-devel
%{!?_without_pulseaudio:BuildRequires: pulseaudio-devel}

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
    --disable-cue \
    --enable-lastfm \
    --disable-sqlite \
    --disable-mms \
    --enable-bzip2 \
    --enable-zip \
    --enable-iso9660 \
    --enable-ffmpeg \
    --enable-mad \
    --enable-mikmod \
    --enable-modplug \
    --disable-sidplay \
    --enable-lsr \
    --enable-vorbis-encoder \
    --enable-lame-encoder \
    --enable-alsa \
    --enable-pipe-output \
    --enable-httpd-output \
    --enable-shout
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
