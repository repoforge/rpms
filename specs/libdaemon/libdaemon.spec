# $Id$
# Authority: dag
# Upstream: Lennart Poettering <mzqnrzba$0pointer,de>

### EL6 ships with libdaemon-0.14-1.el6
# ExclusiveDist: el2 el3 el4 el5

#{?el4:%define _without_lynx 1}
#{?el3:%define _without_lynx 1}

Summary: Lightweight C library which eases the writing of UNIX daemons
Name: libdaemon
Version: 0.6
Release: 1.2%{?dist}
License: GPL
Group: System Environment/Base
URL: http://www.stud.uni-hamburg.de/users/lennart/projects/libdaemon/

Source: http://0pointer.de/lennart/projects/libdaemon/libdaemon-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%{!?_without_lynx:BuildRequires: lynx}
BuildRequires: gcc-c++, doxygen

%description
libdaemon is a leightweight C library which eases the writing of UNIX daemons.
It consists of the following parts:

	wrapper around fork() which does the correct daemonization
	procedure of a process,

	wrapper around syslog() for simpler and compatible log output to
	Syslog or STDERR,

	API for writing PID files

and	An API for serializing UNIX signals into a pipe for usage with
	select() or poll().

Routines like these are included in most of the daemon software available. It
is not that simple to get it done right and code duplication cannot be a goal.

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

%build
%configure \
%{?_without_lynx:--disable-lynx}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%{__install} -d -m0755 %{buildroot}%{_mandir}/man3/
%{__cp} -apv doc/reference/man/man3/* %{buildroot}%{_mandir}/man3/

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%doc doc/README doc/reference/html/
%doc %{_mandir}/man?/*
%{_libdir}/*.a
%{_libdir}/*.so
%{_includedir}/libdaemon/
%{_libdir}/pkgconfig/*.pc
%exclude %{_libdir}/*.la

%changelog
* Sun Apr 18 2004 Dag Wieers <dag@wieers.com> - 0.6-1
- Initial package. (using DAR)
