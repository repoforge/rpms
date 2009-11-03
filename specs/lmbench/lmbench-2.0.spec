# $Id$
# Authority: dag

Summary: Suite of simple, portable benchmarks
Name: lmbench
Version: 2.0.4
Release: 0.1%{?dist}
License: GPL
Group: Applications/System
URL: http://www.bitmover.com/lmbench/

Source: http://dl.sf.net/lmbench/lmbench-%{version}.tgz
Source1: lmbench-2.0.4-config.guess
Patch0: lmbench-2.0.4-no-timeout.patch
Patch1: lmbench-2.0.4-lat_mem_rd-64-bit.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Bandwidth benchmarks: cached file read, memory copy (bcopy), memory read,
memory write, pipe, TCP; Latency benchmarks: context switching, connection
establishment, pipe, TCP, UDP, RPC hot potato, file system creates and
deletes, process creation, signal handling, system call overhead,  memory
read latency; Miscellanious Processor clock rate calculation.

%prep
%setup

%{__install} -Dp -m0755 %{SOURCE1} scripts/gnu-os

### Suppress patch's attempts to get SCCS files
export PATCH_GET="0"
%patch0 -p1
%patch1 -p1

%{__mv} -f src/TODO TODO.lmbench
%{__mv} -f scripts/SHIT SHIT.scripts
%{__mv} -f scripts/TODO TODO.scripts

%build
cd src
CFLAGS="-O -DNO_SERVER_TIMEOUT" ../scripts/build all
cd -

### Remove revision control info
#find . -name "SCCS" -type d -exec %{__rm} -rf {} \;
find . -name 'SCCS' -type d | xargs %{__rm} -rf

%install
%{__rm} -rf %{buildroot}

%{__install} -d -m0755 %{buildroot}%{_prefix}/lib/lmbench/{,results/}
%{__cp} -avx bin/ scripts/ %{buildroot}%{_prefix}/lib/lmbench/

### Clean up a bit
find %{buildroot}%{_prefix}/lib/lmbench/ -name 'Makefile*' -or -name '*.[ao]' -exec %{__rm} -f {} \;

### This gets put in docs later
%{__rm} -f %{buildroot}%{_prefix}/lib/lmbench/scripts/TODO

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING COPYING-2 hbench-REBUTTAL README SHIT.* TODO.* doc/
%{_prefix}/lib/lmbench/

%changelog
* Fri Nov 17 2006 Dag Wieers <dag@wieers.com> - 2.0.4-0.1
- Initial package. (based on RHEL4 version)
- Thanks to Tuomo Soini for investigating and contributing fixes and patches..

* Fri Jan 6 2006 - Will Woods <wwoods@redhat.com>
- lmbench-2.0.4-lat_mem_rd-64-bit.patch: fix a crash when using a memory size
  of 2048MB or larger on x86_64 and ppc64
- Add updated version of config.guess to correctly guess the canonical system
  name on newer systems (e.g. ppc64)

* Mon Sep 26 2005 - Will Woods <wwoods@redhat.com>
- lmbench2-no-timeout.patch: Allows the 1hr idle timeout for server programs
  to be turned off at compile time.

* Fri Aug 5 2005 - Will Woods <wwoods@redhat.com>
- Initial revision
