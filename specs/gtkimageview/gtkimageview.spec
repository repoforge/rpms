# $Id$
# Authority: dag

Summary: Simple image viewer widget
Name: gtkimageview
Version: 1.6.3
Release: 1%{?dist}
License: LGPL
Group: System Environment/Libraries
URL: http://trac.bjourne.webfactional.com/

#Source: http://trac.bjourne.webfactional.com/attachment/wiki/WikiStart/gtkimageview-%{version}.tar.gz?format=raw
Source: gtkimageview-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: glib2-devel
BuildRequires: gtk2-devel >= 2.6
BuildRequires: gtk-doc >= 1.0
BuildRequires: pkgconfig

%description
GtkImageView is a simple image viewer widget for GTK. It makes writing image
viewing and editing applications easy.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: gtk-doc
Requires: pkgconfig

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
%configure --disable-static
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%doc COPYING README
%{_libdir}/libgtkimageview.so.*

%files devel
%defattr(-, root, root, 0755)
%doc %{_datadir}/gtk-doc/html/gtkimageview/
%{_includedir}/*
%{_libdir}/libgtkimageview.so
%{_libdir}/pkgconfig/gtkimageview.pc
%exclude %{_libdir}/libgtkimageview.la

%changelog
* Tue Dec 09 2008 Dag Wieers <dag@wieers.com> - 1.6.1-1
- Initial package. (using DAR)
