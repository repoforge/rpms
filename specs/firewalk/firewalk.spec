# $Id$
# Authority: dag
# Upstream: Mike D. Schiffman <mike$infonexus,com>

%{?dtag: %{expand: %%define %dtag 1}}

%{!?dtag:%define _with_libpcapdevel 1}
%{?el5:%define _with_libpcapdevel 1}
%{?fc6:%define _with_libpcapdevel 1}

Summary: Active reconnaissance network security tool
Name: firewalk
Version: 5.0
Release: 1.2%{?dist}
License: BSD
Group: Applications/Internet
URL: http://www.packetfactory.net/projects/firewalk/

Source: http://www.packetfactory.net/firewalk/dist/firewalk-%{version}.tgz
Patch: firewalk-5.0-gcc34.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libnet >= 1.1.0, libpcap, libdnet-devel, libtool
%{?_with_libpcapdevel:BuildRequires:libpcap-devel}

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
%patch

%build
%{__libtoolize} --force --copy
%{__aclocal} #--force
%{__autoheader}
%{__automake} --add-missing -a --foreign
%{__autoconf}
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%{__install} -Dp -m0644 man/firewalk.8 %{buildroot}%{_mandir}/man8/firewalk.8

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc BUGS README TODO
%doc %{_mandir}/man8/firewalk.8*
%{_sbindir}/firewalk

%changelog
* Sat Apr 10 2004 Dag Wieers <dag@wieers.com> - 5.0-1
- Initial package. (using DAR)
