# $Id$
# Upstream: Toby Inkster <tobyink@cpan.org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)
%define real_name XML-Atom-OWL

Summary: parse an Atom file into RDF
Name: perl-XML-Atom-OWL
Version: 0.101
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-Atom-OWL/

Source: http://search.cpan.org/CPAN/authors/id/T/TO/TOBYINK/XML-Atom-OWL-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl(Carp) >= 1.00
BuildRequires: perl(DateTime)
BuildRequires: perl(Encode)
#BuildRequires: perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires: perl(ExtUtils::MakeMaker) 
BuildRequires: perl(HTTP::Link::Parser) >= 0.04
BuildRequires: perl(LWP::UserAgent)
BuildRequires: perl(MIME::Base64)
BuildRequires: perl(RDF::Trine) >= 0.112
BuildRequires: perl(Test::More) >= 0.61
BuildRequires: perl(URI) >= 1.30
BuildRequires: perl(URI::URL)
BuildRequires: perl(XML::LibXML) >= 1.60
BuildRequires: perl(common::sense)
BuildRequires: perl >= v5.8.0
Requires: perl(Carp) >= 1.00
Requires: perl(DateTime)
Requires: perl(Encode)
Requires: perl(HTTP::Link::Parser) >= 0.04
Requires: perl(LWP::UserAgent)
Requires: perl(MIME::Base64)
Requires: perl(RDF::Trine) >= 0.112
Requires: perl(URI) >= 1.30
Requires: perl(URI::URL)
Requires: perl(XML::LibXML) >= 1.60
Requires: perl(common::sense)
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
%{__make} %{?_smp_mflags} test

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/XML::Atom::OWL.3pm*
%dir %{perl_vendorlib}/
%{perl_vendorlib}/XML/Atom/OWL.pm
%exclude %{perl_vendorarch}/auto/XML/Atom/OWL/.packlist

%changelog
* Mon Feb 07 2011 Christoph Maser <cmaser.gmx.de> - 0.101-1
- initial package
