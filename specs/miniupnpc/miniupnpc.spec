# $Id$
# Authority: dag

Summary: Library and tool to control NAT in UPnP-enabled routers
Name: miniupnpc
Version: 1.5
Release: 1%{?dist}
License: BSD
Group: System Environment/Libraries
URL: http://miniupnp.tuxfamily.org/

Source: http://miniupnp.tuxfamily.org/files/miniupnpc-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
miniupnpc is an implementation of a UPnP client library, enabling applications
to access the services provided by an UPnP "Internet Gateway Device" present
on the network. In UPnP terminology, it is a UPnP Control Point. 

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

%{__perl} -pi -e 's|/lib\b|/%{_lib}|g' Makefile

%build
%{__make} %{?_smp_mflags} CFLAGS="%{optflags} -DNDEBUG" CC="%{__cc} %{optflags} -fPIC -DNDEBUG"

%install
%{__rm} -rf %{buildroot}
%{__make} install PREFIX="%{buildroot}"

%{__install} -Dp -m0644 man3/miniupnpc.3 %{buildroot}%{_mandir}/man3/miniupnpc.3

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%doc Changelog.txt LICENSE README
%{_bindir}/external-ip
%{_bindir}/upnpc
%{_libdir}/libminiupnpc.so.*

%files devel
%defattr(-, root, root, 0755)
%doc %{_mandir}/man3/miniupnpc.3*
%{_includedir}/miniupnpc/
%{_libdir}/libminiupnpc.so
%exclude %{_libdir}/libminiupnpc.a

%changelog
* Sun Jun 19 2011 Dag Wieers <dag@wieers.com> - 1.5-1
- Updated to release 1.5.

* Thu Sep 23 2010 Dag Wieers <dag@wieers.com> - 1.4-1
- Initial package. (using DAR)
