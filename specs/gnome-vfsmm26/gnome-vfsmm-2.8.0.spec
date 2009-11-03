# $Id$
# Authority: dag

%define real_name gnome-vfsmm

Summary: C++ wrapper for gnome-vfs
Name: gnome-vfsmm26
Version: 2.8.0
Release: 1%{?dist}
License: LGPL
Group: System Environment/Libraries
URL: http://gtkmm.sourceforge.net/

Source: http://ftp.gnome.org/pub/GNOME/sources/gnome-vfsmm/2.8/gnome-vfsmm-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: glibmm24-devel >= 2.4.0
BuildRequires: gnome-vfs2-devel >= 2.8.1
Requires: /sbin/ldconfig

%description
This package is part of the gnomemm project and provides a C++ interface for
gnome-vfs.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: glibmm24-devel
Requires: gnome-vfs2-devel

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n %{real_name}-%{version}
#find -type f -regex '.*\.\(cc\|h\)' -perm +111 -exec chmod -x {} ';'

%build
%configure --disable-static
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
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_libdir}/libgnomevfsmm-2.6.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/gnome-vfsmm-2.6/
%{_libdir}/gnome-vfsmm-2.6/
%{_libdir}/libgnomevfsmm-2.6.so
%{_libdir}/pkgconfig/gnome-vfsmm-2.6.pc
%exclude %{_libdir}/libgnomevfsmm-2.6.la

%changelog
* Mon Sep 10 2007 Dag Wieers <dag@wieers.com> - 2.8.0-1
- Initial package. (using DAR)
