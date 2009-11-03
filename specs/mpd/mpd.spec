# $Id$
# Authority: matthias

%{?dtag: %{expand: %%define %dtag 1}}

%{?el5:%define _without_pulseaudio 1}
%{?el4:%define _without_pulseaudio 1}
%{?el3:%define _without_pulseaudio 1}
%{?el2:%define _without_pulseaudio 1}

Summary: Music Player Daemon
Name: mpd
Version: 0.13.0
Release: 2%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://www.musicpd.org/
Source: http://www.musicpd.org/uploads/files/mpd-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: zlib-devel
BuildRequires: alsa-lib-devel, libshout-devel, mikmod-devel
BuildRequires: libid3tag-devel, libmad-devel, libogg-devel, libvorbis-devel
BuildRequires: flac-devel >= 1.1.2, audiofile-devel, faad2-devel, libmpcdec-devel
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
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%{__rm} -rf %{buildroot}%{_datadir}/doc/mpd/


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING README TODO UPGRADING
%doc doc/COMMANDS doc/mpdconf.example
%{_bindir}/mpd
%{_mandir}/man1/mpd.1*
%{_mandir}/man5/mpd.conf.5*


%changelog
* Mon Dec 17 2007 Dag Wieers <dag@wieers.com> - 0.13.0-2
- Rebuild against libmpcdec 1.2.6.

* Thu May 31 2007 Matthias Saou <http://freshrpms.net/> 0.13.0-1
- Update to 0.13.0.

* Wed Oct 18 2006 Matthias Saou <http://freshrpms.net/> 0.12.1-1
- Update to 0.12.1.

* Mon Oct  9 2006 Matthias Saou <http://freshrpms.net/> 0.12.0-1
- Initial RPM release.

