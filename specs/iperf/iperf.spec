# $Id$
# Authority: dag
# Upstream: <iperf-users$dast,nlanr,net>

Summary: Tool for measuring TCP and UDP bandwidth performance
Name: iperf
Version: 2.0.1
Release: 1
License: GPL
Group:  Applications/Internet
URL: http://dast.nlanr.net/Projects/Iperf/

Source: http://dast.nlanr.net/Projects/Iperf/iperf-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++ libstdc++-devel

%description
Iperf is a tool to measure maximum TCP bandwidth, allowing the tuning
of various parameters and UDP characteristics. Iperf reports bandwidth,
delay jitter, datagram loss.

%prep
%setup 

%build
%configure
%{__make} %{?_smp_mflags}

%install
%makeinstall -C src \
	INSTALL_DIR="%{buildroot}%{_bindir}"

%files
%defattr(-, root, root 0755)
%doc README doc/*.html doc/*.gif
%{_bindir}/iperf

%changelog
* Fri Nov 19 2004 Dag Wieers <dag@wieers.com> - 2.1.0-1
- Updated to release 2.1.0.

* Fri Nov 19 2004 Dag Wieers <dag@wieers.com> - 1.7.0-1
- Initial package. (using DAR)
