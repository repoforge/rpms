# $Id$
# Authority: dries

### EL2 ships with SDL_net-1.2.2-1
%{?el2:# Tag: rfx}

Summary: Cross-platform network API
Name: SDL_net
Version: 1.2.7
Release: 1%{?dist}
License: LGPL
Group: System Environment/Libraries
URL: http://www.libsdl.org/projects/SDL_net/

Source: http://www.libsdl.org/projects/SDL_net/release/SDL_net-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: SDL-devel >= 1.2.4, gcc-c++

%description
SDL_net is a thin API layer over sockets which is meant to be a simple
cross-platform network API.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: SDL-devel >= 1.2.4

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
%configure \
    --disable-static
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
%doc COPYING README
%{_libdir}/libSDL_net-*.so.*

%files devel
%defattr(-, root, root, 0755)
%dir %{_includedir}/SDL/
%{_includedir}/SDL/SDL_net.h
%{_libdir}/libSDL_net.so
%exclude %{_libdir}/libSDL_net.la

%changelog
* Sun Sep 09 2007 Dag Wieers <dag@wieers.com> - 1.2.7-1
- Updated to release 1.2.7.

* Fri May 19 2006 Dries Verachtert <dries@ulyssis.org> - 1.2.6-1
- Updated to release 1.2.6.

* Wed Feb 01 2006 Dries Verachtert <dries@ulyssis.org> - 1.2.5-1
- Initial package.
