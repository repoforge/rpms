# Authority: dag

%define rname libgtkhtml

Summary: An HTML widget for GTK+ 2.0.
Name: gtkhtml2
Version: 2.3.3
Release: 0
License: LGPL
Group: System Environment/Libraries
URL: http://ftp.gnome.org/pub/GNOME/sources/libgtkhtml/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://ftp.gnome.org/pub/GNOME/sources/libgtkhtml/2.3/%{rname}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: pango-devel >= 1.0.99, gtk2-devel >= 2.1.0, libxml2-devel >= 2.4.20
BuildRequires: gnome-vfs2-devel >= 2.0.0, gail-devel >= 1.0, fontconfig

%description
GtkHTML2 (sometimes called libgtkhtml) is a widget for
displaying html pages.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n %{rname}-%{version}
#patch1 -p0 -b .styleref

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_libdir}/*.la

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/gtkhtml-2.0/
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
* Sat Jun 28 2003 Dag Wieers <dag@wieers.com> - 2.3.3-0
- Initial package. (using DAR)
