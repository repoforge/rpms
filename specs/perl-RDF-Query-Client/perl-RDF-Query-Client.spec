# $Id$
# Upstream: Toby Inkster <tobyink@cpan.org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)
%define real_name RDF-Query-Client

Summary: get data from W3C SPARQL Protocol 1.0 servers
Name: perl-RDF-Query-Client
Version: 0.103
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/RDF-Query-Client/

Source: http://search.cpan.org/CPAN/authors/id/T/TO/TOBYINK/RDF-Query-Client-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl(Carp)
#BuildRequires: perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires: perl(ExtUtils::MakeMaker) 
BuildRequires: perl(LWP::Simple)
BuildRequires: perl(LWP::UserAgent)
BuildRequires: perl(RDF::Trine) >= 0.111
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Test::More) >= 0.61
BuildRequires: perl(URI::Escape)
BuildRequires: perl >= v5.6.0
Requires: perl(Carp)
Requires: perl(LWP::UserAgent)
Requires: perl(RDF::Trine) >= 0.111
Requires: perl(Scalar::Util)
Requires: perl(URI::Escape)
Requires: perl >= v5.6.0

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup


%description


%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}" --skipdeps
%{__make} %{?_smp_mflags}
%{__make} %{?_smp_mflags} test

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/RDF::Query::Client.3pm*
%dir %{perl_vendorlib}/
%{perl_vendorlib}/RDF/Query/Client.pm
%exclude %{perl_vendorarch}/auto/RDF/Query/Client/.packlist

%changelog
* Mon Feb 07 2011 Christoph Maser <cmaser.gmx.de> - 0.103-1
- initial package
