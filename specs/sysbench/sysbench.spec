# $Id$
# Authority: dag

%{?el4:%define _without_postgresql 1}
%{?el3:%define _without_mysql 1}
%{?el3:%define _without_postgresql 1}

Summary: System performance benchmark
Name: sysbench
Version: 0.4.10
Release: 1%{?dist}
License: GPLv2+
Group: Applications/System
URL: http://sysbench.sourceforge.net/

Source: http://dl.sf.net/sysbench/sysbench-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%{!?_without_mysql:BuildRequires: mysql-devel}
%{!?_without_postgresql:BuildRequires: postgresql-devel}

%description
SysBench is a modular, cross-platform and multi-threaded benchmark
tool for evaluating OS parameters that are important for a system
running a database under intensive load.

The idea of this benchmark suite is to quickly get an impression about
system performance without setting up complex database benchmarks or
even without installing a database at all. Current features allow to
test the following system parameters:
- file I/O performance
- scheduler performance
- memory allocation and transfer speed
- POSIX threads implementation performance
- database server performance (OLTP benchmark)

Primarily written for MySQL server benchmarking, SysBench will be
further extended to support multiple database backends, distributed
benchmarks and third-party plug-in modules.

%prep
%setup

%build
%configure \
%{!?_without_mysql:--with-mysql} \
%{?_without_mysql:--without-mysql} \
%{!?_without_postgresql:--with-pgsql}
%{__make}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING INSTALL README
%{_bindir}/sysbench
%exclude %{_docdir}/sysbench/

%changelog
* Wed Jun 09 2010 Dag Wieers <dag@wieers.com> - 0.4.10-1
- Initial package. (using DAR)
