# $Id$
# Authority: dag
# Upstream: <broadcast$earthling,net>

Summary: Decoder of various derivatives of MPEG standards
Name: libmpeg3
Version: 1.8
Release: 1
License: GPL
Group: System Environment/Libraries
URL: http://heroinewarrior.com/libmpeg3.php3

Source: http://dl.sf.net/heroines/libmpeg3-%{version}-src.tar.bz2
Patch0: libmpeg3-1.7-makefile.patch
Patch1: libmpeg3-1.7-cinelerra_autotools.patch
Patch2: libmpeg3-1.7-cinelerra_hacking.patch
Patch3: libmpeg3-1.7-fix_commented.patch
Patch4: libmpeg3-1.7-spec_in.patch
Patch5: libmpeg3-1.7-pkgconfig.in.patch
Patch6: libmpeg3-1.7-boostrap.patch
# Patches 7/8 from gentoo 
#http://sources.gentoo.org/viewcvs.py/gentoo-x86/media-libs/libmpeg3/files/
Patch7: libmpeg3-1.5.2-gnustack.patch
Patch8: libmpeg3-1.7-memcpy.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: a52dec-devel
BuildRequires: libtool
BuildRequires: nasm

%description
LibMPEG3 decodes the many many derivatives of MPEG standards into
uncompressed data suitable for editing and playback.

libmpeg3 currently decodes:
 - MPEG-1 Layer II/III Audio and program streams
 - MPEG-2 Layer III Audio, program streams and transport streams
 - MPEG-1 and MPEG-2 Video
 - AC3 Audio
 - IFO files
 - VOB files

%package utils
Summary: Utilities from libmpeg3
Group: Applications/Multimedia
Requires: %{name} = %{version}-%{release}

%description utils
LibMPEG3 decodes the many many derivatives of MPEG standards into
uncompressed data suitable for editing and playback.

This package contains utility programs based on libmpeg3.

%package devel
Summary: Development files for libmpeg3
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
LibMPEG3 decodes the many many derivatives of MPEG standards into
uncompressed data suitable for editing and playback.

This package contains files needed to build applications that will use
libmpeg3.

%prep
%setup
#patch0 -p1 -b .makefile
%patch1 -p1
%patch3 -p1 -b .commented
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1 -b .gnustack
#patch8 -p1 -b .memcpy

### Touch docs files:
touch INSTALL README NEWS AUTHORS ChangeLog

### Build autotools
chmod 755 bootstrap
./bootstrap

%build
%configure --enable-shared --disable-static
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}" \
    LIBDIR="%{_libdir}" \
    INSTALL="install -c -p"

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING
%{_libdir}/libmpeg3.so.*

%files utils
%defattr(-, root, root, 0755)
%doc COPYING
%{_bindir}/mpeg3cat
%{_bindir}/mpeg3dump
%{_bindir}/mpeg3peek
%{_bindir}/mpeg3toc

%files devel
%defattr(-, root, root, 0755)
%doc docs/*
%{_libdir}/libmpeg3.so
%{_includedir}/mpeg3/
%{_libdir}/pkgconfig/libmpeg3.pc
%exclude %{_libdir}/libmpeg3.la

%changelog
* Wed Dec 24 2008 Dag Wieers <dag@wieers.com> - 1.8-1
- Updated to release 1.8.

* Fri Jan 11 2008 Dag Wieers <dag@wieers.com> - 1.7-3
- Added patches from Livna.

* Wed Sep 20 2006 Matthias Saou <http://freshrpms.net/> 1.7-2
- Run make twice since there is an EOF error that makes the first run abort.

* Mon Jul  3 2006 Matthias Saou <http://freshrpms.net/> 1.7-1
- Update to 1.7.

* Fri Mar 17 2006 Matthias Saou <http://freshrpms.net/> 1.6-2
- Add -fPIC to the CFLAGS to fix transcode build on x86_64.

* Thu Jan 19 2006 Matthias Saou <http://freshrpms.net/> 1.6-1
- Update to 1.6.
- Split "main" into "utils" (bin) and "devel" (the static lib).
- Add Makefile patch to ease install and get our CFLAGS used.
- Don't enable MMX on x86_64, the x86 asm fails.

* Mon Aug 15 2005 Matthias Saou <http://freshrpms.net/> 1.5.4-5
- Force __USE_LARGEFILE64 to fix FC4 ppc build.

* Fri Apr 22 2005 Matthias Saou <http://freshrpms.net/> 1.5.4-4
- Add gcc4 patch.

* Thu Nov  4 2004 Matthias Saou <http://freshrpms.net/> 1.5.4-3
- Remove unneeded /usr/bin fix, since we don't use "make install".
- Replace -O? with -O1 in optflags since build fails with O2 and gcc 3.4.
- Make nasm mandatory : The configure script won't run without it anyway.
- Use libdir/*.* in order to not catch all debuginfo files too.
- Added -devel provides for now.

* Sat Jun 26 2004 Dag Wieers <dag@wieers.com> - 1.5.4-2
- Fixes for x86_64.

* Wed Apr 07 2004 Dag Wieers <dag@wieers.com> - 1.5.4-1
- Updated to release 1.5.4.

* Mon Sep 08 2003 Dag Wieers <dag@wieers.com> - 1.5.2-0
- Updated to release 1.5.2.

* Wed Feb 12 2003 Dag Wieers <dag@wieers.com> - 1.4-0
- Initial package. (using DAR)
