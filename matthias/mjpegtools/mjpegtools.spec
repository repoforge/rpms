# $Id: mjpegtools.spec,v 1.1 2004/02/26 17:54:30 thias Exp $

Summary: Tools for recording, editing, playing and encoding mpeg video
Name: mjpegtools
Version: 1.6.2
Release: 1.fr
License: GPL
Group: Applications/Multimedia
URL: http://mjpeg.sourceforge.net/
Source: http://prdownloads.sourceforge.net/mjpeg/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: SDL, libjpeg, libpng, gtk+
Requires: libquicktime
%{?_with_avifile:Requires: avifile}
%{?_with_dv:Requires: libdv}
BuildRequires: gcc-c++, SDL-devel, libjpeg-devel, libpng-devel, gtk+-devel
BuildRequires: libquicktime-devel
%{?_with_avifile:BuildRequires: avifile-devel}
%{?_with_dv:BuildRequires: libdv-devel < 0.99}
%{!?_with_dv:BuildConflicts: libdv-devel}
%{?_with_cmov:BuildArch: i686}
%ifarch %{ix86}
BuildRequires: nasm
%endif

%description
The MJPEG-tools are a basic set of utilities for recording, editing, 
playing back and encoding (to mpeg) video under linux. Recording can
be done with zoran-based MJPEG-boards (LML33, Iomega Buz, Pinnacle
DC10(+), Marvel G200/G400), these can also playback video using the
hardware. With the rest of the tools, this video can be edited and
encoded into mpeg1/2 or divx video.

Available rpmbuild rebuild options :
--with : avifile dv cmov


%package devel
Summary: Development headers and libraries for the mjpegtools
Group: Development/Libraries
Requires: %{name} = %{version}

%description devel
This package contains static libraries and C system header files
needed to compile applications that use part of the libraries
of the mjpegtools package.


%prep
%setup -q

%build
%configure \
    --enable-shared \
    --disable-static \
    %{?_with_cmov:--enable-cmov-extension} \
    --with-quicktime
make

%install
rm -rf %{buildroot}
%makeinstall

# Let's remove the static libs for now, as their stripping makes the build fail
# No, give them back as mjpegutils is only built as static and required
#rm -f %{buildroot}%{_libdir}/*.a

%clean
rm -rf %{buildroot}

%post
/sbin/ldconfig
#/sbin/install-info %{_infodir}/mjpeg-howto.info.gz %{_infodir}/dir

%postun
/sbin/ldconfig
#if [ $1 -eq 0 ]; then
#    /sbin/install-info --delete %{_infodir}/mjpeg-howto.info.gz %{_infodir}/dir
#fi
#exit 0

%files
%defattr(-, root, root)
%doc AUTHORS BUGS CHANGES COPYING HINTS PLANS README TODO
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
%{_infodir}/mjpeg-howto.info*
%{_mandir}/man1/*
%{_mandir}/man5/*

%files devel
%defattr(-, root, root)
%{_bindir}/*-config
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.a
%exclude %{_libdir}/*.la
%{_libdir}/*.so

%changelog
* Wed Feb 18 2004 Matthias Saou <http://freshrpms.net/> 1.6.2-1.fr
- Update to 1.6.2.

* Mon Feb  2 2004 Matthias Saou <http://freshrpms.net/> 1.6.1.93-1.fr
- Update to 1.6.1.93.
- Don't remove static libs, as libmjpegutils.a is required by certain apps,
  use --disable-static instead, as that one .a file is built nevertheless.

* Thu Dec  4 2003 Matthias Saou <http://freshrpms.net/> 1.6.1.92-1.fr
- Update to 1.6.1.92.
- Remove static libs for new as their stripping makes the build fail :-(
- Remove the bundled quicktime4linux and libmovtar deps, replaced by cleaner
  libquicktime dependencies.
- Added 'cmov' conditional build, which then forces an i686 build.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 1.6.1.90-1.fr
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

