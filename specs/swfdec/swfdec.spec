# $Id$
# Authority: dag

Summary: Flash animations rendering library
Name: swfdec
Version: 0.3.0
Release: 1
License: LGPL
Group: System Environment/Libraries
URL: http://swfdec.sourceforge.net/

Source: http://www.schleef.org/swfdec/download/swfdec-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: mozilla-devel, libart_lgpl-devel, gtk2-devel >= 2.1.2
BuildRequires: libmad-devel, SDL-devel, gdk-pixbuf-devel, gcc-c++
BuildRequires: gimp-devel >= 2.0, liboil-devel

%description
Libswfdec is a library for rendering Flash animations. Currently it
handles mostFlash 3 animations and some Flash 4. No interactivity is
supported yet.


%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.


%package -n mozilla-swfdec
Summary: Mozilla plugin for Flash rendering
Group: Applications/Internet
Requires: %{name} = %{version}

%description -n mozilla-swfdec
Mozilla plugin for rendering of Flash animations based on the swfdec library.


%prep
%setup


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall


%clean
%{__rm} -rf %{buildroot}


%post
/sbin/ldconfig 2>/dev/null
[ -x %{_bindir}/gdk-pixbuf-query-loaders ] && \
    %{_bindir}/gdk-pixbuf-query-loaders > \
        %{_sysconfdir}/gtk-2.0/gdk-pixbuf.loaders

%postun
/sbin/ldconfig 2>/dev/null
[ -x %{_bindir}/gdk-pixbuf-query-loaders ] && \
    %{_bindir}/gdk-pixbuf-query-loaders > \
        %{_sysconfdir}/gtk-2.0/gdk-pixbuf.loaders


%files 
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING NEWS README TODO 
%exclude %{_sysconfdir}/gtk-2.0/gdk-pixbuf.loaders
%{_bindir}/*
%{_libdir}/*.so.*
%{_libdir}/gimp/1.3/plug-ins/swf
%exclude %{_libdir}/gtk-2.0/*/loaders/*.a
%exclude %{_libdir}/gtk-2.0/*/loaders/*.la
%{_libdir}/gtk-2.0/*/loaders/*.so

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/swfdec/
%{_libdir}/*.a
%exclude %{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%files -n mozilla-swfdec
%defattr(-, root, root, 0755)
%exclude %{_libdir}/mozilla/plugins/*.a
%exclude %{_libdir}/mozilla/plugins/*.la
%{_libdir}/mozilla/plugins/*.so*


%changelog
* Wed Oct 20 2004 Matthias Saou <http://freshrpms.net/> 0.3.0-1
- Update to 0.3.0.
- Added new liboil-devel and gimp2-devel dependencies.
- Added gimp plugin... strange, it goes into 1.3 :-/

* Tue Jan 20 2004 Dag Wieers <dag@wieers.com> - 0.2.2-1
- Added missing swfdec requirement. (Alexandre Oliva)

* Thu Aug 28 2003 Dag Wieers <dag@wieers.com> - 0.2.2-0
- Initial package. (using DAR)

