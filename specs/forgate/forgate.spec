# $Id$
# Authority: dag

%define real_version 0.9b

Summary: Packet redirection tool for interception on switched networks
Name: forgate
Version: 0.9
Release: 0.b.2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://forgate.sourceforge.net/

Source: http://forgate.sf.net/forgate-%{real_version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libnet >= 1.1
Requires: libnet >= 1.1

%description
Forgate was written as a proof of concept in one method of capturing
traffic flows from a 3rd party on a switched network. Forgate uses ARP cache
poisoning, packet capture and packet reconstruction to perform it's task. It
should work with nearly all TCP, ICMP and UDP IPv4 traffic.

%prep
%setup -n %{name}-%{real_version}

%build
#CC='gcc -I/usr/include/pcap' ./configure --prefix=/usr
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%files
%defattr(-, root, root, 0755)
%doc LICENSE
%{_sbindir}/*

%clean
%{__rm} -rf %{buildroot}

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.9-0.b.2
- Rebuild for Fedora Core 5.

* Mon Jan 26 2004 Dag Wieers <dag@wieers.com> - 0.9-0.b
- Initial package. (using DAR)
