# $Id$
# Authority: dag

Summary: Suite of simple, portable benchmarks
Name: lmbench
Version: 3.0
Release: 0.a7.1%{?dist}
License: GPL
Group: Applications/System
URL: http://www.bitmover.com/lmbench/

Source: http://dl.sf.net/lmbench/lmbench-%{version}-a7.tgz
Source1: %{name}-3.0-a7-run.sh
Patch0: %{name}-3.0-a7-clean_script_warnings.patch
Patch1: %{name}-3.0-a7-man_pages.patch
Patch2: %{name}-3.0-a7-bw_tcp.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Requires: perl, make

%description
Bandwidth benchmarks: cached file read, memory copy (bcopy), memory read,
memory write, pipe, TCP; Latency benchmarks: context switching, connection
establishment, pipe, TCP, UDP, RPC hot potato, file system creates and
deletes, process creation, signal handling, system call overhead,  memory
read latency; Miscellanious Processor clock rate calculation.

%prep
%setup -n %{name}-%{version}-a7

export PATCH_GET="0"
%patch0 -p1
%patch1 -p1
%patch2 -p1

%{__mv} -f src/TODO TODO.lmbench
%{__mv} -f scripts/README README.scripts
%{__mv} -f scripts/SHIT SHIT.scripts
%{__mv} -f scripts/TODO TODO.scripts

%build
%{__make} %{?_smp_mflags}
find . -name 'SCCS' -type d -exec %{__rm} -rf {} \;

%install
%{__rm} -rf %{buildroot}

%{__install} -Dp -m0755 %{SOURCE1} %{buildroot}%{_bindir}/lmbench
%{__install} -Dp -m0644 results/Makefile %{buildroot}%{_prefix}/lib/lmbench/results/Makefile
%{__install} -Dp -m0644 src/webpage-lm.tar %{buildroot}%{_prefix}/lib/lmbench/src/webpage-lm.tar

%{__cp} -avx bin/ scripts/ %{buildroot}%{_prefix}/lib/lmbench/
find %{buildroot}%{_prefix}/lib/lmbench/ -name 'Makefile*' -or -name '*.[ao]' -exec %{__rm} -f {} \;

%{__chmod} a-x %{buildroot}%{_prefix}/lib/lmbench/scripts/info-template

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ACKNOWLEDGEMENTS CHANGES COPYING COPYING-2 hbench-REBUTTAL README.* TODO.* doc/
%{_bindir}/lmbench
%{_prefix}/lib/lmbench/

%changelog
* Fri Nov 17 2006 Dag Wieers <dag@wieers.com> - 3.0-0.a7.1
- Updated to release 3.0-a7.
- Thanks to Tuomo Soini for investigating.

* Tue Oct 10 2006 Dag Wieers <dag@wieers.com> - 3.0-0.a5.3
- Fixed group name.

* Tue Sep 13 2005 Dag Wieers <dag@wieers.com> - 3.0-0.a5
Initial package. (using DAR)
