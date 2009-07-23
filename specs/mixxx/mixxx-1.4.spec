# $Id$
# Authority: dag

%{?dtag: %{expand: %%define %dtag 1}}

%{?el4:%define _without_modxorg 1}

%{?el3:%define _without_alsa 1}
%{?el3:%define _without_modxorg 1}

%define desktop_vendor rpmforge

Summary: DJ software emulating an analog mixer with two playback devices
Name: mixxx
Version: 1.4.2
Release: 5
License: GPL
Group: Applications/Multimedia
URL: http://mixxx.sourceforge.net/

Source: http://dl.sf.net/mixxx/mixxx-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%{!?_without_alsa:BuildRequires: alsa-lib-devel}
BuildRequires: audiofile-devel
BuildRequires: desktop-file-utils
BuildRequires: fftw-devel
BuildRequires: gcc-c++
BuildRequires: glib-devel
BuildRequires: libid3tag-devel
BuildRequires: libmad-devel
BuildRequires: libogg-devel
BuildRequires: libsndfile-devel
BuildRequires: libvorbis-devel
BuildRequires: portaudio
BuildRequires: qt-devel >= 3.0
%{?_without_modxorg:BuildRequires: XFree86-devel}
%{!?_without_modxorg:BuildRequires: libXmu-devel, mesa-libGLU-devel}

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
# Create desktop entry
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
    ./configure \
        --prefix="${PWD}%{_prefix}" \
        --enable-alsa
    %{__perl} -pi.orig -e "s|${PWD}||g" Makefile
    # Ugly workaround to not have the docs installed
    %{__perl} -pi.orig -e 's|install_readme install_licence install_copying install_manual ||g' Makefile
    %{__make} %{?_smp_mflags}
popd

%install
%{__rm} -rf %{buildroot}
# That trailing slash is mandatory because of "$(INSTALL_ROOT)usr" lines
%{__make} install -C src INSTALL_ROOT="%{buildroot}/"

%{__install} -Dp -m0644 src/icon.png %{buildroot}%{_datadir}/pixmaps/mixxx.png

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor %{desktop_vendor}    \
    --add-category X-Red-Hat-Base              \
    --dir %{buildroot}%{_datadir}/applications \
    mixxx.desktop

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING LICENSE Mixxx-Manual.pdf README*
%{_bindir}/mixxx
%{_datadir}/mixxx/
%{_datadir}/pixmaps/mixxx.png
%{_datadir}/applications/%{desktop_vendor}-mixxx.desktop

%changelog
* Wed Jul 22 2009 Dag Wieers <dag@wieers.com> - 1.4.2-5
- Rebuild against portaudio-19.

* Fri Mar 17 2006 Matthias Saou <http://freshrpms.net/> 1.4.2-4
- Release bump to drop the disttag number in FC5 build.

* Fri Jan 13 2006 Matthias Saou <http://freshrpms.net/> 1.4.2-3
- Add modular xorg build conditional.

* Wed Nov  3 2004 Matthias Saou <http://freshrpms.net/> 1.4.2-2
- Enable ALSA properly.

* Mon Nov 01 2004 Dag Wieers <dag@wieers.com> -  1.4.2-1
- Updated to release 1.4.2.

* Tue Oct 12 2004 Matthias Saou <http://freshrpms.net/> 1.4-1
- Update to 1.4.

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
