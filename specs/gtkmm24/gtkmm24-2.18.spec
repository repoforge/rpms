# $Id$
# Authority: dag
# ExcludeDist: el3 el4 el5

%define gtkmm_version 2.18

Summary: C++ interface for GTK2 (a GUI library for X)
Name: gtkmm24
Version: 2.18.2
Release: 1%{?dist}
License: LGPL
Group: System Environment/Libraries
URL: http://gtkmm.sourceforge.net/

Source: http://ftp.gnome.org/pub/GNOME/sources/gtkmm/%{gtkmm_version}/gtkmm-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: glibmm24-devel >= 2.22
BuildRequires: atk-devel >= 1.9.0
BuildRequires: pango-devel >= 1.5.2
BuildRequires: gtk2-devel >= 2.10.0
BuildRequires: glib2-devel >= 2.8.0
BuildRequires: cairomm-devel >= 1.1.12
BuildRequires: libsigc++20-devel >= 2.0.0

%description
gtkmm provides a C++ interface to the GTK+ GUI library. gtkmm2 wraps GTK+ 2.
Highlights include typesafe callbacks, widgets extensible via inheritance
and a comprehensive set of widget classes that can be freely combined to
quickly create complex user interfaces.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

Requires: glib2-devel, gtk2-devel, atk-devel, pango-devel
Requires: glibmm24-devel, cairomm-devel, libsigc++20-devel
Requires: pkgconfig

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%description devel
This package contains the static libraries and header files needed for
developing gtkmm applications.

%prep
%setup -n gtkmm-%{version}

%build
%configure \
	--disable-demos \
	--disable-examples \
	--disable-static \
	--enable-shared
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%{__install} -d -m0755 rpm-doc/
%{__mv} %{buildroot}%{_docdir}/gtkmm-2.4/* rpm-doc/
%{__rm} -rf %{buildroot}%{_datadir}/devhelp/books/gtkmm-2.4/

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%doc CHANGES PORTING rpm-doc/*
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/gdkmm-2.4/
%{_libdir}/gtkmm-2.4/
%{_libdir}/pkgconfig/*.pc
%exclude %{_libdir}/*.la

%changelog
* Fri May 07 2010 Steve Huff <shuff@vecna.org> - 2.18.2-1
- Updated to release 2.18.2.

* Thu May 24 2007 Dag Wieers <dag@wieers.com> - 2.10.9-1
- Updated to release 2.10.9.

* Tue Feb 13 2007 Dag Wieers <dag@wieers.com> - 2.4.8-1
- Initial package. (using DAR)
