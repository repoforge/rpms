# $Id$

#define date 20030417

Summary: Powerful image loading and rendering library.
Name: imlib2
Version: 1.1.0
Release: %{?date:0.%{date}.}1.fr
License: BSD
Group: System Environment/Libraries
Source: http://dl.sf.net/enlightenment/%{name}-%{version}.tar.gz
URL: http://www.enlightenment.org/pages/imlib2.html
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: freetype >= 1.2, XFree86-libs
Requires: libjpeg, libpng, libtiff, libungif, zlib
BuildRequires: libjpeg-devel, libpng-devel
BuildRequires: XFree86-devel, freetype-devel >= 1.2
BuildRequires: libungif-devel

%description
Imlib2 is an advanced replacement library for libraries like libXpm that
provides many more features with much greater flexibility and speed than
standard libraries, including font rasterization, rotation, RGBA space
rendering and blending, dynamic binary filters, scripting, and more.


%package devel
Summary: Imlib2 header, static libraries and documentation.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: XFree86-devel, pkgconfig

%description devel
Header, static libraries and documentation for Imlib2.


%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%makeinstall

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-, root, root)
%doc AUTHORS README COPYING ChangeLog doc/
%{_libdir}/*.so.*
%dir %{_libdir}/loaders
%dir %{_libdir}/loaders/filter
%dir %{_libdir}/loaders/image
%{_libdir}/loaders/filter/*.so
%{_libdir}/loaders/image/*.so

%files devel
%defattr(-, root, root)
%{_bindir}/*
%{_includedir}/*
%{_libdir}/*.a
%{_libdir}/*.so
%dir %{_libdir}/loaders
%dir %{_libdir}/loaders/filter
%dir %{_libdir}/loaders/image
%{_libdir}/loaders/filter/*.a
%{_libdir}/loaders/image/*.a
%exclude %{_libdir}/*.la
%exclude %{_libdir}/loaders/filter/*.la
%exclude %{_libdir}/loaders/image/*.la
%{_libdir}/pkgconfig/*.pc

%changelog
* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 1.1.0-1.fr
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

