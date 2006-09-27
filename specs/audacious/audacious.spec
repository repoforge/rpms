# $Id$
# Authority: matthias
# ExcludeDist: fc6

%{?dist: %{expand: %%define %dist 1}}
%{?fedora: %{expand: %%define fc%{fedora} 1}}

%{!?dist:%define _with_modxorg 1}
%{?fc5:%define _with_modxorg 1}

Summary: Media player which uses a skinned interface
Name: audacious
Version: 1.1.2
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://audacious-media-player.org/
Source: http://audacious-media-player.org/release/audacious-%{version}.tgz
Patch0: audacious-0.1.2-default-alsa.patch
Patch1: audacious-1.1.0-xmms-skins.patch
Patch2: audacious-1.1.0-default-skin.patch
Patch3: audacious-1.1.0-no-rpath.patch
Patch4: audacious-1.1.0-quoting.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires(post): /sbin/ldconfig, desktop-file-utils
Requires(postun): /sbin/ldconfig, desktop-file-utils
BuildRequires: gtk2-devel, libglade2-devel, gettext-devel
BuildRequires: libvisual-devel, SDL-devel, gcc-c++
BuildRequires: libogg-devel, libvorbis-devel, flac-devel, id3lib-devel
BuildRequires: alsa-lib-devel, esound-devel, libmpcdec-devel, taglib-devel
%{!?_without_vfs:BuildRequires: gnome-vfs2-devel}
%{!?_without_gconf:BuildRequires: GConf2-devel}
%{!?_without_lirc:BuildRequires: lirc-devel}
BuildRequires: libsndfile-devel, libsamplerate-devel, libsidplay-devel
Buildrequires: libmusicbrainz-devel, curl-devel, bc, libcdio-devel
BuildRequires: jack-audio-connection-kit-devel, arts-devel, libmodplug-devel
%{?_with_modxorg:BuildRequires: libXext-devel, libXt-devel}

%description
Audacious is a media player forked from BMP (Beep Media Player) which uses a
skinned interface based on Winamp 2.x skins, and in turn based on XMMS.


%package devel
Summary: Development files for the audacious media player
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}, gtk2-devel, pkgconfig
%{!?_without_vfs:Requires: gnome-vfs2-devel}
%{!?_without_gconf:Requires: GConf2-devel}
%{?_with_modxorg:Requires: libXext-devel, libXt-devel}

%description devel
Audacious is a media player forked from BMP (Beep Media Player) which uses a
skinned interface based on Winamp 2.x skins, and in turn based on XMMS.

Development files required to develop plugins for audacious.


%package arts
Summary: Audacious output plugin for the analog realtime synthesizer
Group: Applications/Multimedia
Requires: %{name} = %{version}-%{release}

%description arts
This package provides an Audacious output plugin that uses aRts (analog
realtime synthesizer) sound system that KDE uses.


%package esd
Summary: Audacious output plugin for the Enlightened Sound Daemon
Group: Applications/Multimedia
Requires: %{name} = %{version}-%{release}

%description esd
This package provides an Audacious output plugin that uses the Enlightened
Sound Daemon.


%package jack
Summary: Audacious output plugin for the JACK sound service
Group: Applications/Multimedia
Requires: %{name} = %{version}-%{release}

%description jack
This package provides an Audacious output plugin that uses the JACK sound
service.


%prep
%setup
%patch0 -p1 -b .default-alsa
%patch1 -p1 -b .xmms-skins
%patch2 -p1 -b .default-skin
%patch3 -p1 -b .no-rpath
%patch4 -p1 -b .quoting


%build
%configure \
    --disable-rpath \
    %{!?_without_gconf:--enable-gconf} \
    %{!?_without_vfs:--enable-gnome-vfs} \
    --with-xmms-eq \
    --enable-sid \
    --enable-amidiplug
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}
%find_lang %{name}


%clean
%{__rm} -rf %{buildroot}


