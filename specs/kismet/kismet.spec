# $Id$

# Authority: dag

Summary: Kismet is an 802.11b network sniffer and network dissector.
Name: kismet
Version: 3.0.1
Release: 0
License: GPL
Group: Applications/Internet
URL: http://www.kismetwireless.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.kismetwireless.net/code/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: ImageMagick-devel, ncurses-devel

%description
Kismet is an 802.11b network sniffer and network dissector. It is
capable of sniffing using most wireless cards, automatic network IP
block detection via UDP, ARP, and DHCP packets, Cisco equipment lists
via Cisco Discovery Protocol, weak cryptographic packet logging, and
Ethereal and tcpdump compatible packet dump files. It also includes
the ability to plot detected networks and estimated network ranges on
downloaded maps or user supplied image files.

%prep
%setup

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
%{__make} %{?_smp_mflags}

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
%doc CHANGELOG FAQ GPL README TODO docs/DEVEL.* docs/README.*
%doc %{_mandir}/man?/*
%config(noreplace) %{_sysconfdir}/*
%{_bindir}/*
%{_datadir}/kismet/

%changelog
* Wed Aug 13 2003 Dag Wieers <dag@wieers.com> - 3.0.1-0
- Updated to release 3.0.1.

* Thu Jul 31 2003 Dag Wieers <dag@wieers.com> - 3.0.0-0
- Updated to release 3.0.0.

* Sat Jul 12 2003 Dag Wieers <dag@wieers.com> - 2.8.1-0
- Initial package. (using DAR)
