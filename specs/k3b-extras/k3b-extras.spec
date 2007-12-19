# $Id$
# Authority: dag

# ExclusiveDist: el5

%{?dtag: %{expand: %%define %dtag 1}}

%{!?dtag:%define _with_modxorg 1}
%{?fc7:  %define _with_modxorg 1}
%{?el5:  %define _with_modxorg 1}
%{?fc6:  %define _with_modxorg 1}
%{?fc5:  %define _with_modxorg 1}

%{?fc1:%define _without_kde32 1}
%{?el3:%define _without_kde32 1}
%{?rh9:%define _without_kde32 1}
%{?rh7:%define _without_kde32 1}
%{?el2:%define _without_kde32 1}

%{!?k3b_version:%define k3b_version %(rpm -q k3b --qf '%{RPMTAG_VERSION}' | tail -1)}

Summary: Additional codec plugins for the k3b CD/DVD burning application
Name: k3b-extras
Version: %{k3b_version}
Release: 3
License: GPL
Group: Applications/Multimedia
URL: http://www.k3b.org/

Source: http://dl.sf.net/k3b/k3b-%{version}.tar.bz2
# Patch touches globals, better include this.
Patch0: k3b-0.12.2-statfs.patch
Patch1: k3b-0.11.24-no-bad-gcc.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

ExcludeArch: s390 s390x
BuildRequires: k3b
# Some of these are only to make the configure script happy.
BuildRequires: kdelibs-devel >= 6:3.1, libart_lgpl-devel, arts-devel
BuildRequires: zlib-devel, libpng-devel, libjpeg-devel, libmusicbrainz-devel
BuildRequires: gettext, taglib-devel, libmad-devel, lame-devel, ffmpeg-devel
BuildRequires: libmpcdec-devel, libsndfile-devel
%{!?_without_kde32:BuildRequires: libmng-devel fam-devel glib2-devel alsa-lib-devel esound-devel}
%{?_with_modxorg:BuildRequires: libX11-devel}
%{!?_with_modxorg:BuildRequires: XFree86-devel}

Requires: k3b = %{k3b_version}

Obsoletes: k3b-mp3 <= %{version}-%{release}
Provides: k3b-mp3 = %{version}-%{release}
Obsoletes: k3b-extras-nonfree <= %{version}-%{release}
Provides: k3b-extras-nonfree = %{version}-%{release}

%description
Additional decoder/encoder plugins for k3b, a feature-rich and easy to
handle CD/DVD burning application.

%prep
%setup -n k3b-%{version}

%build
source /etc/profile.d/qt.sh
%configure \
	--disable-rpath \
	--without-flac \
	--without-oggvorbis \
	--with-external-libsamplerate="no" \
	--with-k3bsetup="no" \
	--with-musepack \
	--with-qt-libraries="$QTDIR/lib" \
	--with-sndfile

%{__make} -C libk3bdevice %{?_smp_mflags}
%{__make} -C libk3b %{?_smp_mflags}

%{__make} -C plugins/decoder/ffmpeg %{?_smp_mflags}
%{__make} -C plugins/decoder/libsndfile %{?_smp_mflags}
%{__make} -C plugins/decoder/mp3 %{?_smp_mflags}
%{__make} -C plugins/decoder/musepack %{?_smp_mflags}
%{__make} -C plugins/encoder/lame %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} -C plugins/decoder/ffmpeg install DESTDIR="%{buildroot}"
%{__make} -C plugins/decoder/libsndfile install DESTDIR="%{buildroot}"
%{__make} -C plugins/decoder/mp3 install DESTDIR="%{buildroot}"
%{__make} -C plugins/decoder/musepack install DESTDIR="%{buildroot}"
%{__make} -C plugins/encoder/lame install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%dir %{_libdir}/kde3/
%{_libdir}/kde3/libk3bffmpegdecoder.*
%{_libdir}/kde3/libk3blameencoder.*
%{_libdir}/kde3/libk3blibsndfiledecoder.*
%{_libdir}/kde3/libk3bmaddecoder.*
%{_libdir}/kde3/libk3bmpcdecoder.*
%dir %{_datadir}/apps/
%dir %{_datadir}/apps/k3b/
%dir %{_datadir}/apps/k3b/plugins/
%{_datadir}/apps/k3b/plugins/k3bffmpegdecoder.plugin
%{_datadir}/apps/k3b/plugins/k3blameencoder.plugin
%{_datadir}/apps/k3b/plugins/k3blibsndfiledecoder.plugin
%{_datadir}/apps/k3b/plugins/k3bmaddecoder.plugin
%{_datadir}/apps/k3b/plugins/k3bmpcdecoder.plugin

%changelog
* Mon Dec 17 2007 Dag Wieers <dag@wieers.com> - %{version}-3
- Rebuild against libmpcdec 1.2.6.

* Fri Mar 30 2007 Dag Wieers <dag@wieers.com> - %{version}-2
- Added ffmpeg, libsndfile and mpcdec codecs.

* Sun Mar 05 2006 Dag Wieers <dag@wieers.com> - %{version}-1
- Imported based on Livna SPEC file.
- Initial package. (using DAR)
