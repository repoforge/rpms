# $Id$
# Authority: dag
# Upstream: Darren Bounds <dbounds$intrusense,com>

%{!?dtag:%define _with_libpcapdevel 1}
%{?el5:%define _with_libpcapdevel 1}
%{?fc6:%define _with_libpcapdevel 1}

%{?fc1:%define _without_pcapbpf_h 1}
%{?el3:%define _without_pcapbpf_h 1}
%{?rh9:%define _without_pcapbpf_h 1}
%{?rh7:%define _without_pcapbpf_h 1}
%{?el2:%define _without_pcapbpf_h 1}

Summary: Packet redirection tool for interception on switched networks
Name: 4g8
Version: 1.0
Release: 1.2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://forgate.sourceforge.net/

Source: http://forgate.sf.net/downloads/4g8-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Obsoletes: forgate
BuildRequires: libnet >= 1.1, libpcap
%{?_with_libpcapdevel:BuildRequires:libpcap-devel}

%description
Forgate was written as a proof of concept in one method of capturing
traffic flows from a 3rd party on a switched network. Forgate uses ARP cache
poisoning, packet capture and packet reconstruction to perform it's task. It
should work with nearly all TCP, ICMP and UDP IPv4 traffic.

%prep
%setup

%{!?_without_pcapbpf_h:%{__perl} -pi.orig -e 's|net/bpf.h|pcap-bpf.h|' src/*.c src/*.h}

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
#makeinstall
%{__make} install DESTDIR="%{buildroot}"

%files
%defattr(-, root, root, 0755)
%doc LICENSE
%{_sbindir}/4g8

%clean
%{__rm} -rf %{buildroot}

%changelog
* Thu Apr 15 2004 Dag Wieers <dag@wieers.com> - 1.0-1
- Updated to release 1.0.

* Mon Jan 26 2004 Dag Wieers <dag@wieers.com> - 0.9-0.b
- Initial package. (using DAR)
