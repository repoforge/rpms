# $Id$
# Authority: matthias
# Upstream: Gernot Ziegler <gz$lysator,liu,se>
# Upstream: <mjpeg-developer$lists,sourceforge,net>

%{?el4:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}

%{?el3:%define _without_alsa 1}
%{?el2:%define _without_alsa 1}

Summary: Tools for recording, editing, playing and encoding mpeg video
Name: mjpegtools
Version: 1.9.0
Release: 1%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://mjpeg.sourceforge.net/

Source: http://dl.sf.net/mjpeg/mjpegtools-%{version}.tar.gz
#Source: mjpegtools-%{version}cvs.tar.gz
Patch0: mjpegtools-1.9.0-gcc44.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: arts-devel
BuildRequires: SDL-devel
BuildRequires: SDL_gfx-devel
BuildRequires: gcc-c++
BuildRequires: gtk2-devel
BuildRequires: libdv-devel
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: libquicktime-devel
%{!?_without_modxorg:BuildRequires: libXt-devel, libXxf86dga-devel}
# Some other -devel package surely forgot this as a dependency
%{!?_without_alsa:BuildRequires: alsa-lib-devel}
# Required by some other package, it seems... (SDL-devel is a good guess)
Requires(post): /sbin/install-info, /sbin/ldconfig
Requires(preun): /sbin/install-info

%description
The MJPEG-tools are a basic set of utilities for recording, editing,
playing back and encoding (to mpeg) video under linux. Recording can
be done with zoran-based MJPEG-boards (LML33, Iomega Buz, Pinnacle
DC10(+), Marvel G200/G400), these can also playback video using the
hardware. With the rest of the tools, this video can be edited and
encoded into mpeg1/2 or divx video.

%package devel
Summary: Development headers and libraries for the mjpegtools
Group: Development/Libraries
Requires: %{name} = %{version}, pkgconfig

%description devel
This package contains static libraries and C system header files
needed to compile applications that use part of the libraries
of the mjpegtools package.

%prep
%setup -n %{name}-%{version}
%patch0 -p0

%build
%configure \
    --disable-static
# Don't use %{?_smp_mflags}, the build can fail! (1.8.0)
%{__make}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%{__rm} -f %{buildroot}%{_infodir}/dir || :

%clean
%{__rm} -rf %{buildroot}

%post
/sbin/ldconfig
/sbin/install-info %{_infodir}/mjpeg-howto.info.gz %{_infodir}/dir

%preun
if [ $1 -eq 0 ]; then
    /sbin/install-info --delete %{_infodir}/mjpeg-howto.info.gz %{_infodir}/dir
fi

