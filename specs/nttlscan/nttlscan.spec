# $Id$
# Authority: dag
# Upstream: 

Summary: Quick network topology scanner
Name: nttlscan
Version: 0.1
Release: 1
License: GPL
Group: Applications/Internet
URL: http://www.honeyd.org/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.honeyd.org/data/nttlscan-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libpcap

%description
Nttlscan is a quick network topology scanner and functions as a highly
parallel traceroute. It randomly picks destination IP addresses and
sends TCP or UDP probes. Returing ICMP messages are interpreted to
reconstruct the route that packets take to their respective destination.
Nttlscan can be used to construct virtual routing topologies for Honeyd.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc %{_mandir}/man?/*
%{_bindir}/*

%changelog
* Sat Jul 10 2004 Dag Wieers <dag@wieers.com> - 01-1
- Initial package. (using DAR)
