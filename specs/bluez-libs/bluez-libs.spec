# $Id$

# Authority: dag

Summary: Bluetooth libraries.
Name: bluez-libs
Version: 2.5
Release: 0
License: GPL
Group: System Environment/Libraries
URL: http://bluez.sf.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://bluez.sf.net/download/bluez-libs-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

ExcludeArch: s390 s390x
BuildRequires: glib-devel >= 1.2

%description
Libraries for use in Bluetooth applications.

The BLUETOOTH trademarks are owned by Bluetooth SIG, Inc., U.S.A.

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
%makeinstall \
	includedir="%{buildroot}%{_includedir}/bluetooth"

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/*.la

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/bluetooth/*
%{_libdir}/*.a
%{_libdir}/*.so

%changelog
* Wed Feb 04 2004 Dag Wieers <dag@wieers.com> - 2.5-0
- Initial package. (using DAR)
