# $Id$
# Authority: dries

Summary: Cross-platform network API
Name: SDL_net
Version: 1.2.6
Release: 1
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
%{_libdir}/libSDL_net.a
%{_libdir}/libSDL_net.so
%exclude %{_libdir}/*.la

%changelog
* Fri May 19 2006 Dries Verachtert <dries@ulyssis.org> - 1.2.6-1
- Updated to release 1.2.6.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.2.5-1.2
- Rebuild for Fedora Core 5.

* Wed Feb 01 2006 Dries Verachtert <dries@ulyssis.org> - 1.2.5-1
- Initial package.
