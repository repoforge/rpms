# $Id$
# Authority: dag

%define real_name gconfmm

Summary: C++ wrapper for GConf2
Name: gconfmm26
Version: 2.8.1
Release: 1%{?dist}
License: LGPL
Group: System Environment/Libraries
URL: http://gtkmm.sourceforge.net/

Source: http://ftp.gnome.org/pub/GNOME/sources/gconfmm/2.8/gconfmm-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: GConf2-devel >= 2.4.0
BuildRequires: glibmm24-devel >= 2.4.0
BuildRequires: gtkmm24-devel >= 2.4.0
Requires: ldconfig

%description
This package provides a C++ interface for GConf2. It is a subpackage
of the GTKmm project.  The interface provides a convenient interface
for C++ programmers to create Gnome GUIs with GTK+'s flexible
object-oriented framework.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: GConf2-devel
Requires: glibmm24-devel
Requires: gtkmm24-devel

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n %{real_name}-%{version}

%build
%configure \
    --disable-static \
    --enable-shared
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
%doc AUTHORS ChangeLog COPYING NEWS README INSTALL
%{_libdir}/libgconfmm-2.6.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/gconfmm-2.6/
%{_libdir}/gconfmm-2.6/
%{_libdir}/libgconfmm-2.6.so
%{_libdir}/pkgconfig/gconfmm-2.6.pc
%exclude %{_libdir}/libgconfmm-2.6.la

%changelog
* Mon Sep 10 2007 Dag Wieers <dag@wieers.com> - 2.8.1-1
- Initial package. (using DAR)
