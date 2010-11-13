# $Id$
# Authority: dag

Summary: New canvas widget for GTK+ that uses cairo for drawing
Name: goocanvas
Version: 0.15
Release: 1%{?dist}
License: LGPLv2+
Group: System Environment/Libraries
URL: http://live.gnome.org/GooCanvas/

Source: http://ftp.gnome.org/pub/GNOME/sources/goocanvas/%{version}/goocanvas-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: cairo-devel >= 1.4.0
BuildRequires: gettext
BuildRequires: gtk2-devel >= 2.12.0
BuildRequires: pkgconfig

%description
GooCanvas is a new canvas widget for GTK+ that uses the cairo 2D library for
drawing. It has a model/view split, and uses interfaces for canvas items and
views, so you can easily turn any application object into canvas items.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

### Disable demo applications
%{__perl} -pi.orig -e 's| demo | |g' Makefile.am Makefile.in

%build
%configure --disable-static
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_libdir}/libgoocanvas.so.*

%files devel
%defattr(-, root, root, 0755)
%doc %{_datadir}/gtk-doc/html/goocanvas/
%{_includedir}/goocanvas-1.0/
%{_libdir}/libgoocanvas.so
%{_libdir}/pkgconfig/goocanvas.pc
%exclude %{_libdir}/libgoocanvas.la

%changelog
* Thu Jun 03 2010 Dag Wieers <dag@wieers.com> - 0.15-1
- Initial package. (using DAR)
