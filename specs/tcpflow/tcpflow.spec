# $Id$
# Authority: dag
# Upstream: Jeremy Elson <jelson$circlemud,org>


%{!?dtag:%define _with_libpcapdevel 1}
%{?el5:%define _with_libpcapdevel 1}
%{?fc6:%define _with_libpcapdevel 1}

Summary: Network traffic recorder
Name: tcpflow
Version: 0.21
Release: 1.2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://www.circlemud.org/~jelson/software/tcpflow/

Source: http://www.circlemud.org/pub/jelson/tcpflow/tcpflow-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: libpcap
%{?_with_libpcapdevel:BuildRequires:libpcap-devel}

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
%doc %{_mandir}/man1/tcpflow.1*
%{_bindir}/tcpflow

%changelog
* Wed Apr 21 2004 Dag Wieers <dag@wieers.com> - 0.21-1
- updated to release 0.21.

* Thu Oct 23 2003 Dag Wieers <dag@wieers.com> - 0.20-0
- Initial package. (using DAR)
