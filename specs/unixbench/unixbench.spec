# $Id$
# Authority: dag

Summary: BYTE's UNIX Benchmarks
Name: unixbench
Version: 4.0.1
Release: 1
License: Distributable
Group: Applications/System
URL: http://www.tux.org/pub/tux/niemi/unixbench/

Source: http://www.tux.org/pub/tux/niemi/unixbench/unixbench-%{version}.tgz
Patch0: unixbench-4.0.1-altpackage.patch
Patch1: unixbench-4.0.1-buildflags.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Requires: gcc

%description
The BYTE Unix benchmarks that we published in March, 1990, we
expected that they fill our needs for several years. It was only a
few months before we started to see that UNIX workstation performance
was going to make the benchmark design questionable.

The design flaw was that the benchmarks timed a fixed number of loops;
if there were too few loops, the times were too small to be reliable.
Perhaps we could have increased the number of loops and been safe for
another few years (months?). But with IBM's introduction of the RS/6000,
it became obvious that we needed to redesign our benchmarks.

%prep
%setup
%patch0 -p1
%patch1 -p1

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 Run %{buildroot}%{_bindir}/unixbench

%{__install} -d -m0755 %{buildroot}%{_libdir}/unixbench/
%{__cp} -av pgms/ testdir/ %{buildroot}%{_libdir}/unixbench/

%clean
%{__rm} -rf %{buildroot}

%files
%doc README old-doc/bench.doc old-doc/bench3.doc
%{_bindir}/unixbench
%{_libdir}/unixbench/

%changelog
* Fri Feb 16 2007 Dag Wieers <dag@wieers.com> - 4.0.1-1
- Initial package. (using DAR)
