# $Id$
# Authority: dag

Summary: Flash animations rendering library
Name: swfdec
Version: 0.2.2
Release: 1
License: LGPL
Group: System Environment/Libraries
URL: http://swfdec.sourceforge.net/

Source: http://dl.sf.net/swfdec/swfdec-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: mozilla-devel, libart_lgpl-devel, gtk2-devel >= 2.1.2
BuildRequires: libmad-devel, SDL-devel, gdk-pixbuf-devel, gcc-c++

%description
Libswfdec is a library for rendering Flash animations. Currently it
handles mostFlash 3 animations and some Flash 4. No interactivity is
supported yet.

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%package -n mozilla-swfdec
Summary: Mozilla plugin for Flash rendering
Group: Applications/Internet
Requires: mozilla, swfdec = %{version}-%{release}

%description -n mozilla-swfdec
Mozilla plugin for rendering of Flash animations based on swfdec
library

%prep
%setup

%{__perl} -pi.orig -e 's|^NPError NP_GetValue\(NPP |NPError NP_GetValue\(void *|' plugin/plugin.c

%build
export CFLAGS="%{optflags} -DMOZ_X11"
%configure \
	--disable-dependency-tracking \
	--enable-shared
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
#	transform="" \
#	plugindir="%{buildroot}%{_libdir}/mozilla/plugins"

%post
/sbin/ldconfig 2>/dev/null
if [ -x %{_bindir}/gdk-pixbuf-query-loaders ]; then
	%{_bindir}/gdk-pixbuf-query-loaders >%{_sysconfdir}/gtk-2.0/gdk-pixbuf.loaders
fi

%postun
/sbin/ldconfig 2>/dev/null
if [ -x %{_bindir}/gdk-pixbuf-query-loaders ]; then
	%{_bindir}/gdk-pixbuf-query-loaders >%{_sysconfdir}/gtk-2.0/gdk-pixbuf.loaders
fi

%clean
%{__rm} -rf %{buildroot}

%files 
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING NEWS README TODO 
%{_bindir}/*
%{_libdir}/*.so.*
%{_libdir}/gtk-2.0/*/loaders/*.so

%files devel
%defattr(-, root, root, 0755)
%{_libdir}/*.a
%exclude %{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/swfdec/
%exclude %{_libdir}/mozilla/plugins/*.a
%exclude %{_libdir}/mozilla/plugins/*.la
%exclude %{_libdir}/gtk-2.0/*/loaders/*.a
%exclude %{_libdir}/gtk-2.0/*/loaders/*.la
%exclude %{_sysconfdir}/gtk-2.0/gdk-pixbuf.loaders


%files -n mozilla-swfdec
%defattr(-, root, root, 0755)
%{_libdir}/mozilla/plugins/*.so*

%changelog
* Tue Jan 20 2004 Dag Wieers <dag@wieers.com> - 0.2.2-1
- Added missing swfdec requirement. (Alexandre Oliva)

* Thu Aug 28 2003 Dag Wieers <dag@wieers.com> - 0.2.2-0
- Initial package. (using DAR)

