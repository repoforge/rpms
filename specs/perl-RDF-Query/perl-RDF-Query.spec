# $Id$
# Upstream: Gregory Todd Williams <gwilliams@cpan.org>
# Tag: rfx

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)
%define real_name RDF-Query

Summary: An RDF query implementation of SPARQL/RDQL in Perl for use with RDF::Trine.
Name: perl-RDF-Query
Version: 2.904
Release: 2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/RDF-Query/

Source: http://search.cpan.org/CPAN/authors/id/G/GW/GWILLIAMS/RDF-Query-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl(Data::UUID)
BuildRequires: perl(DateTime::Format::W3CDTF)
BuildRequires: perl(Digest::SHA1)
BuildRequires: perl(Error)
#BuildRequires: perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires: perl(ExtUtils::MakeMaker) 
BuildRequires: perl(File::Spec)
BuildRequires: perl(File::Temp)
BuildRequires: perl(FindBin)
BuildRequires: perl(I18N::LangTags)
BuildRequires: perl(JSON) >= 2
BuildRequires: perl(Module::Pluggable)
BuildRequires: perl(Parse::RecDescent)
BuildRequires: perl(RDF::Trine) >= 0.126
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Set::Scalar)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::JSON)
BuildRequires: perl(Test::More) >= 0.61
BuildRequires: perl(URI) >= 1.52
BuildRequires: perl(YAML)
Requires: perl(Data::UUID)
Requires: perl(DateTime::Format::W3CDTF)
Requires: perl(Digest::SHA1)
Requires: perl(Error)
Requires: perl(File::Spec)
Requires: perl(File::Temp)
Requires: perl(I18N::LangTags)
Requires: perl(JSON) >= 2
Requires: perl(Parse::RecDescent)
Requires: perl(RDF::Trine) >= 0.126
Requires: perl(Scalar::Util)
Requires: perl(Set::Scalar)
Requires: perl(URI) >= 1.52

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup


%description


