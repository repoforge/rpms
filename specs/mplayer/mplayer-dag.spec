# Authority: freshrpms
##DarDistcc: 0

%define ffversion cvs-2003-08-07
%define rname MPlayer
%define rversion 20030808

%define plugindir %(xmms-config --input-plugin-dir)
%define dfi %(which desktop-file-install &>/dev/null; echo $?)

Summary: MPlayer, the Movie Player for Linux.
Name: mplayer
Version: 0.90
Release: 4.%{rversion}
License: GPL
Group: Applications/Multimedia
URL: http://mplayerhq.hu/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source0: http://www.mplayerhq.hu/MPlayer/cvs/MPlayer-current.tar.bz2
#Source: http://www2.mplayerhq.hu/MPlayer/releases/%{rname}-%{version}.tar.bz2
Source1: http://ffmpeg.sourceforge.net/cvs/ffmpeg-%{ffversion}.tar.gz
Source2: http://www2.mplayerhq.hu/MPlayer/Skin/Blue-1.0.tar.bz2
Patch0: MPlayer-0.90pre9-runtimemsg.patch
Patch1: MPlayer-0.90-playlist.patch
Patch2: MPlayer-0.90pre10-redhat.patch
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: /usr/bin/find, unzip, w32codec
BuildRequires: libdvdread-devel, libdvdnav-devel, libdv-devel, xvidcore-devel
BuildRequires: gtk+-devel, SDL-devel, lame-devel, libvorbis-devel, libmad-devel
BuildRequires: lzo-devel, aalib-devel, libfame-devel, faad2-devel
BuildRequires: esound-devel, arts-devel, cdparanoia-devel, samba
#BuildRequires: lirc-devel, alsa-lib-devel

Requires: libpostproc = %{version}-%{release}

Requires(pre): /sbin/ldconfig
Requires(post): /sbin/ldconfig

%description
MPlayer is a movie player. It plays most video formats as well as DVDs.
Its big feature is the wide range of supported output drivers. There are also
nice antialiased shaded subtitles and OSD.

%package -n libpostproc
Summary: Video postprocessing library from MPlayer.
Group: System Environment/Libraries

Obsoletes: mplayer-devel
Requires(pre): /sbin/ldconfig
Requires(post): /sbin/ldconfig

%description -n libpostproc
This package contains only MPlayer's libpostproc post-processing library which
other projects such as transcode may use. Install this package if you intend
to use MPlayer, transcode or other similar programs.


%prep
%setup -n %{rname}-%{rversion} -a 1
%{__rm} -rf libavcodec && %{__mv} ffmpeg-%{ffversion}/libavcodec .

%patch0 -p1 -b .runtimemsg
%patch1 -p1 -b .playlist
%patch2 -p0 -b .redhat


%build
%{__find} . -name "CVS" | xargs %{__rm} -rf
./configure \
	--prefix="%{_prefix}" \
	--datadir="%{_datadir}/mplayer" \
	--confdir="%{_sysconfdir}/mplayer" \
	--mandir="%{_mandir}" \
	--with-xmmsplugindir="%{plugindir}" \
	--with-reallibdir="%{_libdir}/real" \
	--enable-gui \
	--enable-largefiles \
	--enable-joystick \
	--enable-opendivx \
	--enable-dynamic-plugins \
	--enable-runtime-cpudetection \
	--enable-xmms \
%{?rh73:--disable-gcc-checking} \
	--enable-i18n \
	--enable-smb \
	--enable-menu \
	--enable-dvdread \
	--enable-win32 \
	--enable-shared-pp \
	--language="all"

#	--enable-dvdnav		(Problems compiling with libdvdnav 0.1.4)
#	--enable-dvdread	(Disabled by libmpdvdkit2)
#	--enable-libfame	(Needs libfame source-dir copied ?)
#	--enable-css		(MPlayer only compatible with <= libcss 0.1)
#	--with-win32libdir="%{_libdir}/win32"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall DESTDIR="%{buildroot}"

