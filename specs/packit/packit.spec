# $Id$
# Authority: dag
# Upstream: Darren Bounds <dbounds@intrusense.com>

%{?dist: %{expand: %%define %dist 1}}

Summary: Network injection and capturing tool
Name: packit
Version: 1.0
Release: 1
License: GPL
Group: Applications/Internet
URL: http://packit.sf.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://packit.sf.net/downloads/packit-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libnet >= 1.1

%description
Packit is a network auditing tool. It's value is derived from its
ability to customize, inject, monitor, and manipulate IP traffic.  By
allowing you to define (spoof) all TCP, UDP, ICMP, IP, ARP, RARP and
Ethernet header options, Packit can be useful in testing firewalls,
intrusion detection systems, port scanning, simulating network traffic
and general TCP/IP auditing.  Packit is also an excellent tool for
learning TCP/IP.

%prep
%setup

%{?fc2:%{__perl} -pi.orig -e 's|net/bpf.h|pcap-bpf.h|' src/*.c src/*.h}

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
%doc ChangeLog LICENSE VERSION docs/ICMP.txt
%doc %{_mandir}/man?/*
%{_sbindir}/*

%changelog
* Thu Apr 15 2004 Dag Wieers <dag@wieers.com> - 1.0-1
- Updated to release 1.0.

* Sat Apr 10 2004 Dag Wieers <dag@wieers.com> - 0.7.1-1
- Initial package. (using DAR)
