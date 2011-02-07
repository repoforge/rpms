# $Id$
# Authority: dries
# Upstream: Barbie <barbie$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name WWW-Scraper-ISBN-Pearson_Driver

Summary: Search driver for Pearson Education's online catalog
Name: perl-WWW-Scraper-ISBN-Pearson_Driver
Version: 0.17
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/WWW-Scraper-ISBN-Pearson_Driver/

Source: http://search.cpan.org/CPAN/authors/id/B/BA/BARBIE/WWW-Scraper-ISBN-Pearson_Driver-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl(Test::More) >= 0.45  
BuildRequires: perl(WWW::Mechanize) >= 1.60
BuildRequires: perl(WWW::Scraper::ISBN) >= 0.25
BuildRequires: perl(WWW::Scraper::ISBN::Driver) >= 0.18
Requires: perl(WWW::Mechanize) >= 1.60
Requires: perl(WWW::Scraper::ISBN) >= 0.25
Requires: perl(WWW::Scraper::ISBN::Driver) >= 0.18

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup


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

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes LICENSE MANIFEST META.yml README examples/
%doc %{_mandir}/man3/WWW::Scraper::ISBN::Pearson_Driver.3pm*
%dir %{perl_vendorlib}/WWW/
%dir %{perl_vendorlib}/WWW/Scraper/
%dir %{perl_vendorlib}/WWW/Scraper/ISBN/
#%{perl_vendorlib}/WWW/Scraper/ISBN/Pearson_Driver/
%{perl_vendorlib}/WWW/Scraper/ISBN/Pearson_Driver.pm

%changelog
* Mon Feb  7 2011 Christoph Maser <cmaser@gmx.de> - 0.17-1
- Updated to version 0.17.

* Sat Aug 29 2009 Christoph Maser <cmr@financial.com> - 0.11-1
- Updated to version 0.11.

* Mon Jun  8 2009 Christoph Maser <cmr@financial.com> - 0.10-1
- Updated to version 0.10.

* Mon Nov 19 2007 Dag Wieers <dag@wieers.com> - 0.09-1
- Updated to release 0.09.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.08-1
- Initial package.
