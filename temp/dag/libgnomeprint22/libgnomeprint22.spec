# Authority: freshrpms
# Dists: rh80

%define rname libgnomeprint

Summary: Printing library for GNOME.
Name: libgnomeprint22
Version: 2.2.1.1
Release: 0
License: LGPL
Group: System Environment/Base
URL: http://ftp.gnome.org/pub/GNOME/sources/libgnomeprint/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://ftp.gnome.org/pub/GNOME/sources/%{rname}/2.2/%{rname}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

PreReq:	urw-fonts
PreReq:	ghostscript
PreReq:	ghostscript-fonts
PreReq:	libxml
PreReq: perl
PreReq: XFree86

BuildRequires: glib2-devel >= 2.0.0
BuildRequires: pango-devel >= 1.1.0
BuildRequires: libxml2-devel >= 2.4.23
BuildRequires: libart_lgpl-devel >= 2.3.8
BuildRequires: libbonobo-devel >= 2.0.0
BuildRequires: bonobo-activation-devel >= 1.0.0
BuildRequires: freetype >= 2.0.3
BuildRequires: gtk-doc >= 0.9
BuildRequires: Xft
BuildRequires: fontconfig
#Buildrequires: cups-devel

%description 
GNOME (GNU Network Object Model Environment) is a user-friendly set of
applications and desktop tools to be used in conjunction with a window
manager for the X Window System. The gnome-print package contains
libraries and fonts needed by GNOME applications for printing.

You should install the gnome-print package if you intend to use any of
the GNOME applications that can print. If you would like to develop
GNOME applications that can print you will also need to install the
gnome-print devel package.

%package devel
Summary: Libraries and include files for developing GNOME applications.
Group: Development/Libraries
Requires: %{name} = %{version}

%description devel
GNOME (GNU Network Object Model Environment) is a user-friendly set of
applications and desktop tools to be used in conjunction with a window
manager for the X Window System. The gnome-print-devel package
includes the libraries and include files needed for developing
applications that use the GNOME printing capabilities.

You should install the gnome-print-devel package if you would like to
develop GNOME applications that will use the GNOME print capabilities.
You do not need to install the gnome-print-devel package if you just
want to use the GNOME desktop environment.

%prep
%setup -n %{rname}-%{version}

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{rname}-2.2

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{rname}-2.2.lang
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_libdir}/*.so.*
%{_libdir}/libgnomeprint/
%{_datadir}/libgnomeprint/

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/pkgconfig/*
%{_datadir}/gtk-doc
%exclude %{_libdir}/*.la

%changelog
* Mon Feb 17 2003 Dag Wieers <dag@wieers.com> - 2.2.1.1-0
- Initial package. (using DAR)
