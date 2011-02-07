# $Id$
# Upstream: Toby Inkster <tobyink@cpan.org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)
%define real_name HTTP-LRDD

Summary: link-based resource descriptor discovery
Name: perl-HTTP-LRDD
Version: 0.103
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/HTTP-LRDD/

Source: http://search.cpan.org/CPAN/authors/id/T/TO/TOBYINK/HTTP-LRDD-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl(Carp) >= 1.00
BuildRequires: perl(Error)
#BuildRequires: perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires: perl(ExtUtils::MakeMaker) 
BuildRequires: perl(HTML::HTML5::Parser)
BuildRequires: perl(HTML::HTML5::Sanity)
BuildRequires: perl(HTTP::Link::Parser)
BuildRequires: perl(HTTP::Status)
BuildRequires: perl(Module::Signature)
BuildRequires: perl(RDF::RDFa::Parser) >= 0.30
BuildRequires: perl(RDF::TrineShortcuts)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Test::More) >= 0.61
BuildRequires: perl(URI) >= 1.30
BuildRequires: perl(URI::Escape)
BuildRequires: perl(XML::Atom::OWL)
BuildRequires: perl(XRD::Parser) >= 0.101
BuildRequires: perl >= v5.8.0
Requires: perl(Carp) >= 1.00
Requires: perl(Error)
Requires: perl(HTML::HTML5::Parser)
Requires: perl(HTML::HTML5::Sanity)
Requires: perl(HTTP::Link::Parser)
Requires: perl(HTTP::Status)
Requires: perl(RDF::RDFa::Parser) >= 0.30
Requires: perl(RDF::TrineShortcuts)
Requires: perl(Scalar::Util)
Requires: perl(URI) >= 1.30
Requires: perl(URI::Escape)
Requires: perl(XML::Atom::OWL)
Requires: perl(XRD::Parser) >= 0.101
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
%doc %{_mandir}/man3/HTTP::LRDD.3pm*
%dir %{perl_vendorlib}/
%{perl_vendorlib}/HTTP/LRDD.pm
%exclude %{perl_vendorarch}/auto/HTTP/LRDD/.packlist

%changelog
* Mon Feb 07 2011 Christoph Maser <cmaser.gmx.de> - 0.103-1
- initial package
