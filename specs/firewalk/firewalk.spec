# $Id$
# Authority: dag
# Upstream: Mike D. Schiffman <mike@infonexus.com>

Summary: Active reconnaissance network security tool
Name: firewalk
Version: 5.0
Release: 1
License: BSD
Group: Applications/Internet
URL: http://www.packetfactory.net/projects/firewalk/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.packetfactory.net/firewalk/dist/firewalk-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libnet >= 1.1.0, libpcap, libdnet

%description
Firewalk is an active reconnaissance network security tool that attempts
to determine what layer 4 protocols a given IP forwarding device will pass.

Firewalk works by sending out TCP or UDP packets with a TTL one greater
than the targeted gateway. If the gateway allows the traffic, it will
forward the packets to the next hop where they will expire and elicit an
ICMP_TIME_EXCEEDED message. If the gateway hostdoes not allow the
traffic, it will likely drop the packets on the floor and we will see no
response.

%prep
%setup -n Firewalk

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%{__install} -D -m0644 man/firewalk.8 %{buildroot}%{_mandir}/man8/firewalk.8

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc BUGS README TODO
%doc %{_mandir}/man?/*
%{_sbindir}/*

%changelog
* Sat Apr 10 2004 Dag Wieers <dag@wieers.com> - 5.0-1
- Initial package. (using DAR)
