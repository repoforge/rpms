# $Id$
# Authority: dries
# Upstream: A. Schiffler <aschiffler$appwares,com>

# Screenshot: http://www.ferzkopp.net/~aschiffler/Software/SDL_gfx-2.0/Screenshots/SDL_gfxPrimitives.jpg
# ScreenshotURL: http://www.ferzkopp.net/~aschiffler/Software/SDL_gfx-2.0/index.html

Summary: Graphic primitives, rotozoomer, framerate control and image filters
Name: SDL_gfx
Version: 2.0.19
Release: 1
License: LGPL
Group: System Environment/Libraries
URL: http://www.ferzkopp.net/mambo/index.php?option=com_content&task=view&id=14&Itemid=29

Source: http://www.ferzkopp.net/Software/SDL_gfx-2.0/SDL_gfx-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: SDL-devel, gcc-c++, automake, autoconf, perl

%description
The SDL_gfx library offers several components: Graphic Primitives,
Rotozoomer, Framerate control, and MMX image filters. The Primitives
component provides basic drawing routines: pixels, hlines, vlines, lines,
aa-lines, rectangles, circles, ellipses, trigons, polygons, Bezier curves,
and an 8x8 pixmap font for drawing onto any SDL Surface. Full alpha
blending, hardware surface locking, and all surface depths are supported.
The Rotozoomer can use interpolation for high quality output.

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
%configure \
%ifnarch %{ix86}
    --disable-mmx \
%endif
    --disable-static 
### Buildtools have problems even when -j1 is added
%{__make} #%{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%post -p/sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING LICENSE NEWS README
%{_libdir}/libSDL_gfx.so.*

%files devel
%defattr(-, root, root, 0755)
%dir %{_includedir}/SDL/
%{_includedir}/SDL/*.h
%{_libdir}/libSDL_gfx.so
%{_libdir}/pkgconfig/SDL_gfx.pc
%exclude %{_libdir}/libSDL_gfx.la

%changelog
* Mon Apr 27 2009 Dag Wieers <dag@wieers.com> - 2.0.19-1
- Updated to release 2.0.19.

* Sat Dec 23 2006 Dries Verachtert <dries@ulyssis.org> - 2.0.15-1
- Updated to release 2.0.15.

* Wed Dec 20 2006 Dries Verachtert <dries@ulyssis.org> - 2.0.14-1
- Updated to release 2.0.14.

* Fri Nov 11 2005 Dries Verachtert <dries@ulyssis.org - 2.0.13-2
- Fixed the project and source urls.

* Tue Dec 21 2004 Dries Verachtert <dries@ulyssis.org> 2.0.13-1
- Updated to release 2.0.13 and removed the patch (has been
  applied upstream)

* Thu Nov 11 2004 Matthias Saou <http://freshrpms.net/> 2.0.12-3
- Explicitly disable mmx for non-ix86 to fix build on x86_64.

* Fri Oct 22 2004 Dries Verachtert <dries@ulyssis.org> 2.0.12-3
- fixed some buildrequirements so the correct version of libSDL_gfx.so
  can be found in the list of provides.

* Fri Oct 22 2004 Dries Verachtert <dries@ulyssis.org> 2.0.12-2
- rebuild

* Wed Sep 01 2004 Dries Verachtert <dries@ulyssis.org> 2.0.12-1
- Update to version 2.0.12.

* Mon Apr 26 2004 Dries Verachtert <dries@ulyssis.org> 2.0.10-1
- Initial package