%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}
%{__make} %{?_smp_mflags} test

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc MANIFEST META.yml README
%doc %{_mandir}/man3/RDF::Query.3pm*
%doc %{_mandir}/man3/RDF::Query::Algebra.3pm.gz
%doc %{_mandir}/man3/RDF::Query::Algebra::Aggregate.3pm.gz
%doc %{_mandir}/man3/RDF::Query::Algebra::BasicGraphPattern.3pm.gz
%doc %{_mandir}/man3/RDF::Query::Algebra::Clear.3pm.gz
%doc %{_mandir}/man3/RDF::Query::Algebra::Construct.3pm.gz
%doc %{_mandir}/man3/RDF::Query::Algebra::Create.3pm.gz
%doc %{_mandir}/man3/RDF::Query::Algebra::Distinct.3pm.gz
%doc %{_mandir}/man3/RDF::Query::Algebra::Extend.3pm.gz
%doc %{_mandir}/man3/RDF::Query::Algebra::Filter.3pm.gz
%doc %{_mandir}/man3/RDF::Query::Algebra::GroupGraphPattern.3pm.gz
%doc %{_mandir}/man3/RDF::Query::Algebra::Limit.3pm.gz
%doc %{_mandir}/man3/RDF::Query::Algebra::Load.3pm.gz
%doc %{_mandir}/man3/RDF::Query::Algebra::Minus.3pm.gz
%doc %{_mandir}/man3/RDF::Query::Algebra::NamedGraph.3pm.gz
%doc %{_mandir}/man3/RDF::Query::Algebra::Offset.3pm.gz
%doc %{_mandir}/man3/RDF::Query::Algebra::Optional.3pm.gz
%doc %{_mandir}/man3/RDF::Query::Algebra::Path.3pm.gz
%doc %{_mandir}/man3/RDF::Query::Algebra::Project.3pm.gz
%doc %{_mandir}/man3/RDF::Query::Algebra::Quad.3pm.gz
%doc %{_mandir}/man3/RDF::Query::Algebra::Sequence.3pm.gz
%doc %{_mandir}/man3/RDF::Query::Algebra::Service.3pm.gz
%doc %{_mandir}/man3/RDF::Query::Algebra::Sort.3pm.gz
%doc %{_mandir}/man3/RDF::Query::Algebra::SubSelect.3pm.gz
%doc %{_mandir}/man3/RDF::Query::Algebra::TimeGraph.3pm.gz
%doc %{_mandir}/man3/RDF::Query::Algebra::Triple.3pm.gz
%doc %{_mandir}/man3/RDF::Query::Algebra::Union.3pm.gz
%doc %{_mandir}/man3/RDF::Query::Algebra::Update.3pm.gz
%doc %{_mandir}/man3/RDF::Query::BGPOptimizer.3pm.gz
%doc %{_mandir}/man3/RDF::Query::Compiler::SQL.3pm.gz
%doc %{_mandir}/man3/RDF::Query::Error.3pm.gz
%doc %{_mandir}/man3/RDF::Query::ExecutionContext.3pm.gz
%doc %{_mandir}/man3/RDF::Query::Expression.3pm.gz
%doc %{_mandir}/man3/RDF::Query::Expression::Alias.3pm.gz
%doc %{_mandir}/man3/RDF::Query::Expression::Binary.3pm.gz
%doc %{_mandir}/man3/RDF::Query::Expression::Function.3pm.gz
%doc %{_mandir}/man3/RDF::Query::Expression::Nary.3pm.gz
%doc %{_mandir}/man3/RDF::Query::Expression::Unary.3pm.gz
%doc %{_mandir}/man3/RDF::Query::Federate.3pm.gz
%doc %{_mandir}/man3/RDF::Query::Federate::Plan.3pm.gz
%doc %{_mandir}/man3/RDF::Query::Functions.3pm.gz
%doc %{_mandir}/man3/RDF::Query::Functions::Geo.3pm.gz
%doc %{_mandir}/man3/RDF::Query::Functions::Jena.3pm.gz
%doc %{_mandir}/man3/RDF::Query::Functions::Kasei.3pm.gz
%doc %{_mandir}/man3/RDF::Query::Functions::SPARQL.3pm.gz
%doc %{_mandir}/man3/RDF::Query::Functions::Xpath.3pm.gz
%doc %{_mandir}/man3/RDF::Query::Node.3pm.gz
%doc %{_mandir}/man3/RDF::Query::Node::Blank.3pm.gz
%doc %{_mandir}/man3/RDF::Query::Node::Literal.3pm.gz
%doc %{_mandir}/man3/RDF::Query::Node::Resource.3pm.gz
%doc %{_mandir}/man3/RDF::Query::Node::Variable.3pm.gz
%doc %{_mandir}/man3/RDF::Query::Parser.3pm.gz
%doc %{_mandir}/man3/RDF::Query::Parser::RDQL.3pm.gz
%doc %{_mandir}/man3/RDF::Query::Parser::SPARQL.3pm.gz
%doc %{_mandir}/man3/RDF::Query::Parser::SPARQL11.3pm.gz
%doc %{_mandir}/man3/RDF::Query::Plan.3pm.gz
%doc %{_mandir}/man3/RDF::Query::Plan::Aggregate.3pm.gz
%doc %{_mandir}/man3/RDF::Query::Plan::BasicGraphPattern.3pm.gz
%doc %{_mandir}/man3/RDF::Query::Plan::Clear.3pm.gz
%doc %{_mandir}/man3/RDF::Query::Plan::ComputedStatement.3pm.gz
%doc %{_mandir}/man3/RDF::Query::Plan::Constant.3pm.gz
%doc %{_mandir}/man3/RDF::Query::Plan::Construct.3pm.gz
%doc %{_mandir}/man3/RDF::Query::Plan::Distinct.3pm.gz
%doc %{_mandir}/man3/RDF::Query::Plan::Extend.3pm.gz
%doc %{_mandir}/man3/RDF::Query::Plan::Filter.3pm.gz
%doc %{_mandir}/man3/RDF::Query::Plan::Iterator.3pm.gz
%doc %{_mandir}/man3/RDF::Query::Plan::Join.3pm.gz
%doc %{_mandir}/man3/RDF::Query::Plan::Join::NestedLoop.3pm.gz
%doc %{_mandir}/man3/RDF::Query::Plan::Join::PushDownNestedLoop.3pm.gz
%doc %{_mandir}/man3/RDF::Query::Plan::Limit.3pm.gz
%doc %{_mandir}/man3/RDF::Query::Plan::Load.3pm.gz
%doc %{_mandir}/man3/RDF::Query::Plan::Minus.3pm.gz
%doc %{_mandir}/man3/RDF::Query::Plan::NamedGraph.3pm.gz
%doc %{_mandir}/man3/RDF::Query::Plan::Offset.3pm.gz
%doc %{_mandir}/man3/RDF::Query::Plan::Path.3pm.gz
%doc %{_mandir}/man3/RDF::Query::Plan::Project.3pm.gz
%doc %{_mandir}/man3/RDF::Query::Plan::Quad.3pm.gz
%doc %{_mandir}/man3/RDF::Query::Plan::Sequence.3pm.gz
%doc %{_mandir}/man3/RDF::Query::Plan::Service.3pm.gz
%doc %{_mandir}/man3/RDF::Query::Plan::Sort.3pm.gz
%doc %{_mandir}/man3/RDF::Query::Plan::SubSelect.3pm.gz
%doc %{_mandir}/man3/RDF::Query::Plan::ThresholdUnion.3pm.gz
%doc %{_mandir}/man3/RDF::Query::Plan::Triple.3pm.gz
%doc %{_mandir}/man3/RDF::Query::Plan::Union.3pm.gz
%doc %{_mandir}/man3/RDF::Query::Plan::Update.3pm.gz
%doc %{_mandir}/man3/RDF::Query::ServiceDescription.3pm.gz
%doc %{_mandir}/man3/RDF::Query::Temporal.3pm.gz
%doc %{_mandir}/man3/RDF::Query::Util.3pm.gz
%doc %{_mandir}/man3/RDF::Query::VariableBindings.3pm.gz
%dir %{perl_vendorlib}/
%{_bindir}/rqsh
%{perl_vendorlib}/RDF/Query.pm
%{perl_vendorlib}/RDF/Query/Algebra.pm
%{perl_vendorlib}/RDF/Query/Algebra/Aggregate.pm
%{perl_vendorlib}/RDF/Query/Algebra/BasicGraphPattern.pm
%{perl_vendorlib}/RDF/Query/Algebra/Clear.pm
%{perl_vendorlib}/RDF/Query/Algebra/Construct.pm
%{perl_vendorlib}/RDF/Query/Algebra/Create.pm
%{perl_vendorlib}/RDF/Query/Algebra/Distinct.pm
%{perl_vendorlib}/RDF/Query/Algebra/Extend.pm
%{perl_vendorlib}/RDF/Query/Algebra/Filter.pm
%{perl_vendorlib}/RDF/Query/Algebra/GroupGraphPattern.pm
%{perl_vendorlib}/RDF/Query/Algebra/Limit.pm
%{perl_vendorlib}/RDF/Query/Algebra/Load.pm
%{perl_vendorlib}/RDF/Query/Algebra/Minus.pm
%{perl_vendorlib}/RDF/Query/Algebra/NamedGraph.pm
%{perl_vendorlib}/RDF/Query/Algebra/Offset.pm
%{perl_vendorlib}/RDF/Query/Algebra/Optional.pm
%{perl_vendorlib}/RDF/Query/Algebra/Path.pm
%{perl_vendorlib}/RDF/Query/Algebra/Project.pm
%{perl_vendorlib}/RDF/Query/Algebra/Quad.pm
%{perl_vendorlib}/RDF/Query/Algebra/Sequence.pm
%{perl_vendorlib}/RDF/Query/Algebra/Service.pm
%{perl_vendorlib}/RDF/Query/Algebra/Sort.pm
%{perl_vendorlib}/RDF/Query/Algebra/SubSelect.pm
%{perl_vendorlib}/RDF/Query/Algebra/TimeGraph.pm
%{perl_vendorlib}/RDF/Query/Algebra/Triple.pm
%{perl_vendorlib}/RDF/Query/Algebra/Union.pm
%{perl_vendorlib}/RDF/Query/Algebra/Update.pm
%{perl_vendorlib}/RDF/Query/BGPOptimizer.pm
%{perl_vendorlib}/RDF/Query/Compiler/SQL.pm
%{perl_vendorlib}/RDF/Query/Error.pm
%{perl_vendorlib}/RDF/Query/ExecutionContext.pm
%{perl_vendorlib}/RDF/Query/Expression.pm
%{perl_vendorlib}/RDF/Query/Expression/Alias.pm
%{perl_vendorlib}/RDF/Query/Expression/Binary.pm
%{perl_vendorlib}/RDF/Query/Expression/Function.pm
%{perl_vendorlib}/RDF/Query/Expression/Nary.pm
%{perl_vendorlib}/RDF/Query/Expression/Unary.pm
%{perl_vendorlib}/RDF/Query/Federate.pm
%{perl_vendorlib}/RDF/Query/Federate/Plan.pm
%{perl_vendorlib}/RDF/Query/Functions.pm
%{perl_vendorlib}/RDF/Query/Functions/Geo.pm
%{perl_vendorlib}/RDF/Query/Functions/Jena.pm
%{perl_vendorlib}/RDF/Query/Functions/Kasei.pm
%{perl_vendorlib}/RDF/Query/Functions/SPARQL.pm
%{perl_vendorlib}/RDF/Query/Functions/Xpath.pm
%{perl_vendorlib}/RDF/Query/Node.pm
%{perl_vendorlib}/RDF/Query/Node/Blank.pm
%{perl_vendorlib}/RDF/Query/Node/Literal.pm
%{perl_vendorlib}/RDF/Query/Node/Resource.pm
%{perl_vendorlib}/RDF/Query/Node/Variable.pm
%{perl_vendorlib}/RDF/Query/Parser.pm
%{perl_vendorlib}/RDF/Query/Parser/RDQL.pm
%{perl_vendorlib}/RDF/Query/Parser/SPARQL.pm
%{perl_vendorlib}/RDF/Query/Parser/SPARQL11.pm
%{perl_vendorlib}/RDF/Query/Plan.pm
%{perl_vendorlib}/RDF/Query/Plan/Aggregate.pm
%{perl_vendorlib}/RDF/Query/Plan/BasicGraphPattern.pm
%{perl_vendorlib}/RDF/Query/Plan/Clear.pm
%{perl_vendorlib}/RDF/Query/Plan/ComputedStatement.pm
%{perl_vendorlib}/RDF/Query/Plan/Constant.pm
%{perl_vendorlib}/RDF/Query/Plan/Construct.pm
%{perl_vendorlib}/RDF/Query/Plan/Distinct.pm
%{perl_vendorlib}/RDF/Query/Plan/Extend.pm
%{perl_vendorlib}/RDF/Query/Plan/Filter.pm
%{perl_vendorlib}/RDF/Query/Plan/Iterator.pm
%{perl_vendorlib}/RDF/Query/Plan/Join.pm
%{perl_vendorlib}/RDF/Query/Plan/Join/NestedLoop.pm
%{perl_vendorlib}/RDF/Query/Plan/Join/PushDownNestedLoop.pm
%{perl_vendorlib}/RDF/Query/Plan/Limit.pm
%{perl_vendorlib}/RDF/Query/Plan/Load.pm
%{perl_vendorlib}/RDF/Query/Plan/Minus.pm
%{perl_vendorlib}/RDF/Query/Plan/NamedGraph.pm
%{perl_vendorlib}/RDF/Query/Plan/Offset.pm
%{perl_vendorlib}/RDF/Query/Plan/Path.pm
%{perl_vendorlib}/RDF/Query/Plan/Project.pm
%{perl_vendorlib}/RDF/Query/Plan/Quad.pm
%{perl_vendorlib}/RDF/Query/Plan/Sequence.pm
%{perl_vendorlib}/RDF/Query/Plan/Service.pm
%{perl_vendorlib}/RDF/Query/Plan/Sort.pm
%{perl_vendorlib}/RDF/Query/Plan/SubSelect.pm
%{perl_vendorlib}/RDF/Query/Plan/ThresholdUnion.pm
%{perl_vendorlib}/RDF/Query/Plan/Triple.pm
%{perl_vendorlib}/RDF/Query/Plan/Union.pm
%{perl_vendorlib}/RDF/Query/Plan/Update.pm
%{perl_vendorlib}/RDF/Query/ServiceDescription.pm
%{perl_vendorlib}/RDF/Query/Temporal.pm
%{perl_vendorlib}/RDF/Query/Util.pm
%{perl_vendorlib}/RDF/Query/VariableBindings.pm

%exclude %{perl_vendorarch}/auto/*/*/.packlist

%changelog
* Mon Mar 26 2012 Steve Huff <shuff@vecna.org> - 2.904-2
- Rebuild as RFX.

* Mon Feb 07 2011 Christoph Maser <cmaser.gmx.de> - 2.904-1
- initial package
