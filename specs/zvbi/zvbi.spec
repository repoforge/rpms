# $Id$
# Authority: dag

%{?dtag: %{expand: %%define %dtag 1}}

%{?el4:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}
%{?el2:%define _without_modxorg 1}

Summary: Raw VBI, Teletext and Closed Caption decoding library
Name: zvbi
Version: 0.2.33
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://zapping.sourceforge.net/

Source: http://dl.sf.net/zapping/zvbi-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libpng-devel, gcc-c++, doxygen, gettext
%{!?_without_modxorg:BuildRequires: libXt-devel}
%{?_without_modxorg:BuildRequires: XFree86-devel}
Obsoletes: libzvbi <= 0.2.4

%description
This library provides routines to access raw vbi sampling devices
(currently the V4L and V4L2 API are supported), a versatile raw vbi
bit slicer, decoders for various data services and basic search,
render and export functions for text pages. The library is the
vbi decoding backbone of the Zapping Gnome TV viewer and Zapzilla
Teletext browser. Documentation included.

%package devel
Summary: Static libraries and header files for zvbi development
Group: Development/Libraries
Requires: %{name} = %{version}, pkgconfig
Obsoletes: libzvbi-devel <= 0.2.4

%description devel
The static libraries and header files needed for building programs that use
the zvbi library.

%prep
%setup

%build
%configure \
    --disable-gtk-doc \
    --disable-static
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS BUGS COPYING ChangeLog NEWS README TODO doc/html
%doc %{_mandir}/man1/zvbi-chains.1*
%doc %{_mandir}/man1/zvbi-atsc-cc.1*
%doc %{_mandir}/man1/zvbi-ntsc-cc.1*
%doc %{_mandir}/man1/zvbid.1*
%{_bindir}/zvbi-chains
%{_bindir}/zvbi-atsc-cc
%{_bindir}/zvbi-ntsc-cc
%{_libdir}/libzvbi.so.*
%{_libdir}/libzvbi-chains.so.*
%{_sbindir}/zvbid

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/libzvbi.h
%{_libdir}/libzvbi.so
%{_libdir}/libzvbi-chains.so
%{_libdir}/pkgconfig/zvbi-0.2*.pc
%exclude %{_libdir}/libzvbi.la
%exclude %{_libdir}/libzvbi-chains.la

%changelog
* Sun Sep 14 2008 Dag Wieers <dag@wieers.com> - 0.2.33-1
- Updated to release 0.2.33.

* Sun Jul 27 2008 Dag Wieers <dag@wieers.com> - 0.2.31-1
- Updated to release 0.2.31.

* Mon Jun 09 2008 Dag Wieers <dag@wieers.com> - 0.2.30-1
- Updated to release 0.2.30.

* Tue Feb 26 2008 Dag Wieers <dag@wieers.com> - 0.2.29-1
- Updated to release 0.2.29.

* Tue Feb 26 2008 Dag Wieers <dag@wieers.com> - 0.2.28-1
- Updated to release 0.2.28.

* Sun Mar 18 2007 Dag Wieers <dag@wieers.com> - 0.2.25-1
- Updated to release 0.2.25.

* Wed Mar  7 2007 Matthias Saou <http://freshrpms.net/> 0.2.24-1
- Update to 0.2.24.
- Remove no longer needed compiler patch.

* Tue Sep 19 2006 Matthias Saou <http://freshrpms.net/> 0.2.21-2
- Add patch to remove linux/compiler.h include.

* Thu May 11 2006 Dag Wieers <dag@wieers.com> - 0.2.21-1
- Updated to release 0.2.21.

* Wed Mar 22 2006 Matthias Saou <http://freshrpms.net/> 0.2.19-2
- Add missing modular X build requirement.
- Try to disable static library, but the build fails, so exclude in %%files.

* Fri Mar 17 2006 Matthias Saou <http://freshrpms.net/> 0.2.19-1
- Update to 0.2.19.

* Sun Feb 12 2006 Dag Wieers <dag@wieers.com> - 0.2.18-1
- Updated to release 0.2.18.

* Fri Jan 13 2006 Matthias Saou <http://freshrpms.net/> 0.2.17-1
- Update to 0.2.17.
- Add now zvbi-ntsc-cc binary and man page.
- Add modular xorg build conditional.

* Thu Mar 31 2005 Dag Wieers <dag@wieers.com> - 0.2.15-1
- Updated to release 0.2.15.

* Sun Feb 20 2005 Matthias Saou <http://freshrpms.net/> 0.2.13-1
- Update to 0.2.13.
- Added X and libpng build requirements.

* Wed Jan 19 2005 Dag Wieers <dag@wieers.com> - 0.2.12-1
- Updated to release 0.2.12.

* Thu Nov 11 2004 Matthias Saou <http://freshrpms.net/> 0.2.9-1
- Update to 0.2.9.
- Include new binaries, man pages and pkgconfig file.

* Wed May 19 2004 Matthias Saou <http://freshrpms.net/> 0.2.8-1
- Update to 0.2.8.
- Rebuilt for Fedora Core 2.

* Tue Nov 11 2003 Matthias Saou <http://freshrpms.net/> 0.2.5-1
- Update to 0.2.5.
- Rebuild for Fedora Core 1.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.

* Thu Mar 20 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.2.4.
- Exclude .la file.

* Wed Oct  9 2002 Michael H. Schimek <mschimek@users.sourceforge.net>
- Update to 0.2.2.

* Tue Aug  6 2002 Michael H. Schimek <mschimek@users.sourceforge.net>
- Added %%find_lang for locale support.
- Split with a devel package.
- Disabled gtk-doc since detection works but not build if not in /usr/local.

* Tue Jun  4 2002 Michael H. Schimek <mschimek@users.sourceforge.net>
- Removed libunicode requirement
- Made package relocatable

* Sat Jan 26 2002 Michael H. Schimek <mschimek@users.sourceforge.net>
- Created

