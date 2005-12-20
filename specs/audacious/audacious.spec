# $Id$
# Authority: matthias

Summary: Media player which uses a skinned interface
Name: audacious
Version: 0.1.2
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://audacious-media-player.org/
Source: http://audacious-media-player.org/release/audacious-%{version}.tgz
Patch: audacious-0.1.2-default-alsa.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires(post): /sbin/ldconfig, desktop-file-utils
Requires(postun): /sbin/ldconfig, desktop-file-utils
BuildRequires: gtk2-devel, libglade2-devel, gettext-devel
BuildRequires: libvisual-devel, SDL-devel
BuildRequires: libogg-devel, libvorbis-devel, flac-devel, id3lib-devel
BuildRequires: alsa-lib-devel, esound-devel
%{?_with_gconf:Buildrequires: GConf2-devel}
%{?_with_vfs:BuildRequires: gnome-vfs2-devel}
%{!?_without_lirc:BuildRequires: lirc-devel}
BuildRequires: libsndfile, libsamplerate, libsidplay
BuildRequires: ImageMagick

%description
Audacious is a media player forked from BMP (Beep Media Player) which uses a
skinned interface based on Winamp 2.x skins, and in turn based on XMMS.


%package devel
Summary: Development files for the audacious media player
Group: Development/Libraries
Requires: %{name} = %{version}, pkgconfig

%description devel
Audacious is a media player forked from BMP (Beep Media Player) which uses a
skinned interface based on Winamp 2.x skins, and in turn based on XMMS.

Development files required to develop plugins for audacious.


%prep
%setup
%patch -p1 -b .default-alsa


%build
%configure \
    --disable-rpath \
    %{?_with_gconf:--enable-gconf} \
    %{?_with_vfs:--enable-gnome-vfs} \
    --with-xmms-eq \
    --enable-sid
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}
%find_lang %{name}
%{__mkdir_p} %{buildroot}%{_datadir}/pixmaps
convert audacious/images/audacious_player.xpm \
    %{buildroot}%{_datadir}/pixmaps/audacious.png


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
%{_libdir}/audacious/
%exclude %{_libdir}/audacious/*/*.la
%{_libdir}/libaudacious.so.*
%{_datadir}/applications/audacious.desktop
%{_datadir}/audacious/
%{_datadir}/pixmaps/audacious.png
%{_mandir}/man1/audacious.1*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/audacious/
%exclude %{_includedir}/mp4.h
%{_libdir}/pkgconfig/audacious.pc
%exclude %{_libdir}/libaudacious.la
%{_libdir}/libaudacious.so


%changelog
* Tue Dec 20 2005 Matthias Saou <http://freshrpms.net/> 0.1.2-1
- Initial RPM release.
- Can't seem to get libsamplerate nor sndfile enabled.
- Disable GConf and VFS by default, since nothing seems to work otherwise.

