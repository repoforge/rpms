# $Id$
# Authority: dag
# Upstream: <wireless$kismetwireless,net>

%define real_version 2004-04-R1

Summary: 802.11 (wireless) network sniffer and network dissector
Name: kismet
Version: 3.0.1
Release: 1.200404r1
License: GPL
Group: Applications/Internet
URL: http://www.kismetwireless.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source0: http://www.kismetwireless.net/code/kismet-%{real_version}.tar.gz
#Source1: http://www.kismetwireless.net/code/configure
#Patch0: http://www.kismetwireless.net/code/kismet-feb.04.01.diff.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: ImageMagick-devel, ncurses-devel, autoconf, flex

%description
Kismet is an 802.11 (wireless) network sniffer and network dissector.
It is capable of sniffing using most wireless cards, automatic network
IP block detection via UDP, ARP, and DHCP packets, Cisco equipment lists
via Cisco Discovery Protocol, weak cryptographic packet logging, and
Ethereal and tcpdump compatible packet dump files. It also includes
the ability to plot detected networks and estimated network ranges on
downloaded maps or user supplied image files.

%prep
%setup -n %{name}-%{real_version}
#%patch0 -p1
#%{__install} -m0755 %{SOURCE1} .

### FIXME: Get rid of the ownership changes
%{__perl} -pi.orig -e '
		s|-o \$\(INSTUSR\) -g \$\(INSTGRP\) ||g;
		s|-o \$\(INSTUSR\) -g \$\(MANGRP\) ||g;
	' Makefile.in

### FIXME: Fix configure to work
#%{__perl} -pi.orig -e 's|^,$||' configure

%build
cd libpcap-*
%{__autoconf}
cd -
%{__autoconf}
%configure
#	--enable-syspcap
%{__make} %{?_smp_mflags} dep all

%install
%{__rm} -rf %{buildroot}
%makeinstall rpm \
	ETC="%{buildroot}%{_sysconfdir}" \
	BIN="%{buildroot}%{_bindir}" \
	SHARE="%{buildroot}%{_datadir}/kismet/" \
	MAN="%{buildroot}%{_mandir}" \
	WAV="%{buildroot}%{_datadir}/kismet/wav/"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGELOG GPL README TODO docs/DEVEL.* docs/README*
%doc %{_mandir}/man?/*
%config(noreplace) %{_sysconfdir}/*
%{_bindir}/*
%{_datadir}/kismet/

%changelog
* Fri Apr 09 2004 Dag Wieers <dag@wieers.com> - 3.0.1-1.200404r1
- Updated to release 2004-04-R1.

* Tue Mar 16 2004 Dag Wieers <dag@wieers.com> - 3.0.1-1
- Updated to release 3.0.1-feb.04.01.

* Wed Aug 13 2003 Dag Wieers <dag@wieers.com> - 3.0.1-0
- Updated to release 3.0.1.

* Thu Jul 31 2003 Dag Wieers <dag@wieers.com> - 3.0.0-0
- Updated to release 3.0.0.

* Sat Jul 12 2003 Dag Wieers <dag@wieers.com> - 2.8.1-0
- Initial package. (using DAR)
