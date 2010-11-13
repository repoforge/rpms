# $Id$
# Authority: dag

### EL6 ships with libsexy-0.1.11-13.el6
# ExclusiveDist: el2 el3 el4 el5

Summary: Collection of GTK+ widgets that extend functionality
Name: libsexy
Version: 0.1.11
Release: 1%{?dist}
License: LGPL
Group: System Environment/Libraries
URL: http://www.chipx86.com/wiki/Libsexy

Source: http://releases.chipx86.com/libsexy/libsexy/libsexy-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libxml2-devel, gtk2-devel, iso-codes-devel
BuildRequires: gtk-doc, enchant-devel
Requires: enchant

%description
libsexy is a collection of GTK+ widgets that extend the functionality of such
standard widgets as GtkEntry and GtkLabel by subclassing them and working
around the limitations of the widgets.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig, gtk2-devel

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
%configure \
    --disable-static \
    --enable-gtk-doc
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
%doc AUTHORS COPYING NEWS
%{_libdir}/libsexy.so.*

%files devel
%defattr(-, root, root, 0755)
%doc %{_datadir}/gtk-doc/html/libsexy/
%{_includedir}/libsexy/
%{_libdir}/libsexy.so
%{_libdir}/pkgconfig/libsexy.pc
%exclude %{_libdir}/libsexy.la

%changelog
* Mon Jun 25 2007 Dag Wieers <dag@wieers.com> - 0.1.11-1
- Initial package. (using DAR)
