# $Id$

# Authority: dag

%define dfi %(which desktop-file-install &>/dev/null; echo $?)

Summary: Zinf Audio Player
Name: zinf
Version: 2.2.5
Release: 0
License: GPL
Group: Applications/Multimedia
URL: http://www.zinf.org/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source0: http://dl.sf.net/zinf/zinf-%{version}.tar.gz
Source1: zinf-2.2.3-zinf.png
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: nasm, gtk2-devel, gdk-pixbuf-devel, ORBit-devel, libstdc++-devel, gdbm-devel
BuildRequires: zlib-devel, ncurses-devel, libogg-devel, libvorbis-devel, libmusicbrainz-devel
BuildRequires: arts-devel, audiofile-devel, esound-devel, boost-devel
BuildRequires: id3lib-devel > 3.8.0

%description
The Zinf audio player is a simple, but powerful audio player for Linux
and Win32. It supports MP3, Ogg/Vorbis, WAV and Audio CD playback,
SHOUTcast/Icecast HTTP streaming, RTP streaming, a powerful music browser,
theme support and a download manager. 

%prep
%setup

### Disable freetype support. (Use X-support)
%{__perl} -pi.orig -e 's|test "\$have_freetype" = "true"|false|' configure

%{__cat} <<EOF >zinf.desktop
[Desktop Entry]
Name=Zinf Audio Player
Exec=zinf
Info=Zinf audio player
Icon=zinf.png
Terminal=false
MultipleArgs=false
Type=Application
StartupNotify=true
Categories=Application;AudioVideo;
EOF

%build
%configure \
	--disable-dependency-tracking \
	--enable-corba \
	--enable-rio
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%{__install} -d -m0755 %{buildroot}%{_datadir}/pixmaps/
%{__install} -m0644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/zinf.png

%if %{dfi}
        %{__install} -d -m0755 %{buildroot}%{_datadir}/gnome/apps/Multimedia/
        %{__install} -m0644 %{name}.desktop %{buildroot}%{_datadir}/gnome/apps/Multimedia/
%else
        %{__install} -d -m0755 %{buildroot}%{_datadir}/applications
        desktop-file-install --vendor gnome                \
                --add-category X-Red-Hat-Base              \
                --add-category Application                 \
                --add-category AudioVideo                  \
                --dir %{buildroot}%{_datadir}/applications \
                %{name}.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README doc/README.linux doc/*.txt doc/WISHLIST
%{_bindir}/zinf
%{_libdir}/zinf/
%{_datadir}/zinf/
%{_datadir}/pixmaps/*
%if %{dfi}
        %{_datadir}/gnome/apps/Multimedia/*.desktop
%else
        %{_datadir}/applications/*.desktop
%endif

%changelog
* Mon Feb 16 2004 Dag Wieers <dag@wieers.com> - 2.2.5-0
- Updated to release 2.2.5.

* Mon Aug 18 2003 Dag Wieers <dag@wieers.com> - 2.2.4-0
- Initial package. (using DAR)
