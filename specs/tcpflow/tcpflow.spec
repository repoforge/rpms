# $Id$

# Authority: dag

Summary: Network traffic recorder.
Name: tcpflow
Version: 0.20
Release: 0
License: GPL
Group: Applications/Internet
URL: http://www.circlemud.org/~jelson/software/tcpflow/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: ftp://ftp.circlemud.org/pub/jelson/tcpflow/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


%description
tcpflow is a program that captures data transmitted as part of TCP
connections (flows), and stores the data in a way that is convenient
for protocol analysis or debugging. A program like 'tcpdump' shows a
summary of packets seen on the wire, but usually doesn't store the
data that's actually being transmitted. In contrast, tcpflow
reconstructs the actual data streams and stores each flow in a
separate file for later analysis.

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
%doc AUTHORS ChangeLog COPYING NEWS README
%doc %{_mandir}/man?/*
%{_bindir}/*

%changelog
* Thu Oct 23 2003 Dag Wieers <dag@wieers.com> - 0.20-0
- Initial package. (using DAR)
