# Authority: dag
# Upstream: Rafal Wojtczuk <nergal@icm.edu.pl>

Summary: An implementation of an E-component of Network Intrusion Detection System.
Name: libnids
Version: 1.18
Release: 0
License: GPL
Group: System Environment/Libraries
URL: http://libnids.sf.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.packetfactory.net/projects/libnids/dist/libnids-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: libnet, libpcap

%description
Libnids is an implementation of an E-component of Network Intrusion
Detection System. It emulates the IP stack of Linux 2.0.x. Libnids
offers IP defragmentation, TCP stream assembly and TCP port scan
detection.

Using libnids, one has got a convenient access to data carried by a
TCP stream, no matter how artfully obscured by an attacker.

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
%doc COPYING MISC README doc/ samples/
%doc %{_mandir}/man?/*
%{_libdir}/*.a
%{_includedir}/*.h

%changelog
* Sun Nov 23 2003 Dag Wieers <dag@wieers.com> - 1.18-0
- Updated to release 1.18

* Mon Sep 15 2003 Dag Wieers <dag@wieers.com> - 1.16-0
- Initial package. (using DAR)
