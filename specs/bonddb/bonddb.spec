# $Id$
# Authority: dries
# Upstream: <dru$treshna,com>


Summary: Object oriented wrapper for PostgreSQL
Name: bonddb
Version: 2.2.3
Release: 1.2%{?dist}
License: GPL
Group: Development/Tools
URL: http://www.treshna.com/bonddb/

Source: http://www.treshna.com/downloads/bonddb-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Patch0: bonddb-fixmakefile.patch

BuildRequires: postgresql-devel, libtool
BuildRequires: glib2-devel, pkgconfig, bison, flex
%{?fc4:BuildRequires: compat-gcc-32}

%description
bonddb is an object orientated wrapper for PostgreSQL. It's a fast data
abstraction layer written in C for C/C++ applications, to allow easy
access to class objects. You can use existing PostgreSQL databases without
any modification or additional tables needed in the backend.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n %{name}
%patch0 -p1

%build
%{__libtoolize} --force --copy
%{__aclocal} #--force
%{__autoheader}
%{__automake} --add-missing -a --foreign
%{__autoconf}
%{?fc4:export CC=gcc32}
%{expand: %%define optflags -O2}
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
#%doc AUTHORS COPYING INSTALL README TODO docs ChangeLog
%{_libdir}/libbond_gather.so.*
%{_libdir}/libbondcommon.so.*
%{_libdir}/libbonddb.so.*
%{_libdir}/libbonddb_gda.so.*
%{_libdir}/libbonddb_mysql.so.*
%{_libdir}/libbonddb_pg.so.*
%{_libdir}/libbondsql.so.*

%files devel
%defattr(-, root, root, 0755)
%{_libdir}/pkgconfig/bond*.pc
%{_includedir}/bond/
%{_includedir}/config.h
%{_libdir}/libbond*.a
%{_libdir}/libbond*.so
%exclude %{_libdir}/libbond*.la

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 2.2.3-1.2
- Rebuild for Fedora Core 5.

* Sun Feb 12 2006 Dries Verachtert <dries@ulyssis.org> - 2.2.3-1
- Updated to release 2.2.3.

* Mon Jan 09 2006 Dries Verachtert <dries@ulyssis.org> - 2.2.2-1
- Updated to release 2.2.2.

* Wed Nov 02 2005 Dries Verachtert <dries@ulyssis.org> - 2.2.0-1
- Updated to release 2.2.0.

* Tue Sep 20 2005 Dries Verachtert <dries@ulyssis.org> - 2.0.2-1
- Initial package.
