# $Id$
# Authority: dag
# Upstream: Paul Gampe <pgampe$users,sourceforge,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-Whois-RIPE

Summary: Perl module that implemens RIPE Whois
Name: perl-Net-Whois-RIPE
Version: 2.00002
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-Whois-RIPE/

Source: http://search.cpan.org/CPAN/authors/id/L/LM/LMC/Net-Whois-RIPE-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Iterator)
BuildRequires: perl(Iterator::Util)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::More)
BuildRequires: perl >= 5.006
Requires: perl(Iterator)
Requires: perl(Iterator::Util)
Requires: perl(Test::Exception)
Requires: perl(Test::More)
Requires: perl >= 5.006


%description
perl-Net-Whois-RIPE is a Perl module that implemens RIPE Whois.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make}
%{__make} test

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Net::Whois::RIPE.3pm*
#%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/Net/
%dir %{perl_vendorlib}/Net/Whois/
%{perl_vendorlib}/Net/Whois/RIPE.pm

%changelog
* Wed Feb  3 2010 Christoph Maser <cmr@financial.com> - 2.00002-1
- Updated to version 2.00002.

* Mon Jul 13 2009 Christoph Maser <cmr@financial.com> - 1.30-1
- Updated to version 1.30.

* Sun Oct 07 2007 Dag Wieers <dag@wieers.com> - 1.22-1
- Initial package. (using DAR)
