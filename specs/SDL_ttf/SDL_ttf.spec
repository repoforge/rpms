# $Id$
# Authority: dag

%{?dist: %{expand: %%define %dist 1}}

Summary: Simple DirectMedia Layer - Sample TrueType Font Library
Name: SDL_ttf
Version: 2.0.6
Release: 0
License: LGPL
Group: System Environment/Libraries
URL: http://www.libsdl.org/projects/SDL_ttf/

Source: http://www.libsdl.org/projects/SDL_ttf/release/SDL_ttf-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: SDL-devel >= 1.2.4, freetype-devel >= 2.0

%description
This library allows you to use TrueType fonts to render text in SDL
applications.

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

### FIXME: Add missing ftbuild.h include (fix upstream please)
%{?fc2:%{__perl} -pi.orig -e 's|^(#include <freetype/freetype.h>)$|#include <ft2build.h>\n$1|' SDL_ttf.c}

### FIXME: Fix openstream reference for RH9 (fix upstream please)
%{?rh9:%{__perl} -pi.orig -e 's|ft_open_stream|FT_OPEN_STREAM|g' SDL_ttf.c}

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/*.la

%clean
%{__rm} -rf %{buildroot}

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%files
%defattr(-, root, root, 0755)
%doc CHANGES COPYING README
%{_libdir}/lib*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_libdir}/*.a
%{_libdir}/*.so
%{_includedir}/SDL/
#exclude %{_libdir}/*.la

%changelog
* Thu Sep 04 2003 Dag Wieers <dag@wieers.com> - 2.0.6-0
- Initial package. (using DAR)

