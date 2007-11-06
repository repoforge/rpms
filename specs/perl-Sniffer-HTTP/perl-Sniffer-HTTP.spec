# $Id$
# Authority: dries
# Upstream: Max Maischein <corion$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Sniffer-HTTP

Summary: Multi-connection sniffer driver
Name: perl-Sniffer-HTTP
Version: 0.16
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Sniffer-HTTP/

Source: http://search.cpan.org//CPAN/authors/id/C/CO/CORION/Sniffer-HTTP-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
A multi-connection sniffer driver.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes
%doc %{_mandir}/man3/Sniffer::*
%doc %{_mandir}/man3/Net::Pcap::FindDevice*
%{perl_vendorlib}/Sniffer/
%{perl_vendorlib}/Net/Pcap/

%changelog
* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.16-1
- Initial package.
