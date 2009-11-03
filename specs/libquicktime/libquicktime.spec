# $Id$
# Authority: matthias
# Upstream: <libquicktime-devel$lists,sourceforge,net>


### Problems when compiling against EL4 alsa-lib
%{?el4:%define _without_alsa 1}
%{?el4:%define _without_modxorg 1}

%{?el3:%define _without_alsa 1}
%{?el3:%define _without_gtk24 1}
%{?el3:%define _without_modxorg 1}
%{?el3:%define _without_libswscale 1}

Summary: Library for reading and writing quicktime files
Name: libquicktime
Version: 1.1.3
Release: 1%{?dist}
License: GPL
Group: System Environment/Libraries
URL: http://libquicktime.sourceforge.net/

Source: http://dl.sf.net/libquicktime/libquicktime-%{version}.tar.gz
Patch0: libquicktime-1.0.0-plugin_dir.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++
BuildRequires: lame-devel
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel >= 1.0.8
%{?_with_modxorg:BuildRequires: libXt-devel, libGLU-devel, libXaw-devel, libXv-devel}
%{!?_without_1394:BuildRequires: libraw1394-devel, libavc1394-devel}
%{!?_without_alsa:BuildRequires: alsa-lib-devel}
%{!?_without_dv:BuildRequires: libdv-devel}
%{!?_without_faac:BuildRequires: faac-devel}
%{!?_without_faad2:BuildRequires: faad2-devel}
%{!?_without_ffmpeg:BuildRequires: ffmpeg-devel}
%{!?_without_gtk24:BuildRequires: gtk2-devel >= 2.4}
%{!?_without_vorbis:BuildRequires: libvorbis-devel}
%{!?_without_x264:BuildRequires: x264-devel}
# A bug, the devel libs don't require the main ones :-(
%{?yd3:BuildRequires: libraw1394, libavc1394}

# The configure automatically adds MMX stuff if detected, so x86 becomes i586
#ifarch %{ix86}
#BuildArch: i586
#endif

%description
Libquicktime is a library for reading and writing QuickTime files
on UNIX systems. Video CODECs supported by this library are OpenDivX, MJPA,
JPEG Photo, PNG, RGB, YUV 4:2:2, and YUV 4:2:0 compression.  Supported
audio CODECs are Ogg Vorbis, IMA4, ulaw, and any linear PCM format.

Libquicktime is based on the quicktime4linux library.  Libquicktime add
features such as a GNU build tools-based build process and dynamically
loadable CODECs.

%package devel
Summary: Development files from the libquicktime library
Group: Development/Libraries
Requires: %{name} = %{version}, zlib-devel, pkgconfig

%description devel
libquicktime is a library for reading and writing quicktime files. It
is based on the quicktime4linux library, with many extensions.

You will need to install this development package if you intend to rebuild
programs that need to access quicktime files using libquicktime.

%prep
%setup
%patch0 -p0 -b .plugin_dir

%build
%configure \
%{?_without_libswscale:--disable-libswscale} \
    --enable-gpl \
    --with-cpuflags="%{optflags}" \
%{?_without_alsa:--without-alsa} \
%{?_without_dv:--without-dv} \
%{?_without_vorbis:--without-vorbis}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

# Add compatibility symlink for "quicktime/lqt.h" includes
# (for transcode 1.0.0beta3)
%{__ln_s} -f lqt %{buildroot}%{_includedir}/quicktime

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc COPYING README TODO
%doc %{_mandir}/man1/lqtplay.1*
%{_bindir}/lqtplay
%{_bindir}/lqt_transcode
%{_bindir}/qt*
%{_libdir}/libquicktime.so.*
%dir %{_libdir}/libquicktime/
%{_libdir}/libquicktime/lqt_*.so

