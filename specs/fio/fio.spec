# $Id$
# Authority: dag
# Upstream: Jens Axboe

Summary: I/O benchmark and stress/hardware verification tool
Name: fio
Version: 1.20
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
%setup -n %{name}

#%{__perl} -pi -e 's| \$\(libdir\)| \$(DESTDIR)\$(libdir)|' Makefile

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
#%{__make} install DESTDIR="%{buildroot}" prefix="%{_prefix}" bindir="%{_bindir}" libdir="%{_libdir}/fio"
%{__make} install DESTDIR="%{buildroot}" prefix="%{_prefix}" bindir="%{_bindir}" mandir="%{_mandir}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING README examples/
%doc %{_mandir}/man1/fio.1*
%{_bindir}/fio
%{_bindir}/fio_generate_plots
#%{_libdir}/fio/

%changelog
* Fri May 02 2008 Dag Wieers <dag@wieers.com> - 1.20-1
- Updated to release 1.20.

* Sun Feb 24 2008 Dries Verachtert <dries@ulyssis.org> - 1.19-1
- Updated to release 1.19.

* Tue Feb 19 2008 Dag Wieers <dag@wieers.com> - 1.18.1-1
- Updated to release 1.18.1.

* Tue Feb  5 2008 Dries Verachtert <dries@ulyssis.org> - 1.18-1
- Updated to release 1.18.

* Thu Jan 31 2008 Dries Verachtert <dries@ulyssis.org> - 1.17.3-1
- Updated to release 1.17.3.

* Tue Oct 30 2007 Dag Wieers <dag@wieers.com> - 1.17.2-1
- Updated to release 1.17.2.

* Thu Aug 16 2007 Dag Wieers <dag@wieers.com> - 1.17-1
- Updated to release 1.17.

* Tue Jun 19 2007 Dag Wieers <dag@wieers.com> - 1.16.5-1
- Updated to release 1.16.5.

* Wed Apr 25 2007 Dag Wieers <dag@wieers.com> - 1.16-1
- Updated to release 1.16.

* Wed Mar 28 2007 Dag Wieers <dag@wieers.com> - 1.15-1
- Updated to release 1.15.

* Sun Mar 18 2007 Dag Wieers <dag@wieers.com> - 1.14-1
- Updated to release 1.14.

* Sun Mar 04 2007 Dag Wieers <dag@wieers.com> - 1.13-1
- Updated to release 1.13.

* Thu Mar 01 2007 Dag Wieers <dag@wieers.com> - 1.12-1
- Updated to release 1.12.

* Sat Dec 23 2006 Dries Verachtert <dries@ulyssis.org> - 1.10-1
- Updated to release 1.10.

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
