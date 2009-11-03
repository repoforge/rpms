# $Id$
# Authority: dag

%define real_name libgnomecanvasmm

Summary: C++ interface for Gnome libs (a GUI library for X)
Name: libgnomecanvasmm26
Version: 2.8.0
Release: 1%{?dist}
License: LGPL
Group: System Environment/Libraries
URL: http://gtkmm.sourceforge.net/

Source: http://ftp.gnome.org/pub/GNOME/sources/libgnomecanvasmm/2.8/libgnomecanvasmm-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtkmm24-devel >= 2.4.0
BuildRequires: libgnomecanvas-devel >= 2.6.0
Requires: /sbin/ldconfig

%description
This package provides a C++ interface for GnomeUI.  It is a subpackage
of the gnomemm project.  The interface provides a convenient interface for C++
programmers to create Gnome GUIs with GTK+'s flexible object-oriented
framework.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: gtkmm24-devel
Requires: libgnomecanvas-devel

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n %{real_name}-%{version}

%build
%configure \
    --disable-static \
    --enable-docs
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
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README
%{_libdir}/libgnomecanvasmm-2.6.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/libgnomecanvasmm-2.6/
%{_libdir}/libgnomecanvasmm-2.6/
%{_libdir}/libgnomecanvasmm-2.6.so
%{_libdir}/pkgconfig/libgnomecanvasmm-2.6.pc
%exclude %{_libdir}/libgnomecanvasmm-2.6.la

%changelog
* Tue Sep 11 2007 Dag Wieers <dag@wieers.com> - 2.8.0-1
- Initial package. (using DAR)
