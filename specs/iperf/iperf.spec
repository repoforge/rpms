# $Id$
# Authority: dag
# Upstream: <iperf-users$dast,nlanr,net>

Summary: Tool for measuring TCP and UDP bandwidth performance
Name: iperf
Version: 1.7.0
Release: 1
License: GPL
Group:  Applications/Internet
URL: http://dast.nlanr.net/Projects/Iperf/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dast.nlanr.net/Projects/Iperf/iperf-%{version}-source.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++ libstdc++-devel

%description
Iperf is a tool to measure maximum TCP bandwidth, allowing the tuning
of various parameters and UDP characteristics. Iperf reports bandwidth,
delay jitter, datagram loss.

%prep
%setup 

%build
%{__make} %{?_smp_mflags}

%install
%makeinstall -C src \
	INSTALL_DIR="%{buildroot}%{_bindir}"

%files
%defattr(-, root, root 0755)
%doc README KNOWN_PROBLEMS doc/*
%{_bindir}/iperf

%changelog
* Fri Nov 19 2004 Dag Wieers <dag@wieers.com> - 1.7.0-1
- Initial package. (using DAR)