%files devel
%defattr(-, root, root, 0755)
%doc doc/*.html doc/*.html doc/apiref/
%{?!_without_gtk24:%{_bindir}/libquicktime_config}
%{_bindir}/lqt-config
%{_datadir}/aclocal/*.m4
%{_includedir}/lqt/
%{_includedir}/quicktime
%{_libdir}/*.so
%{_libdir}/pkgconfig/libquicktime.pc
%exclude %{_docdir}/libquicktime/
%exclude %{_libdir}/libquicktime.la
%exclude %{_libdir}/libquicktime/lqt_*.la

%changelog
* Tue Jul 14 2009 Dag Wieers <dag@wieers.com> - 1.1.3-1
- Updated to release 1.1.3.

* Wed Jul 08 2009 Dag Wieers <dag@wieers.com> - 1.1.2-2
- Rebuild against x264-0.4.20090708.
- Rebuild against ffmpeg-0.5.

* Thu Jun 18 2009 Dag Wieers <dag@wieers.com> - 1.1.2-1
- Updated to release 1.1.2.

* Mon Dec 15 2008 Dag Wieers <dag@wieers.com> - 1.1.1-1
- Updated to release 1.1.1.

* Mon Nov 10 2008 Dag Wieers <dag@wieers.com> - 1.1.0-1
- Updated to release 1.1.0.

* Mon Jul 14 2008 Dag Wieers <dag@wieers.com> - 1.0.3-1
- Updated to release 1.0.3.

* Wed Jan 09 2008 Dag Wieers <dag@wieers.com> - 1.0.2-1
- Updated to release 1.0.2.

* Sun Oct 14 2007 Dag Wieers <dag@wieers.com> - 1.0.1-1
- Updated to release 1.0.1.

* Mon Jun 04 2007 Dag Wieers <dag@wieers.com> - 1.0.0-2
- Rebuild against x264-0.4.20070529 because I missed it.

* Sat Apr 21 2007 Dag Wieers <dag@wieers.com> - 1.0.0-1
- Updated to release 1.0.0.

* Mon Jan  8 2007 Matthias Saou <http://freshrpms.net/> 0.9.10-3
- Include patch to fix runtime against latest faad2.
- Add explicit faac, faad2, x264 buildreqs (ffmpeg was pulling them in anyway).

* Tue Oct 24 2006 Matthias Saou <http://freshrpms.net/> 0.9.10-2
- Include patch to rebuild against latest x264.

* Mon Aug 28 2006 Matthias Saou <http://freshrpms.net/> 0.9.10-1
- Update to 0.9.10.

* Fri Jun 30 2006 Dag Wieers <dag@wieers.com> - 0.9.9-1
- Updated to release 0.9.9.

* Thu Jun  8 2006 Matthias Saou <http://freshrpms.net/> 0.9.8-3
- Add patch to fix plugin_dir on 64bit.

* Fri Mar 17 2006 Matthias Saou <http://freshrpms.net/> 0.9.8-2
- Release bump to drop the disttag number in FC5 build.

* Mon Jan 30 2006 Matthias Saou <http://freshrpms.net/> 0.9.8-1
- Update to 0.9.8.
- Remove static libraries, as nothing actually uses them.
- Remove from %%files no longer included lqtvrplay binary.

* Thu Jan 12 2006 Matthias Saou <http://freshrpms.net/> 0.9.7-3
- Enable modular xorg conditional build.

* Sun Jun  5 2005 Matthias Saou <http://freshrpms.net/> 0.9.7-2
- Add quicktime -> lqt include symlink (required currently for transcode).
- Add zlib-devel devel package requirement.

* Thu May 26 2005 Matthias Saou <http://freshrpms.net/> 0.9.7-1
- Update to 0.9.7, remove all patches (gcc4 build is fixed).
- Remove hack for putting optflags in configure.ac, remove autogen run.
- Remove hack for replacing libdir.
- Remove explicit mmx disabling on non x86, not needed anymore.
- Change gtk+-devel requirement to gtk2-devel.

* Fri May 20 2005 Dag Wieers <dag@wieers.com> - 0.9.6-1
- Updated to release 0.9.6.

* Mon May 16 2005 Dag Wieers <dag@wieers.com> - 0.9.5-1
- Updated to release 0.9.5.

* Thu Apr 21 2005 Matthias Saou <http://freshrpms.net/> 0.9.4-3
- Add _without_ffmpeg on FC4 for now, current ffmpeg doesn't work here anyway.
- Add gcc4 patch, where rt-jpeg is disabled :-/

* Fri Feb  4 2005 Matthias Saou <http://freshrpms.net/> 0.9.4-2
- Added alsa-lib-devel and lame-devel build requirement.
- Fixed missing libtool and autotools build reqs for autogen.sh to work.

* Fri Jan 14 2005 Dag Wieers <dag@wieers.com> - 0.9.4-1
- Updated to release 0.9.4.
- Added lqtvrplay to the package.
- Added pkgconfig entry to the devel package.

* Tue Jul 20 2004 Dag Wieers <dag@wieers.com> - 0.9.3-1
- Updated to release 0.9.3.

* Wed Jun 02 2004 Dag Wieers <dag@wieers.com> - 0.9.2-3
- Fixes for x86_64 from MandrakeCooker.

* Wed May 19 2004 Matthias Saou <http://freshrpms.net/> 0.9.2-3
- Rebuild for Fedora Core 1.

* Fri Apr 16 2004 Matthias Saou <http://freshrpms.net/> 0.9.2-2
- Rebuild against new libdv.

* Tue Nov 11 2003 Matthias Saou <http://freshrpms.net/> 0.9.2-1
- Update to 0.9.2 final.
- Rebuild for Fedora Core 1.

* Tue Apr 22 2003 Matthias Saou <http://freshrpms.net/>
- Fix plugin compilation, thanks to Dag.

* Wed Apr  9 2003 Matthias Saou <http://freshrpms.net/>
- Initial RPM release.

