# Authority: freshrpms
%define rversion cvs-2003-07-01

Summary: Hyper fast MPEG1/MPEG4/H263/RV and AC3/MPEG audio encoder.
Name: ffmpeg
Version: 0.4.7
Release: 0.20030701
License: GPL
Group: Applications/Multimedia
URL: http://ffmpeg.sourceforge.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://prdownloads.sourceforge.net/ffmpeg/%{name}-%{rversion}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: imlib2-devel, libvorbis-devel, a52dec-devel, lame-devel, zlib-devel
BuildRequires: faad2-devel, imlib2-devel
Provides: libavcodec.so
Provides: libavcodec-CVS-2003-07-01.so

%description
FFmpeg is the first complete and free Internet Live Audio and Video
Broadcasting solution. FFMpeg aims at being the command line tool to
handle audio and video. It is a "three-in-one" solution.

FFmpeg includes a soft VCR capable of encoding in many different
formats simultaneously, a streaming server for Netcasting multimedia
and is available under the GNU General Public License.

FFmpeg generates streaming files, in many popular formats
simultaneously, faster than any other solution.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n %{name}-%{rversion}

%build
%configure \
	--enable-a52bin \
	--enable-faad \
	--enable-faadbin \
	--enable-mp3lame \
	--enable-vorbis \
	--enable-shared \
	--disable-mmx
### FIXME: Disable MMX to make it build. (Please fix upstream)
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__install} -m0644 libavcodec/libavcodec.a %{buildroot}%{_libdir}

%{__install} -d -m0755 %{buildroot}%{_libdir}/libavcodec/
%{__ln_s} -f %{_libdir}/libavcodec.a %{buildroot}%{_libdir}/libavcodec/

%{__rm} -f doc/Makefile

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%doc Changelog COPYING CREDITS README VERSION doc/*
%{_bindir}/*
%{_libdir}/*.so
%{_libdir}/vhook/

%files devel
%{_includedir}/ffmpeg/
%{_libdir}/*.a
%{_libdir}/libavcodec/

%changelog
* Thu Sep 18 2003 Dag Wieers <dag@wieers.com> - 0.4.7-0.20030701
- Updated to release cvs-2003-07-01.
- Resync with Matthias Saou (FreshRPMS).

* Thu Feb 20 2003 Dag Wieers <dag@wieers.com> - 0.4.6-2
- Added link for compatibility.

* Wed Feb 19 2003 Dag Wieers <dag@wieers.com> - 0.4.6-1
- Added devel package and shared library.
- Build against new lame-3.93.1-1 package.

* Sun Feb 09 2003 Dag Wieers <dag@wieers.com> - 0.4.6-0
- Updated to 0.4.6. (using DAR)

* Sun Aug 19 2001 Dag Wieers <dag@wieers.com> - 0.4.5-1
- Initial package
