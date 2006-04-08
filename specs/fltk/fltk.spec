# $Id$
# Authority: dries
# Upstream: <fltk-dev$easysw,com>

# Screenshot: http://www.fltk.org/images/fluid.gif

%{?dist: %{expand: %%define %dist 1}}

%{?fc1:%define _without_xorg 1}
%{?el3:%define _without_xorg 1}
%{?rh9:%define _without_xorg 1}
%{?rh8:%define _without_xorg 1}
%{?rh7:%define _without_xorg 1}
%{?el2:%define _without_xorg 1}
%{?rh6:%define _without_xorg 1}


Summary: Cross-platform C++ GUI toolkit
Name: fltk
Version: 1.1.7
Release: 1.2
License: FLTK
Group: System Environment/Libraries
URL: http://www.fltk.org/

Source: http://dl.sf.net/fltk/fltk-%{version}-source.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc, gcc-c++, zlib-devel
BuildRequires: libjpeg-devel, libpng-devel
%{?_without_xorg:BuildRequires: XFree86-devel}
%{!?_without_xorg:BuildRequires: xorg-x11-devel}

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

%prep
%setup

### FIXME: Make Makefile use autotool directory standard. (Please fix upstream)
%{__perl} -pi.orig -e '
		s|\$\(mandir\)/cat1|\$(mandir)/man1|g;
		s|\$\(mandir\)/cat3|\$(mandir)/man3|g;
	' documentation/Makefile

%build
%configure \
	--enable-shared="yes"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}

### FIXME: Makefile doesn't create target directories (Please fix upstream)
%{__install} -d -m0755 %{buildroot}%{_bindir} \
			%{buildroot}%{_includedir}/FL/

%makeinstall

%{__mv} -f %{buildroot}%{_docdir} rpm-doc/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ANNOUNCEMENT CHANGES COPYING CREDITS README rpm-doc/*
%doc %{_mandir}/man1/*
%{_bindir}/*
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%doc %{_mandir}/man3/*
%{_includedir}/F*
%{_libdir}/*.a
%{_libdir}/*.so

%changelog
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
