# $Id$
# Authority: dag

%{?dtag: %{expand: %%define %dtag 1}}

%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}
%{?rh6:%define _without_freedesktop 1}

%define desktop_vendor rpmforge

Summary: Zinf Audio Player
Name: zinf
Version: 2.2.5
Release: 0.2%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://www.zinf.org/

Source0: http://dl.sf.net/zinf/zinf-%{version}.tar.gz
Source1: zinf-2.2.3-zinf.png
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: nasm, gtk2-devel, gdk-pixbuf-devel, ORBit-devel, libstdc++-devel, gdbm-devel
BuildRequires: zlib-devel, ncurses-devel, libogg-devel, libvorbis-devel, libmusicbrainz-devel
BuildRequires: arts-devel, audiofile-devel, esound-devel, boost-devel, gcc-c++
BuildRequires: id3lib-devel > 3.8.0
%{?!_without_freedesktop:BuildRequires: desktop-file-utils}

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
	--enable-corba \
	--enable-rio
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%{__install} -Dp -m0644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/zinf.png

%if %{?_without_freedesktop:1}0
        %{__install} -Dp -m0644 zinf.desktop %{buildroot}%{_datadir}/gnome/apps/Multimedia/zinf.desktop
%else
        %{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
        desktop-file-install --vendor %{desktop_vendor}    \
                --add-category X-Red-Hat-Base              \
                --dir %{buildroot}%{_datadir}/applications \
                zinf.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING doc/*.txt doc/README.linux doc/WISHLIST NEWS README
%{_bindir}/zinf
%{_libdir}/zinf/
%{_datadir}/zinf/
%{_datadir}/pixmaps/zinf.png
%{?_without_freedesktop:%{_datadir}/gnome/apps/Multimedia/zinf.desktop}
%{!?_without_freedesktop:%{_datadir}/applications/%{desktop_vendor}-zinf.desktop}

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 2.2.5-0.2
- Rebuild for Fedora Core 5.

* Mon Feb 16 2004 Dag Wieers <dag@wieers.com> - 2.2.5-0
- Updated to release 2.2.5.

* Mon Aug 18 2003 Dag Wieers <dag@wieers.com> - 2.2.4-0
- Initial package. (using DAR)
