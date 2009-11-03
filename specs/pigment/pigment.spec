# $Id$
# Authority: dag

%{?dtag: %{expand: %%define %dtag 1}}

%{?el4:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}
%{?rh9:%define _without_modxorg 1}
%{?rh7:%define _without_modxorg 1}
%{?el2:%define _without_modxorg 1}

%{?el5:%define _with_gl libGLU-devel}
%{?el4:%define _with_gl xorg-x11-Mesa-libGLU}
%{?el3:%define _with_gl XFree86-Mesa-libGLU}
%{?rh9:%define _with_gl XFree86-Mesa-libGLU}
%{?rh7:%define _with_gl Glide3-devel}
%{?el2:%define _with_gl Mesa-devel}

Summary: Media Center Toolkit
Name: pigment
Version: 0.3.13
Release: 1%{?dist}
License: GPL
Group: Applications/Multimedia
URL: https://code.fluendo.com/pigment/trac

Source: http://elisa.fluendo.com/static/download/pigment/pigment-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: cairo-devel
BuildRequires: glib2-devel
BuildRequires: gstreamer-devel
BuildRequires: gstreamer-plugins-base-devel
BuildRequires: gtk2-devel
BuildRequires: gtk-doc
BuildRequires: pygobject2-devel
BuildRequires: python-devel
%{?_without_modxorg:BuildRequires: XFree86-devel}
%{!?_without_modxorg:BuildRequires: libX11-devel libXrender-devel}
%{?_with_gl:BuildRequires: %{_with_gl}}

%description
Pigment is a toolkit for writing Media Center software.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: glib2-devel, pkgconfig, gtk-doc

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

### Get rid of incorrect requirement
%{__perl} -pi.orig -e 's|cairo_req=1.4|cairo_req=1.2|g' configure

%build
%configure --disable-static --enable-gtk-doc --enable-imaging-library
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
%doc AUTHORS ChangeLog COPYING README TODO
%{_libdir}/libpigment*.so.*
%{_libdir}/pigment-0.3/

%files devel
%defattr(-, root, root, 0755)
%doc %{_datadir}/gtk-doc/html/pigment/
%{_includedir}/pigment-0.3/
%{_libdir}/libpigment*.so
%{_libdir}/pkgconfig/pigment-0.3.pc
%{_libdir}/pkgconfig/pigment-gtk-0.3.pc
%{_libdir}/pkgconfig/pigment-imaging-0.3.pc
%exclude %{_libdir}/libpigment*.la

%changelog
* Wed Dec 10 2008 Dag Wieers <dag@wieers.com> - 0.3.13-1
- Initial package. (based on fedora)
