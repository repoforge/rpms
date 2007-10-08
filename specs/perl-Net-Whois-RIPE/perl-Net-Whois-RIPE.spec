# $Id$
# Authority: dag
# Upstream: Paul Gampe <pgampe$users,sourceforge,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-Whois-RIPE

Summary: Perl module that implemens RIPE Whois
Name: perl-Net-Whois-RIPE
Version: 1.22
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-Whois-RIPE/

Source: http://www.cpan.org/modules/by-module/Net/Net-Whois-RIPE-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Net-Whois-RIPE is a Perl module that implemens RIPE Whois.

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
%doc ChangeLog MANIFEST META.yml README
%doc %{_mandir}/man3/Net::Whois::RIPE.3pm*
%doc %{_mandir}/man3/Net::Whois::RIPE::Iterator.3pm*
%doc %{_mandir}/man3/Net::Whois::RIPE::Object.3pm*
#%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/Net/
%dir %{perl_vendorlib}/Net/Whois/
%{perl_vendorlib}/Net/Whois/RIPE/
%{perl_vendorlib}/Net/Whois/RIPE.pm
%{perl_vendorlib}/Net/Whois/RIPE.pod
%{perl_vendorlib}/Net/Whois/update.pl

%changelog
* Sun Oct 07 2007 Dag Wieers <dag@wieers.com> - 1.22-1
- Initial package. (using DAR)
