# Authority: dag

Summary: Library for using OBEX.
Name: openobex
Version: 1.0.1
Release: 1
License: LGPL
Group: System Environment/Libraries
URL: http://openobex.sourceforge.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://prdownloads.sourceforge.net/openobex/openobex-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: glib-devel >= 1.2.0
%{?rhfc1:BuildRequires: bluez-libs-devel}
%{?rh90:BuildRequires: bluez-libs-devel}

%description
Open OBEX shared c-library.

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

%{?rhfc1:echo "Don't build for RHFC1 !"; exit 1}

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall \
	includedir="%{buildroot}%{_includedir}/openobex"

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/*.la

%clean
%{__rm} -rf %{buildroot}

%post
/sbin/ldconfig &>/dev/null

%postun
/sbin/ldconfig &>/dev/null

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_bindir}/*
%{_libdir}/*.a
%{_libdir}/*.so
%{_includedir}/openobex/
%{_datadir}/aclocal/*.m4

%changelog
* Wed Feb 04 2004 Dag Wieers <dag@wieers.com> - 1.0.1-1
- Rebuild against bluez-libs-devel (bluetooth support).

* Wed Oct 29 2003 Dag Wieers <dag@wieers.com> - 1.0.1-0
- Initial package. (using DAR)
