# $Id$

# Authority: dag

Summary: Open Source implementation of the GDI+ API
Name: libgdiplus
Version: 0.2
Release: 0
License: MIT X11
Group: System Environment/Libraries
URL: http://www.go-mono.com/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.go-mono.com/archive/libgdiplus-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: pkgconfig, cairo-devel >= 0.1.17, glib2-devel >= 2.2.1
BuildRequires: mono-devel, zlib-devel

%description
libgdiplus is an Open Source implementation of the GDI+ API, it is part
of the Mono Project

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
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/pkgconfig/*.pc
#%{_libdir}/*.la

%changelog
* Fri Mar 19 2004 Dag Wieers <dag@wieers.com> - 0.2-0
- Updated to release 0.2.

* Wed Feb 25 2004 Dag Wieers <dag@wieers.com> - 0.1-0
- Initial package. (using DAR)
