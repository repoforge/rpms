# $Id$

# Authority: dag
# Upstream: Fabrice Bellard <fabrice.bellard@free.fr>
# Upstream: <fftv-devel@lists.sourceforge.net>

Summary: Advanced television viewing and recording program
Name: fftv
Version: 0.7.4
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://fftv.sf.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/fftv/fftv-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: a52dec-devel, faad2-devel, faac-devel, libvorbis-devel
BuildRequires: tcron-devel >= 0.4.3
Requires: xawtv, ffmpeg

%description
fftv is an advanced TV viewing and recording program.

%prep
%setup

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=FFTV Television Viewer
Comment=Advanced television viewing program.
Icon=fftv.png
Exec=fftv
Terminal=false
Type=Application
Categories=Application;AudioVideo;
EOF

%build
%configure \
	--disable-mmx \
	--enable-mp3lame \
	--enable-vorbis \
	--enable-a52 \
	--enable-faad \
	--enable-faac
#	--enable-shared

### FIXME: Make buildsystem use standard autotools directories (Fix upstream please)
%{__perl} -pi.orig -e 's|^(FFTV_SHARE_ICON)=share/(.*)$|$1=$2|;' config.mak

%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications
desktop-file-install --vendor gnome                \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	%{name}.desktop

### FIXME: Clean up buildroot to make it co-exist with ffmpeg/ffmpeg-devel (Fix upstream please)
%{__rm} -f %{buildroot}%{_libdir}/vhook/{drawtext,fish,null}.so

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changelog* CREDITS* COPYING INSTALL README
%doc doc/*.html doc/*.txt
%{_bindir}/*
#%{_libdir}/*.so
%{_libdir}/fftv/
%{_libdir}/vhook/
%{_datadir}/icons/fftv/
%{_datadir}/applications/*.desktop
#%{_includedir}/ffmpeg/

%changelog
* Tue Mar 23 2004 Dag Wieers <dag@wieers.com> - 0.7.4-1
- Updated to release 0.7.4.

* Mon Mar 22 2004 Dag Wieers <dag@wieers.com> - 0.7.3-1
- Updated to release 0.7.3.

* Tue Mar 16 2004 Dag Wieers <dag@wieers.com> - 0.7.2-1
- Updated to release 0.7.2.

* Tue Mar 09 2004 Dag Wieers <dag@wieers.com> - 0.6.9-1
- Updated to release 0.6.9.

* Thu Jan 15 2004 Dag Wieers <dag@wieers.com> - 0.6.4-0
- Initial package. (using DAR)
