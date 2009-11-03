# $Id$
# Authority: dag
# Upstream: Sam Hocevar <sam$zoy,org>

%{?dtag: %{expand: %%define %dtag 1}}

%{!?dtag:%define _with_modxorg 1}
%{?fc7:  %define _with_modxorg 1}
%{?el5:  %define _with_modxorg 1}
%{?fc6:  %define _with_modxorg 1}
%{?fc5:  %define _with_modxorg 1}

%{?el3:%define _without_glut 1}
%{?el2:%define _without_glut 1}

Summary: Library for Colour AsCii Art, text mode graphics
Name: libcaca
Version: 0.99
Release: 0.1.beta11%{?dist}
License: LGPL
Group: System Environment/Libraries
URL: http://sam.zoy.org/projects/libcaca/

Source: http://libcaca.zoy.org/files/libcaca-%{version}.beta11.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: ncurses-devel >= 5, slang-devel, pango-devel
BuildRequires: imlib2-devel, zlib-devel, doxygen, tetex-latex, tetex-dvips
%{!?_without_glut:BuildRequires: glut-devel}
%{!?_with_modxorg:BuildRequires: XFree86-devel}
%{?_with_modxorg:BuildRequires: libX11-devel, libXt-devel}

%description
libcaca is the Colour AsCii Art library. It provides high level functions
for colour text drawing, simple primitives for line, polygon and ellipse
drawing, as well as powerful image to text conversion routines.

%package devel
Summary: Development files for libcaca, the library for Colour AsCii Art
Group: Development/Libraries
Requires: ncurses-devel >= 5, slang-devel
%{!?_with_modxorg:Requires: XFree86-devel}

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
%setup -n %{name}-%{version}.beta11

%build
%configure \
	--program-prefix="%{?_program_prefix}" \
	--x-libraries="%{_prefix}/X11R6/%{_lib}" \
	--disable-rpath \
	--enable-imlib2 \
	--enable-ncurses \
	--enable-slang \
	--enable-x11
%{__perl} -pi.orig -e '
		s|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g;
		s|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g;
	' libtool
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

# We want to include the docs ourselves from the source directory
%{__mv} %{buildroot}%{_docdir}/libcucul-dev libcucul-dev-docs

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_libdir}/libcaca.so.*
%{_libdir}/libcucul.so.*

%files devel
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING libcucul-dev-docs/*
%doc %{_mandir}/man1/caca-config.1*
%doc %{_mandir}/man3/*.3*
%{_bindir}/caca-config
%{_includedir}/caca.h
%{_includedir}/caca0.h
%{_includedir}/cucul.h
%{_libdir}/libcaca.a
%exclude %{_libdir}/libcaca.la
%{_libdir}/libcaca.so
%{_libdir}/libcucul.a
%exclude %{_libdir}/libcucul.la
%{_libdir}/libcucul.so
%{_libdir}/pkgconfig/caca.pc
%{_libdir}/pkgconfig/cucul.pc

%files -n caca-utils
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING NEWS NOTES README THANKS TODO
%doc %{_mandir}/man1/cacademo.1*
%doc %{_mandir}/man1/cacafire.1*
%doc %{_mandir}/man1/cacaplay.1*
%doc %{_mandir}/man1/cacaserver.1*
%doc %{_mandir}/man1/cacaview.1*
%doc %{_mandir}/man1/img2irc.1*
%{_bindir}/cacademo
%{_bindir}/cacafire
%{_bindir}/cacaplay
%{_bindir}/cacaserver
%{_bindir}/cacaview
%{_bindir}/img2irc
%{_datadir}/libcaca/

%changelog
* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 0.99-0.1.beta11
- Updated to release 0.99.beta11.

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

