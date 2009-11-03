# $Id$
# Authority: dag
# Upstream: Jorge Ferrer <jferrer$ieeesb,etsit,upm,es>


%{?fc4:%define _without_mdbtools 1}
%{?rh7:%define _without_mdbtools 1}
%{?el2:%define _without_mdbtools 1}
%{?rh6:%define _without_mdbtools 1}

Summary: Library for writing gnome database programs
Name: libgda
Version: 1.2.3
Release: 1.2%{?dist}
License: LGPL
Group: System Environment/Libraries
URL: http://www.gnome-db.org/

Source: http://ftp.gnome.org/pub/GNOME/sources/libgda/1.2/libgda-%{version}.tar.bz2
#Source: ftp://ftp.gnome-db.org/pub/gnome-db/sources/v%{version}/libgda-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: pkgconfig >= 0.8, glib2-devel >= 2.0, ncurses-devel
BuildRequires: libxml2-devel, libxslt-devel >= 1.0.9
BuildRequires: mysql-devel, postgresql-devel, unixODBC-devel, sqlite-devel
BuildRequires: freetds-devel, xbase-devel, readline-devel
BuildRequires: intltool, perl(XML::Parser)
%{!?_without_mdbtools:BuildRequires: mdbtools-devel}
BuildRequires: scrollkeeper

Requires(post): scrollkeeper

%description
libgda is a library that eases the task of writing
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
%{__install} -d -m0755 %{buildroot}%{_datadir}
%makeinstall
%find_lang %{name}-2

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/libgda/providers/*.{a,la}

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
%doc AUTHORS ChangeLog COPYING NEWS README
%doc %{_mandir}/man?/*
%config %{_sysconfdir}/libgda/
%{_bindir}/*
%{_datadir}/libgda/
%{_libdir}/*.so.*
%{_libdir}/libgda/

%files devel
%defattr(-, root, root, 0755)
%doc %{_datadir}/gtk-doc/html/libgda/
%{?!rh7:%{_datadir}/omf/libgda/}
%{_includedir}/libgda/
%{_includedir}/libgda-report/
%{_libdir}/*.a
%exclude %{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.2.3-1.2
- Rebuild for Fedora Core 5.

* Fri Nov 11 2005 Dries Verachtert <dries@ulyssis.org> - 1.2.3-1
- Updated to release 1.2.3.

* Thu Nov 10 2005 Dries Verachtert <dries@ulyssis.org> - 1.2.2-1
- Updated to release 1.2.2.

* Wed Aug 18 2004 Dag Wieers <dag@wieers.com> - 1.1.6-1
- Updated to release 1.1.6.

* Fri Jun 11 2004 Dag Wieers <dag@wieers.com> - 1.1.4-1
- Updated to release 1.1.4.

* Thu Jun 03 2004 Dag Wieers <dag@wieers.com> - 1.1.3-1
- Updated to release 1.1.3.

* Mon May 17 2004 Dag Wieers <dag@wieers.com> - 1.1.2-1
- Updated to release 1.1.2.

* Mon Apr 05 2004 Dag Wieers <dag@wieers.com> - 1.1.1-1
- Updated to release 1.1.1.

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
