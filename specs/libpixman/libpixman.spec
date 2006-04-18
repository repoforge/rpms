# $Id$
# Authority: dag

Summary: Merge of libpixregion and libic
Name: libpixman
Version: 0.1.2
Release: 1.2
License: MIT
Group: System Environment/Libraries
URL: http://www.cairographics.org/

Source: http://www.cairographics.org/snapshots/libpixman-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: pkgconfig, gcc-c++
Obsoletes: slim, libic, libpixregion

%description
libpixman is a merge of libpixregion and libic.

%package devel
Summary: Header files, libraries and development documentation for %{name}
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

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING NEWS README
%{_libdir}/libpixman.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/pixman.h
%{_libdir}/libpixman.a
%exclude %{_libdir}/libpixman.la
%{_libdir}/libpixman.so
%{_libdir}/pkgconfig/libpixman.pc

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.1.2-1.2
- Rebuild for Fedora Core 5.

* Sun Jan 02 2005 Dag Wieers <dag@wieers.com> - 0.1.2-1
- Updated to release 0.1.1.

* Sun Jul 25 2004 Dag Wieers <dag@wieers.com> - 0.1.1-1
- Updated to release 0.1.1.

* Wed Feb 25 2004 Dag Wieers <dag@wieers.com> - 0.1.0-0
- Initial package. (using DAR)
