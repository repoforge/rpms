# $Id$
# Authority: dag
# Upstream: Jorge Ferrer <jferrer$ieeesb,etsit,upm,es>

Summary: Library for writing gnome database programs
Name: libgnomedb
Version: 1.2.2
Release: 1.2%{?dist}
License: LGPL
Group: System Environment/Libraries
URL: http://www.gnome-db.org/

Source: http://ftp.gnome.org/pub/GNOME/sources/libgnomedb/1.2/libgnomedb-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: pkgconfig >= 0.8, gtk-doc, gettext
BuildRequires: gtk2-devel >= 1.3.6, libbonoboui-devel, libglade2-devel
BuildRequires: libgnomeui-devel >= 1.103.0, libgda-devel
BuildRequires: scrollkeeper, gcc-c++, gtksourceview-devel

Requires(post): scrollkeeper

%description
libgnomedb is a library that eases the task of writing
gnome database programs.

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
	--disable-schemas-install
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL="1"
%makeinstall
%find_lang %{name}-2

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/*.la \
		%{buildroot}%{_libdir}/bonobo/monikers/*.a \
		%{buildroot}%{_libdir}/bonobo/monikers/*.la \
		%{buildroot}%{_libdir}/gnome-vfs-2.0/modules/*.a \
		%{buildroot}%{_libdir}/gnome-vfs-2.0/modules/*.la \
		%{buildroot}%{_libdir}/libglade/2.0/*.a \
		%{buildroot}%{_libdir}/libglade/2.0/*.la \

%post
/sbin/ldconfig 2>/dev/null
export GCONF_CONFIG_SOURCE="$(gconftool-2 --get-default-source)"
gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/%{name}.schemas &>/dev/null
scrollkeeper-update -q || :

%postun
/sbin/ldconfig 2>/dev/null
scrollkeeper-update -q || :

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}-2.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README
%config %{_sysconfdir}/gconf/schemas/*.schemas
#%config %{_sysconfdir}/gnome-vfs-2.0/modules/*
%{_bindir}/*
#%{_libexecdir}/*
%{_datadir}/control-center-2.0/capplets/*
%{_datadir}/gnome-db/
%{_datadir}/mime-info/*
%{_datadir}/pixmaps/libgnomedb/
%{_libdir}/*.so.*
#%{_libdir}/bonobo/monikers/*.so
#%{_libdir}/bonobo/servers/*.server
#%{_libdir}/gnome-vfs-2.0/modules/*.so
%{_libdir}/libglade/2.0/*.so

%files devel
%defattr(-, root, root, 0755)
%doc %{_datadir}/gtk-doc/html/libgnomedb/
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/omf/libgnomedb/
%dir %{_includedir}/libgnomedb-*/
%{_includedir}/libgnomedb-*/libgnomedb/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.2.2-1.2
- Rebuild for Fedora Core 5.

* Fri Jul 22 2005 Dries Verachtert <dries@ulyssis.org> - 1.2.2-1
- Updated to release 1.2.2.

* Tue Apr 06 2004 Dag Wieers <dag@wieers.com> - 1.1.1-1
- Updated to release 1.1.1.

* Thu Jan 22 2004 Dag Wieers <dag@wieers.com> - 1.0.3-0
- Updated to release 1.0.3.

* Sun Nov 30 2003 Dag Wieers <dag@wieers.com> - 1.0.2-0
- Updated to release 1.0.2.

* Mon Oct 13 2003 Dag Wieers <dag@wieers.com> - 1.0.1-0
- Updated to release 1.0.1.

* Tue Sep 16 2003 Dag Wieers <dag@wieers.com> - 1.0.0-0
- Updated to release 1.0.0.

* Thu Sep 11 2003 Dag Wieers <dag@wieers.com> - 0.99.0-0
- Updated to release 0.99.0.

* Fri Jul 04 2003 Dag Wieers <dag@wieers.com> - 0.90.0-0
- Updated to release 0.90.0.

* Fri Jun 13 2003 Dag Wieers <dag@wieers.com> - 0.12.2-0
- Initial package. (using DAR)