%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%doc AUTHORS BUGS CHANGES COPYING HINTS PLANS README TODO
%doc %{_infodir}/mjpeg-howto.info*
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/mjpegtools/
%{_libdir}/pkgconfig/mjpegtools.pc
%{_libdir}/*.so
%exclude %{_libdir}/*.la

%changelog
* Sun Nov 14 2010 Dag Wieers <dag@wieers.com> - 1.9.0-1
- Updated to release 1.9.0.

* Mon Apr 27 2009 Dag Wieers <dag@wieers.com> - 1.9.0-0.6.rc2
- Rebuild against SDL_gfx 2.0.19.

* Wed Mar  7 2007 Matthias Saou <http://freshrpms.net/> 1.9.0-0.5.rc2
- Update to 1.9.0rc2.

* Tue Jan 16 2007 Matthias Saou <http://freshrpms.net/> 1.9.0-0.4
- Disable forcing our optflags as they seem to work again "the simple way".

* Thu Dec 28 2006 Dag Wieers <dag@wieers.com> - 1.9.0-0.3
- Rebuild against SDL_gfx 2.0.15.

* Mon Dec 11 2006 Matthias Saou <http://freshrpms.net/> 1.9.0-0.2
- Update to today's CVS.
- Remove jpeg-mmx as it's been officially discontinued (very little to no
  speed improvement on modern x86 CPUs).
- Remove nasm build requirement (was used by jpeg-mmx).
- Make sure we use *only* our CFLAGS, thus make the package i386 again instead
  of i686. I wonder how much this impacts performance, not much in theory.

* Wed Oct 18 2006 Matthias Saou <http://freshrpms.net/> 1.9.0-0.1
- Update to today's CVS to fix ppc build.

* Wed Mar 22 2006 Matthias Saou <http://freshrpms.net/> 1.8.0.1-1
- Update to today's CVS to fix libquicktime 0.9.8 compatibility and ppc build.
- Add missing modular X build requirements.
- Add SDL_gfx support.

* Fri Mar 17 2006 Matthias Saou <http://freshrpms.net/> 1.8.0-3
- Include jpeg-mmx patch to fix build on FC5.

* Thu Jan 12 2006 Matthias Saou <http://freshrpms.net/> 1.8.0-2
- Add -fpermissive to CFLAGS for now, as otherwise the build fails on FC5.
- Fix mmx conditional to actually get jpeg-mmx used.
- Disable mmx on FC5 for now, since the included jpeg-mmx fails to build.

* Fri Dec  9 2005 Matthias Saou <http://freshrpms.net/> 1.8.0-1
- Update to 1.8.0.
- Remove %%{?_smp_mflags}, as the build failed for me on x86_64 with -j4.
- Remove obsolete PPC-only mplex patch.

* Mon Aug 15 2005 Matthias Saou <http://freshrpms.net/> 1.6.3-0.2.rc2
- Update to 1.6.3-rc2.
- Include mjpegtools-1.6.3-rc2-mplex.patch (for ppc only, fails for others).

* Sun Jun  5 2005 Matthias Saou <http://freshrpms.net/> 1.6.3-0.1.rc1
- Update to 1.6.3-rc1.
- Don't enable "MPEG Z/Alpha" anymore : It fails to compile.
- Clean up configure options and patches : Static lib doesn't make stripping
  fail anymore, explicit -fPIC no longer required, etc.
- Update gtk build requirement to gtk2 for glav.
- Remove no longer included *-config binaries (only pkgconfig now).
- Re-enable install-info calls, things are working again now.

* Thu May  5 2005 Matthias Saou <http://freshrpms.net/> 1.6.2-5
- Add gcc4 patch, a backport of recent CVS changes.
- Disable libquicktime in configure for now.
- Add mjpegtools-1.6.2-quantize_x86.patch (ASM changes from CVS).

* Mon Nov 15 2004 Matthias Saou <http://freshrpms.net/> 1.6.2-4
- Add gcc34 patch from bugs.gentoo.org #48890.
- Add gcc34 patch to jpeg-mmx from linuxfromscratch commit 629.
- (Re?)-add -fPIC to build on x86_64.
- Seems like static lib stripping works again on x86, but not x86_64.

* Mon Aug 30 2004 Matthias Saou <http://freshrpms.net/> 1.6.2-3
- Added install-info calls... not, "no info dir entry" :-(

* Wed May 19 2004 Matthias Saou <http://freshrpms.net/> 1.6.2-3
- Rebuild for Fedora Core 2.
- Bundle jpeg-mmx again, seems to be the only way to use it
  (can't be packaged separately and included sanely).
- Removed obsolete avifile conditionnal build.
- Removed no longer working cmov conditional build.

* Sun Apr 11 2004 Dag Wieers <dag@wieers.com> - 1.6.2-2
- Rebuild against libdv 0.102.

* Wed Feb 18 2004 Matthias Saou <http://freshrpms.net/> 1.6.2-1
- Update to 1.6.2.

* Mon Feb  2 2004 Matthias Saou <http://freshrpms.net/> 1.6.1.93-1
- Update to 1.6.1.93.
- Don't remove static libs, as libmjpegutils.a is required by certain apps,
  use --disable-static instead, as that one .a file is built nevertheless.

* Thu Dec  4 2003 Matthias Saou <http://freshrpms.net/> 1.6.1.92-1
- Update to 1.6.1.92.
- Remove static libs for new as their stripping makes the build fail :-(
- Remove the bundled quicktime4linux and libmovtar deps, replaced by cleaner
  libquicktime dependencies.
- Added 'cmov' conditional build, which then forces an i686 build.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 1.6.1.90-1
- Update to 1.6.1.90.
- Added new info files and binaries.
- Rebuild for Fedora Core 1.

* Fri Apr 25 2003 Matthias Saou <http://freshrpms.net/>
- Added missing defattr for the devel package.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.
- Out goes libmovtar!
- Disable dv by default, as build fails with the latest 0.99.

* Sat Jan 11 2003 Matthias Saou <http://freshrpms.net/>
- Changed avifile to be disabled by default.

* Wed Dec 11 2002 Matthias Saou <http://freshrpms.net/>
- Spec file cleanup.

* Wed May 20 2002 Thomas Vander Stichele <thomas@apestaart.org>
- Added BuildRequires and Requires

* Tue Feb 12 2002 Geoffrey T. Dairiki <dairiki@dairiki.org>
- Fix spec file to build in one directory, etc...

* Thu Dec 06 2001 Ronald Bultje <rbultje@ronald.bitfreak.net>
- separated mjpegtools and mjpegtools-devel
- added changes by Marcel Pol <mpol@gmx.net> for cleaner RPM build

* Wed Jun 06 2001 Ronald Bultje <rbultje@ronald.bitfreak.net>
- 1.4.0-final release, including precompiled binaries (deb/rpm)

