# $Id$
# Authority: dag

%define desktop_vendor dag

Summary: DJ software emulating an analog mixer with two playback devices
Name: mixxx
Version: 1.3
Release: 0
License: GPL
Group: Applications/Multimedia
URL: http://mixxx.sf.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/mixxx/mixxx-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: glibc-devel, XFree86-devel, qt3-devel, glib-devel
BuildRequires: audiofile-devel, libmad-devel, libid3tag-devel
BuildRequires: libvorbis-devel, libogg-devel, libsndfile-devel
BuildRequires: portaudio, alsa-lib-devel, fftw-devel
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}

%description
Press play. Mixxx gives you full access to your digital sound library. Go
ahead and use Ogg Vorbis, MP3 and wave files in your live DJ mix. Pitch the
sound with same high sound quality as on your good old Technics 1210.
Beat track and automatic tempo sync makes beat mixing a breeeze, waveform
displays makes visual sync possible, and FishEye view mode gives you a tight
startup.
Use mouse, keyboard, MIDI equipment, PowerMates, and joystics to interact with
Mixxx. Low latency operation and hardware controllers makes the big difference
in a live gig. Mixxx supports it all.

%prep
%setup

%build
source "%{_sysconfdir}/profile.d/qt.sh"
# The PWD thing is an ugly hack since relative paths mess everything up...
pushd src
    # Alsa doesn't seem to get enabled for now (unimplemented?)
    ./configure --prefix="${PWD}%{_prefix}" --enable-features="Alsa"
    %{__perl} -pi.orig -e "s|${PWD}||g" Makefile
    %{__make} %{?_smp_mflags}
popd

%install
%{__rm} -rf %{buildroot}
pushd src
    # That trailing slash is mandatory because of "$(INSTALL_ROOT)usr" lines
    %{__make} install INSTALL_ROOT="%{buildroot}/"
popd

# Install menu entry
%{__cat} > %{name}.desktop << EOF
[Desktop Entry]
Name=Mixxx
Comment=DJ mixing software
Icon=mixxx.png
Exec=mixxx
Terminal=false
Type=Application
Categories=Application;AudioVideo;
Encoding=UTF-8
EOF
                                                                                
%if %{!?_without_freedesktop:1}0
%{__mkdir_p} %{buildroot}%{_datadir}/applications
desktop-file-install \
    --vendor %{desktop_vendor} \
    --dir %{buildroot}%{_datadir}/applications \
    %{name}.desktop
%else
%{__install} -D -m 0644 %{name}.desktop \
    %{buildroot}%{_sysconfdir}/X11/applnk/Multimedia/%{name}.desktop
%endif

# Install icon for the menu entry
%{__install} -D -m 644 src/icon.png %{buildroot}%{_datadir}/pixmaps/mixxx.png

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING LICENSE README Mixxx-Manual.pdf
%{_bindir}/*
%{_datadir}/mixxx/
%{_datadir}/pixmaps/mixxx.png
%if %{!?_without_freedesktop:1}0
%{_datadir}/applications/%{desktop_vendor}-%{name}.desktop
%else
%{_sysconfdir}/X11/applnk/Multimedia/%{name}.desktop
%endif

%changelog
* Wed Jun  9 2004 Matthias Saou <http://freshrpms.net/> 1.3-0
- Update to 1.3.
- Added missing build requirements.
- Updated description.
- Switched to the new configure/make (still weird, though) build method.

* Sun Jan 04 2004 Dag Wieers <dag@wieers.com> - 1.2.1-0
- Updated to release 1.2.1.

* Thu Oct 09 2003 Dag Wieers <dag@wieers.com> - 1.0.1-0
- Initial package. (using DAR)
