# $Id$

# Authority: dag

Summary: Flash animations rendering library.
Name: swfdec
Version: 0.2.0
Release: 0
License: LGPL
Group: System Environment/Libraries
URL: http://swfdec.sf.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/swfdec/swfdec-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: mozilla-devel, libart_lgpl-devel
BuildRequires: libmad-devel, SDL-devel

%description
Libswfdec is a library for rendering Flash animations. Currently it
handles mostFlash 3 animations and some Flash 4. No interactivity is
supported yet.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%package -n mozilla-swfdec
Summary: Mozilla plugin for Flash rendering.
Group: Applications/Internet
Requires: mozilla

%description -n mozilla-swfdec
Mozilla plugin for rendering of Flash animations based on swfdec
library

%prep
%setup

%{__perl} -pi.orig -e 's|^NPError NP_GetValue\(NPP |NPError NP_GetValue\(void *|' plugin/plugin.c

%build
export CFLAGS="%optflags -DMOZ_X11"
%configure \
	--disable-dependency-tracking \
	--enable-shared
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
#	transform="" \
#	plugindir="%{buildroot}%{_libdir}/mozilla/plugins"

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/*.la \
		%{buildroot}%{_libdir}/mozilla/plugins/*.{a,la} \
		%{buildroot}%{_libdir}/gtk-2.0/2.2.0/loaders/*.{a,la}

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files 
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING NEWS README TODO 
%{_bindir}/*
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/swfdec/

%files -n mozilla-swfdec
%defattr(-, root, root, 0755)
%{_libdir}/mozilla/plugins/*.so*

%changelog
* Thu Aug 28 2003 Dag Wieers <dag@wieers.com> - 0.2.0-0
- Initial package. (using DAR)