%post
/sbin/ldconfig
update-desktop-database -q || :

%postun
/sbin/ldconfig
update-desktop-database -q || :


%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_bindir}/audacious
%{_bindir}/audtool
%{_libdir}/audacious/
%dir %{_libdir}/amidi-plug/
%dir %{_libdir}/amidi-plug/backends/
%{_libdir}/amidi-plug/backends/ap-alsa.so
%{_libdir}/amidi-plug/backends/ap-dummy.so
%exclude %{_libdir}/audacious/Output/libarts.so
%exclude %{_libdir}/audacious/Output/libESD.so
%exclude %{_libdir}/audacious/Output/libjackout.so
%{_libdir}/libaudacious.so.*
%{_datadir}/applications/audacious.desktop
%{_datadir}/audacious/
%{_datadir}/pixmaps/audacious.png
%{_mandir}/man1/audacious.1*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/audacious/
%{_libdir}/pkgconfig/audacious.pc
%{_libdir}/libaudacious.so

%files arts
%defattr(-, root, root, 0755)
%{_bindir}/audacious-arts-helper
%{_libdir}/audacious/Output/libarts.so

%files esd
%defattr(-, root, root, 0755)
%{_libdir}/audacious/Output/libESD.so

%files jack
%defattr(-, root, root, 0755)
%{_libdir}/audacious/Output/libjackout.so


%changelog
* Fri Sep 15 2006 Matthias Saou <http://freshrpms.net/> 1.1.2-1
- Update to 1.1.2.
- ExcludeDist fc6 since it's in Extras.
- Remove no longer present amidi files.

* Wed Jul 19 2006 Matthias Saou <http://freshrpms.net/> 1.1.0-1
- Update to 1.1.0.
- No longer convert the xpm icon as a png is installed by default.
- Add modplug, jack and arts support.
- Enable gnome-vfs by default now.
- Add new audtool and amidi-plug libraries.
- Include all patches from Fedora Extras, update rpath and quoting patches.
- Split off jack, esd and arts sub-packages for compatibility with Extras.

* Wed Apr 19 2006 Matthias Saou <http://freshrpms.net/> 1.0.0-1
- Update to 1.0.0.
- Remove the install fix, but the new Makefile still symlinks in absolute :-/

* Wed Mar 22 2006 Matthias Saou <http://freshrpms.net/> 0.2.2-3
- Add modular X requirements to the devel sub-package to fix plugins build.

* Fri Mar 17 2006 Matthias Saou <http://freshrpms.net/> 0.2.2-2
- Release bump to drop the disttag number in FC5 build.

* Mon Mar 13 2006 Matthias Saou <http://freshrpms.net/> 0.2.2-1
- Update to 0.2.2... the main .so isn't versionned anymore, something wrong :-(
- Add libmusicbrainz and curl build requirements (for the Scrobbler).
- No longer exclude .la files and mp4.h, they're not installed anymore (good!).
- Add install fix to prevent absolute symlinks with buildroot in them.

* Mon Feb 13 2006 Matthias Saou <http://freshrpms.net/> 0.2-2
- Rebuild against proper FC4 gtk2 to fix unexisting dependencies.

* Thu Feb  9 2006 Matthias Saou <http://freshrpms.net/> 0.2-1
- Update to 0.2.
- Enable GConf, as things seem fine with it now.
- Opening files still fails for me when gnome-vfs is enabled :-(
- Force --enable-amidiplug since configure checks for /proc entries.
- Add libmpcdec-devel and taglib-devel build requirements to enable musepack.
- Require the -devel libsamplerate, libsndfile and libsidplay, d'oh!
- Add requirements to the devel package to match what pkgconfig expects.

* Tue Dec 20 2005 Matthias Saou <http://freshrpms.net/> 0.1.2-1
- Initial RPM release.
- Can't seem to get libsamplerate nor sndfile enabled.
- Disable GConf and VFS by default, since nothing seems to work otherwise.

