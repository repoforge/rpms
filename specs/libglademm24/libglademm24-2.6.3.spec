# $Id$
# Authority: dag

%define real_name libglademm

Summary: C++ wrapper for libglade
Name: libglademm24
Version: 2.6.3
Release: 1%{?dist}
License: LGPL
Group: System Environment/Libraries
URL: http://gtkmm.sourceforge.net/

Source: http://ftp.gnome.org/pub/GNOME/sources/libglademm/2.6/libglademm-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtkmm24-devel >= 2.6.0
BuildRequires: libglade2-devel >= 2.6.0
Requires: /sbin/ldconfig

%description
This package provides a C++ interface for libglademm. It is a
subpackage of the GTKmm project.  The interface provides a convenient
interface for C++ programmers to create Gnome GUIs with GTK+'s
flexible object-oriented framework.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: gtkmm24-devel
Requires: libglade2-devel

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n %{real_name}-%{version}

%build
%configure --disable-static --enable-docs
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

### Clean up buildroot
%{__mv} %{buildroot}%{_docdir}/gnomemm-2.6/libglademm-2.4/ rpm-docs/
%{__rm} -f %{buildroot}%{_datadir}/devhelp/books/libglademm-2.4/*

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%{_libdir}/libglademm-2.4.so.*

%files devel
%defattr(-, root, root, 0755)
%doc rpm-docs/*
%{_includedir}/libglademm-2.4/
%{_libdir}/libglademm-2.4/
%{_libdir}/libglademm-2.4.so
%{_libdir}/pkgconfig/libglademm-2.4.pc
%exclude %{_libdir}/libglademm-2.4.la

%changelog
* Mon Sep 10 2007 Dag Wieers <dag@wieers.com> - 2.6.3-1
- Initial package. (using DAR)
