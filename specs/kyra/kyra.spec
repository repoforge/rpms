# $Id: $

# Authority: dries
# Upstream: 

%define real_version 2_0_7

Summary: Sprite Engine
Name: kyra
Version: 2.0.7
Release: 1
License: GPL
Group: Development/LibrariesDevelopment/Libraries
URL: http://grinninglizard.com/kyra/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://dl.sf.net/kyra/kyra_src_%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: SDL-devel, gcc-c++, SDL_image-devel, libtiff-devel
%{?fc2:BuildRequires: alsa-lib-devel}

# Screenshot: http://grinninglizard.com/kyra/demoBemSingle.jpg
# ScreenshotURL : http://grinninglizard.com/kyra/demo.html

%description
Kyra is a simple, fully featured, industrial strength Sprite engine written
in C++.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n kyra

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%{_bindir}/*
%{_libdir}/*.so.*
%{_datadir}/aclocal/kyra.m4

%files devel
%{_includedir}/Kyra
%{_libdir}/*.a
%{_libdir}/*.so
%exclude %{_libdir}/*.la

%changelog
* Sun May 30 2004 Dries Verachtert <dries@ulyssis.org> - 2.0.7-1
- Initial package.

