# $Id$
# Authority: matthias

%define real_name libgnomeuimm

Summary: C++ wrappers for libgnomeui, for use with gtkmm
Name: libgnomeuimm2
Version: 2.0.0
Release: 0%{?dist}
License: LGPL
Group: System Environment/Libraries
URL: http://gtkmm.sourceforge.net/

Source: http://dl.sf.net/gtkmm/libgnomeuimm-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libgnomemm2-devel >= 1.3, libgnomeui-devel >= 2.0
BuildRequires: libgnomecanvasmm2 >= 2.0 gconfmm2 >= 2.0
BuildRequires: libbonobouimm2 >= 1.3, libglademm2 >= 2.0

%description
libgnomeuimm provides C++ wrappers for libgnomeui, for use with gtkmm.

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n %{real_name}-%{version}

%build
%configure \
	--enable-static \
	--enable-shared
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/*.la

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/libgnomeuimm-2.0/
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/libgnomeuimm-2.0/
%{_libdir}/pkgconfig/*.pc
#exclude %{_libdir}/*.la

%changelog
* Wed Feb 04 2004 Dag Wieers <dag@wieers.com> - 2.0.0-0
- Updated to release 2.0.0.

* Tue Nov 23 2003 Dag Wieers <dag@wieers.com> - 1.3.17-0
- Updated to release 1.3.17.

* Sat Mar 29 2003 Dag Wieers <dag@wieers.com> - 1.3.16-0
- Initial package. (using DAR)
