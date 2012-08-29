# $Id$
# Upstream: Gregory Todd Williams <gwilliams@cpan.org>

### Requires perl(URI) >= 0:1.52 from Extras
# Tag: rfx

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)
%define real_name RDF-Trine

Summary: An RDF Framework for Perl
Name: perl-RDF-Trine
Version: 0.132
Release: 2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/RDF-Trine/

Source: http://search.cpan.org/CPAN/authors/id/G/GW/GWILLIAMS/RDF-Trine-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl(DBD::SQLite) >= 1.14
BuildRequires: perl(DBI)
BuildRequires: perl(Data::UUID)
BuildRequires: perl(Digest::MD5)
BuildRequires: perl(Digest::SHA1)
BuildRequires: perl(Error)
#BuildRequires: perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires: perl(ExtUtils::MakeMaker) 
BuildRequires: perl(HTTP::Negotiate)
BuildRequires: perl(JSON) >= 2
BuildRequires: perl(LWP::UserAgent)
BuildRequires: perl(List::MoreUtils)
BuildRequires: perl(List::Util)
BuildRequires: perl(Log::Log4perl)
BuildRequires: perl(Math::BigInt)
BuildRequires: perl(Math::Combinatorics) >= 0.09
BuildRequires: perl(Module::Load::Conditional)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Set::Scalar)
BuildRequires: perl(Storable)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::JSON)
#BuildRequires: perl(Test::More) >= 0.88
BuildRequires: perl(Test::More) 
BuildRequires: perl(Text::CSV)
BuildRequires: perl(Text::Table)
BuildRequires: perl(Time::HiRes)
BuildRequires: perl(URI) >= 1.52
BuildRequires: perl(Unicode::Escape)
BuildRequires: perl(Unicode::String) >= 2.09
BuildRequires: perl(XML::CommonNS) >= 0.04
BuildRequires: perl(XML::LibXML) >= 1.7
BuildRequires: perl(XML::Namespace)
BuildRequires: perl(XML::SAX)
BuildRequires: perl >= v5.8.3
Requires: perl(DBD::SQLite) >= 1.14
Requires: perl(DBI)
Requires: perl(Data::UUID)
Requires: perl(Digest::MD5)
Requires: perl(Digest::SHA1)
Requires: perl(Error)
Requires: perl(HTTP::Negotiate)
Requires: perl(JSON) >= 2
Requires: perl(LWP::UserAgent)
Requires: perl(List::MoreUtils)
Requires: perl(List::Util)
Requires: perl(Log::Log4perl)
Requires: perl(Math::BigInt)
Requires: perl(Math::Combinatorics) >= 0.09
Requires: perl(Module::Load::Conditional)
Requires: perl(Scalar::Util)
Requires: perl(Set::Scalar)
Requires: perl(Storable)
Requires: perl(Text::CSV)
Requires: perl(Text::Table)
Requires: perl(Time::HiRes)
Requires: perl(URI) >= 1.52
Requires: perl(Unicode::Escape)
Requires: perl(Unicode::String) >= 2.09
Requires: perl(XML::CommonNS) >= 0.04
Requires: perl(XML::LibXML) >= 1.7
Requires: perl(XML::Namespace)
Requires: perl(XML::SAX)
Requires: perl >= v5.8.3

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup


%description


