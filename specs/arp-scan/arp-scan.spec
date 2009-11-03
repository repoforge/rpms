# $Id$
# Authority: dag
# Upstream: Roy Hills

%{?dtag: %{expand: %%define %dtag 1}}

%{!?dtag:%define _with_libpcapdevel 1}
%{?el5:%define _with_libpcapdevel 1}
%{?fc6:%define _with_libpcapdevel 1}

Summary: ARP scanning and fingerprinting tool
Name: arp-scan
Version: 1.7
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://www.nta-monitor.com/tools/arp-scan/

Source: http://www.nta-monitor.com/tools/arp-scan/download/arp-scan-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

#libdnet-devel, 
BuildRequires: libpcap
%{?_with_libpcapdevel:BuildRequires:libpcap-devel}

%description
arp-scan sends ARP (Address Resolution Protocol) queries to the specified
targets, and displays any responses that are received. It allows any part
of the outgoing ARP packets to be changed, allowing the behavior of targets
to non-standard ARP packets to be examined. The IP address and hardware
address of received packets are displayed, together with the vendor details.

These details are obtained from the IEEE OUI and IAB listings, plus a few
manual entries. It includes arp-fingerprint, which allows a system to be
fingerprinted based on how it responds to non-standard ARP packets.

%prep
%setup

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
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%doc %{_mandir}/man1/arp-fingerprint.1*
%doc %{_mandir}/man1/arp-scan.1*
%doc %{_mandir}/man1/get-iab.1*
%doc %{_mandir}/man1/get-oui.1*
%doc %{_mandir}/man5/mac-vendor.5*
%{_bindir}/arp-fingerprint
%{_bindir}/arp-scan
%{_bindir}/get-iab
%{_bindir}/get-oui
%{_datadir}/arp-scan/

%changelog
* Wed Oct 15 2008 Dag Wieers <dag@wieers.com> - 1.7-1
- Updated to release 1.7.

* Sun Apr 15 2007 Dag Wieers <dag@wieers.com> - 1.6-1
- Updated to release 1.6.

* Thu Jul 27 2006 Dag Wieers <dag@wieers.com> - 1.5-1
- Initial package. (using DAR)
