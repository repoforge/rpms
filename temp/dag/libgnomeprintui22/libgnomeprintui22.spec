# Authority: freshrpms
# Dists: rh80

%define rname libgnomeprintui

Summary: GUI support for libgnomeprint
Name: libgnomeprintui22
Version: 2.2.1.1
Release: 0
License: LGPL
Group: System Environment/Libraries
URL: http://ftp.gnome.org/pub/gnome/sources/libgnomeprintui/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: %{rname}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: gtk2-devel >= 2.0.0
BuildRequires: libgnomeprint22-devel >= 2.2.1.1
BuildRequires: libgnomecanvas-devel >= 2.0.0
BuildRequires: fontconfig-devel

%description
The libgnomeprintui package contains GTK+ widgets related to printing.

%package devel
Summary: Libraries and headers for libgnomeprintui
Group: Development/Libraries
Requires: %{name} = %{version}

%description devel
The libgnomeprintui package contains GTK+ widgets related to printing.

You should install the libgnomeprintui-devel package if you would like
to compile applications that use the widgets in libgnomeprintui. You
do not need to install it if you just want to use precompiled
applications.

%prep
%setup -n %{rname}-%{version}

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{rname}-2.2

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files -f %{rname}-2.2.lang
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*.h
%{_datadir}/gtk-doc
%exclude %{_libdir}/*.la

%changelog
* Mon Feb 17 2003 Dag Wieers <dag@wieers.com> - 2.2.1.1-0
- Initial package. (using DAR)
