# $Id$
# Authority: dag

%{?fc1:%define _without_alsa 1}
%{?el3:%define _without_alsa 1}
%{?rh9:%define _without_alsa 1}
%{?rh8:%define _without_alsa 1}
%{?rh7:%define _without_alsa 1}
%{?el2:%define _without_alsa 1}

Summary: DJ software emulating an analog mixer with two playback devices
Name: mixxx
Version: 1.3.2
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
BuildRequires: portaudio, fftw-devel
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}
%{!?_without_alsa:BuildRequires: alsa-lib-devel}

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

%{__cat} <<EOF >mixxx.desktop
[Desktop Entry]
Name=Mixxx DJ Software
Comment=Create your own mixes
Icon=mixxx.png
Exec=mixxx
Terminal=false
Type=Application
Encoding=UTF-8
Categories=Application;AudioVideo;
EOF

%build
source "/etc/profile.d/qt.sh"
# The PWD thing is an ugly hack since relative paths mess everything up...
pushd src
    # Alsa doesn't seem to get enabled for now (unimplemented?)
    ./configure --prefix="${PWD}%{_prefix}" --enable-features="Alsa"
    %{__perl} -pi.orig -e "s|${PWD}||g" Makefile
    # Ugly workaround to not have the docs installed
    %{__perl} -pi.orig -e 's|install_readme install_licence install_copying install_manual ||g' Makefile
    %{__make} %{?_smp_mflags}
popd

%install
%{__rm} -rf %{buildroot}
# That trailing slash is mandatory because of "$(INSTALL_ROOT)usr" lines
%{__make} install -C src \
	INSTALL_ROOT="%{buildroot}/"

%{__install} -D -m0644 src/icon.png %{buildroot}%{_datadir}/pixmaps/mixxx.png

%if %{!?_without_freedesktop:1}0
	%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
	desktop-file-install --vendor net \
		--dir %{buildroot}%{_datadir}/applications \
		mixxx.desktop
%else
	%{__install} -D -m0644 mixxx.desktop %{buildroot}%{_datadir}/gnome/apps/Multimedia/mixxx.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING LICENSE README Mixxx-Manual.pdf
%{_bindir}/*
%{_datadir}/mixxx/
%{_datadir}/pixmaps/mixxx.png
%{!?_without_freedesktop:%{_datadir}/applications/net-mixxx.desktop}
%{?_without_freedesktop:%{_datadir}/gnome/apps/Multimedia/mixxx.desktop}

%changelog
* Mon Jun 14 2004 Matthias Saou <http://freshrpms.net/> 1.3.2-0
- Update to 1.3.2.

* Fri Jun 11 2004 Matthias Saou <http://freshrpms.net/> 1.3.1-0
- Update to 1.3.1.

* Wed Jun  9 2004 Matthias Saou <http://freshrpms.net/> 1.3-0
- Update to 1.3.
- Added missing build requirements.
- Updated description.
- Switched to the new configure/make (still weird, though) build method.

* Sun Jan 04 2004 Dag Wieers <dag@wieers.com> - 1.2.1-0
- Updated to release 1.2.1.

* Thu Oct 09 2003 Dag Wieers <dag@wieers.com> - 1.0.1-0
- Initial package. (using DAR)
