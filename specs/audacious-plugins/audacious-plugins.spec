# $Id$
# Authority: hadams

%define desktop_vendor rpmforge
%define         aud_ver 1.3.0

Name:           audacious-plugins
Version:        1.3.5
Release:        4
Summary:        Plugins for the Audacious media player

Group:          Applications/Multimedia
License:        GPL
URL:            http://audacious-media-player.org/
Source0:        http://static.audacious-media-player.org/release/%{name}-%{version}.tgz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  audacious-devel >= %{aud_ver}, taglib-devel >= 1.4, alsa-lib-devel
BuildRequires:  libmad-devel, libnotify-devel, gettext, curl-devel, libmms-devel
BuildRequires:  libogg-devel >= 1.0
#BuildRequires:  esound-devel >= 0.2, libvorbis-devel >= 1.0
#BuildRequires:  zlib-devel, desktop-file-utils >= 0.9, alsa-lib-devel
#BuildRequires:  libsidplay-devel, libnotify-devel
#BuildRequires:  libmpcdec-devel, libmusicbrainz-devel
#BuildRequires:  taglib-devel >= 1.4, libogg-devel >= 1.0, flac-devel >= 1.1.2
#BuildRequires:  libvisual-devel >= 0.2, SDL-devel >= 1.2.9
#BuildRequires:  gettext, curl-devel, libbinio-devel
#BuildRequires:  arts-devel, libmodplug-devel, lirc-devel
#BuildRequires:  jack-audio-connection-kit-devel, libsamplerate-devel
#BuildRequires:  pulseaudio-devel, fluidsynth-devel
#BuildRequires:  wavpack-devel >= 4.31
#BuildRequires:  libXcomposite-devel

Requires:       audacious >= %{aud_ver}

Requires(post):   desktop-file-utils >= 0.9, /sbin/ldconfig
Requires(postun): desktop-file-utils >= 0.9, /sbin/ldconfig

%description
Audacious is a media player that currently uses a skinned
user interface based on Winamp 2.x skins. It is based on ("forked off")
BMP.
This package provides essential plugins for audio input, audio output
and visualization.


#%package        jack
#Summary:        Audacious output plugin for JACK sound service
#Group:          Applications/Multimedia
#Obsoletes:      audacious-jack <= 1.1.2

#Requires:       audacious >= %{aud_ver}, audacious-plugins >= %{aud_ver}

#%description    jack
#This package provides an Audacious output plugin that uses the
#JACK sound service.


%package        esd
Summary:        Audacious output plugin for esd sound service
Group:          Applications/Multimedia
Obsoletes:      audacious-esd <= 1.1.2

Requires:       audacious >= %{aud_ver}, audacious-plugins >= %{aud_ver}

%description    esd
This package provides an Audacious output plugin that uses the
ESD sound server.


#%package        arts
#Summary:        Audacious output plugin for KDE arts sound service
#Group:          Applications/Multimedia
#Obsoletes:      audacious-arts <= 1.1.2

#Requires:       audacious >= %{aud_ver}, audacious-plugins >= %{aud_ver}

#%description    arts
#This package provides an Audacious output plugin that uses the
#KDE arts sound server.


#%package        pulseaudio
#Summary:        Audacious output plugin for PulseAudio
#Group:          Applications/Multimedia

#Requires:       audacious >= %{aud_ver}, audacious-plugins >= %{aud_ver}

#%description    pulseaudio
#This package provides an Audacious output plugin that uses the
#PulseAudio sound server.



%package        amidi
Summary:        Audacious imput plugin for amidi
Group:          Applications/Multimedia

Requires:       audacious >= %{aud_ver}, audacious-plugins >= %{aud_ver}

%description    amidi
This package provides an Audacious input plugin that uses the
amidi sound service.



#%package        wavpack
#Summary:        Audacious imput plugin for wavpack
#Group:          Applications/Multimedia

