# $Id$
# Authority: dag
# Upstream: Richard Hipp <drh$hwaci,com>

%{?dtag: %{expand: %%define %dtag 1}}

%{?rh9:%define _without_tcltk_devel 1}
%{?rh8:%define _without_tcltk_devel 1}
%{?rh7:%define _without_tcltk_devel 1}
%{?el2:%define _without_tcltk_devel 1}

Summary: Library that implements an embeddable SQL database engine
Name: sqlite
Version: 2.8.17
Release: 1%{?dist}
License: LGPL
Group: Applications/Databases
URL: http://www.sqlite.org/
Source:	http://www.sqlite.org/sqlite-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, readline-devel
%{!?_without_tcltk_devel:BuildRequires: tcl-devel >= 8.3}
%{?_without_tcltk_devel:BuildRequires: tcl >= 8.3}
Obsoletes: sqlite2 <= %{version}-%{release}
Provides: sqlite2 = %{version}-%{release}

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
Obsoletes: sqlite2-devel <= %{version}-%{release}
Provides: sqlite2-devel = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

### FIXME: Make Makefile use autotool directory standard. (Please fix upstream)
%{__perl} -pi.orig -e 's|\$\(exec_prefix\)/lib|\$(libdir)|g' Makefile.in

%build
CFLAGS="%{optflags} -DNDEBUG=1" \
CXXFLAGS="%{optflags} -DNDEBUG=1" \
%configure \
    --enable-utf8
%{__make} %{?_smp_mflags}
%{__make} doc

%install
%{__rm} -rf %{buildroot}

%makeinstall
# Install the man page, it's not automatically (2.8.16)
%{__install} -Dp -m0644 sqlite.1 %{buildroot}%{_mandir}/man1/sqlite.1

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%{_bindir}/sqlite
%{_libdir}/libsqlite.so.*
%{_mandir}/man1/sqlite.1*

%files devel
%defattr(-, root, root, 0755)
%doc doc/*
%{_includedir}/sqlite.h
%{_libdir}/libsqlite.a
%exclude %{_libdir}/libsqlite.la
%{_libdir}/libsqlite.so
%{_libdir}/pkgconfig/sqlite.pc

%changelog
* Wed Feb 14 2007 Dag Wieers <dag@wieers.com> - 2.8.17-1
- Updated to release 2.8.17.

* Tue Feb 15 2005 Dag Wieers <dag@wieers.com> - 2.8.16-1
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
