# $Id$
# Authority: dag
# Upstream: Jeremy Elson <jelson$circlemud,org>

Summary: Network traffic recorder
Name: tcpflow
Version: 0.21
Release: 1.2
License: GPL
Group: Applications/Internet
URL: http://www.circlemud.org/~jelson/software/tcpflow/

Source: http://www.circlemud.org/pub/jelson/tcpflow/tcpflow-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: libpcap

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
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.21-1.2
- Rebuild for Fedora Core 5.

* Wed Apr 21 2004 Dag Wieers <dag@wieers.com> - 0.21-1
- updated to release 0.21.

* Thu Oct 23 2003 Dag Wieers <dag@wieers.com> - 0.20-0
- Initial package. (using DAR)
