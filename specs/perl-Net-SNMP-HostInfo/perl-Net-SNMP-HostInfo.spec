# $Id$
# Authority: dries
# Upstream: James Macfarlane <jmacfarla$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-SNMP-HostInfo

Summary: Access the IP statistics of a MIB-II host
Name: perl-Net-SNMP-HostInfo
Version: 0.04
Release: 1.2%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-SNMP-HostInfo/

Source: http://www.cpan.org/modules/by-module/Net/Net-SNMP-HostInfo-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Net::SNMP::HostInfo is a class that simplifies access to the
IP, TCP, and UDP information of a MIB-II compliant network host,
such as a router or a PC.

You can use it to retrieve numerous statistics on IP, ICMP, TCP, and UDP,
as well as the IP routing table (ipRouteTable),
the IP address table (ipAddrTable),
the ARP table (ipNetToMediaTable),
the TCP connection table (tcpConnTable),
and the UDP listener table (udpTable).
Browse the list of available methods to see what values are available.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Net/SNMP/HostInfo.pm
%{perl_vendorlib}/Net/SNMP/HostInfo/*

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.04-1.2
- Rebuild for Fedora Core 5.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 0.04-1
- Initial package.
