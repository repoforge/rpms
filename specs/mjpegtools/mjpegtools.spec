# $Id$
# Authority: matthias
# Upstream: Gernot Ziegler <gz@lysator.liu.se>
# Upstream: <mjpeg-developer@lists.sf.net>

%define jpegmmx_version 0.1.5

Summary: Tools for recording, editing, playing and encoding mpeg video
Name: mjpegtools
Version: 1.6.2
Release: 3
License: GPL
Group: Applications/Multimedia
URL: http://mjpeg.sourceforge.net/
Source0: http://dl.sf.net/mjpeg/mjpegtools-%{version}.tar.gz
Source1: http://dl.sf.net/mjpeg/jpeg-mmx-%{jpegmmx_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: SDL, libjpeg, libpng, gtk+
Requires: libquicktime, libdv
BuildRequires: gcc-c++, SDL-devel, libjpeg-devel, libpng-devel, gtk+-devel
BuildRequires: libquicktime-devel, libdv-devel
# Some other -devel package surely forgot this as a dependency
BuildRequires: alsa-lib-devel
%ifarch %{ix86}
# Optimisations are automatically turned on when detected
# as we build on i686, this will be an i686 only package
BuildArch: i686
BuildRequires: nasm
%endif


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
Requires: %{name} = %{version}

%description devel
This package contains static libraries and C system header files
needed to compile applications that use part of the libraries
of the mjpegtools package.


%prep
%setup -a 1


%build
%ifarch %{ix86}
pushd jpeg-mmx-%{jpegmmx_version}
    ./configure && %{__make} %{?_smp_mflags}
popd
%endif
# ### FIXME Stripping of libmjpegutils.a fails (hence --disable-static)
%configure \
    --enable-shared \
    --disable-static \
%ifarch %{ix86}
    --with-jpeg-mmx="`pwd`/jpeg-mmx-%{jpegmmx_version}" \
%endif
    --with-quicktime
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall

# Let's remove the static libs for now, as their stripping makes the build fail
# No, give them back as mjpegutils is only built as static and required
#rm -f %{buildroot}%{_libdir}/*.a


%clean
%{__rm} -rf %{buildroot}

%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%files
%defattr(-, root, root, 0755)
%doc AUTHORS BUGS CHANGES COPYING HINTS PLANS README TODO
%doc %{_mandir}/man?/*
%doc %{_infodir}/*.info*
%{?_with_avifile:%{_bindir}/divxdec}
%{_bindir}/glav
#%{_bindir}/img2mpg
%{_bindir}/jpeg2yuv
%{_bindir}/lav*
%{_bindir}/mp*
%{_bindir}/pgmtoy4m
%{_bindir}/png2yuv
%{_bindir}/ppm*
%{_bindir}/testrec
%{_bindir}/y4m*
%{_bindir}/ypipe
%{_bindir}/yuv*
%{_bindir}/*.flt
%{_libdir}/*.so.*
%exclude %{_infodir}/dir

%files devel
%defattr(-, root, root, 0755)
%{_bindir}/*-config
%{_includedir}/mjpegtools/
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.a
%{_libdir}/*.so
%exclude %{_libdir}/*.la


%changelog
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

