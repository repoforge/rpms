# $Id$
# Authority: matthias
# Upstream: <libmpeg2-devel@lists.sf.net>

#define date 20030701

Summary: MPEG-2 and MPEG-1 decoding library and test program
Name: mpeg2dec
Version: 0.4.0
Release: %{?date:0.%{date}.}3b
License: LGPL
Group: System Environment/Libraries
URL: http://libmpeg2.sf.net/

Source: http://libmpeg2.sf.net/files/mpeg2dec-%{?date:date}%{!?date:%{version}b}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: XFree86-devel, pkgconfig, gcc-c++
Requires(post,postun): /sbin/ldconfig

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


%build
CFLAGS="%{optflags} -fPIC -fomit-frame-pointer -DPIC" \
%configure --enable-shared
#	--disable-sdl
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall


%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null


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
%doc doc/*.txt doc/*.c
%{_includedir}/mpeg2dec/
%{_libdir}/*.a
%exclude %{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/pkgconfig/*


%changelog
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
- removed %attr and changed %defattr to (-,root,root)

* Fri May 03 2002 Thomas Vander Stichele <thomas@apestaart.org>
- adapted from PLD spec for 0.2.1

