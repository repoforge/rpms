# $Id$
# Authority: matthias

Summary: Portable C++ class library for image loading, saving and manipulation
Name: paintlib
Version: 2.6.1
Release: 1
License: OSI certified
Group: System Environment/Libraries
URL: http://www.paintlib.de/paintlib/
Source: http://www.paintlib.de/paintlib/paintlib-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc-c++, curl-devel, zlib-devel, SDL-devel, XFree86-devel
BuildRequires: libungif-devel, libjpeg-devel, libtiff-devel, libpng-devel

%description
Paintlib is a portable C++ class library for image loading, saving and
manipulation. Images can be loaded from BMP, GIF, IFF, JPEG, PCX, PGM, PICT,
PNG, PSD, SGI, TGA, TIFF and WMF files and saved in BMP, JPEG, PNG and TIFF
formats. Image manipulation can be done either through filters implemented
in filter classes or by directly accessing the bitmap bits.


%package devel
Summary: Development files for the paintlib library
Group: Development/Libraries
Requires: %{name} = %{version}

%description devel
Paintlib is a portable C++ class library for image loading, saving and
manipulation. Images can be loaded from BMP, GIF, IFF, JPEG, PCX, PGM, PICT,
PNG, PSD, SGI, TGA, TIFF and WMF files and saved in BMP, JPEG, PNG and TIFF
formats. Image manipulation can be done either through filters implemented
in filter classes or by directly accessing the bitmap bits.

This package contains the header files and the static libraries for paintlib.


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
/sbin/ldconfig

%postun
/sbin/ldconfig


%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%doc doc/*
%{_bindir}/*-config
%{_includedir}/*
%{_libdir}/*.a
%exclude %{_libdir}/*.la
%{_libdir}/*.so
%{_mandir}/man1/*-config.1*


%changelog
* Fri Jun 11 2004 Matthias Saou <http://freshrpms.net/> 2.6.1-1
- Initial RPM release.

