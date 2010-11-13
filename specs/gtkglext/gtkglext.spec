# $Id$
# Authority: matthias
# Upstream: <gtkglext-list$gnome,org>

### EL6 ships with gtkglext-devel-1.2.0-11.el6
# ExclusiveDist: el2 el3 el4 el5

%{?el4:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}
%{?el2:%define _without_modxorg 1}

%{?el3:%define _without_xorg 1}
%{?el2:%define _without_xorg 1}

Summary: OpenGL Extension to GTK
Name: gtkglext
Version: 1.0.6
Release: 1%{?dist}
License: LGPL
Group: System Environment/Libraries
URL: http://gtkglext.sourceforge.net/

Source: http://dl.sf.net/gtkglext/gtkglext-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk2-devel
# libtool *sigh*
BuildRequires: gcc-c++
%if 0%{?_without_modxorg:1}
%{?_without_xorg:BuildRequires: XFree86-devel, XFree86-Mesa-libGLU}
%{!?_without_xorg:BuildRequires: xorg-x11-devel, xorg-x11-Mesa-libGLU}
%else
BuildRequires: libXt-devel, mesa-libGLU-devel
%endif

%description
GtkGLExt is an OpenGL extension to GTK. It provides the GDK objects
which support OpenGL rendering in GTK, and GtkWidget API add-ons to
make GTK+ widgets OpenGL-capable.


%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}, gtk2-devel

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.


%prep
%setup


%build
%configure --with-pic
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall


%clean
%{__rm} -rf %{buildroot}


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING COPYING.LIB NEWS README TODO
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%doc examples/
%doc %{_datadir}/gtk-doc/html/gtkglext/
%{_includedir}/gtkglext-1.0/
%{_libdir}/gtkglext-1.0/
%{_libdir}/*.a
%exclude %{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/aclocal/*.m4


%changelog
* Mon Nov 15 2004 Matthias Saou <http://freshrpms.net/> 1.0.6-1
- Rebuild for Fedora Core 3.
- Fix gtk1 vs. gtk2 dependencies.

* Thu Mar 11 2004 Dag Wieers <dag@wieers.com> - 1.0.6-1
- Updated to release 1.0.6.

* Sat Jan 24 2004 Dag Wieers <dag@wieers.com> - 1.0.5-0
- Initial package. (using DAR)

