# $Id$
# Authority: matthias
# Upstream: Carsten Haitzler <raster$rasterman,com>
# Upstream: <enlightenment-devel$lists,sourceforge,net>

#define date 20030417

Summary: Powerful image loading and rendering library
Name: imlib2
Version: 1.1.2
Release: %{?date:0.%{date}.}2
License: BSD
Group: System Environment/Libraries
URL: http://enlightenment.org/pages/imlib2.html
Source: http://dl.sf.net/enlightenment/imlib2-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: XFree86-devel, freetype-devel >= 1.2
BuildRequires: zlib-devel, bzip2-devel
BuildRequires: libpng-devel, libjpeg-devel, libungif-devel, libtiff-devel
# The ltdl.h file is required...
BuildRequires: libtool

%description
Imlib2 is an advanced replacement library for libraries like libXpm that
provides many more features with much greater flexibility and speed than
standard libraries, including font rasterization, rotation, RGBA space
rendering and blending, dynamic binary filters, scripting, and more.


%package devel
Summary: Imlib2 header, static libraries and documentation
Group: Development/Libraries
Requires: %{name} = %{version}
Requires: XFree86-devel, pkgconfig

%description devel
Header, static libraries and documentation for Imlib2.


%prep
%setup
%{__perl} -pi.orig -e 's|/lib\b|/%{_lib}|g' configure

%build
%configure \
    --with-pic \
%ifarch %{ix86}
    --enable-mmx
%else
    --disable-mmx
%endif
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall


%clean
%{__rm} -rf %{buildroot}


%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null


%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING README doc/
%{_bindir}/*test
%{_bindir}/color_spaces
%{_bindir}/imconvert
%{_bindir}/imlib2*
%{_libdir}/libImlib2.so.*
%dir %{_libdir}/imlib2_loaders/
%dir %{_libdir}/imlib2_loaders/filter/
%dir %{_libdir}/imlib2_loaders/image/
%{_libdir}/imlib2_loaders/filter/*.so
%{_libdir}/imlib2_loaders/image/*.so

%files devel
%defattr(-, root, root, 0755)
%{_bindir}/imlib2-config
%{_includedir}/Imlib2.h
%{_libdir}/libImlib2.a
%exclude %{_libdir}/libImlib2.la
%{_libdir}/libImlib2.so
%exclude %{_libdir}/imlib2_loaders/filter/*.a
%exclude %{_libdir}/imlib2_loaders/filter/*.la
%exclude %{_libdir}/imlib2_loaders/image/*.a
%exclude %{_libdir}/imlib2_loaders/image/*.la
%{_libdir}/pkgconfig/*.pc


%changelog
* Fri Nov  5 2004 Matthias Saou <http://freshrpms.net/> 1.1.2-2
- Added bzip2 support.
- Add --with-pic configure option, but lib still seems to have non-pic code.

* Sat Sep 25 2004 Dag Wieers <dag@wieers.com> - 1.1.2-1
- Updated to release 1.1.2. (Antti Markus)

* Sat May 29 2004 Dag Wieers <dag@wieers.com> - 1.1.0-3
- Merged my imlib2 package.
- Disable mmx on non-ix86 architectures.

* Thu Mar 25 2004 Matthias Saou <http://freshrpms.net/> 1.1.0-2
- Removed the explicit XFree86-libs dependency.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 1.1.0-1
- Update to 1.1.0.
- Added pkgconfig entry and devel dependency.
- Rebuild for Fedora Core 1.

* Thu Apr 17 2003 Matthias Saou <http://freshrpms.net/>
- Update to today's CVS 1.0.7 snapshot.
- Spec file cleanup, main and devel are what they should be now.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.
- Exclude .la files.

* Fri Feb 21 2003 Matthias Saou <http://freshrpms.net/>
- Fixed s/XFree86/XFree86-libs/ in dependencies.

* Wed Nov 13 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt against Red Hat Linux 8.0.

* Fri May  3 2002 Matthias Saou <http://freshrpms.net/>
- Update to 1.0.6.
- Rebuilt against Red Hat Linux 7.3.
- Added the %{?_smp_mflags} expansion.

* Mon Nov 26 2001 Matthias Saou <http://freshrpms.net/>
- Spec file cleanup and update to 1.0.4.

* Mon Jan 8 2001 The Rasterman <raster@rasterman.com>
- Fix Requires & BuildRequires for freetype.

* Sat Sep 30 2000 Lyle Kempler <term@kempler.net>
- Bring back building imlib2 as root via autogen.sh for the lazy (me)
- Some minor changes

* Sat Sep 30 2000 Joakim Bodin <bodin@dreamhosted.com>
- Linux-Mandrake:ise the spec file

* Tue Sep 12 2000 The Rasterman <raster@rasterman.com>
- Redo spec file

* Wed Aug 30 2000 Lyle Kempler <kempler@utdallas.edu>
- Include imlib2-config

* Sat May 20 2000 Lyle Kempler <kempler@utdallas.edu>
- Fixed problems with requiring imlib2_view
- Went back to imlib2_view (not imlib2-view)

* Tue Nov 2 1999 Lyle Kempler <kempler@utdallas.edu>
- Mangled imlib 1.9.8 imlib spec file into imlib2 spec file

