# $Id$

# Authority: dag
# Upstream: 

Summary: Measures bandwidth between two point-to-point connections.
Name: bing
Version: 1.0.4
Release: 1
License: GPL
Group: Applications/Internet

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: ftp://ftp.ibp.fr/pub/networking/bing-%{version}.tar.gz
Patch0: bing.diff
Patch1: bing.rh6.patch
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

%description
bing computes point-to-point throughput using two sizes of ICMP ECHO_REQUEST
packets to a pair of remote hosts.

%prep
%setup
%patch0 -p1
%patch1 -p1

%build
%{__make} %{?_smp_mflags}

%install
%makeinstall

%files
%defattr(-, root, root, 0755)
%doc bing.ps
%doc %{_mandir}/man?/*
%{_bindir}/*

%changelog
* Tue Mar 16 2004 Dag Wieers <dag@wieers.com> - 1.0.4-1
- Initial package. (using DAR)
