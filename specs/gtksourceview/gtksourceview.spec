# $Id$
# Authority: dag

### EL6 ships with gtksourceview-1.8.5-7.el6.1
### EL5 ships with gtksourceview-1.8.0-1.fc6
### EL4 ships with gtksourceview-1.1.0-4
# ExclusiveDist: el2 el3

Summary: Source code viewer
Name: gtksourceview
Version: 0.9.0
Release: 0%{?dist}
License: GPL
Group: Applications/Editors
URL: http://gtksourceview.sourceforge.net/

Source: http://ftp.gnome.org/pub/GNOME/sources/gtksourceview/0.9/gtksourceview-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc-c++, intltool, perl-XML-Parser, gtk2-devel
BuildRequires: pkgconfig, libxml2-devel, libgnomeprint22
BuildRequires: libgnomeprint22-devel, gnome-vfs2-devel, libgnomeprintui22-devel

%description
GtkSourceView is a text widget that extends the standard gtk+ 2.x
text widget GtkTextView.
It improves GtkTextView by implementing syntax highlighting and other
features typical of a source editor.

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
%configure \
	--disable-dependency-tracking
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}-1.0

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/*.la

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}-1.0.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING MAINTAINERS NEWS README TODO
%{_libdir}/*.so.*
%{_datadir}/gtksourceview-1.0/

%files devel
%defattr(-, root, root, 0755)
%doc HACKING
%doc %{_datadir}/gtk-doc/html/gtksourceview/
%{_includedir}/gtksourceview-1.0/
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
* Mon Feb 16 2004 Dag Wieers <dag@wieers.com> - 0.9.0-0
- Updated to release 0.9.0

* Mon Sep 15 2003 Dag Wieers <dag@wieers.com> - 0.6.0-0
- Updated to release 0.6.0

* Thu Jul 24 2003 Dag Wieers <dag@wieers.com> - 0.4.0-0
- Initial package. (using DAR)
