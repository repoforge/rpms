# $Id$
# Authority: dries
# Upstream: Max Maischein <corion$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Sniffer-HTTP

Summary: Multi-connection sniffer driver
Name: perl-Sniffer-HTTP
Version: 0.19
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Sniffer-HTTP/

Source: http://www.cpan.org/authors/id/C/CO/CORION/Sniffer-HTTP-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
A multi-connection sniffer driver.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST MANIFEST.skip META.yml
%doc %{_mandir}/man3/Net::Pcap::FindDevice.3pm*
%doc %{_mandir}/man3/Sniffer::*
%dir %{perl_vendorlib}/Net/Pcap/
%{perl_vendorlib}/Net/Pcap/FindDevice.pm
%{perl_vendorlib}/Sniffer/

%changelog
* Thu Jun 18 2009 Christoph Maser <cmr@financial.com> - 0.19-1
- Updated to version 0.19.

* Thu Nov 15 2007 Dag Wieers <dag@wieers.com> - 0.17-1
- Updated to release 0.17.

* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.16-1
- Initial package.
