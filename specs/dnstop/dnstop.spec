# $Id$

# Authority: dag

%define real_version 20030228

Summary: Displays various tables of DNS traffic on your network
Name: dnstop
Version: 0.0.%{real_version}
Release: 0
License: BSD
Group: Applications/Internet
URL: http://dnstop.measurement-factory.com/

Source: http://dnstop.measurement-factory.com/src/%{name}-%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: libpcap, ncurses-devel

%description
dnstop is a libpcap application (ala tcpdump) that displays various
tables of DNS traffic on your network, including tables of source and
destination IP addresses, query types, top level domains and second
level domains. 

%prep
%setup -c

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 dnstop %{buildroot}%{_sbindir}/dnstop
%{__install} -Dp -m0644 dnstop.8 %{buildroot}%{_mandir}/man8/dnstop.8
						
%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc LICENSE
%doc %{_mandir}/man?/*
%{_sbindir}/*

%changelog
* Wed Sep 03 2003 Dag Wieers <dag@wieers.com> - 0.0.20030228-0
- Initial package. (using DAR)
