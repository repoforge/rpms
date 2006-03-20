# $Id$
# Authority: matthias

%{?dist: %{expand: %%define %dist 1}}
%{?fedora: %{expand: %%define fc%{fedora} 1}}

%{!?dist:%define _with_modxorg 1}
%{?fc5:%define _with_modxorg 1}

%define prever 20060317

Summary: Advanced audio and video capturing, compositing, and editing
Name: cinelerra
Version: 2.0
Release: 0.6%{?prever:.%{prever}}
License: GPL
Group: Applications/Multimedia
URL: http://cvs.cinelerra.org/
# Obtained from :
# svn checkout svn://cvs.cinelerra.org/repos/cinelerra/trunk/hvirtual
# cd hvirtual; find . -name .svn | xargs rm -rf
# ./autogen.sh && ./configure && make dist
# mv cinelerra-2.0.tar.gz cinelerra-2.0-svn20060317.tar.gz
Source0: cinelerra-2.0%{?prever:-svn%{prever}}.tar.gz
Patch0: cinelerra-2.0-ffmpeg.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
%{?_with_modxorg:BuildRequires: libXt-devel, libXv-devel, libXxf86vm-devel, libXext-devel}
%{!?_with_modxorg:BuildRequires: xorg-x11-devel}
BuildRequires: gettext-devel
Buildrequires: esound-devel
BuildRequires: alsa-lib-devel >= 1.0.2
BuildRequires: mjpegtools-devel
# Required for libuuid
BuildRequires: e2fsprogs-devel
BuildRequires: fftw3-devel
BuildRequires: a52dec-devel
BuildRequires: lame-devel
BuildRequires: libsndfile-devel
BuildRequires: OpenEXR-devel
BuildRequires: faad2-devel
BuildRequires: libraw1394-devel >= 1.2.0
BuildRequires: libiec61883-devel
# >= 0.5.0 required because of the use of avc1394_vcr_get_timecode2
BuildRequires: libavc1394-devel >= 0.5.0
BuildRequires: x264-devel
BuildRequires: libogg-devel, libvorbis-devel, libtheora-devel
# Stuff not checked by configure, but still required
BuildRequires: nasm
BuildRequires: libtool
BuildRequires: freetype-devel
# Included ffmpeg snapshot requires this
BuildRequires: faac-devel
BuildRequires: libjpeg-devel, libpng-devel, libtiff-devel
BuildRequires: libdv-devel

%description
Heroine Virtual Ltd. presents an advanced content creation system for Linux.


%prep
%setup
%patch0 -p1 -b .ffmpeg
# Add category "AudioVideo", as it ends up in "Others" otherwise
%{__perl} -pi -e 's|^(Categories=.*)|$1AudioVideo;|g' image/cinelerra.desktop


%build
%configure \
    --with-plugindir=%{_libdir}/cinelerra \
%ifarch %{ix86} x86_64
    --enable-mmx \
%endif
%ifarch ppc
    --enable-altivec \
%endif
    --disable-rpath
# Using %{?_smp_mflags} makes the libmpeg3 part fail (20060317 SVN)
%{__make}


%install
%{__rm} -rf %{buildroot}
%makeinstall \
    plugindir=%{buildroot}%{_libdir}/cinelerra
%find_lang %{name}


%clean
%{__rm} -rf %{buildroot}


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING LICENSE NEWS TODO
%{_bindir}/cinelerra
%{_bindir}/mpeg3cat
%{_bindir}/mpeg3dump
%{_bindir}/mpeg3toc
%{_bindir}/mplexlo
%exclude %{_includedir}/
%{_libdir}/cinelerra/
%exclude %{_libdir}/*.la
%exclude %{_libdir}/*.so
%{_libdir}/*.so.*
%{_datadir}/applications/*cinelerra.desktop
%{_datadir}/pixmaps/cinelerra.xpm


%changelog
* Fri Mar 17 2006 Matthias Saou <http://freshrpms.net/> 2.0-0.6.20060317
- Update to today's SVN code.
- Remove no longer needed extraqualif patch.
- Add gettext-devel build requirement since "make dist" requires it.
- Remove _smp_mflags since the build fails with it.

* Thu Jan 12 2006 Matthias Saou <http://freshrpms.net/> 2.0-0.5.20051210
- Add modular xorg conditional build.
- Include extraqualif patch to fix build with gcc 4.1.
- Add missing freetype-devel build requirement, weird (FC5).

* Sat Dec 10 2005 Matthias Saou <http://freshrpms.net/> 2.0-0.4.20051210
- Force plugindir, so that 64bit plugins go into /usr/lib64.

* Sat Dec 10 2005 Matthias Saou <http://freshrpms.net/> 2.0-0.3.20051210
- Update to today's SVN code.
- Rebuild against mjpegtools 1.8.0.

* Fri Nov 18 2005 Matthias Saou <http://freshrpms.net/> 2.0-0.2.20051118
- Update to today's svn code.
- Add --enable-altivec for ppc (we require high end machines anyway).

* Tue Oct  4 2005 Matthias Saou <http://freshrpms.net/> 2.0-0.1
- Initial RPM release.
- Include patch to fix local ffmpeg search path.

