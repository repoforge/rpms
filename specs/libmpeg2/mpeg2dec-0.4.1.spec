# $Id$
# Authority: matthias
# Upstream: <libmpeg2-devel$lists,sf,net>

%{?dtag: %{expand: %%define %dtag 1}}
%{?fedora: %{expand: %%define fc%{fedora} 1}}

%{?el4:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}

#define date 20040610

Summary: MPEG-2 and MPEG-1 decoding library and test program
Name: mpeg2dec
Version: 0.4.1
Release: 2%{?date:.%{date}}
License: LGPL
Group: System Environment/Libraries
URL: http://libmpeg2.sourceforge.net/
Source: http://libmpeg2.sourceforge.net/files/mpeg2dec-%{?date:snapshot}%{!?date:%{version}}.tar.gz
Patch0: mpeg2dec-0.4.0b-pic.patch
Patch1: mpeg2dec-0.4.1-automake-1.10.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: SDL-devel, pkgconfig, gcc-c++
%{!?_without_modxorg:BuildRequires: libXt-devel, libXv-devel}
%{?_without_modxorg:BuildRequires: XFree86-devel}
# Required for ./bootstrap
BuildRequires: autoconf, automake, libtool

%description
A free library for decoding MPEG-2 and MPEG-1 video streams.


%package devel
Summary: Development files for mpeg2dec's libmpeg2
Group: Development/Libraries
Requires: %{name} = %{version}, pkgconfig

%description devel
A free library for decoding MPEG-2 and MPEG-1 video streams.

This package contains files needed to build applications that use mpeg2dec's
libmpeg2.


%prep
%setup -n %{name}-%{version}%{?date:-cvs}
%patch0 -p0 -b .pic
%patch1 -p1 -b .automake-1.10
./bootstrap


%build
CFLAGS="%{optflags}" \
%configure \
%ifnarch %{ix86}
    --disable-accel-detect \
%endif
    --enable-shared \
    --disable-static
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING NEWS README TODO
%{_bindir}/*
%{_libdir}/*.so.*
%{_mandir}/man1/*


%files devel
%defattr(-, root, root, 0755)
%doc doc/*.c doc/*.txt
%{_includedir}/mpeg2dec/
%exclude %{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/pkgconfig/*


%changelog
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

