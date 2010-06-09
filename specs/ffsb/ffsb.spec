# $Id$
# Authority: dag

Summary: The Flexible Filesystem Benchmark
Name: ffsb
Version: 5.2.1
Release: 1%{?dist}
License: GPLv2+
Group: Applications/System
URL: http://sourceforge.net/projects/ffsb/

Source: http://dl.sf.net/ffsb/ffsb-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
The Flexible Filesystem Benchmark (FFSB) is a cross-platform filesystem
performance measurement tool. It uses customizable profiles to measure
of different workloads, and it supports multiple groups of threads
across multiple filesystems.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

### Remove leftover file in tarball
%{__rm} -v examples/profile_smallfile_reads~

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING README USAGE examples/
%{_bindir}/ffsb

%changelog
* Wed Jun 09 2010 Dag Wieers <dag@wieers.com> - 5.2.1-1
- Initial package. (using DAR)