#Requires:       audacious >= %{aud_ver}, audacious-plugins >= %{aud_ver}

#%description    wavpack
#This package provides an Audacious input plugin that reads WavPack
#compressed files.



%package        metronome
Summary:        Audacious imput plugin simulating a metronome
Group:          Applications/Multimedia

Requires:       audacious >= %{aud_ver}, audacious-plugins >= %{aud_ver}

%description    metronome
This package provides an Audacious input plugin that simulates
a metronome.



%package        vortex
Summary:        Audacious imput plugin for vortex audio files
Group:          Applications/Multimedia

Requires:       audacious >= %{aud_ver}, audacious-plugins >= %{aud_ver}

%description    vortex
This package provides an Audacious input plugin that reads
vortex compressed files.



%prep
%setup -q -n %{name}-%{version}

# Fix incorrect use of sprintf in the cdaudio plugin
# %patch0 -p1 -b .cddb-buffer

%build
%configure \
    --disable-rpath \
    --enable-gconf \
    --disable-gnome-vfs \
    --enable-chardet \
    --disable-dependency-tracking \
    --enable-amidiplug \
    --disable-amidiplug-dummy \
    --disable-sndfile

make V=1 %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
%find_lang %{name}

#desktop-file-install --vendor fedora \
#    --dir $RPM_BUILD_ROOT%{_datadir}/applications   \
#    %{SOURCE1}

%clean
rm -rf $RPM_BUILD_ROOT


%post
/sbin/ldconfig
update-desktop-database %{_datadir}/applications


%postun
/sbin/ldconfig
update-desktop-database %{_datadir}/applications


%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog NEWS
%{_libdir}/audacious/Input
%{_libdir}/audacious/Output
%{_libdir}/audacious/Container
%{_libdir}/audacious/Effect
%{_libdir}/audacious/General
%{_libdir}/audacious/Visualization
%exclude %{_libdir}/audacious/Input/libamidi-plug.so
#%exclude %{_libdir}/audacious/Input/libwavpack.so
%exclude %{_libdir}/audacious/Input/libmetronom.so
%exclude %{_libdir}/audacious/Input/libvtx.so
#%exclude %{_libdir}/audacious/Output/libjackout.so
#%exclude %{_libdir}/audacious/Output/libarts.so
%exclude %{_libdir}/audacious/Output/libESD.so
#%exclude %{_libdir}/audacious/Output/libpulse_audio.so
#%{_datadir}/applications/fedora-audacious-plugins.desktop
%{_datadir}/audacious/images/audioscrobbler.png
%{_datadir}/audacious/images/audioscrobbler_badge.png
#%{_datadir}/audacious-plugins

#%files jack
#%defattr(-,root,root,-)
#%{_libdir}/audacious/Output/libjackout.so

#%files arts
#%defattr(-,root,root,-)
#%{_bindir}/audacious-arts-helper
#%{_libdir}/audacious/Output/libarts.so

%files esd
%defattr(-,root,root,-)
%{_libdir}/audacious/Output/libESD.so

#%files pulseaudio
#%defattr(-,root,root,-)
#%{_libdir}/audacious/Output/libpulse_audio.so

%files amidi
%defattr(-,root,root,-)
%{_libdir}/audacious/Input/libamidi-plug.so
%{_libdir}/audacious/amidi-plug

#%files wavpack
#%defattr(-,root,root,-)
#%{_libdir}/audacious/Input/libwavpack.so

%files metronome
%defattr(-,root,root,-)
%{_libdir}/audacious/Input/libmetronom.so

%files vortex
%defattr(-,root,root,-)
%{_libdir}/audacious/Input/libvtx.so


%changelog
* Mon Mar 24 2008 Heiko Adams <info-2007@fedora-blog.de> 1.3.5-4
- added libmms-devel and libogg-devel to BuildRequires

* Sat Mar 22 2008 Heiko Adams <info-2007@fedora-blog.de> 1.3.5-3
- rebuild for rpmforge

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
