# $Id$

# Authority: dag
# Upstream: Jorge Ferrer <jferrer@ieeesb.etsit.upm.es>

### FIXME: Makefiles don't allow -jX (parallel compilation)
# Distcc: 0

Summary: Library for writing gnome database programs.
Name: libgda
Version: 1.0.3
Release: 0
License: LGPL
Group: System Environment/Libraries
URL: http://www.gnome-db.org/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://ftp.gnome.org/pub/GNOME/sources/libgda/%{version}/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: pkgconfig >= 0.8, glib2-devel >= 2.0, ncurses-devel
BuildRequires: libxml2-devel, libxslt-devel >= 1.0.9
BuildRequires: mysql-devel, postgresql-devel, unixODBC-devel, sqlite-devel
BuildRequires: freetds-devel, xbase-devel
%{?rhfc1:BuildRequires: mdbtools-devel}
%{?rhel3:BuildRequires: mdbtools-devel}
%{?rh90:BuildRequires: mdbtools-devel}
%{?rh80:BuildRequires: mdbtools-devel}
BuildRequires: scrollkeeper

Requires(post): scrollkeeper

%description
libgda is a library that eases the task of writing
gnome database programs.

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

### FIXME: Xbase support is called 'xbase' not 'xdb' (Please fix upstream)
%{__perl} -pi.orig -e 's|xdb|xbase|g' configure
%{__perl} -pi.orig -e 's|xdb/|xbase/|g' providers/xbase/gda-xbase-database.cpp

%build
%configure \
	--with-freetds \
	--with-ldap \
	--with-mdb \
	--with-mysql \
	--with-odbc \
	--with-postgres \
	--with-sqlite \
	--with-tds
#	--disable-gtk-doc
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}-2

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/*.la \
		%{buildroot}%{_libdir}/libgda/providers/*.a \
		%{buildroot}%{_libdir}/libgda/providers/*.la

%post
/sbin/ldconfig 2>/dev/null

%post devel
scrollkeeper-update -q || :

%postun
/sbin/ldconfig 2>/dev/null

%postun devel
scrollkeeper-update -q || :

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}-2.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING README NEWS
%doc %{_mandir}/man?/*
%config %{_sysconfdir}/libgda/
%{_bindir}/*
%{_datadir}/libgda/
%{_libdir}/*.so.*
%{_libdir}/libgda/

%files devel
%defattr(-,root,root)
%doc %{_datadir}/gtk-doc/html/libgda/
%{?!rh73:%{_datadir}/omf/libgda/}
%{_includedir}/libgda/
%{_includedir}/libgda-report/
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
* Thu Jan 22 2004 Dag Wieers <dag@wieers.com> - 1.0.3-0
- Updated to release 1.0.3.

* Sun Nov 30 2003 Dag Wieers <dag@wieers.com> - 1.0.2-0
- Updated to release 1.0.2.

* Mon Oct 13 2003 Dag Wieers <dag@wieers.com> - 1.0.1-0
- Updated to release 1.0.1.

* Tue Sep 16 2003 Dag Wieers <dag@wieers.com> - 1.0.0-0
- Updated to release 1.0.0.

* Fri Sep 12 2003 Dag Wieers <dag@wieers.com> - 0.99.0-1
- Added xbase support.

* Thu Sep 11 2003 Dag Wieers <dag@wieers.com> - 0.99.0-0
- Updated to release 0.99.0.

* Fri Jul 04 2003 Dag Wieers <dag@wieers.com> - 0.90.0-0
- Updated to release 0.90.0.

* Fri Jun 13 2003 Dag Wieers <dag@wieers.com> - 0.12.1-0
- Initial package. (using DAR)