%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc MANIFEST META.yml README
%doc %{_mandir}/man3/RDF::Trine.3pm*
%doc %{_mandir}/man3/RDF::Trine::Error.3pm.gz
%doc %{_mandir}/man3/RDF::Trine::Exporter::CSV.3pm.gz
%doc %{_mandir}/man3/RDF::Trine::Graph.3pm.gz
%doc %{_mandir}/man3/RDF::Trine::Iterator.3pm.gz
%doc %{_mandir}/man3/RDF::Trine::Iterator::Bindings.3pm.gz
%doc %{_mandir}/man3/RDF::Trine::Iterator::Bindings::Materialized.3pm.gz
%doc %{_mandir}/man3/RDF::Trine::Iterator::Boolean.3pm.gz
%doc %{_mandir}/man3/RDF::Trine::Iterator::Graph.3pm.gz
%doc %{_mandir}/man3/RDF::Trine::Iterator::Graph::Materialized.3pm.gz
%doc %{_mandir}/man3/RDF::Trine::Iterator::SAXHandler.3pm.gz
%doc %{_mandir}/man3/RDF::Trine::Model.3pm.gz
%doc %{_mandir}/man3/RDF::Trine::Model::Dataset.3pm.gz
%doc %{_mandir}/man3/RDF::Trine::Model::StatementFilter.3pm.gz
%doc %{_mandir}/man3/RDF::Trine::Model::Union.3pm.gz
%doc %{_mandir}/man3/RDF::Trine::Namespace.3pm.gz
%doc %{_mandir}/man3/RDF::Trine::Node.3pm.gz
%doc %{_mandir}/man3/RDF::Trine::Node::Blank.3pm.gz
%doc %{_mandir}/man3/RDF::Trine::Node::Literal.3pm.gz
%doc %{_mandir}/man3/RDF::Trine::Node::Nil.3pm.gz
%doc %{_mandir}/man3/RDF::Trine::Node::Resource.3pm.gz
%doc %{_mandir}/man3/RDF::Trine::Node::Variable.3pm.gz
%doc %{_mandir}/man3/RDF::Trine::Parser.3pm.gz
%doc %{_mandir}/man3/RDF::Trine::Parser::NQuads.3pm.gz
%doc %{_mandir}/man3/RDF::Trine::Parser::NTriples.3pm.gz
%doc %{_mandir}/man3/RDF::Trine::Parser::RDFJSON.3pm.gz
%doc %{_mandir}/man3/RDF::Trine::Parser::RDFXML.3pm.gz
%doc %{_mandir}/man3/RDF::Trine::Parser::RDFa.3pm.gz
%doc %{_mandir}/man3/RDF::Trine::Parser::Redland.3pm.gz
%doc %{_mandir}/man3/RDF::Trine::Parser::TriG.3pm.gz
%doc %{_mandir}/man3/RDF::Trine::Parser::Turtle.3pm.gz
%doc %{_mandir}/man3/RDF::Trine::Pattern.3pm.gz
%doc %{_mandir}/man3/RDF::Trine::Serializer.3pm.gz
%doc %{_mandir}/man3/RDF::Trine::Serializer::NQuads.3pm.gz
%doc %{_mandir}/man3/RDF::Trine::Serializer::NTriples.3pm.gz
%doc %{_mandir}/man3/RDF::Trine::Serializer::NTriples::Canonical.3pm.gz
%doc %{_mandir}/man3/RDF::Trine::Serializer::RDFJSON.3pm.gz
%doc %{_mandir}/man3/RDF::Trine::Serializer::RDFXML.3pm.gz
%doc %{_mandir}/man3/RDF::Trine::Serializer::Turtle.3pm.gz
%doc %{_mandir}/man3/RDF::Trine::Statement.3pm.gz
%doc %{_mandir}/man3/RDF::Trine::Statement::Quad.3pm.gz
%doc %{_mandir}/man3/RDF::Trine::Store.3pm.gz
%doc %{_mandir}/man3/RDF::Trine::Store::DBI.3pm.gz
%doc %{_mandir}/man3/RDF::Trine::Store::DBI::Pg.3pm.gz
%doc %{_mandir}/man3/RDF::Trine::Store::DBI::SQLite.3pm.gz
%doc %{_mandir}/man3/RDF::Trine::Store::DBI::mysql.3pm.gz
%doc %{_mandir}/man3/RDF::Trine::Store::Hexastore.3pm.gz
%doc %{_mandir}/man3/RDF::Trine::Store::Memory.3pm.gz
%doc %{_mandir}/man3/RDF::Trine::Store::Redland.3pm.gz
%doc %{_mandir}/man3/RDF::Trine::Store::SPARQL.3pm.gz
%doc %{_mandir}/man3/RDF::Trine::VariableBindings.3pm.gz
%dir %{perl_vendorlib}/
%{perl_vendorlib}/RDF/Trine.pm
%{perl_vendorlib}/RDF/Trine/Error.pm
%{perl_vendorlib}/RDF/Trine/Exporter/CSV.pm
%{perl_vendorlib}/RDF/Trine/Graph.pm
%{perl_vendorlib}/RDF/Trine/Iterator.pm
%{perl_vendorlib}/RDF/Trine/Iterator/Bindings.pm
%{perl_vendorlib}/RDF/Trine/Iterator/Bindings/Materialized.pm
%{perl_vendorlib}/RDF/Trine/Iterator/Boolean.pm
%{perl_vendorlib}/RDF/Trine/Iterator/Graph.pm
%{perl_vendorlib}/RDF/Trine/Iterator/Graph/Materialized.pm
%{perl_vendorlib}/RDF/Trine/Iterator/SAXHandler.pm
%{perl_vendorlib}/RDF/Trine/Model.pm
%{perl_vendorlib}/RDF/Trine/Model/Dataset.pm
%{perl_vendorlib}/RDF/Trine/Model/StatementFilter.pm
%{perl_vendorlib}/RDF/Trine/Model/Union.pm
%{perl_vendorlib}/RDF/Trine/Namespace.pm
%{perl_vendorlib}/RDF/Trine/Node.pm
%{perl_vendorlib}/RDF/Trine/Node/Blank.pm
%{perl_vendorlib}/RDF/Trine/Node/Literal.pm
%{perl_vendorlib}/RDF/Trine/Node/Nil.pm
%{perl_vendorlib}/RDF/Trine/Node/Resource.pm
%{perl_vendorlib}/RDF/Trine/Node/Variable.pm
%{perl_vendorlib}/RDF/Trine/Parser.pm
%{perl_vendorlib}/RDF/Trine/Parser/NQuads.pm
%{perl_vendorlib}/RDF/Trine/Parser/NTriples.pm
%{perl_vendorlib}/RDF/Trine/Parser/RDFJSON.pm
%{perl_vendorlib}/RDF/Trine/Parser/RDFXML.pm
%{perl_vendorlib}/RDF/Trine/Parser/RDFa.pm
%{perl_vendorlib}/RDF/Trine/Parser/Redland.pm
%{perl_vendorlib}/RDF/Trine/Parser/TriG.pm
%{perl_vendorlib}/RDF/Trine/Parser/Turtle.pm
%{perl_vendorlib}/RDF/Trine/Pattern.pm
%{perl_vendorlib}/RDF/Trine/Serializer.pm
%{perl_vendorlib}/RDF/Trine/Serializer/NQuads.pm
%{perl_vendorlib}/RDF/Trine/Serializer/NTriples.pm
%{perl_vendorlib}/RDF/Trine/Serializer/NTriples/Canonical.pm
%{perl_vendorlib}/RDF/Trine/Serializer/RDFJSON.pm
%{perl_vendorlib}/RDF/Trine/Serializer/RDFXML.pm
%{perl_vendorlib}/RDF/Trine/Serializer/Turtle.pm
%{perl_vendorlib}/RDF/Trine/Statement.pm
%{perl_vendorlib}/RDF/Trine/Statement/Quad.pm
%{perl_vendorlib}/RDF/Trine/Store.pm
%{perl_vendorlib}/RDF/Trine/Store/DBI.pm
%{perl_vendorlib}/RDF/Trine/Store/DBI/Pg.pm
%{perl_vendorlib}/RDF/Trine/Store/DBI/SQLite.pm
%{perl_vendorlib}/RDF/Trine/Store/DBI/mysql.pm
%{perl_vendorlib}/RDF/Trine/Store/Hexastore.pm
%{perl_vendorlib}/RDF/Trine/Store/Memory.pm
%{perl_vendorlib}/RDF/Trine/Store/Redland.pm
%{perl_vendorlib}/RDF/Trine/Store/SPARQL.pm
%{perl_vendorlib}/RDF/Trine/VariableBindings.pm

%exclude %{perl_vendorarch}/auto/*/*/.packlist

%changelog
* Mon Mar 26 2012 Steve Huff <shuff@vecna.org> - 0.132-2
- Rebuild as RFX.

* Mon Feb 07 2011 Christoph Maser <cmaser.gmx.de> - 0.132-1
- initial package
