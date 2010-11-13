# $Id$
# Authority: dag

### EL6 ships with libgnomeuimm26-2.28.0-1.el6
# ExclusiveDist: el2 el3 el4 el5

%define real_name libgnomeuimm

Summary: C++ wrapper for Gnome libs (a GUI library for X)
Name: libgnomeuimm26
Version: 2.18.0
Release: 1%{?dist}
License: LGPL
Group: System Environment/Libraries
URL: http://gtkmm.sourceforge.net/

Source: http://ftp.gnome.org/pub/GNOME/sources/libgnomeuimm/2.18/libgnomeuimm-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gconfmm26-devel >= 2.6.0
BuildRequires: gnome-vfsmm26-devel >= 2.6.0
BuildRequires: libglademm24-devel >= 2.4.0
BuildRequires: libgnomecanvasmm26-devel >= 2.6.0
BuildRequires: libgnomemm26-devel >= 2.14.0
BuildRequires: libgnomeui-devel >= 2.7.1

%description
This package provides a C++ interface for GnomeUI.  It is a subpackage
of the Gtk-- project.  The interface provides a convenient interface for C++
programmers to create Gnome GUIs with GTK+'s flexible object-oriented
framework.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: libgnomeui-devel
Requires: libgnomemm26-devel
Requires: libgnomecanvasmm26-devel
Requires: gconfmm26-devel
Requires: libglademm24-devel
Requires: gnome-vfsmm26-devel

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
%{_libdir}/libgnomeuimm-2.6.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/libgnomeuimm-2.6/
%{_libdir}/libgnomeuimm-2.6.so
%{_libdir}/libgnomeuimm-2.6/
%{_libdir}/pkgconfig/libgnomeuimm-2.6.pc
%exclude %{_libdir}/libgnomeuimm-2.6.la

%changelog
* Mon Sep 24 2007 Dag Wieers <dag@wieers.com> - 2.18.0-1
- Initial package. (using DAR)
