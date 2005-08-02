# $Id$
# Authority: dag
# Upstream: <cairo$cairographics,org>

%{?dist: %{expand: %%define %dist 1}}

%{?fc1:%define _without_xorg 1}
%{?el3:%define _without_xorg 1}
%{?rh9:%define _without_xorg 1}
%{?rh8:%define _without_xorg 1}
%{?rh7:%define _without_xorg 1}
# %{?el2:%define _without_xorg 1}
%{?rh6:%define _without_xorg 1}
%{?yd3:%define _without_xorg 1}

Summary: Anti-aliased vector-based rendering for X
Name: cairo
Version: 0.2.0
Release: 1
License: MIT
Group: System Environment/Libraries
URL: http://cairo.freedesktop.org/

Source: http://cairo.freedesktop.org/snapshots/cairo-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: pkgconfig, freetype-devel, fontconfig-devel, libpixman-devel
BuildRequires: libpng-devel, gcc-c++
#BuildRequires: glitz-devel, libxcb-devel
%{?_without_xorg:BuildRequires: XFree86-devel}
%{!?_without_xorg:BuildRequires: xorg-x11-devel}

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
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%{_libdir}/libcairo.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/cairo.h
%{_includedir}/cairo-features.h
%{_libdir}/libcairo.a
%exclude %{_libdir}/libcairo.la
%{_libdir}/libcairo.so
%{_libdir}/pkgconfig/cairo.pc

%changelog
* Wed Feb 25 2004 Dag Wieers <dag@wieers.com> - 0.1.23-1
- Updated to release 0.1.23.

* Wed Feb 25 2004 Dag Wieers <dag@wieers.com> - 0.1.18-0
- Initial package. (using DAR)
