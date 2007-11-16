# $Id$
# Authority: dag

%{?dtag: %{expand: %%define %dtag 1}}

%{!?dtag:%define _with_libpcapdevel 1}
%{?el5:%define _with_libpcapdevel 1}
%{?fc6:%define _with_libpcapdevel 1}

Summary: Displays various tables of DNS traffic on your network
Name: dnstop
%define real_version 20030228
Version: 0.0.20030228
Release: 0.2
License: BSD
Group: Applications/Internet
URL: http://dnstop.measurement-factory.com/

Source: http://dnstop.measurement-factory.com/src/dnstop-%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libpcap, ncurses-devel
%{?_with_libpcapdevel:BuildRequires:libpcap-devel}

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
%doc %{_mandir}/man8/dnstop.8*
%{_sbindir}/dnstop

%changelog
* Wed Sep 03 2003 Dag Wieers <dag@wieers.com> - 0.0.20030228-0
- Initial package. (using DAR)
