# $Id$

# Authority: dag

Summary: An active reconnaissance network security tool.
Name: firewalk
Version: 5.0
Release: 0
License: BSD
Group: Applications/Internet
URL: http://www.packetfactory.net/projects/firewalk/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.packetfactory.net/firewalk/dist/%{name}-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: libnet-devel >= 1.1.0, libpcap, libdnet

%description
Firewalk is an active reconnaissance network security tool that attempts
to determine what layer 4 protocols a given IP forwarding device will pass.

Firewalk works by sending out TCP or UDP packets with a TTL one greater
than the targeted gateway. If the gateway allows the traffic, it will
forward the packets to the next hop where they will expire and elicit an
ICMP_TIME_EXCEEDED message. If the gateway hostdoes not allow the
traffic, it will likely drop the packets on the floor and we will see no
response.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

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

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_libdir}/*

%changelog
* Wed Oct 22 2003 Dag Wieers <dag@wieers.com> - 5.0-0
- Initial package. (using DAR)
