# $Id$
# Authority: dries
# Upstream: Alistair Riddoch <alriddoch$zepler,org>

Summary: Terrain generation and management library
Name: mercator
Version: 0.2.6
Release: 1%{?dist}
License: GPL
Group: Development/Libraries
URL: http://www.worldforge.org/dev/eng/libraries/mercator

Source: http://dl.sf.net/worldforge/mercator-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, pkgconfig, wfmath-devel

%description
Mercator is a terrain generation and management library that handles the
data required to handle terrain rendering and physics, including classes
to handle vegetation.

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
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%{_libdir}/libmercator*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/Mercator-0.2/
%{_libdir}/libmercator-0.2.so
%exclude %{_libdir}/libmercator-0.2.la
%{_libdir}/pkgconfig/mercator-0.2.pc

%changelog
* Mon Aug 18 2008 Dries Verachtert <dries@ulyssis.org> - 0.2.6-1
- Updated to release 0.2.6.

* Wed May 09 2007 Dag Wieers <dag@wieers.com> - 0.2.5-2
- Rebuild against wfmath 0.3.5.

* Thu Aug 24 2006 Dries Verachtert <dries@ulyssis.org> - 0.2.5-1
- Updated to release 0.2.5.

* Wed Jan 04 2006 Dries Verachtert <dries@ulyssis.org> - 0.2.4-1
- Initial package.