### Set the default skin
%{__install} -d -m0755 %{buildroot}%{_datadir}/mplayer/Skin \
			%{buildroot}%{_datadir}/pixmaps
tar -xvj -f %{SOURCE2} -C %{buildroot}%{_datadir}/mplayer/Skin/
%{__perl} -pi -e 's|# skin = default|skin = Blue|' %{buildroot}%{_sysconfig}/mplayer/mplayer.conf

%{__install} -m0644 Gui/mplayer/pixmaps/logo.xpm %{buildroot}%{_datadir}/pixmaps/mplayer-logo.xpm

### Add a link to libpostproc.so.0.0.1
%{__ln_s} -f libpostproc.so.0.0.1 %{buildroot}%{_libdir}/libpostproc.so.0

%{__cat} <<EOF >gnome-%{name}.desktop
[Desktop Entry]
Name=Movie Player
Comment=Play DivX ;-), MPEG and other more
Icon=mplayer-logo.xpm
Exec=gmplayer %f
Terminal=false
MimeType=video/mpeg;video/x-msvideo;video/quicktime
Type=Application
EOF

%if %{dfi}
	%{__install} -d -m0755 %{buildroot}%{_datadir}/gnome/apps/Multimedia/
	%{__install} -m0644 gnome-%{name}.desktop %{buildroot}%{_datadir}/gnome/apps/Multimedia/
%else
	install -d -m0755 %{buildroot}%{_datadir}/applications
	desktop-file-install --vendor "gnome"              \
		--add-category X-Red-Hat-Base              \
		--add-category Application                 \
		--add-category AudioVideo                  \
		--dir %{buildroot}%{_datadir}/applications \
		gnome-%{name}.desktop
%endif

# Install libpostproc if not already installed
test -e %{buildroot}%{_prefix}/lib/libpostproc.so || \
        make prefix=%{buildroot}%{_prefix} -C libavcodec/libpostproc install

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%post -n libpostproc
/sbin/ldconfig

%postun -n libpostproc
/sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog DOCS/ README etc/*.conf
%doc %{_mandir}/man1/*
%doc %{_mandir}/*/man1/*
%config %{_sysconfdir}/mplayer/
%{_bindir}/*
%{_libdir}/libdha.so*
%{_libdir}/mplayer/
%{_datadir}/mplayer/
%{_datadir}/pixmaps/*
%if %{dfi}
        %{_datadir}/gnome/apps/Multimedia/*.desktop
%else
        %{_datadir}/applications/*.desktop
%endif

%files -n libpostproc
%defattr(-, root, root, 0755)
%{_includedir}/postproc/*.h
%{_libdir}/libpostproc.so*

%changelog
* Mon Aug 25 2003 Dag Wieers <dag@wieers.com> - 0.90-4.20030808
- Resync with Matthias Saou (FreshRPMS).

* Wed May 28 2003 Dag Wieers <dag@wieers.com> - 0.90-4
- Added libpostproc.so.0 symbolic link.

* Sun May 11 2003 Dag Wieers <dag@wieers.com> - 0.90-3
- Added libpostproc-dependency to mplayer. (Robbie Vanbrabant)

* Wed Apr 09 2003 Dag Wieers <dag@wieers.com> - 0.90-2
- Renamed devel subpackage to libpostproc.

* Sun Apr 06 2003 Dag Wieers <dag@wieers.com> - 0.90-1
- Build against new (renamed) libxvidcore package.
- Updated to release 0.90.

* Sun Mar 16 2003 Dag Wieers <dag@wieers.com> - 0.89.95-0
- Updated to release 0.90rc5.

* Sun Mar 16 2003 Dag Wieers <dag@wieers.com> - 0.89.94-2
- Added /dev/mga_vid to the %setup section.

* Thu Feb 19 2003 Dag Wieers <dag@wieers.com> - 0.89.94-1
- Rebuild against aalib-1.3.95-0 package.
- Initial package. (using DAR)
