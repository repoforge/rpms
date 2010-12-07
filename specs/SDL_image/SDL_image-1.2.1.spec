# $Id: SDL_image.spec 9276 2010-11-13 22:01:11Z dag $
# Authority: dries
# Upstream: Sam Latinga <slouken$devolution,com>

# ExclusiveDist: el2

### EL2 ships with SDL_image-1.2.0-3
%{?el2:# Tag: rfx}

Summary: Load images as SDL surfaces
Name: SDL_image
Version: 1.2.1
Release: 1%{?dist}
License: LGPL
Group: System Environment/Libraries
URL: http://www.libsdl.org/projects/SDL_image/

Source: http://www.libsdl.org/projects/SDL_image/release/SDL_image-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: automake
BuildRequires: autoconf
BuildRequires: gcc-c++
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: libtiff-devel
BuildRequires: perl
BuildRequires: SDL-devel >= 1.2.2
BuildRequires: zlib-devel

%description
SDL_image is an image file loading library. It loads images as SDL surfaces,
and supports the following formats: BMP, PNM, XPM, LBM, PCX, GIF, JPEG, PNG,
TGA.

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

%build
%configure --disable-static
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
%{_libdir}/libSDL_image*.so.*

%files devel
%defattr(-, root, root, 0755)
%dir %{_includedir}/SDL/
%{_includedir}/SDL/SDL_image.h
%{_libdir}/libSDL_image.so
%exclude %{_libdir}/*.la

%changelog
* Mon Dec 06 2010 Dag Wieers <dag@wieers.com> - 1.2.1-1
- Initial package. (using DAR)
