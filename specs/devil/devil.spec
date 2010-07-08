# $Id$
# Authority: shuff
# Upstream: Nicolas Weber <thakis$users,sourceforge,net>

Summary: A full-featured cross-platform image library
Name: devil
Version: 1.7.8
Release: 1%{?dist}
License: GPL
Group: System Environment/Libraries
URL: http://openil.sourceforge.net/

Source: http://downloads.sourceforge.net/project/openil/DevIL/%{version}/DevIL-%{version}.tar.gz
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-%{dist}-%{arch}-XXXXXX)

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: allegro-devel >= 4.2.0
BuildRequires: freeglut-devel
BuildRequires: gcc-c++
BuildRequires: imake
BuildRequires: lcms-devel
BuildRequires: libjasper-devel
BuildRequires: libjpeg-devel
BuildRequires: libmng-devel
BuildRequires: libpng-devel
BuildRequires: libtiff-devel
BuildRequires: pkgconfig >= 0.9.0
BuildRequires: openexr-devel
BuildRequires: rpm-macros-rpmforge
BuildRequires: SDL-devel
BuildRequires: zlib-devel

%description
Developer's Image Library (DevIL) is a programmer's library to develop
applications with very powerful image loading capabilities, yet is easy for a
developer to learn and use. Ultimate control of images is left to the
developer, so unnecessary conversions, etc. are not performed. DevIL utilizes a
simple, yet powerful, syntax. DevIL can load, save, convert, manipulate, filter
and display a wide variety of image formats.

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
%{__chmod} +x ./configure
%configure \
    --disable-dependency-tracking \
    --with-examples=yes \
    --with-nvtt=no \
    --with-x \
    --with-squish=no \
    --with-zlib=yes \
    --enable-ILU=yes \
    --enable-ILUT=yes \
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
%doc AUTHORS ChangeLog COPYING CREDITS INSTALL Libraries.txt NEWS 
%doc README README.unix TODO 
%doc docs/DevIL_manual.pdf
%doc %{_infodir}/*
%{_bindir}/*
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%doc docs/html
%{_datadir}/devil/examples/
%{_includedir}/IL/
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%exclude %{_libdir}/*.la

%changelog
* Thu Jul 08 2010 Steve Huff <shuff@vecna.org> - 1.7.8-1
- Initial package.
