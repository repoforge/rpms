# $Id$
# Authority: cmr
# Upstream: Andrew Schamp <andy$schamp,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name WWW-Scraper-ISBN-Record

Summary: Perl module named WWW-Scraper-ISBN-Record
Name: perl-WWW-Scraper-ISBN-Record
Version: 0.17
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/WWW-Scraper-ISBN-Record/

Source: http://www.cpan.org/modules/by-module/WWW/WWW-Scraper-ISBN-Record-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-WWW-Scraper-ISBN-Record is a Perl module.

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
%doc Changes MANIFEST README
%doc %{_mandir}/man3/WWW::Scraper::ISBN::Record.3pm*
%dir %{perl_vendorlib}/WWW/
%dir %{perl_vendorlib}/WWW/Scraper/
%dir %{perl_vendorlib}/WWW/Scraper/ISBN/
#%{perl_vendorlib}/WWW/Scraper/ISBN/Record/
%{perl_vendorlib}/WWW/Scraper/ISBN/Record.pm

%changelog
* Sat Aug 29 2009 Christoph Maser <cmr@financial.com> - 0.17-1
- Initial package. (using DAR)
