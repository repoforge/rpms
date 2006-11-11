# $Id$
# Authority: dag
# Upstream: Jens Axboe

Summary: I/O benchmark and stress/hardware verification tool
Name: fio
Version: 1.9
Release: 1
License: GPL
Group: Applications/System
URL: http://freshmeat.net/projects/fio/

Source: http://brick.kernel.dk/snaps/fio-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libaio-devel

%description
fio is an I/O tool meant to be used both for benchmark and stress/hardware
verification. It has support for 6 different types of I/O engines (sync,
mmap, libaio, posixaio, SG v3, splice), I/O priorities (for newer Linux
kernels), rate I/O, forked or threaded jobs, and much more.

It can work on block devices as well as files. fio accepts job descriptions
in a simple-to-understand text format. Several example job files are included.
fio displays all sorts of I/O performance information, such as completion and
submission latencies (avg/mean/deviation), bandwidth stats, CPU, and disk
utilization, and more. It supports Linux, FreeBSD, and OpenSolaris.

%prep
%setup

%{__perl} -pi -e 's| \$\(libdir\)| \$(DESTDIR)\$(libdir)|' Makefile

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}" prefix="%{_prefix}" bindir="%{_bindir}" libdir="%{_libdir}/fio"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING README examples/
%{_bindir}/fio
%{_bindir}/fio_generate_plots
%{_libdir}/fio/

%changelog
* Tue Nov 07 2006 Dag Wieers <dag@wieers.com> - 1.9-1
- Updated to release 1.9.

* Tue Nov 07 2006 Dag Wieers <dag@wieers.com> - 1.8-1
- Updated to release 1.8.

* Mon Oct 23 2006 Dag Wieers <dag@wieers.com> - 1.7-1
- Updated to release 1.7.

* Wed Aug 30 2006 Dag Wieers <dag@wieers.com> - 1.6-1
- Updated to release 1.6.

* Wed Jun 14 2006 Dag Wieers <dag@wieers.com> - 1.5-1
- Initial package. (using DAR)
