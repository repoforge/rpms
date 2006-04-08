# $Id$
# Authority: dries
# Upstream: Alistair Riddoch <alriddoch$zepler,org>

Summary: Terrain generation and management library
Name: mercator
Version: 0.2.4
Release: 1.2
License: GPL
Group: Development/Libraries
URL: http://www.worldforge.org/dev/eng/libraries/mercator

Source: http://dl.sf.net/worldforge/mercator-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: wfmath-devel, gcc-c++, pkgconfig

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
%makeinstall

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%{_libdir}/libmercator*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/Mercator*/
%{_libdir}/libmercator*.so
%exclude %{_libdir}/libmercator*.la
%{_libdir}/pkgconfig/mercator*.pc

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.2.4-1.2
- Rebuild for Fedora Core 5.

* Wed Jan 04 2006 Dries Verachtert <dries@ulyssis.org> - 0.2.4-1
- Initial package.
