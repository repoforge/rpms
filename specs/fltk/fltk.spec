# $Id$
# Authority: dries
# Upstream: <fltk-dev$easysw,com>

# Screenshot: http://www.fltk.org/images/fluid.gif

%{?dtag: %{expand: %%define %dtag 1}}

%{?fc4:%define _without_modxorg 1}
%{?el4:%define _without_modxorg 1}
%{?fc3:%define _without_modxorg 1}
%{?fc2:%define _without_modxorg 1}
%{?fc1:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}
%{?rh9:%define _without_modxorg 1}
%{?rh7:%define _without_modxorg 1}
%{?el2:%define _without_modxorg 1}
%{?rh6:%define _without_modxorg 1}

%define desktop_vendor rpmforge

### Fix problem with Makefiles in 64bit build
%if "%{_lib}" == "lib64"
%define sixtyfourbit 1
%endif

Summary: Cross-platform C++ GUI toolkit
Name: fltk
Version: 1.1.7
Release: 2%{?dist}
License: FLTK
Group: System Environment/Libraries
URL: http://www.fltk.org/

Source: http://ftp.easysw.com/pub/fltk/1.1.7/fltk-%{version}-source.tar.bz2
Patch1: fltk-1.1.7-config.patch
Patch2: fltk-1.1.7-test.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc, gcc-c++, zlib-devel
BuildRequires: libjpeg-devel, libpng-devel
%{!?_without_modxorg:BuildRequires: libX11-devel}
%{?_without_modxorg:BuildRequires: XFree86-devel}

%description
FLTK (pronounced "fulltick") is a cross-platform C++ GUI toolkit for
UNIX/Linux (X11), Microsoft Windows and MacOS X. FLTK provides modern GUI
functionality and supports 3D graphics via OpenGL and its built-in GLUT
emulation.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%package fluid
Summary: Fast Light User Interface Designer
Group: Development/Tools
Requires: %{name}-devel = %{version}-%{release}

%description fluid
Fast Light User Interface Designer, an interactive GUI designer for fltk.

%prep
%setup
%patch1 -p1 -b .199656
%patch2 -p1 -b .test

### FIXME: Make Makefile use autotool directory standard. (Please fix upstream)
%{__perl} -pi.orig -e '
		s|\$\(mandir\)/cat1|\$(mandir)/man1|g;
		s|\$\(mandir\)/cat3|\$(mandir)/man3|g;
		s|\$\(mandir\)/cat6|\$(mandir)/man6|g;
	' documentation/Makefile

#%{__perl} -pi.orig -e 's|/lib\b|/%{_lib}|g' configure makeinclude.in Makefile.in */Makefile.in */*/Makefile.in

%build
%configure \
	--enable-shared="yes" \
	--enable-threads \
	--enable-xdbe \
	--enable-xft
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_libdir}

%{?sixtyfourbit:%{__ln_s} -f %{_lib} %{buildroot}%{_prefix}/lib}
%{__make} install install-desktop DESTDIR="%{buildroot}"
%{?sixtyfourbit:%{__rm} -f %{buildroot}%{_prefix}/lib}

%{__mv} -f %{buildroot}%{_docdir} rpm-doc/

### Clean up buildroot
%{__rm} -f %{buildroot}%{_datadir}/applnk/Games/{checkers,sudoku}.desktop
%{__rm} -f %{buildroot}%{_mandir}/man6/{checkers,sudoku}.?

desktop-file-install --delete-original \
	--vendor %{desktop_vendor} \
	--add-category Development \
	--add-category X-Red-Hat-Base \
	--dir %{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/applnk/Development/*.desktop

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post fluid
touch --no-create %{_datadir}/icons/hicolor ||:
gtk-update-icon-cache -q %{_datadir}/icons/hicolor &>/dev/null ||:
update-desktop-database &>/dev/null ||:

%postun fluid
touch --no-create %{_datadir}/icons/hicolor ||:
gtk-update-icon-cache -q %{_datadir}/icons/hicolor &>/dev/null ||:
update-desktop-database &>/dev/null ||:

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ANNOUNCEMENT CHANGES COPYING CREDITS README rpm-doc/*
%{_libdir}/libfltk.so.*
%{_libdir}/libfltk_forms.so.*
%{_libdir}/libfltk_gl.so.*
%{_libdir}/libfltk_images.so.*

%files devel
%defattr(-, root, root, 0755)
%doc %{_mandir}/man1/fltk-config.1*
%doc %{_mandir}/man3/fltk.3*
%{_bindir}/fltk-config
%{_includedir}/Fl
%{_includedir}/FL/
%exclude %{_libdir}/libfltk.a
%exclude %{_libdir}/libfltk_forms.a
%exclude %{_libdir}/libfltk_gl.a
%exclude %{_libdir}/libfltk_images.a
%{_libdir}/libfltk.so
%{_libdir}/libfltk_forms.so
%{_libdir}/libfltk_gl.so
%{_libdir}/libfltk_images.so

%files fluid
%defattr(-, root, root, 0755)
%doc %{_mandir}/man1/fluid.1*
%{_bindir}/fluid
%{_datadir}/applications/*fluid.desktop
%{_datadir}/mimelnk/*/*.desktop
%{_datadir}/icons/hicolor/*/*/*

%changelog
* Sun Apr 01 2007 Dag Wieers <dag@wieers.com> - 1.1.7-2
- Added Fedora patches.

* Mon May 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.1.7-2
- Added --enable-threads, thanks to Pekka Vuorela.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.1.7-1.2
- Rebuild for Fedora Core 5.

* Thu Jan 26 2006 Dries Verachtert <dries@ulyssis.org> 1.1.7-1
- Update to release 1.1.7.

* Sun Dec 19 2004 Dries Verachtert <dries@ulyssis.org> 1.1.6-1
- Update to release 1.1.6.

* Fri Oct 22 2004 Dries Verachtert <dries@ulyssis.org> 1.1.5-1
- Update to release 1.1.5.

* Thu May 20 2004 Dag Wieers <dag@wieers.com> - 1.1.4-1
- Cosmetic cleanup.

* Sat Dec 20 2003 Dries Verachtert <dries@ulyssis.org> 1.1.4-1
- first packaging for Fedora Core 1
