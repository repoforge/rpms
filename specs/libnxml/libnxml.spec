# $Id$
# Authority: dries
# Upstream: Andrea Marchesini <bakunin$autistici,org>

Summary: Library for parsing, writing and creating XML
Name: libnxml
Version: 0.18.2
Release: 1
License: GPL
Group: Development/Libraries
URL: http://autistici.org/bakunin/codes.php

Source: http://autistici.org/bakunin/libnxml/libnxml-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, curl-devel

%description
nXML is a C library for parsing, writing, and creating XML 1.0 and 1.1
files or streams. It supports UTF-8, UTF-16be and UTF-16le, UCS-4 (1234,
4321, 2143, 2312).

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
%configure
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
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%{_libdir}/libnxml.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/nxml.h
%{_libdir}/libnxml.so
%{_libdir}/pkgconfig/nxml.pc
%exclude %{_libdir}/libnxml.a
%exclude %{_libdir}/libnxml.la

%changelog
* Thu Feb 28 2008 Dag Wieers <dag@wieers.com> - 0.18.2-1
- Updated to release 0.18.2.

* Wed Sep 19 2007 Dries Verachtert <dries@ulyssis.org> - 0.18.1-1
- Updated to release 0.18.1.

* Fri Jul 06 2007 Dag Wieers <dag@wieers.com> - 0.18.0-1
- Updated to release 0.18.0.

* Fri Jun 08 2007 Dag Wieers <dag@wieers.com> - 0.17.3-1
- Updated to release 0.17.3.

* Wed Apr 18 2007 Dries Verachtert <dries@ulyssis.org> - 0.17.2-1
- Updated to release 0.17.2.

* Tue Apr 17 2007 Dries Verachtert <dries@ulyssis.org> - 0.17.1-1
- Updated to release 0.17.1.

* Sun Mar 18 2007 Dag Wieers <dag@wieers.com> - 0.17-1
- Updated to release 0.17.

* Sat Dec 30 2006 Dries Verachtert <dries@ulyssis.org> - 0.16-1
- Updated to release 0.16.

* Tue Nov 07 2006 Dag Wieers <dag@wieers.com> - 0.15-1
- Updated to release 0.15.

* Sat Oct 28 2006 Dag Wieers <dag@wieers.com> - 0.14-1
- Updated to release 0.14.

* Tue Sep 12 2006 Dag Wieers <dag@wieers.com> - 0.13-1
- Updated to release 0.13.

* Fri Jul 14 2006 Dag Wieers <dag@wieers.com> - 0.12-1
- Updated to release 0.12.

* Wed Jun 14 2006 Dag Wieers <dag@wieers.com> - 0.11-1
- Updated to release 0.11.

* Tue Mar 07 2006 Dag Wieers <dag@wieers.com> - 0.9-1
- Updated to release 0.9.

* Sun Feb 12 2006 Dries Verachtert <dries@ulyssis.org> - 0.8-1
- Updated to release 0.8.

* Mon Feb 06 2006 Dag Wieers <dag@wieers.com> - 0.6-1
- Updated to release 0.6.

* Wed Jan 25 2006 Dries Verachtert <dries@ulyssis.org> - 0.5-1
- Updated to release 0.5.

* Fri Dec 16 2005 Dries Verachtert <dries@ulyssis.org> - 0.3-1
- Initial package.
