# $Id$
# Authority: dag
# Upstream: Philippe Biondi <biondi$cartel-securite,fr>

Summary: Interactive packet manipulation tool and network scanner
Name: scapy
Version: 0.9.17
Release: 1
License: GPL
Group: Applications/Internet
URL: http://www.cartel-securite.fr/pbiondi/projects/scapy.html

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.cartel-securite.fr/pbiondi/python/scapy-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
Requires: python >= 2.2, nmap

%description
Scapy is a powerful interactive packet manipulation tool, packet generator,
network scanner, network discovery, packet sniffer, etc. It can for the
moment replace hping, 85% of nmap, arpspoof, arp-sk, arping, tcpdump,
tethereal, p0f, ....

Scapy uses the python interpreter as a command board. That means that you
can use directly python language (assign variables, use loops, define
functions, etc.) If you give a file as parameter when you run scapy, your
session (variables, functions, intances, ...) will be saved when you leave
the interpretor, and restored the next time you launch scapy. 

%prep
%setup

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -D -m0755 scapy.py %{buildroot}%{_bindir}/scapy

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING README
%{_bindir}/scapy

%changelog
* Fri Sep 03 2004 Dag Wieers <dag@wieers.com> - 0.9.17-1
- Updated to release 0.9.17.

* Fri Aug 01 2003 Dag Wieers <dag@wieers.com> - 0.9.14-0
- Added nmap as a dependency.
- Updated to release 0.9.14.

* Sat May 17 2003 Dag Wieers <dag@wieers.com> - 0.9.13-0.beta
- Initial package. (using DAR)
