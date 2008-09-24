# $Id$
# Authority: dag

Summary: Cairomm is the C++ API for the cairo graphics library
Name: cairomm
Version: 1.2.4
Release: 2.1
License: LGPL
Group: System Environment/Libraries
URL: http://www.cairographics.org/

Source: http://www.cairographics.org/releases/cairomm-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: cairo-devel >= 1.2.0
BuildRequires: directfb-devel
BuildRequires: pkgconfig

%description
Cairomm is the C++ API for the cairo graphics library. It offers all the power
of cairo with an interface familiar to C++ developers, including use of the 
Standard Template Library where it makes sense.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: cairo-devel >= 1.2.0, pkgconfig

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
%configure \
    --enable-docs="no" \
    --enable-static="no"
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
%doc AUTHORS ChangeLog COPYING README NEWS
%{_libdir}/libcairomm-1.0.so.*

%files devel
%defattr(-, root, root, 0755)
%doc docs/reference/
%{_includedir}/cairomm-1.0/
%{_libdir}/libcairomm-1.0.so
%{_libdir}/pkgconfig/cairomm-1.0.pc
%exclude %{_libdir}/libcairomm-1.0.la

%changelog
* Wed Sep 24 2008 Dag Wieers <dag@wieers.com> - 1.2.4-2.1
- Rebuild against directfb-1.2.4.

* Sat Jul 05 2008 Dag Wieers <dag@wieers.com> - 1.2.4-2
- Rebuild against directfb-1.0.1.

* Thu May 24 2007 Dag Wieers <dag@wieers.com> - 1.2.4-1
- Initial package. (using DAR)
