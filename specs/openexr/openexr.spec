# $Id$
# Authority: dries
# Upstream: Drew Hess <dhess$yahoo,com>

%define real_name OpenEXR

Summary: High dynamic range image file format
Name: openexr
Version: 1.2.2
Release: 1
License: BSD
Group: Development/Libraries
URL: http://www.openexr.com

Source: http://savannah.nongnu.org/download/openexr/OpenEXR-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, fltk-devel, 

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

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n %{real_name}-%{version}
perl -pi -e 's|include .map.|include <map>\nclass Image;|g;' exrmaketiled/Image.h

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__mv} %{buildroot}%{_datadir}/doc/OpenEXR-* rpmdocs

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

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
%{_libdir}/libImath.so.*
%{_libdir}/libIlmImf.so.*

%files devel
%doc rpmdocs/*
%{_includedir}/OpenEXR
%{_libdir}/libHalf.a
%{_libdir}/libIex.a
%{_libdir}/libImath.a
%{_libdir}/libIlmImf.a
%{_libdir}/*.so
%{_libdir}/pkgconfig/OpenEXR.pc
%{_datadir}/aclocal/openexr.m4
%exclude %{_libdir}/*.la


%changelog
* Tue Nov 15 2005 Dries Verachtert <dries@ulyssis.org> - 1.2.2-1
- Initial package.
