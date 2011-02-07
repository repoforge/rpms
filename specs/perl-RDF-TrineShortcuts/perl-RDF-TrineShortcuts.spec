# $Id$
# Upstream: Toby Inkster <tobyink@cpan.org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)
%define real_name RDF-TrineShortcuts

Summary: totally unauthorised module for cheats and charlatans
Name: perl-RDF-TrineShortcuts
Version: 0.104
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/RDF-TrineShortcuts/

Source: http://search.cpan.org/CPAN/authors/id/T/TO/TOBYINK/RDF-TrineShortcuts-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl(Exporter)
#BuildRequires: perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires: perl(ExtUtils::MakeMaker) 
BuildRequires: perl(File::Slurp)
BuildRequires: perl(Getopt::Long)
BuildRequires: perl(LWP::Simple)
BuildRequires: perl(Module::Signature) >= 0.66
BuildRequires: perl(Pod::Usage)
BuildRequires: perl(RDF::Query) >= 2.903
BuildRequires: perl(RDF::Query::Client) >= 0.03
BuildRequires: perl(RDF::RDFa::Parser) >= 1.093
BuildRequires: perl(RDF::Trine) >= 0.130
BuildRequires: perl(Test::More) >= 0.61
BuildRequires: perl(URI) >= 1.30
BuildRequires: perl(URI::file)
BuildRequires: perl(YAML)
BuildRequires: perl >= v5.8.0
Requires: perl(Exporter)
Requires: perl(File::Slurp)
Requires: perl(Getopt::Long)
Requires: perl(LWP::Simple)
Requires: perl(Pod::Usage)
Requires: perl(RDF::Query) >= 2.903
Requires: perl(RDF::Query::Client) >= 0.03
Requires: perl(RDF::RDFa::Parser) >= 1.093
Requires: perl(RDF::Trine) >= 0.130
Requires: perl(URI) >= 1.30
Requires: perl(URI::file)
Requires: perl(YAML)
Requires: perl >= v5.8.0

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup


%description


%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}" --skipdeps
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/RDF::TrineShortcuts.3pm*
%doc %{_mandir}/man1/toquet.1*
%doc %{_mandir}/man1/trapper.1*
%doc %{_mandir}/man1/trist.1*
%{_bindir}/toquet
%{_bindir}/trapper
%{_bindir}/trist
%dir %{perl_vendorlib}/
%{perl_vendorlib}/RDF/TrineShortcuts.pm
%exclude %{perl_vendorarch}/auto/RDF/TrineShortcuts/.packlist

%changelog
* Mon Feb 07 2011 Christoph Maser <cmaser.gmx.de> - 0.104-1
- initial package
