# $Id$
# Authority: dag

Summary: Open Source implementation of the GDI+ API
Name: libgdiplus
Version: 1.0.5
Release: 1.2%{?dist}
License: MIT X11
Group: System Environment/Libraries
URL: http://www.go-mono.com/

Source: http://www.go-mono.com/archive/%{version}/libgdiplus-%{version}.tar.gz
Patch0: libgdiplus-remove-ltmain.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: pkgconfig, cairo-devel >= 0.1.17, glib2-devel >= 2.2.3
BuildRequires: mono-devel, zlib-devel, freetype-devel, libungif-devel,
BuildRequires: libjpeg-devel,

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
%patch0 -p1

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
%{_libdir}/libgdiplus.so.*

%files devel
%defattr(-, root, root, 0755)
%{_libdir}/libgdiplus.so
%{_libdir}/libgdiplus.a
%{_libdir}/pkgconfig/libgdiplus.pc
%exclude %{_libdir}/libgdiplus.la

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.0.5-1.2
- Rebuild for Fedora Core 5.

* Sun Jan 02 2005 Dag Wieers <dag@wieers.com> - 1.0.4-1
- Updated to release 1.0.4.

* Fri Mar 19 2004 Dag Wieers <dag@wieers.com> - 0.2-0
- Updated to release 0.2.

* Wed Feb 25 2004 Dag Wieers <dag@wieers.com> - 0.1-0
- Initial package. (using DAR)
