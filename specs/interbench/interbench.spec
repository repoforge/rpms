# $Id$
# Authority: dag
# Upstream: Con Kolivas

Summary: Interactivity benchmark tool
Name: interbench
Version: 0.22
Release: 1
License: GPL
Group: System Environment/Base
URL: http://members.optusnet.com.au/ckolivas/interbench/

Source: http://ck.kolivas.org/apps/interbench/interbench-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
interbench is designed to measure the effect of changes in Linux kernel
design or system configuration changes such as cpu, I/O scheduler and
filesystem changes and options. With careful benchmarking, different
hardware can be compared.

%prep
%setup

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 interbench %{buildroot}%{_bindir}/interbench

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING readme* sample.log
%{_bindir}/interbench

%changelog
* Wed Jul 20 2005 Dag Wieers <dag@wieers.com> - 0.22-1
- Updated to release 0.22.

* Fri Jul 15 2005 Dag Wieers <dag@wieers.com> - 0.21-1
- Initial package. (using DAR)
