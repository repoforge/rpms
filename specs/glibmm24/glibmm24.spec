# $Id$
# Authority: dag

### EL6 ships with glibmm24-2.22.1-1.el6
# DistExclusive: el2 el3 el4 el5

Summary: C++ interface for GTK2 (a GUI library for X)
Name: glibmm24
Version: 2.4.8
Release: 1%{?dist}
License: LGPL
Group: System Environment/Libraries
URL: http://gtkmm.sourceforge.net/

Source: http://ftp.gnome.org/pub/GNOME/sources/glibmm/2.4/glibmm-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libsigc++20-devel >= 2.0.0
BuildRequires: glib2-devel >= 2.4.0

%description
gtkmm provides a C++ interface to the GTK+ GUI library. gtkmm2 wraps GTK+ 2.
Highlights include typesafe callbacks, widgets extensible via inheritance
and a comprehensive set of widget classes that can be freely combined to
quickly create complex user interfaces.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: glib2-devel
Requires: libsigc++20-devel

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n glibmm-%{version}

%build
%configure \
	--disable-static
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%{__install} -dp -m0755 rpm-doc/
%{__mv} -f %{buildroot}%{_docdir}/glibmm-2.4/* rpm-doc/

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_libdir}/libglibmm-2.4.so.*
%{_libdir}/libglibmm_generate_extra_defs-2.4.so.*

%files devel
%defattr(-, root, root, 0755)
%doc CHANGES rpm-doc/*
%{_datadir}/aclocal/glibmm_check_perl.m4
%{_includedir}/glibmm-2.4/
%{_libdir}/glibmm-2.4/
%{_libdir}/libglibmm-2.4.so
%{_libdir}/libglibmm_generate_extra_defs-2.4.so
%{_libdir}/pkgconfig/glibmm-2.4.pc
%exclude %{_libdir}/libglibmm-2.4.la
%exclude %{_libdir}/libglibmm_generate_extra_defs-2.4.la

%changelog
* Tue Feb 13 2007 Dag Wieers <dag@wieers.com> - 2.4.8-1
- Initial package. (using DAR)
