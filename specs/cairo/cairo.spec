# $Id$

# Authority: dag

Summary: Anti-aliased vector-based rendering for X.
Name: cairo
Version: 0.1.18
Release: 0
License: MIT
Group: System Environment/Libraries
URL: http://www.cairographics.org/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.cairographics.org/snapshots/cairo-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: pkgconfig, freetype-devel, fontconfig-devel, libpixman-devel, XFree86-devel

%description
Cairo provides anti-aliased vector-based rendering for X. Paths consist
of line segments and cubic splines and can be rendered at any width with
various join and cap styles. All colors may be specified with optional
translucence (opacity/alpha) and combined using the extended Porter/Duff
compositing algebra as found in the X Render Extension.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: libpixman-devel, XFree86-devel

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_libdir}/*.la

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/pkgconfig/*.pc
#%{_libdir}/*.la

%changelog
* Wed Feb 25 2004 Dag Wieers <dag@wieers.com> - 0.1.18-0
- Initial package. (using DAR)
