# $Id$

# Authority: dag

%define rname gtkhtml

Summary: The Gtk+ HTML viewing widget version 3
Name: gtkhtml3
Version: 3.0.8
Release: 0
License: GPL
Group: System Environment/Libraries
URL: http://www.gnome.org/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://ftp.acc.umu.se/pub/GNOME/sources/gtkhtml/3.0/%{rname}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: libgal >= 2.2
#Requires: gtk2 >= 2.2.2, libxml2 >= 2.5.7, gnome-vfs2 >= 2.3.5, gail >= 1.3.3
#Requires: libsoup >= 1.99.24, libgal >= 2.1.0.99

%description
Gtkhtml3 (sometimes called libgtkhtml3) is a small
and standards compilant library for displaying
html pages.

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n %{rname}-%{version}

%build
%configure \
	--enable-shlib-factory
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{rname}-3.1

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/*.la \
		%{buildroot}%{_libdir}/gtkhtml/*.la

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files -f %{rname}-3.1.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_libdir}/bonobo/servers/GNOME_GtkHTML_Editor.server
%{_libdir}/*.so.*
%{_libdir}/gtkhtml/*.so*
%{_datadir}/gtkhtml-3.1/

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/libgtkhtml-3.1/
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/gtkhtml/*.a
%{_libdir}/pkgconfig/*.pc

%changelog
* Thu Aug 14 2003 Dag Wieers <dag@wieers.com> - 3.1.0-2
- Initial package. (using DAR)
