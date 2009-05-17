# $Id$
# Authority: dag
# Upstream: Con Kolivas

Summary: Interactivity benchmark tool
Name: interbench
Version: 0.30
Release: 1.2
License: GPL
Group: System Environment/Base
URL: http://users.on.net/~ckolivas/interbench/

Source: http://www.kernel.org/pub/linux/kernel/people/ck/apps/interbench/interbench-%{version}.tar.bz2
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
%{__install} -Dp -m0644 interbench.8 %{buildroot}%{_mandir}/man8/interbench.8

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING readme*
%doc %{_mandir}/man8/interbench.8*
%{_bindir}/interbench

%changelog
* Fri Aug 12 2005 Dag Wieers <dag@wieers.com> - 0.30-1
- Updated to release 0.30.

* Fri Aug 12 2005 Dag Wieers <dag@wieers.com> - 0.29-1
- Updated to release 0.29.

* Sat Aug 06 2005 Dag Wieers <dag@wieers.com> - 0.28-1
- Updated to release 0.28.

* Thu Aug 04 2005 Dag Wieers <dag@wieers.com> - 0.27-1
- Updated to release 0.27.

* Fri Jul 29 2005 Dag Wieers <dag@wieers.com> - 0.24-1
- Updated to release 0.24

* Wed Jul 27 2005 Dag Wieers <dag@wieers.com> - 0.23-1
- Updated to release 0.23.

* Wed Jul 20 2005 Dag Wieers <dag@wieers.com> - 0.22-1
- Updated to release 0.22.

* Fri Jul 15 2005 Dag Wieers <dag@wieers.com> - 0.21-1
- Initial package. (using DAR)
