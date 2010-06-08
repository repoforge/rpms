# $Id$
# Authority: dag
# Upstream: Bert Vermeulen <bert$biot,com>

%{?el4:%define _without_libpcapdevel 1}
%{?el3:%define _without_libpcapdevel 1}

Summary: Tool to generate byte and packet counters based on Berkeley Packet Filter (BPF) expressions
Name: capstats
Version: 0.2
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://biot.com/capstats/

Source: http://biot.com/capstats/capstats-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%{?_without_libpcapdevel:BuildRequires: libpcap >= 0.8}
%{!?_without_libpcapdevel:BuildRequires: libpcap-devel >= 0.8}

%description
Capstats generates byte and packet counters based on a Berkeley Packet
Filter (BPF) expression.

%prep
%setup

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}

%{__install} -Dp -m0755 capstats %{buildroot}%{_sbindir}/capstats

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING README
%{_sbindir}/capstats

%changelog
* Sun May 30 2010 Dag Wieers <dag@wieers.com> - 0.2-1
- Initial package. (using DAR)
