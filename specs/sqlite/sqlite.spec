# $Id$
# Authority: dag
# Upstream: Richard Hipp <drh$hwaci,com>

### Builds fine, but related python-sqlite needs python >= 2.3 and yum 2.4 needs sqlite2
# ExcludeDist: el2 rh7 rh9 el3 el4


%{?el3:%define _without_tcl 1}
%{?rh9:%define _without_tcl 1}
%{?rh9:%define _without_tcltk_devel 1}
%{?rh7:%define _without_tcl 1}
%{?rh7:%define _without_tcltk_devel 1}
%{?el2:%define _without_tcl 1}
%{?el2:%define _without_tcltk_devel 1}

Summary: Library that implements an embeddable SQL database engine
Name: sqlite
Version: 3.3.13
Release: 1%{?dist}
License: LGPL
Group: Applications/Databases
URL: http://www.sqlite.org/

Source:	http://www.sqlite.org/sqlite-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, libtool, readline-devel, ncurses-devel
%{!?_without_tcltk_devel:BuildRequires: tcl-devel >= 8.3}
%{?_without_tcltk_devel:BuildRequires: tcl >= 8.3}
Obsoletes: sqlite3 <= %{version}-%{release}

%description
SQLite is a C library that implements an SQL database engine. A large
subset of SQL92 is supported. A complete database is stored in a
single disk file. The API is designed for convenience and ease of use.
Applications that link against SQLite can enjoy the power and
flexiblity of an SQL database without the administrative hassles of
supporting a separate database server.

Because it omits the client-server interaction overhead and writes
directly to disk, SQLite is also faster than the big database servers
for most operations. In addition to the C library, the SQLite
distribution includes a command-line tool for interacting with SQLite
databases and SQLite bindings for Tcl/Tk.

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Obsoletes: sqlite3-devel <= %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%package tcl
Summary: Tcl module for the sqlite3 embeddable SQL database engine.
Group: Development/Languages
Requires: %{name} = %{version}-%{release}

%description tcl
This package contains the tcl modules for %{name}.

%prep
%setup

### FIXME: Make Makefile use autotool directory standard. (Please fix upstream)
%{__perl} -pi.orig -e '
		s|\$\(exec_prefix\)/lib|\$(libdir)|g;
		s|/usr/lib|\$(libdir)|g;
	' Makefile.in */Makefile.in */*/Makefile.in

%build
export CFLAGS="%{optflags} -DNDEBUG=1 -fno-strict-aliasing"
export CXXFLAGS="%{optflags} -DNDEBUG=1 -fno-strict-aliasing" \
%configure \
	--enable-utf8 \
%{?_without_tcl:--disable-tcl}
%{__make} %{?_smp_mflags}
%{__make} doc

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

# Install the man page, it's not automatically (2.8.16)
%{__install} -Dp -m0644 sqlite3.1 %{buildroot}%{_mandir}/man1/sqlite3.1

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%doc %{_mandir}/man1/sqlite3.1*
%{_bindir}/sqlite3
%{_libdir}/libsqlite3.so.*

%files devel
%defattr(-, root, root, 0755)
%doc doc/*
%{_includedir}/sqlite3.h
%{_includedir}/sqlite3ext.h
%{_libdir}/libsqlite3.a
%exclude %{_libdir}/libsqlite3.la
%{_libdir}/libsqlite3.so
%{_libdir}/pkgconfig/sqlite3.pc

%if {!?_without_tcl:1}0
%files tcl
%defattr(-, root, root, 0755)
%{_datadir}/tcl*/sqlite3/
%endif

%changelog
* Wed Feb 14 2007 Dag Wieers <dag@wieers.com> - 3.3.13-1
- Updated to release 3.3.13.

* Tue Feb 15 2005 Dag Wieers <dag@wieers.com> - 2.8.15-1
- Updated to release 2.8.16.

* Thu Aug 26 2004 Matthias Saou <http://freshrpms.net/> 2.8.15-1
- Update to 2.8.15.
- Minor cleanups, removed now unneeded workarounds.

* Sat Jun 19 2004 Dag Wieers <dag@wieers.com> - 2.8.14-1
- Updated to release 2.8.14.

* Thu Jun 03 2004 Dag Wieers <dag@wieers.com> - 2.8.13-2
- Added UTF8 support. (Vladimir Vukicevic)

* Sun May 30 2004 Dag Wieers <dag@wieers.com> - 2.8.13-1
- Fixes for building on x86_64 arch.

* Thu May 27 2004 Matthias Saou <http://freshrpms.net/> 2.8.13-0
- Updated to release 2.8.13.
- Added tcl-devel build dependency for Fedora Core 2.

* Sun Feb 29 2004 Dag Wieers <dag@wieers.com> - 2.8.12-0
- Updated to release 2.8.12.

* Thu Jan 08 2004 Dag Wieers <dag@wieers.com> - 2.8.9-0
- Updated to release 2.8.9.

* Thu Dec 18 2003 Dag Wieers <dag@wieers.com> - 2.8.8-0
- Updated to release 2.8.8.

* Mon Jun 30 2003 Dag Wieers <dag@wieers.com> - 2.8.4-0
- Updated to release 2.8.4.

* Fri Jun 13 2003 Dag Wieers <dag@wieers.com> - 2.8.3-0
- Initial package. (using DAR)
