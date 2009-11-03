# $Id$
# Authority: dag

# ExcludeDist: el2 rh7 rh9 el3 el4

Summary: Image loading and rendering library for X11R6
Name: imlib
Version: 1.9.13
Release: 1%{?dist}
Epoch: 1
License: LGPL
Group: System Environment/Libraries
URL: http://www.enlightenment.org/Libraries/Imlib.html

Source: http://ftp.gnome.org/pub/GNOME/sources/imlib/1.9/imlib-%{version}.tar.gz
Patch2: imlib-1.9.10-ac25.patch
Patch3: imlib-1.9.10-cppflags.patch
Patch4: imlib-1.9.13-gmodulehack.patch
Patch5: imlib-1.9.13-waitpid.patch
Patch6: imlib-1.9.13-underquoted.patch
Patch7: imlib-1.9.14-bounds.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: zlib-devel, libX11-devel, gtk+-devel, libungif-devel
BuildRequires: libpng-devel >= 1.2.2, libtiff-devel, libjpeg-devel

Requires: gtk+ >= 1:1.2

Obsoletes: imlib-cfgeditor <= %{version}-%{release}
Provides: imlib-cfgeditor = %{version}-%{release}

Obsoletes: Imlib <= %{version}-%{release}
Provides: Imlib = %{version}-%{release}

%description
Imlib is a display depth independent image loading and rendering
library. Imlib is designed to simplify and speed up the process of
loading images and obtaining X Window System drawables. Imlib
provides many simple manipulation routines which can be used for
common operations.

The imlib package also contains the imlib_config program, which
you can use to configure the Imlib image loading and rendering
library. Imlib_config can be used to control how Imlib uses color and
handles gamma corrections, etc.

Install imlib if you need an image loading and rendering library for
X11R6, or if you are installing GNOME. 

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: libtiff-devel, libjpeg-devel
Requires: zlib-devel, gtk+-devel

Obsoletes: Imlib-devel <= %{version}-%{release}
Provides: Imlib-devel = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup
%patch2 -p1 -b .ac25
%patch3 -p1 -b .cppflags
%patch4 -p1 -b .gmodulehack
%patch5 -p1 -b .waitpid
%patch6 -p1 -b .underquoted
%patch7 -p1 -b .bounds

%build
%configure
%{__make}

###########################################################################

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING.LIB README
%config(noreplace) %{_sysconfdir}/im_palette*.pal
%config(noreplace) %{_sysconfdir}/imrc
%{_bindir}/imlib_config
%{_libdir}/libgdk_imlib.so.*
%{_libdir}/libImlib.so.*
%{_libdir}/libimlib-*.so

%files devel
%defattr(-, root, root, 0755)
%doc doc/*.gif doc/*.html
%doc %{_datadir}/man/man*/*
%{_bindir}/imlib-config
%{_includedir}/Imlib*.h
%{_includedir}/gdk_imlib*.h
%{_datadir}/aclocal/imlib.m4
%exclude %{_libdir}/libgdk_imlib.a
%exclude %{_libdir}/libgdk_imlib.la
%{_libdir}/libgdk_imlib.so
%exclude %{_libdir}/libImlib.a
%exclude %{_libdir}/libImlib.la
%{_libdir}/libImlib.so
%exclude %{_libdir}/libimlib-*.a
%exclude %{_libdir}/libimlib-*.la
%{_libdir}/pkgconfig/*

%changelog
* Mon Mar 26 2007 Dag Wieers <dag@wieers.com> 1:1.9.13-1
- Initial package. (using DAR)
