# $Id: libxml++.spec 4303 2006-04-18 22:05:03Z dries $
# Authority: dag
# Upstream: <libxmlplusplus-general$lists,sf,net>

Summary: C++ interface for working with XML files
Name: libxml++
Version: 0.26.0
Release: 1%{?dist}
License: LGPL
Group: System Environment/Libraries
URL: http://libxmlplusplus.sourceforge.net/

Source: http://dl.sf.net/libxmlplusplus/libxml++-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, libxml2-devel >= 2.5.1

%description
libxml++ is a C++ interface for working with XML files, using libxml
(gnome-xml) to parse and write the actual XML files. It has a simple
but complete API.

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
%configure --disable-static
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
%doc AUTHORS ChangeLog COPYING NEWS README
%{_libdir}/libxml++-0.1.so.*

%files devel
%defattr(-, root, root, 0755)
%doc examples/
%{_includedir}/libxml++-1.0/
%{_libdir}/libxml++-0.1.so
%{_libdir}/pkgconfig/libxml++-1.0.pc
%exclude %{_libdir}/libxml++-0.1.la

%changelog
* Tue Aug 07 2007 Dag Wieers <dag@wieers.com> - 0.26.0-1
- Cosmetic cleanup.

* Mon Jan 05 2004 Dag Wieers <dag@wieers.com> - 0.26.0-0
- Updated to release 0.26.0.

* Thu Sep 11 2003 Dag Wieers <dag@wieers.com> - 0.25.0-0
- Initial package. (using DAR)
