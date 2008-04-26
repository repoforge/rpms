# $Id$
# Authority: dag

%{?dtag: %{expand: %%define %dtag 1}}

%{!?dtag:%define _with_modxorg 1}
%{?fc7:%define _with_modxorg 1}
%{?el5:%define _with_modxorg 1}
%{?fc6:%define _with_modxorg 1}
%{?fc5:%define _with_modxorg 1}

Summary: Anti-Grain Geometry, a rendering engine
Name: agg
Version: 2.5
Release: 1
License: GPL
Group: System Environment/Libraries
URL: http://www.antigrain.com/

Source: http://www.antigrain.com/agg-%{version}.tar.gz
Patch0: agg-2.4-depends.patch
Patch1: agg-2.5-pkgconfig.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: automake, libtool, freetype-devel, SDL-devel
%{?_with_modxorg:BuildRequires: libX11-devel}
%{!?_with_modxorg:BuildRequires: XFree86-devel}

%description
Anti-Grain Geometry is a high quality rendering engine for C++.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: freetype-devel

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup
%patch0 -p1 -b .agg-2.4-depends
%patch1 -p1 -b .agg-2.5-pkgconfig.patch

%build
sh autogen.sh
%configure \
    --disable-gpc \
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
%doc authors ChangeLog copying install news readme
%{_libdir}/libagg*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_datadir}/aclocal/libagg.m4
%{_includedir}/agg2/
%{_libdir}/libagg*.so
%{_libdir}/pkgconfig/libagg.pc
%exclude %{_libdir}/libagg*.la

%changelog
* Mon Sep 24 2007 Dag Wieers <dag@wieers.com> - 2.5-1
- Initial package. (using DAR)
