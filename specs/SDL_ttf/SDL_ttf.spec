# $Id$
# Authority: dag

%{?dtag: %{expand: %%define %dtag 1}}

%{!?dtag: %define _freetype_fix 1}
%{?fc3: %define _freetype_fix 1}
%{?fc2: %define _freetype_fix 1}

Summary: Simple DirectMedia Layer - Sample TrueType Font Library
Name: SDL_ttf
Version: 2.0.8
Release: 1%{?dist}
License: LGPL
Group: System Environment/Libraries
URL: http://www.libsdl.org/projects/SDL_ttf/

Source: http://www.libsdl.org/projects/SDL_ttf/release/SDL_ttf-%{version}.tar.gz
Patch0: SDL_ttf-2.0.7-freetype-internals.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: SDL-devel >= 1.2.4, freetype-devel >= 2.0, zlib-devel, gcc-c++

%description
This library allows you to use TrueType fonts to render text in SDL
applications.

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}, SDL-devel

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup
%patch0 -p1 -b .freetype

### FIXME: Add missing ftbuild.h include (fix upstream please)
%{?_freetype_fix:%{__perl} -pi.orig -e 's|^(#include <freetype/freetype.h>)$|#include <ft2build.h>\n$1|' SDL_ttf.c}

### FIXME: Fix openstream reference for RH9 (fix upstream please)
%{?rh9:%{__perl} -pi.orig -e 's|ft_open_stream|FT_OPEN_STREAM|g' SDL_ttf.c}

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"


%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%doc CHANGES COPYING README
%{_libdir}/lib*.so.*

%files devel
%defattr(-, root, root, 0755)
%dir %{_includedir}/SDL/
%{_includedir}/SDL/*.h
%{_libdir}/*.a
%exclude %{_libdir}/*.la
%{_libdir}/*.so

%changelog
* Fri Mar 30 2007 Dag Wieers <dag@wieers.com> - 2.0.8-1
- Updated to release 2.0.8.

* Mon Sep 05 2005 Dries Verachtert <dries@ulyssis.org> - 2.0.7-0
- Updated to release 2.0.7.

* Thu Sep 04 2003 Dag Wieers <dag@wieers.com> - 2.0.6-0
- Initial package. (using DAR)

