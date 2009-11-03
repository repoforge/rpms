# $Id$
# Authority: matthias

%define real_name libglademm

Summary: C++ wrappers for libglade, for use with gtkmm
Name: libglademm2
Version: 2.0.1
Release: 0%{?dist}
License: LGPL
Group: System Environment/Libraries
URL: http://gtkmm.sourceforge.net/

Source: http://dl.sf.net/gtkmm/libglademm-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtkmm2-devel >= 2.0, libsigc++ >= 1.2, glib2-devel >= 2.0
BuildRequires: pango-devel >= 1.0, freetype-devel >= 2.0
BuildRequires: atk-devel >= 1.0, libglade2 >= 2.0, libxml2 >= 2.0

%description
libglademm provides C++ wrappers for libglade, for use with gtkmm.

%package devel
Summary: Headers for developing programs that will use %{real_name}
Group: Development/Libraries

%description devel
This package contains the static libraries and header files needed for
developing gtkmm applications.

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
%{_includedir}/libglademm-2.0/
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/libglademm-2.0/
%{_libdir}/pkgconfig/*.pc
%exclude %{_libdir}/*.la

%changelog
* Sat Mar 29 2003 Dag Wieers <dag@wieers.com> - 2.0.1-0
- Initial package. (using DAR)
