# $Id$
# Authority: matthias
# Upstream: Tim Wright <tim$ignavus,net>

%{?dtag: %{expand: %%define %dtag 1}}

%{?el4:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}
%{?el2:%define _without_modxorg 1}

%define xmms_generaldir %(xmms-config --general-plugin-dir 2>/dev/null || echo %{_libdir}/xmms/General)

Summary: Displays transparent text on your screen like the OSD of TVs
Name: xosd
Version: 2.2.14
Release: 1%{?dist}
License: GPL
Group: System Environment/Libraries
URL: http://libxosd.sourceforge.net/
Source: http://dl.sf.net/libxosd/xosd-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc-c++, gtk+-devel, gdk-pixbuf-devel
%{!?_without_xmms:BuildRequires: xmms-devel}
%{!?_without_modxorg:BuildRequires: libX11-devel, libXext-devel, libXinerama-devel}
%{?_without_modxorg:BuildRequires: XFree86-devel}

%description
XOSD displays text on your screen, sounds simple right? The difference is
it is unmanaged and shaped, so it appears transparent. This gives the
effect of an On Screen Display, like your TV/VCR etc.. The package also
includes an xmms plugin, which automatically displays various interesting
things as they change (song name, volume etc...)


%package devel
Summary: Development files for the XOSD on-screen display library
Group: Development/Libraries
Requires: %{name} = %{version}

%description devel
The xosd-devel package contains static libraries, header files and
documentation for developing applications that use the XOSD on-screen
display.


%package -n xmms-xosd
Summary: XMMS plugin for on-screen display that uses the XOSD library
Group: Applications/Multimedia
Requires: %{name} = %{version}, xmms
Obsoletes: xosd-xmms <= 2.2.1

%description -n xmms-xosd
An X MultiMedia System plugin to display information on-screen through the
XOSD library, similarly to TV OSD.


%prep
%setup

%build
%configure \
    --disable-dependency-tracking \
    --enable-old-plugin \
    --with-plugindir="%{xmms_generaldir}"
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
%doc AUTHORS ChangeLog COPYING README
%{_bindir}/osd_cat
%{_datadir}/xosd/
%{_libdir}/libxosd.so.*
%{_mandir}/man1/osd_cat.1*

%files devel
%defattr(-, root, root, 0755)
%{_bindir}/xosd-config
%{_datadir}/aclocal/*.m4
%{_includedir}/xosd.h
%{_libdir}/libxosd.a
%exclude %{_libdir}/libxosd.la
%{_libdir}/libxosd.so
%{_mandir}/man1/xosd-config.1*
%{_mandir}/man3/*.3*

%if %{!?_without_xmms:1}0
%files -n xmms-xosd
%defattr(-, root, root, 0755)
%{xmms_generaldir}/*.so
%exclude %{xmms_generaldir}/*.la
%endif


%changelog
* Tue Nov 07 2006 Dag Wieers <dag@wieers.com> - 2.2.14-1
- Updated to release 2.2.14.

* Tue Sep 14 2004 Matthias Saou <http://freshrpms.net/> 2.2.12-1
- Update to 2.2.12.

* Fri Aug 27 2004 Matthias Saou <http://freshrpms.net/> 2.2.10-1
- Update to 2.2.10.

* Mon Jul  5 2004 Matthias Saou <http://freshrpms.net/> 2.2.8-1
- Update to 2.2.8.

* Mon Jun  7 2004 Matthias Saou <http://freshrpms.net/> 2.2.7-1
- Update to 2.2.7.

* Wed May  5 2004 Matthias Saou <http://freshrpms.net/> 2.2.5-2
- Minor spec file cleanups.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 2.2.5-1
- Update to 2.2.5 at last.
- Rebuild for Fedora Core 1.

* Sun Jun 29 2003 Matthias Saou <http://freshrpms.net/>
- Update to 2.2.2.
- Renamed xosd-xmms to xmms-xosd.

* Tue Apr 21 2003 Matthias Saou <http://freshrpms.net/>
- Update to 2.2.1.
- Use --enable-old-plugin since RHL9 has gdk-pixbuf 0.18.0 and not the
  required 0.22.0 to build the new one.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.
- Exclude .la files.

* Fri Mar  7 2003 Matthias Saou <http://freshrpms.net/>
- Update to 2.1.3.

* Sun Feb 23 2003 Matthias Saou <http://freshrpms.net/>
- Update to 2.1.2.

* Wed Feb  5 2003 Matthias Saou <http://freshrpms.net/>
- Update to 2.1.0.
- Spec file updates to reflect upstream changes.

* Wed Jan  8 2003 Matthias Saou <http://freshrpms.net/>
- Update to 2.0.1.

* Mon Oct 21 2002 Matthias Saou <http://freshrpms.net/>
- Update to 1.1.1.

* Sun Sep 29 2002 Matthias Saou <http://freshrpms.net/>
- Update to 1.0.4.
- Rebuilt for Red Hat Linux 8.0.

* Fri Aug 30 2002 Matthias Saou <http://freshrpms.net/>
- Update to 1.0.3.

* Wed Aug 28 2002 Matthias Saou <http://freshrpms.net/>
- Update to 1.0.2.
- Fixed %%defattr for xmms plugin sub-package.

* Mon Jul 22 2002 Matthias Saou <http://freshrpms.net/>
- Update to 1.0.0.
- Spec file cleanup (near rewrite), added devel and xmms sub-packages.

* Wed Aug  1 2001 Matthias Saou <http://freshrpms.net/>
- Update to 0.7.0 and spec file cleanup.
- Changed the plugin path.
- Added ldconfig execution since I also changed the lib filename.

* Sat Feb  3 2001 Matthias Saou <http://freshrpms.net/>
- Initial RPM release.

