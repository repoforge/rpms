# $Id$
# Authority: dag

### EL6 ships with libgnomemm26-2.28.0-2.el6
# ExclusiveDist: el2 el3 el4 el5

%define real_name libgnomemm

Summary: C++ wrapper for Gnome libs
Name: libgnomemm26
Version: 2.18.0
Release: 1%{?dist}
License: LGPL
Group: System Environment/Libraries
URL: http://gtkmm.sourceforge.net/

Source: http://ftp.gnome.org/pub/GNOME/sources/libgnomemm/2.18/libgnomemm-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtkmm24-devel >= 2.8.0
BuildRequires: libgnome-devel >= 2.6.0
Requires: /sbin/ldconfig

%description
This package provides a C++ interface for GnomeUI.  It is a subpackage
of the Gtk-- project.  The interface provides a convenient interface for C++
programmers to create Gnome GUIs with GTK+'s flexible object-oriented
framework.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: gtkmm24-devel
Requires: libgnome-devel

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
%{_libdir}/libgnomemm-2.6.so.*

%files devel
%defattr(-, root, root, -)
%doc %{_datadir}/doc/*
%{_includedir}/libgnomemm-2.6/
%{_libdir}/libgnomemm-2.6/
%{_libdir}/libgnomemm-2.6.so
%{_libdir}/pkgconfig/libgnomemm-2.6.pc
%exclude %{_libdir}/libgnomemm-2.6.la

%changelog
* Tue Sep 11 2007 Dag Wieers <dag@wieers.com> - 2.18.0-1
- Initial package. (using DAR)
