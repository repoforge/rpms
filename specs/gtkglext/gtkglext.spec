# Authority: newrpms

Summary: OpenGL Extension to GTK.
Name: gtkglext
Version: 1.0.5
Release: 0
License: LGPL
Group: System Environment/Libraries
URL: http://gtkglext.sourceforge.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://umn.dl.sourceforge.net/sourceforge/gtkglext/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/root-%{name}-%{version}
BuildRequires: XFree86-devel, gtk+-devel, pkgconfig

%description
GtkGLExt is an OpenGL extension to GTK. It provides the GDK objects
which support OpenGL rendering in GTK, and GtkWidget API add-ons to
make GTK+ widgets OpenGL-capable.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}, XFree86-devel, gtk+-devel

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
export CFLAGS="-UGTK_DISABLE_DEPRECATED"
%configure \
	--disable-gtk-doc
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/*.la

%clean
%{__rm} -rf %{buildroot}

%post
/sbin/ldconfig &>/dev/null

%postun
/sbin/ldconfig &>/dev/null

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING COPYING.LIB NEWS README TODO
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%doc examples/
%doc %{_datadir}/gtk-doc/html/gtkglext/
%{_includedir}/gtkglext-1.0/
%{_libdir}/gtkglext-1.0/
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/pkgconfig/*.pc
%{_datadir}/aclocal/*.m4

%changelog
* Sat Jan 24 2004 Dag Wieers <dag@wieers.com> - 1.0.5-0
- Initial package. (using DAR)
