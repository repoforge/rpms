# $Id$
# Authority: dag
# Upstream: <libmpeg2-devel$lists,sf,net>

%{?fedora: %{expand: %%define fc%{fedora} 1}}

%{?el4:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}

Summary: Free MPEG-1 and MPEG-2 video stream decoder
Name: libmpeg2
Version: 0.5.1
Release: 2%{?dist}
License: LGPL
Group: System Environment/Libraries
URL: http://libmpeg2.sourceforge.net/

Source: http://libmpeg2.sourceforge.net/files/libmpeg2-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: SDL-devel, pkgconfig, gcc-c++
%{!?_without_modxorg:BuildRequires: libXt-devel, libXv-devel}
%{?_without_modxorg:BuildRequires: XFree86-devel}

%description
A free library for decoding MPEG-2 and MPEG-1 video streams.

%package utils
Summary: Utilities from libmpeg2
Group: Applications/Multimedia
Requires: %{name} = %{version}-%{release}
Obsoletes: mpeg2dec <= %{version}-%{release}
Provides: mpeg2dec = %{version}-%{release}

%description utils
LibMPEG2 decodes the many many derivatives of MPEG standards into
uncompressed data suitable for editing and playback.

This package contains utility programs based on libmpeg2.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Obsoletes: mpeg2dec-devel <= %{version}-%{release}
Provides: mpeg2dec-devel = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
%configure \
%ifnarch %{ix86}
    --disable-accel-detect \
%endif
    --disable-static \
    --enable-shared
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%{_libdir}/libmpeg2.so.*
%{_libdir}/libmpeg2convert.so.*

%files utils
%doc %{_mandir}/man1/extract_mpeg2.1*
%doc %{_mandir}/man1/mpeg2dec.1*
%{_bindir}/corrupt_mpeg2
%{_bindir}/extract_mpeg2
%{_bindir}/mpeg2dec

%files devel
%defattr(-, root, root, 0755)
%doc CodingStyle doc/*.c doc/*.txt
%{_libdir}/libmpeg2.so
%{_libdir}/libmpeg2convert.so
%{_includedir}/mpeg2dec/
%{_libdir}/pkgconfig/libmpeg2.pc
%{_libdir}/pkgconfig/libmpeg2convert.pc
%exclude %{_libdir}/libmpeg2.la
%exclude %{_libdir}/libmpeg2convert.la

%changelog
* Wed Jul 23 2008 Dag Wieers <dag@wieers.com> - 0.5.1-2
- Added --enable-shared to address SELinux text relocation issues. (David Savinkoff)

* Fri Jul 18 2008 Dag Wieers <dag@wieers.com> - 0.5.1-1
- Updated to release 0.5.1.

* Thu May 31 2007 Matthias Saou <http://freshrpms.net/> 0.4.1-2
- Include patch for bootstrap to work with automake 1.10 (F7).

* Wed Mar  7 2007 Matthias Saou <http://freshrpms.net/> 0.4.1-1
- Update to 0.4.1.

* Wed Mar 22 2006 Matthias Saou <http://freshrpms.net/> 0.4.0-8b
- Fix modular X build requirement.

* Fri Mar 17 2006 Matthias Saou <http://freshrpms.net/> 0.4.0-7b
- Disable/remove static library, nothing seems to use it.

* Thu Jan 12 2006 Matthias Saou <http://freshrpms.net/> 0.4.0-6b
- Add modular xorg build conditional.

* Fri Dec 10 2004 Matthias Saou <http://freshrpms.net/> 0.4.0-5b
- Add patch from rpm.livna.org to remove -prefer-non-pic.
- Downgrade to 0.4.0b to fix permanent segfaults...

* Fri Nov 26 2004 Matthias Saou <http://freshrpms.net/> 0.4.1-0.20040610.2
- Use --disable-accel-detect for non-x86 to fix asm build failure on x86_64.

* Mon Nov 15 2004 Matthias Saou <http://freshrpms.net/> 0.4.1-0.20040610.1
- Update to latest available CVS snaphsot, fixes build issues on FC3.
- Added SDL support.

* Sun May 30 2004 Dag Wieers <dag@wieers.com> - 0.4.0-4b
- Added -fPIC for non ix86 archs.
- Merged with my SPEC file.

* Wed Mar 24 2004 Matthias Saou <http://freshrpms.net/> 0.4.0-3b
- Removed explicit dependency on XFree86 for the binary package.

* Thu Feb  5 2004 Matthias Saou <http://freshrpms.net/> 0.4.0-2b
- Update to 0.4.0b.

* Mon Jan  5 2004 Matthias Saou <http://freshrpms.net/> 0.4.0-1
- Update to 0.4.0.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 0.3.2-0.20030701.2
- Rebuild for Fedora Core 1.

* Tue Jul  1 2003 Matthias Saou <http://freshrpms.net/>
- Update to today's snapshot, enabled the spec to build snapshots since
  videolan-client 0.6.0 requires 0.3.2 cvs.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.

* Thu Jan 16 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.3.1.

* Mon Oct 28 2002 Matthias Saou <http://freshrpms.net/>
- Major spec file cleanup.

* Mon Jun 17 2002 Thomas Vander Stichele <thomas@apestaart.org>
- remove .la
- release 3

* Wed May 29 2002 Thomas Vander Stichele <thomas@apestaart.org>
- wrote out the different libs
- added docs
- removed autogen.sh option

* Wed May 08 2002 Erik Walthinsen <omega@temple-baptist.com>
- changed whitespace
- removed %%attr and changed %%defattr to (-,root,root)

* Fri May 03 2002 Thomas Vander Stichele <thomas@apestaart.org>
- adapted from PLD spec for 0.2.1
