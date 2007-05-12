# $Id$
# Authority: matthias

%{?dist: %{expand: %%define %dist 1}}
%{?fedora: %{expand: %%define fc%{fedora} 1}}

%{!?dist:%define _with_modxorg 1}
%{?el5:%define _with_modxorg 1}
%{?fc6:%define _with_modxorg 1}
%{?fc5:%define _with_modxorg 1}

%define prever 20070108

Summary: Advanced audio and video capturing, compositing, and editing
Name: cinelerra
Version: 2.1
Release: 0.12%{?prever:.%{prever}}
License: GPL
Group: Applications/Multimedia
URL: http://cvs.cinelerra.org/
# Obtained from :
# svn checkout svn://cvs.cinelerra.org/repos/cinelerra/trunk/hvirtual
# cd hvirtual; find . -name .svn | xargs rm -rf
# ./autogen.sh && ./configure && make dist
# mv cinelerra-2.1.tar.gz cinelerra-2.1-svn20060918.tar.gz
Source0: cinelerra-%{version}%{?prever:-svn%{prever}}.tar.gz
Source1: cinelerra-64x64.png
Patch0: cinelerra-2.1-faad2.patch
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
BuildRequires: openexr-devel
BuildRequires: faad2-devel
BuildRequires: libraw1394-devel >= 1.2.0
BuildRequires: libiec61883-devel
# >= 0.5.0 required because of the use of avc1394_vcr_get_timecode2
BuildRequires: libavc1394-devel >= 0.5.0
BuildRequires: x264-devel
BuildRequires: libogg-devel, libvorbis-devel, libtheora-devel
# This seems to actually require OpenGL 2.0 (NVidia proprietary only?)
%{?_with_opengl:BuildRequires: libGL-devel, libGLU-devel}
# Stuff not checked by configure, but still required
BuildRequires: nasm
BuildRequires: libtool
BuildRequires: freetype-devel
# Included ffmpeg snapshot requires this - No longer needed with shared ffmpeg
#BuildRequires: faac-devel
BuildRequires: libjpeg-devel, libpng-devel, libtiff-devel
BuildRequires: libdv-devel
Buildrequires: ffmpeg-devel
BuildRequires: gcc-c++

%description
Heroine Virtual Ltd. presents an advanced content creation system for Linux.


%prep
%setup
%patch0 -p1 -b .faad2
# Add category "AudioVideo", as it ends up in "Others" otherwise
# Replace the ugly small xpm icon with a nicer png one
%{__perl} -pi -e 's|^(Categories=.*)|$1AudioVideo;|g;
                  s|^Icon=.*|Icon=cinelerra.png|g' image/cinelerra.desktop


%build
%configure \
    --with-plugindir=%{_libdir}/cinelerra \
    --with-external-ffmpeg \
%ifarch %{ix86} x86_64
    --enable-mmx \
%endif
%ifarch ppc
    --enable-altivec \
%endif
    --disable-rpath
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall \
    plugindir=%{buildroot}%{_libdir}/cinelerra
%find_lang %{name}

# Remove xpm icon and place png one
%{__rm} -f %{buildroot}%{_datadir}/pixmaps/cinelerra.xpm
%{__install} -m 0644 -p %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/cinelerra.png


%clean
%{__rm} -rf %{buildroot}


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING LICENSE NEWS TODO
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
%{_datadir}/pixmaps/cinelerra.png


%changelog
* Mon Jan  8 2007 Matthias Saou <http://freshrpms.net/> 2.0-0.12.20070108
- Update to today's SVN code.
- Include faad2 patch.
- Try to enable OpenGL, but it seems like only proprietary NVidia libraries
  would work, and the configure detection would need some changes too. So no.
- Switch to using external ffmpeg since the internal fails to build on i386.

* Tue Oct 24 2006 Matthias Saou <http://freshrpms.net/> 2.0-0.10.20061024
- Update to today's SVN code.
- Rebuild against new x264.
- Re-enable _smp_mflags as they work again, yeah!
- Add --with opengl build conditional, disabled for now, needs testing.

* Tue Sep 26 2006 Matthias Saou <http://freshrpms.net/> 2.0-0.9.20060918
- Replace xpm icon with a nicer png one.
- Remove empty AUTHORS file.

* Mon Sep 18 2006 Matthias Saou <http://freshrpms.net/> 2.0-0.8.20060918
- Update to today's SVN code.

* Fri May 12 2006 Matthias Saou <http://freshrpms.net/> 2.0-0.7.20060512
- Update to today's SVN code.
- Remove no longer needed ffmpeg patch.

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

