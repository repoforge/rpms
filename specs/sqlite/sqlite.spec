# $Id$
# Authority: dag
# Upstream: Richard Hipp <drh@hwaci.com>

%{?dist: %{expand %%define %dist 1}}

Summary: library that implements an embeddable SQL database engine
Name: sqlite
Version: 2.8.12
Release: 0
License: LGPL
Group: Applications/Databases
URL: http://www.sqlite.org/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source:	http://www.sqlite.org/sqlite-%{version}.tar.gz
Patch0: sqlite-2.8.12-encode.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: readline-devel
%{?fc1:BuildRequires: tcllib}
%{?rh9:BuildRequires: tcllib}
%{?rh8:BuildRequires: tcllib}
%{?rh7:BuildRequires: tcllib}
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
%patch0 -b .encode

%build
CFLAGS="%{optflags} -DNDEBUG=1" \
CXXFLAGS="%{optflags} -DNDEBUG=1" \
%configure
%{__make} %{?_smp_mflags}
%{__make} doc

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir} \
			%{buildroot}%{_libdir} \
			%{buildroot}%{_includedir} \
			%{buildroot}%{_mandir}/man1/
%makeinstall
%{__install} -m0644 sqlite.1 %{buildroot}%{_mandir}/man1/

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/*.la

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%doc doc/
%{_includedir}/*.h
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
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
