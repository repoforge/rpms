# $Id$
# Authority: dries
# Upstream: Drew Hess <dhess$yahoo,com>


%{?fc4:%define _without_modxorg 1}
%{?el4:%define _without_modxorg 1}
%{?fc3:%define _without_modxorg 1}
%{?fc2:%define _without_modxorg 1}
%{?fc1:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}
%{?rh9:%define _without_modxorg 1}
%{?rh7:%define _without_modxorg 1}
%{?el2:%define _without_modxorg 1}
%{?rh6:%define _without_modxorg 1}

Summary: High dynamic range image file format
Name: openexr
%define real_version 1.4.0
Version: 1.4.0a
Release: 1%{?dist}
License: BSD
Group: Development/Libraries
URL: http://www.openexr.com/

Source: http://savannah.nongnu.org/download/openexr/openexr-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, fltk-devel
%{?_without_modxorg:BuildRequires: XFree86-devel}
%{!?_without_modxorg:BuildRequires: libXext-devel}
Obsoletes: OpenEXR <= %{version}-%{release}
Provides: OpenEXR = %{version}-%{release}

%description
OpenEXR is a high dynamic range (HDR) image file format developed by
Industrial Light & Magic for use in computer imaging applications. It
includes support for 16-bit floating-point pixels (compatible with
NVIDIA's Cg shader language "half" datatype), several lossless compression
algorithms, and extensible image metadata attributes.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Obsoletes: OpenEXR-devel <= %{version}-%{release}
Provides: OpenEXR-devel = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n %{name}-%{real_version}
%{__perl} -pi.orig -e 's|include .map.|include <map>\nclass Image;|g;' exrmaketiled/Image.h

%build
%configure \
	--program-prefix="%{?_program_prefix}" \
	--disable-static
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%{__mv} %{buildroot}%{_datadir}/doc/OpenEXR-* rpm-doc/

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL LICENSE NEWS README
%{_bindir}/exrmaketiled
%{_bindir}/exrstdattr
%{_bindir}/exrmakepreview
%{_bindir}/exrenvmap
%{_bindir}/exrheader
%{_bindir}/exrdisplay
%{_libdir}/libHalf.so.*
%{_libdir}/libIex.so.*
%{_libdir}/libIlmImf.so.*
%{_libdir}/libIlmThread.so.*
%{_libdir}/libImath.so.*

%files devel
%doc rpm-doc/*
%{_datadir}/aclocal/openexr.m4
%{_includedir}/OpenEXR/
%{_libdir}/libHalf.so
%{_libdir}/libIex.so
%{_libdir}/libIlmImf.so
%{_libdir}/libIlmThread.so
%{_libdir}/libImath.so
%{_libdir}/pkgconfig/OpenEXR.pc
%exclude %{_libdir}/*.la

%changelog
* Sat May 12 2007 Dag Wieers <dag@wieers.com> - 1.4.0a-1
- Updated to release 1.4.0a.

* Sat Aug 12 2006 Dries Verachtert <dries@ulyssis.org> - 1.3.0-1
- Updated to release 1.3.0.

* Tue Nov 15 2005 Dries Verachtert <dries@ulyssis.org> - 1.2.2-1
- Initial package.
