# $Id$

# Authority: dries
# Upstream: Glenn Wood <glenwood$alumni,caltech,edu>

%define real_name Scraper
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Framework for scraping results from search engines
Name: perl-Scraper
Version: 3.05
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Scraper/

Source: http://search.cpan.org/CPAN/authors/id/G/GL/GLENNWOOD/Scraper-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
These modules scrape data from search engines on the WWW.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -f %{buildroot}%{perl_vendorlib}/prereqinst.pl
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/WWW/Scraper*.pm
%{perl_vendorlib}/WWW/Scraper/*
%changelog
* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 3.05-1
- Initial package.
