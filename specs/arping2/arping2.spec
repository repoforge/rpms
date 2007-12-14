# $Id$
# Authority: dag

%{?dtag: %{expand: %%define %dtag 1}}

%{!?dtag:%define _with_libpcapdevel 1}
%{?el5:%define _with_libpcapdevel 1}
%{?fc6:%define _with_libpcapdevel 1}

%define real_name arping

Summary: Layer2 Ethernet pinger
Name: arping2
Version: 2.06
Release: 1
License: GPL
Group: Applications/Internet
URL: http://www.habets.pp.se/synscan/programs.php

Source: ftp://ftp.habets.pp.se/pub/synscan/arping-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libdnet-devel, libpcap
%{?_with_libpcapdevel:BuildRequires:libpcap-devel}

%description
Arping is a util to find out it a specific IP address on the LAN is
'taken' and what MAC address owns it. Sure, you *could* just use
'ping' to find out if it's taken and even if the computer blocks ping
(and everything else) you still get an entry in your ARP cache. But
what if you aren't on a routable net? Or the host blocks ping (all
ICMP even)? Then you're screwed. Or you use arping.

%prep
%setup -n %{real_name}-%{version}

%build
%{__make} arping2

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 arping %{buildroot}%{_sbindir}/arping2

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc LICENSE README arping-scan-net.sh
%{_sbindir}/arping2

%changelog
* Fri Dec 14 2007 Dag Wieers <dag@wieers.com>- 2.06-1
- Initial package. (using DAR)
