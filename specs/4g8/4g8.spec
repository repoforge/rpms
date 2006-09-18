# $Id$
# Authority: dag
# Upstream: Darren Bounds <dbounds$intrusense,com>

%{?dist: %{expand: %%define %dist 1}}

Summary: Packet redirection tool for interception on switched networks
Name: 4g8
Version: 1.0
Release: 1.2
License: GPL
Group: Applications/Internet
URL: http://forgate.sourceforge.net/

Source: http://forgate.sf.net/downloads/4g8-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Obsoletes: forgate
BuildRequires: libnet >= 1.1, libpcap

%description
Forgate was written as a proof of concept in one method of capturing
traffic flows from a 3rd party on a switched network. Forgate uses ARP cache
poisoning, packet capture and packet reconstruction to perform it's task. It
should work with nearly all TCP, ICMP and UDP IPv4 traffic.

%prep
%setup

%{?el4:%{__perl} -pi.orig -e 's|net/bpf.h|pcap-bpf.h|' src/*.c src/*.h}
%{?fc3:%{__perl} -pi.orig -e 's|net/bpf.h|pcap-bpf.h|' src/*.c src/*.h}
%{?fc2:%{__perl} -pi.orig -e 's|net/bpf.h|pcap-bpf.h|' src/*.c src/*.h}

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%files
%defattr(-, root, root, 0755)
%doc LICENSE
%{_sbindir}/*

%clean
%{__rm} -rf %{buildroot}

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.0-1.2
- Rebuild for Fedora Core 5.

* Thu Apr 15 2004 Dag Wieers <dag@wieers.com> - 1.0-1
- Updated to release 1.0.

* Mon Jan 26 2004 Dag Wieers <dag@wieers.com> - 0.9-0.b
- Initial package. (using DAR)
