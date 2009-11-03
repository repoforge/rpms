# $Id$
# Authority: dag
# Upstream: Darren Bounds <dbounds$intrusense,com>

%{?dtag: %{expand: %%define %dtag 1}}

%{!?dtag:%define _with_libpcapdevel 1}
%{?el5:%define _with_libpcapdevel 1}
%{?fc6:%define _with_libpcapdevel 1}

%{?fc1:%define _without_pcapbpf_h 1}
%{?el3:%define _without_pcapbpf_h 1}
%{?rh9:%define _without_pcapbpf_h 1}
%{?rh7:%define _without_pcapbpf_h 1}
%{?el2:%define _without_pcapbpf_h 1}

Summary: Network injection and capturing tool
Name: packit
Version: 1.0
Release: 1.2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://packit.sourceforge.net/

Source: http://packit.sf.net/downloads/packit-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libnet >= 1.1, libpcap
%{?_with_libpcapdevel:BuildRequires:libpcap-devel}

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

%{!?_without_pcapbpf_h:%{__perl} -pi.orig -e 's|net/bpf.h|pcap-bpf.h|' src/*.c src/*.h}

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog LICENSE VERSION docs/ICMP.txt
%doc %{_mandir}/man8/packit.8*
%{_sbindir}/packit

%changelog
* Thu Apr 15 2004 Dag Wieers <dag@wieers.com> - 1.0-1
- Updated to release 1.0.

* Sat Apr 10 2004 Dag Wieers <dag@wieers.com> - 0.7.1-1
- Initial package. (using DAR)
