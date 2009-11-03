# $Id$
# Authority: dag
# Upstream: Steve Benson <steve$rhythm,cx>


%{!?dtag:%define _with_libpcapdevel 1}
%{?el5:%define _with_libpcapdevel 1}
%{?fc6:%define _with_libpcapdevel 1}

Summary: Packet sniffer which displays TCP information like the 'top' command
Name: tcptrack
Version: 1.3.0
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://www.rhythm.cx/~steve/devel/tcptrack/

Source: http://www.rhythm.cx/~steve/devel/tcptrack/release/%{version}/source/tcptrack-%{version}.tar.gz
Patch: remove-extra-qualifications.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, ncurses-devel, libpcap
%{?_with_libpcapdevel:BuildRequires:libpcap-devel}

%description
tcptrack is a sniffer which displays information about TCP connections it
sees on a network interface. It passively watches for connections on the
network interface, keeps track of their state and displays a list of
connections in a manner similar to the unix 'top' command. It displays
source and destination addresses and ports, connection state, idle time, and
bandwidth usage.

%prep
%setup
#patch -p1

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
%doc AUTHORS ChangeLog COPYING README
%doc %{_mandir}/man1/tcptrack.1*
%{_bindir}/tcptrack

%changelog
* Thu Feb 07 2008 Dag Wieers <dag@wieers.com> - 1.3.0-1
- Updated to release 1.3.0.

* Mon Mar 28 2005 Dag Wieers <dag@wieers.com> - 1.1.5-1
- Updated to release 1.1.5.

* Mon Oct 11 2004 Dag Wieers <dag@wieers.com> - 1.1.4-1
- Updated to release 1.1.4.

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
