# $Id: openobex.spec 4308 2006-04-21 22:20:20Z dries $
# Authority: dag

##ExcludeDist: fc1 fc2 fc3
#ExclusiveDist: el2 rh7 rh9 el3 el4

%{?dtag: %{expand: %%define %dtag 1}}

Summary: Library for using OBEX
Name: openobex
Version: 1.3
Release: 1%{?dist}
License: LGPL
Group: System Environment/Libraries
#URL: http://openobex.sourceforge.net/
URL: http://openobex.triq.net/

Source: http://dl.sf.net/openobex/openobex-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: glib-devel >= 1.2.0, bluez-libs-devel

%description
Open OBEX shared c-library.

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
%makeinstall \
	includedir="%{buildroot}%{_includedir}/openobex"

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_libdir}/libopenobex.so.*

%files devel
%defattr(-, root, root, 0755)
%{_bindir}/openobex-config
%{_libdir}/libopenobex.a
%exclude %{_libdir}/libopenobex.la
%{_libdir}/libopenobex.so
%{_includedir}/openobex/
%{_datadir}/aclocal/openobex.m4

%changelog
* Wed Feb 04 2004 Dag Wieers <dag@wieers.com> - 1.0.1-1
- Rebuild against bluez-libs-devel (bluetooth support).

* Wed Oct 29 2003 Dag Wieers <dag@wieers.com> - 1.0.1-0
- Initial package. (using DAR)
