# $Id$
# Authority: dag
# Upstream: Steve Benson <steve@rhythm.cx>

Summary: Packet sniffer which displays TCP information like the 'top' command
Name: tcptrack
Version: 1.1.2
Release: 1
License: GPL
Group: Applications/Internet
URL: http://www.rhythm.cx/~steve/devel/tcptrack/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.rhythm.cx/~steve/devel/tcptrack/release/%{version}/source/tcptrack-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description 
tcptrack is a sniffer which displays information about TCP connections it
sees on a network interface. It passively watches for connections on the
network interface, keeps track of their state and displays a list of
connections in a manner similar to the unix 'top' command. It displays
source and destination addresses and ports, connection state, idle time, and
bandwidth usage.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING README
%doc %{_mandir}/man?/*
%{_bindir}/*

%changelog
* Tue Jun 15 2004 Dag Wieers <dag@wieers.com> - 1.1.2-1
- Updated to release 1.1.2.

* Thu May 13 2004 Dag Wieers <dag@wieers.com> - 1.1.1-1
- Updated to release 1.1.1.

* Fri Apr 23 2004 Dag Wieers <dag@wieers.com> - 1.1.0-1
- Updated to release 1.1.0.

* Tue Mar 09 2004 Dag Wieers <dag@wieers.com> - 1.0.2-1
- Updated to release 1.0.2.

* Tue Nov 23 2003 Dag Wieers <dag@wieers.com> - 1.0.0-0
- Initial package. (using DAR)
