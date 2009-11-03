# $Id$
# Authority: dag

Summary: Structured Storage OLE2 library
Name: libole2
Version: 0.2.4
Release: 1%{?dist}
License: GPL
Group: System Environment/Libraries
URL: ftp://ftp.gnome.org/pub/GNOME/sources/libole2/

Source: ftp://ftp.gnome.org/pub/GNOME/sources/libole2/0.2/libole2-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: glib2-devel >= 1.2

%description
The libole2 library contains functionality for manipulating OLE2
Structured Storage files. It is used by GNOME's Gnumeric, AbiSuite's
AbiWord, and other programs.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
#libtoolize --copy --force
%configure \
    --disable-static
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
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%{_libdir}/libgnomeole2.so.*

%files devel
%defattr(-, root, root, 0755)
%doc %{_datadir}/libole2/html/
%{_bindir}/libole2-config
%{_datadir}/aclocal/gnome-libole2.m4
%{_datadir}/aclocal/libole2.m4
%dir %{_datadir}/libole2/
%{_includedir}/libole2/
%{_libdir}/libgnomeole2.so
%{_libdir}/libole2Conf.sh
%exclude %{_libdir}/libgnomeole2.la

%changelog
* Mon Mar 17 2008 Dag Wieers <dag@wieers.com> - 0.2.4-1
- Initial package. (using DAR)
