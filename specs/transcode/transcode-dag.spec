# Authority: freshrpms
# Upstream: Thomas Östreich <ostreich@theorie.physik.uni-goettingen.de>
# Upstream: Tilmann Bitterberg <transcode@tibit.org>

Summary: Linux video stream processing utility
Name: transcode
Version: 0.6.11
Release: 0
License: GPL
Group: Applications/Multimedia
URL: http://zebra.fh-weingarten.de/~transcode/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://zebra.fh-weingarten.de/~transcode/pre/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: avifile-devel >= 0.6.0, ImageMagick-devel >= 5.4.3, lame-devel >= 3.89
BuildRequires: libogg-devel, libvorbis-devel, libdvdread-devel, libdv-devel
BuildRequires: libfame-devel, mjpegtools-devel, SDL-devel, libpostproc
BuildRequires: libxml2-devel, libjpeg-devel, a52dec-devel, glib-devel, xvidcore-devel
BuildRequires: nasm

%description
transcode is a linux text-console utility for video stream processing,
running on a platform that supports shared libraries and threads.
Decoding and encoding is done by loading modules that are responsible
for feeding transcode with raw video/audio streams (import modules) and
encoding the frames (export modules). It supports elementary video and
audio frame transformations, including de-interlacing or fast resizing
of video frames and loading of external filters.

%prep
%setup

%build
%configure \
	--x-includes="/usr/X11R6/include/X11" \
	--disable-dependency-tracking \
	--enable-v4l \
	--with-a52 \
	--with-avifile-mods \
	--with-dv \
	--with-dvdread \
	--with-lame \
	--with-libjpeg-mods \
	--with-libmpeg3 \
	--with-lzo \
	--with-magick-mods="no" \
	--with-ogg \
	--with-openqt \
	--with-qt \
	--with-vorbis \
	--with-x \
	--with-xvidcore
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall \
	docsdir="../installed-docs/"

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/transcode/*.la

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING README TODO installed-docs/*
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_libdir}/transcode/
#exclude %{_libdir}/transcode/*.la

%changelog
* Sat Nov 08 2003 Dag Wieers <dag@wieers.com> - 0.6.11-0
- Updated to release 0.6.11.

* Sat Sep 27 2003 Dag Wieers <dag@wieers.com> - 0.6.10-0
- Updated to release 0.6.10.

* Mon Sep 08 2003 Dag Wieers <dag@wieers.com> - 0.6.9-0
- Updated to release 0.6.9.

* Sat Jul 12 2003 Dag Wieers <dag@wieers.com> - 0.6.8-0
- Updated to release 0.6.8.

* Thu Jul 03 2003 Dag Wieers <dag@wieers.com> - 0.6.7-0
- Updated to release 0.6.7.

* Fri May 02 2003 Dag Wieers <dag@wieers.com> - 0.6.4-0
- Updated to release 0.6.4.

* Wed Apr 16 2003 Dag Wieers <dag@wieers.com> - 0.6.3.20030409-0
- Updated to release 0.6.4.20030409.

* Thu Apr 10 2003 Dag Wieers <dag@wieers.com> - 0.6.3.20030325-3
- Build against new (split) libpostproc package.

* Tue Apr 08 2003 Dag Wieers <dag@wieers.com> - 0.6.3.20030325-2
- Build against new (renamed) libxvidcore package.

* Sun Mar 30 2003 Dag Wieers <dag@wieers.com> - 0.6.3.20030325-0
- Updated to release 0.6.4.20030325.
- Rebuild with explicit options.
- Fixed the problem with -lioaux.

* Mon Feb 17 2003 Dag Wieers <dag@wieers.com> - 0.6.3-0
- Rebuild against newer libdvdread-0.9.4.

* Sat Feb 01 2003 Dag Wieers <dag@wieers.com> - 0.6.2-0
- Initial package. (using DAR)
