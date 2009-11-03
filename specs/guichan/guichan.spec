# $Id$
# Authority: dries
# Upstream: Olof Naessen <olof$darkbits,org>

%{?dtag: %{expand: %%define %dtag 1}}

Summary: Small efficient C++ GUI library
Name: guichan
Version: 0.8.1
Release: 1%{?dist}
License: BSD
Group: Development/Libraries
URL: http://guichan.sourceforge.net/

Source: http://guichan.googlecode.com/files/guichan-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, autoconf, automake, allegro-devel, SDL-devel
BuildRequires: SDL_image-devel, libtool, freeglut-devel

%description
Guichan is a small, efficient C++ GUI library designed for games. It comes
with a standard set of widgets and can use several different backends for
displaying graphics and grabbing user input.

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
%{__perl} -pi.orig -e 's|-Werror||g;' configure*

%build
%configure
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
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%{_libdir}/libguichan-%{version}.so.*
%{_libdir}/libguichan_allegro-%{version}.so.*
%{_libdir}/libguichan_opengl-%{version}.so.*
%{_libdir}/libguichan_sdl-%{version}.so.*
#%{_libdir}/libguichan_glut.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/guichan.hpp
%{_includedir}/guichan/
%{_libdir}/libguichan.so
%{_libdir}/libguichan_allegro.so
%{_libdir}/libguichan_opengl.so
%{_libdir}/libguichan_sdl.so
#%{_libdir}/libguichan_glut.a
#%{_libdir}/libguichan_glut.so
%exclude %{_libdir}/*.a
%exclude %{_libdir}/*.la

%changelog
* Sun Apr 27 2008 Dries Verachtert <dries@ulyssis.org> - 0.8.1-1
- Updated to release 0.8.1.

* Sun Apr  6 2008 Dries Verachtert <dries@ulyssis.org> - 0.8.0-1
- Updated to release 0.8.0.

* Mon Jul 16 2007 Dries Verachtert <dries@ulyssis.org> - 0.7.1-1
- Updated to release 0.7.1.

* Tue Jul 10 2007 Dries Verachtert <dries@ulyssis.org> - 0.7.0-1
- Updated to release 0.7.0.

* Sat Jan 27 2007 Dries Verachtert <dries@ulyssis.org> - 0.6.1-1
- Updated to release 0.6.1.

* Sun Jan 14 2007 Dries Verachtert <dries@ulyssis.org> - 0.6.0-1
- Updated to release 0.6.0.

* Sun Jul 30 2006 Dries Verachtert <dries@ulyssis.org> - 0.5.0-1
- Updated to release 0.5.0.

* Thu Mar 30 2006 Dries Verachtert <dries@ulyssis.org> - 0.4.0-2
- Simplify buildequirements: SDL-devel already requires xorg-x11-devel/XFree86-devel

* Tue Oct 18 2005 Dries Verachtert <dries@ulyssis.org> - 0.4.0-1
- Initial package.
