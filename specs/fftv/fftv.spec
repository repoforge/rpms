# $Id$

# Authority: dag
# Upstream: Fabrice Bellard <fabrice.bellard@free.fr>
# Upstream: <fftv-devel@lists.sourceforge.net>

Summary: Advanced TV program.
Name: fftv
Version: 0.6.9
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://fftv.sf.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/fftv/fftv-%{version}.tar.bz2
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: a52dec-devel, faad2-devel, faac-devel, libvorbis-devel
BuildRequires: tcron-devel >= 0.4.3
Requires: xawtv

%description
fftv is an advanced TV iviewing and recording program.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

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

### FIXME: Remove asf-enc.o in order to get it to build. (Please fix upstream)
%{__perl} -pi.orig -e 's|sierravmd.o asf-enc.o|sierravmd.o|' libavformat/Makefile

%build
%configure \
	--disable-mmx \
	--enable-mp3lame \
	--enable-vorbis \
	--enable-a52 \
	--enable-faad \
	--enable-faac \
	--enable-shared

### FIXME: Make buildsystem use standard autotools directories (Fix upstream please)
%{__perl} -pi.orig -e '
		s|=/usr/lib|=\$(libdir)|;
		s|=/usr/share|=\$(datadir)|;
	' config.mak

%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}

### FIXME: Makefile doesn't create target directories (Please fix upstream)
%{__install} -d -m0755 %{buildroot}%{_bindir}

%makeinstall

### FIXME: Fix binaries to co-exist with ffmpeg. (Please fix upstream)
%{__mv} -f %{buildroot}%{_bindir}/ffmpeg %{buildroot}%{_bindir}/fftv
%{__ln_s} -f fftv %{buildroot}%{_bindir}/ffradio

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications
desktop-file-install --vendor gnome                \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	%{name}.desktop

### Clean up buildroot
%{__rm} -f %{buildroot}%{_bindir}/{ffmpeg,ffplay,ffserver} \
		%{buildroot}%{_libdir}/*.so \
		%{buildroot}%{_libdir}/vhook/{drawtext,fish,null}.so
%{__rm} -rf %{buildroot}%{_includedir}/ffmpeg/

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
* Tue Mar 09 2004 Dag Wieers <dag@wieers.com> - 0.6.9-1
- Updated to release 0.6.9.

* Thu Jan 15 2004 Dag Wieers <dag@wieers.com> - 0.6.4-0
- Initial package. (using DAR)
