# $Id$
# Authority: matthias
# Upstream: Sam Hocevar <sam$zoy,org>

Summary: Library for Colour AsCii Art, text mode graphics
Name: libcaca
Version: 0.9
Release: 4
License: LGPL
Group: System Environment/Libraries
URL: http://sam.zoy.org/projects/libcaca/
Source: http://sam.zoy.org/projects/libcaca/libcaca-%{version}.tar.bz2
Patch: libcaca-0.9-man3.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Buildrequires: XFree86-devel, ncurses-devel >= 5, slang-devel, imlib2-devel
Buildrequires: zlib-devel, doxygen, tetex-latex, tetex-dvips

%description
libcaca is the Colour AsCii Art library. It provides high level functions
for colour text drawing, simple primitives for line, polygon and ellipse
drawing, as well as powerful image to text conversion routines.


%package devel
Summary: Development files for libcaca, the library for Colour AsCii Art
Group: Development/Libraries
Requires: XFree86-devel, ncurses-devel >= 5, slang-devel

%description devel
libcaca is the Colour AsCii Art library. It provides high level functions
for colour text drawing, simple primitives for line, polygon and ellipse
drawing, as well as powerful image to text conversion routines.

This package contains the header files and static libraries needed to
compile applications or shared objects that use libcaca.


%package -n caca-utils
Summary: Colour AsCii Art Text mode graphics utilities based on libcaca
Group: Amusements/Graphics

%description -n caca-utils
This package contains utilities and demonstration programs for libcaca, the
Colour AsCii Art library.

cacaview is a simple image viewer for the terminal. It opens most image
formats such as JPEG, PNG, GIF etc. and renders them on the terminal using
ASCII art. The user can zoom and scroll the image, set the dithering method
or enable anti-aliasing.

cacaball is a tiny graphic program that renders animated ASCII metaballs on
the screen, cacafire is a port of AALib's aafire and displays burning ASCII
art flames, and cacademo is a simple application that shows the libcaca
rendering features such as line and ellipses drawing, triangle filling and
sprite blitting.


%prep
%setup
%patch -p1 -b .man3


%build
%configure \
    --program-prefix="%{?_program_prefix}" \
    --enable-slang \
    --enable-ncurses \
    --enable-x11 \
    --enable-imlib2
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall
# We want to include the docs ourselves from the source directory
%{__mv} %{buildroot}%{_docdir}/%{name}-dev %{name}-devel-docs


%clean
%{__rm} -rf %{buildroot}


%files devel
%defattr(-, root, root, 0755)
%doc %{name}-devel-docs/* COPYING
%{_libdir}/*.a
%{_bindir}/caca-config
%{_includedir}/*
%{_mandir}/man1/caca-config.1*
#{_mandir}/man3/*

%files -n caca-utils
%defattr(-, root, root, 0755)
%doc AUTHORS BUGS COPYING NEWS NOTES README THANKS TODO
%{_bindir}/cacaball
%{_bindir}/cacademo
%{_bindir}/cacafire
%{_bindir}/cacamoir
%{_bindir}/cacaplas
%{_bindir}/cacaview
%{_datadir}/libcaca/
%{_mandir}/man1/cacaball.1*
%{_mandir}/man1/cacademo.1*
%{_mandir}/man1/cacafire.1*
%{_mandir}/man1/cacamoir.1*
%{_mandir}/man1/cacaplas.1*
%{_mandir}/man1/cacaview.1*

%changelog
* Wed Nov  3 2004 Matthias Saou <http://freshrpms.net/> 0.9-4
- Disable man3 pages, they don't build on FC3, this needs fixing.
- Fix to not get the debuginfo files go into the devel package.

* Wed May 19 2004 Matthias Saou <http://freshrpms.net/> 0.9-3
- Rebuild for Fedora Core 2.

* Tue Feb 24 2004 Matthias Saou <http://freshrpms.net/> 0.9-2
- Fix License tag from GPL to LGPL.

* Mon Feb  9 2004 Matthias Saou <http://freshrpms.net/> 0.9-1
- Update to 0.9.
- Added cacamoir and cacaplas.

* Fri Jan  9 2004 Matthias Saou <http://freshrpms.net/> 0.7-1
- Spec file cleanup for Fedora Core 1.

* Sat Jan 7 2004 Sam Hocevar (RPM packages) <sam+rpm@zoy.org> 0.7-1
- new release

* Sat Jan 4 2004 Sam Hocevar (RPM packages) <sam+rpm@zoy.org> 0.6-2
- install documentation into {doc}/package-version instead of {doc}/package
- added tetex-dvips to the build dependencies

* Sat Jan 3 2004 Sam Hocevar (RPM packages) <sam+rpm@zoy.org> 0.6-1
- new release
- more detailed descriptions
- split the RPM into libcaca-devel and caca-utils
- packages are rpmlint clean

* Mon Dec 29 2003 Richard Zidlicky <rz@linux-m68k.org> 0.5-1
- created specfile

