# $Id$
# Authority: dag
# Upstream: <cairo$cairographics,org>

### EL5 ships with version 1.2.4-5.el5
# ExclusiveDist: el2 rh7 rh9 el3 el4

%{?dtag: %{expand: %%define %dtag 1}}

%{?el4:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}

Summary: Anti-aliased vector-based rendering for X
Name: cairo
Version: 1.2.4
Release: 2.1%{?dist}
License: MIT
Group: System Environment/Libraries
URL: http://cairo.freedesktop.org/

Source: http://cairo.freedesktop.org/snapshots/cairo-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: pkgconfig, freetype-devel, libpixman-devel
BuildRequires: libpng-devel, gcc-c++
%{!?_without_directfb:BuildRequires: directfb-devel >= 0.9.24}
%{!?_without_fontconfig:BuildRequires: fontconfig-devel}
#BuildRequires: glitz-devel, libxcb-devel
%{!?_without_modxorg:BuildRequires: libX11-devel}
%{?_without_modxorg:BuildRequires: XFree86-devel}

%description
Cairo provides anti-aliased vector-based rendering for X. Paths consist
of line segments and cubic splines and can be rendered at any width with
various join and cap styles. All colors may be specified with optional
translucence (opacity/alpha) and combined using the extended Porter/Duff
compositing algebra as found in the X Render Extension.

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: libpixman-devel, XFree86-devel

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
%{?_without_pkgconfig:export png_CFLAGS="$(libpng-config --cflags)"}
%{?_without_pkgconfig:export png_LIBS="$(libpng-config --libs)"}
%{?_without_pkgconfig:export png_REQUIRES=" "}

%configure \
    --disable-static \
%{!?_without_directfb:--enable-directfb}
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
%{_libdir}/libcairo.so.*

%files devel
%defattr(-, root, root, 0755)
%doc %{_datadir}/gtk-doc/html/cairo/
%{_includedir}/cairo/
%{_libdir}/libcairo.so
%{_libdir}/pkgconfig/cairo.pc
%{_libdir}/pkgconfig/cairo-*.pc
%exclude %{_libdir}/libcairo.la

%changelog
* Tue Sep 23 2008 Dag Wieers <dag@wieers.com> - 1.2.4-2.1
- Rebuild against directfb-1.2.4.

* Fri Jul 04 2008 Dag Wieers <dag@wieers.com> - 1.2.4-2
- Rebuild against directfb-1.0.1.

* Sun Mar 25 2007 Dag Wieers <dag@wieers.com> - 1.2.4-1
- Updated to release 1.2.4

* Sun Jan 02 2005 Dag Wieers <dag@wieers.com> - 0.2.0-1
- Updated to release 0.2.0.

* Wed Feb 25 2004 Dag Wieers <dag@wieers.com> - 0.1.23-1
- Updated to release 0.1.23.

* Wed Feb 25 2004 Dag Wieers <dag@wieers.com> - 0.1.18-0
- Initial package. (using DAR)
