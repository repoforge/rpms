# $Id$
# Authority: dag
# Upstream: Richard Hipp <drh$hwaci,com>

%{?dist: %{expand: %%define %dist 1}}

Summary: Library that implements an embeddable SQL database engine
Name: sqlite
Version: 2.8.15
Release: 1
License: LGPL
Group: Applications/Databases
URL: http://www.sqlite.org/
Source:	http://www.sqlite.org/sqlite-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, readline-devel
%{!?dist:BuildRequires: tcl-devel}
%{?fc2:BuildRequires: tcl-devel}
%{?fc1:BuildRequires: tcllib}
%{?rh9:BuildRequires: tcllib}
%{?rh8:BuildRequires: tcllib}
%{?rh7:BuildRequires: tcllib, tcl}
%{?el2:BuildRequires: tcllib}
%{?rh6:BuildRequires: tcllib}

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

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n %{name}
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
# Install the man page, it's not automatically (2.8.15)
%{__install} -D -m0644 sqlite.1 %{buildroot}%{_mandir}/man1/sqlite.1

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%{_bindir}/sqlite
%{_libdir}/*.so.*
%{_mandir}/man1/*

%files devel
%defattr(-, root, root, 0755)
%doc doc/*
%{_includedir}/*.h
%{_libdir}/*.a
%exclude %{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
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
