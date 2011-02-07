# $Id$
# Upstream: Toby Inkster <tobyink@cpan.org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)
%define real_name RDF-RDFa-Parser

Summary: flexible RDFa parser
Name: perl-RDF-RDFa-Parser
Version: 1.093
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/RDF-RDFa-Parser/

Source: http://search.cpan.org/CPAN/authors/id/T/TO/TOBYINK/RDF-RDFa-Parser-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl(Archive::Zip)
BuildRequires: perl(Carp)
BuildRequires: perl(Data::Dumper)
BuildRequires: perl(Data::UUID)
#BuildRequires: perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires: perl(ExtUtils::MakeMaker) 
BuildRequires: perl(File::ShareDir)
BuildRequires: perl(File::Slurp)
BuildRequires: perl(File::Spec)
BuildRequires: perl(File::Temp)
BuildRequires: perl(HTML::HTML5::Parser)
BuildRequires: perl(HTML::HTML5::Sanity)
BuildRequires: perl(HTTP::Cache::Transparent)
BuildRequires: perl(HTTP::Response)
BuildRequires: perl(LWP::UserAgent)
BuildRequires: perl(Module::Pluggable)
BuildRequires: perl(Module::Signature)
BuildRequires: perl(RDF::Trine) >= 0.123
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Storable)
BuildRequires: perl(Test::More) >= 0.61
BuildRequires: perl(URI::Escape)
BuildRequires: perl(URI::URL)
BuildRequires: perl(URI::file)
BuildRequires: perl(XML::LibXML) >= 1.66
BuildRequires: perl(XML::RegExp)
BuildRequires: perl(common::sense)
BuildRequires: perl >= v5.8.0
Requires: perl(Carp)
Requires: perl(Data::Dumper)
Requires: perl(Data::UUID)
Requires: perl(File::ShareDir)
Requires: perl(File::Spec)
Requires: perl(File::Temp)
Requires: perl(HTML::HTML5::Parser)
Requires: perl(HTML::HTML5::Sanity)
Requires: perl(HTTP::Cache::Transparent)
Requires: perl(LWP::UserAgent)
Requires: perl(Module::Pluggable)
Requires: perl(RDF::Trine) >= 0.123
Requires: perl(Scalar::Util)
Requires: perl(Storable)
Requires: perl(URI::Escape)
Requires: perl(URI::URL)
Requires: perl(URI::file)
Requires: perl(XML::LibXML) >= 1.66
Requires: perl(XML::RegExp)
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

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/RDF::RDFa::Parser.3pm*
%doc %{_mandir}/man3/RDF::RDFa::Parser::Config.3pm.gz
%doc %{_mandir}/man3/RDF::RDFa::Parser::Profile.3pm.gz
%doc %{_mandir}/man3/RDF::RDFa::Parser::Profile::ARIARoles.3pm.gz
%doc %{_mandir}/man3/RDF::RDFa::Parser::Profile::AbstractLinkTypes.3pm.gz
%doc %{_mandir}/man3/RDF::RDFa::Parser::Profile::AbstractRoles.3pm.gz
%doc %{_mandir}/man3/RDF::RDFa::Parser::Profile::GRDDLLinkTypes.3pm.gz
%doc %{_mandir}/man3/RDF::RDFa::Parser::Profile::HTML32LinkTypes.3pm.gz
%doc %{_mandir}/man3/RDF::RDFa::Parser::Profile::HTML4LinkTypes.3pm.gz
%doc %{_mandir}/man3/RDF::RDFa::Parser::Profile::HTML5LinkTypes.3pm.gz
%doc %{_mandir}/man3/RDF::RDFa::Parser::Profile::IETFLinkTypes.3pm.gz
%doc %{_mandir}/man3/RDF::RDFa::Parser::Profile::Null.3pm.gz
%doc %{_mandir}/man3/RDF::RDFa::Parser::Profile::PrefixCC.3pm.gz
%doc %{_mandir}/man3/RDF::RDFa::Parser::Profile::RDF.3pm.gz
%doc %{_mandir}/man3/RDF::RDFa::Parser::Profile::RDFa10LinkTypes.3pm.gz
%doc %{_mandir}/man3/RDF::RDFa::Parser::Profile::SearchMonkey.3pm.gz
%doc %{_mandir}/man3/RDF::RDFa::Parser::Profile::XHTML.3pm.gz
%doc %{_mandir}/man3/RDF::RDFa::Parser::Profile::XHTMLRoles.3pm.gz
%dir %{perl_vendorlib}/
%{perl_vendorlib}/RDF/RDFa/Parser.pm
%{perl_vendorlib}/RDF/RDFa/Parser/Config.pm
%{perl_vendorlib}/RDF/RDFa/Parser/OpenDocumentObjectModel.pm
%{perl_vendorlib}/RDF/RDFa/Parser/Profile.pm
%{perl_vendorlib}/RDF/RDFa/Parser/Profile/ARIARoles.pm
%{perl_vendorlib}/RDF/RDFa/Parser/Profile/AbstractLinkTypes.pm
%{perl_vendorlib}/RDF/RDFa/Parser/Profile/AbstractRoles.pm
%{perl_vendorlib}/RDF/RDFa/Parser/Profile/GRDDLLinkTypes.pm
%{perl_vendorlib}/RDF/RDFa/Parser/Profile/HTML32LinkTypes.pm
%{perl_vendorlib}/RDF/RDFa/Parser/Profile/HTML4LinkTypes.pm
%{perl_vendorlib}/RDF/RDFa/Parser/Profile/HTML5LinkTypes.pm
%{perl_vendorlib}/RDF/RDFa/Parser/Profile/IETFLinkTypes.pm
%{perl_vendorlib}/RDF/RDFa/Parser/Profile/Null.pm
%{perl_vendorlib}/RDF/RDFa/Parser/Profile/PrefixCC.pm
%{perl_vendorlib}/RDF/RDFa/Parser/Profile/RDF.pm
%{perl_vendorlib}/RDF/RDFa/Parser/Profile/RDFa10LinkTypes.pm
%{perl_vendorlib}/RDF/RDFa/Parser/Profile/SearchMonkey.pm
%{perl_vendorlib}/RDF/RDFa/Parser/Profile/XHTML.pm
%{perl_vendorlib}/RDF/RDFa/Parser/Profile/XHTMLRoles.pm
%{perl_vendorlib}/auto/share/dist/RDF-RDFa-Parser
%exclude %{perl_vendorarch}/auto/RDF/RDFa/Parser/.packlist

%changelog
* Mon Feb 07 2011 Christoph Maser <cmaser.gmx.de> - 1.093-1
- initial package
