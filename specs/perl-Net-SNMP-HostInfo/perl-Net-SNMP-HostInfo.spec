# $Id$

# Authority: dries
# Upstream: James Macfarlane <jmacfarla$cpan,org>

%define real_name Net-SNMP-HostInfo
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Access the IP statistics of a MIB-II host
Name: perl-Net-SNMP-HostInfo
Version: 0.04
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-SNMP-HostInfo/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/J/JM/JMACFARLA/Net-SNMP-HostInfo-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

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
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README Changes
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Net/SNMP/HostInfo.pm
%{perl_vendorlib}/Net/SNMP/HostInfo/*

%changelog
* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 0.04-1
- Initial package.
