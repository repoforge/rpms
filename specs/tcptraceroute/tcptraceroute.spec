# $Id$
# Authority: dag
# Upstream: Michael C. Toren <mct@toren.net>
# Upstream: <tcptraceroute-dev@netisland.net>

Summary: traceroute implementation using TCP packets
Name: tcptraceroute
Version: 1.4
Release: 3
License: GPL
Group: Applications/Internet
URL: http://michael.toren.net/code/tcptraceroute/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://michael.toren.net/code/tcptraceroute/tcptraceroute-%{version}.tar.gz
Patch: tcptraceroute-1.4-gcc33.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libnet <= 1.0.2, libpcap

%description
tcptraceroute is a traceroute implementation using TCP packets.

The more traditional traceroute(8) sends out either UDP or ICMP ECHO
packets with a TTL of one, and increments the TTL until the destination
has been reached. By printing the gateways that generate ICMP time
exceeded messages along the way, it is able to determine the path
packets are taking to reach the destination.

The problem is that with the widespread use of firewalls on the modern
Internet, many of the packets that traceroute(8) sends out end up being
filtered, making it impossible to completely trace the path to the
destination. However, in many cases, these firewalls will permit inbound
TCP packets to specific ports that hosts sitting behind the firewall are
listening for connections on. By sending out TCP SYN packets instead of
UDP or ICMP ECHO packets, tcptraceroute is able to bypass the most common
firewall filters.

%prep
%setup 
%patch0 -b .gcc3

%build
%{__make} %{?rh80:CC="gcc296"} \
	CFLAGS="%{optflags} -I%{_includedir}/pcap"

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir} \
			%{buildroot}%{_mandir}/man8
%{__install} -m 644 tcptraceroute.8 %{buildroot}%{_mandir}/man8
%makeinstall \
	DESTDIR="%{buildroot}%{_bindir}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc changelog COPYING examples.txt tcptraceroute.8.html
%doc %{_mandir}/man?/*
%{_bindir}/*

%changelog
* Fri Nov 21 2003 Dag Wieers <dag@wieers.com> - 1.4-3
- Patch to build with gcc-3.3.

* Thu May 01 2003 Dag Wieers <dag@wieers.com> - 1.4-2
- Removed libnet requirement. (Build staticly)

* Mon Dec 16 2002 Dag Wieers <dag@wieers.com> - 1.4-0
- Updated to 1.4.

* Thu Aug 02 2001 Dag Wieers <dag@wieers.com> - 1.2
- Initial package.
