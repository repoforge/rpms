# $Id$
# Authority: dries
# Upstream: Barbie <barbie$missbarbell,co,uk>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name WWW-Scraper-ISBN-Pearson_Driver

Summary: Search driver for Pearson Education's online catalog
Name: perl-WWW-Scraper-ISBN-Pearson_Driver
Version: 0.08
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/WWW-Scraper-ISBN-Pearson_Driver/

Source: http://search.cpan.org//CPAN/authors/id/B/BA/BARBIE/WWW-Scraper-ISBN-Pearson_Driver-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Search driver for Pearson Education's online catalog.

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
%doc Changes README
%doc %{_mandir}/man3/WWW::Scraper::ISBN::Pearson_Driver*
%{perl_vendorlib}/WWW/Scraper/ISBN/Pearson_Driver.pm
%dir %{perl_vendorlib}/WWW/Scraper/ISBN/
%dir %{perl_vendorlib}/WWW/Scraper/

%changelog
* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.08-1
- Initial package.
