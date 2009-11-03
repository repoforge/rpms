# $Id$
# Authority: dries


%{!?dtag:%define _with_libpcapdevel 1}
%{?el5:%define _with_libpcapdevel 1}
%{?fc6:%define _with_libpcapdevel 1}

Summary: Tests and attacks for network protocols
Name: yersinia
Version: 0.7
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://www.yersinia.net/

Source: http://www.yersinia.net/download/yersinia-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libnet, libpcap, ncurses-devel, gtk2-devel
%{?_with_libpcapdevel:BuildRequires:libpcap-devel}

%description
Yersinia implements several attacks for the following protocols:
Spanning Tree (STP), Cisco Discovery (CDP), Dynamic Host Configuration
(DHCP), Hot Standby Router (HSRP), Dynamic Trunking (DTP), 802.1q,
Inter-Switch Link Protocol (ISL), and VLAN Trunking (VTP). It helps
the pen-tester in different tasks, such as becoming the root role in
the Spanning Tree, creating virtual CDP neighbors, setting up rogue
DHCP servers, becoming the active router in a HSRP scenario, enabling
trunk, performing ARP spoofing over VLAN hopping, adding or deleting
VLANs (via VTP), and more.

%prep
%setup

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
%doc AUTHORS ChangeLog COPYING FAQ INSTALL NEWS README THANKS TODO
%doc %{_mandir}/man8/yersinia*
%{_bindir}/yersinia

%changelog
* Mon Nov 12 2006 Dries Verachtert <dries@ulyssis.org> - 0.7-1
- Updated to release 0.7.

* Tue Sep 20 2005 Dries Verachtert <dries@ulyssis.org> - 0.5.6
- Initial package.
