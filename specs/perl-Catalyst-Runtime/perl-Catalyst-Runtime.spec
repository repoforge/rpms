# $Id$
# Authority: dag
# Upstream: Tomas Doran <bobtfish@bobtfish.net>
# Needs new MooseX::*
# ExcludeDist: el4

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Catalyst-Runtime

Summary: Catalyst  Runtime version
Name: perl-Catalyst-Runtime
Version: 5.80016
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Catalyst-Runtime/

Source: http://search.cpan.org/CPAN/authors/id/B/BO/BOBTFISH/Catalyst-Runtime-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(B::Hooks::EndOfScope) >= 0.08
BuildRequires: perl(CGI::Simple::Cookie)
BuildRequires: perl(Carp)
BuildRequires: perl(Class::C3::Adopt::NEXT) >= 0.07
BuildRequires: perl(Class::Data::Inheritable)
BuildRequires: perl(Class::MOP) >= 0.95
BuildRequires: perl(Data::Dump)
#BuildRequires: perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(HTML::Entities)
BuildRequires: perl(HTTP::Body) >= 1.04
BuildRequires: perl(HTTP::Headers) >= 1.64
BuildRequires: perl(HTTP::Request) >= 5.814
BuildRequires: perl(HTTP::Request::AsCGI) >= 1.0
BuildRequires: perl(HTTP::Response) >= 5.813
BuildRequires: perl(LWP::UserAgent)
BuildRequires: perl(List::MoreUtils)
BuildRequires: perl(MRO::Compat)
BuildRequires: perl(Module::Pluggable) >= 3.9
BuildRequires: perl(Moose) >= 0.93
BuildRequires: perl(MooseX::Emulate::Class::Accessor::Fast) >= 0.00903
BuildRequires: perl(MooseX::Getopt) >= 0.25
BuildRequires: perl(MooseX::MethodAttributes::Inheritable) >= 0.17
BuildRequires: perl(MooseX::Role::WithOverloading) >= 0.03
BuildRequires: perl(MooseX::Types)
BuildRequires: perl(MooseX::Types::Common::Numeric)
BuildRequires: perl(Path::Class) >= 0.09
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(String::RewritePrefix) >= 0.004
BuildRequires: perl(Sub::Exporter)
BuildRequires: perl(Task::Weaken)
BuildRequires: perl(Test::Exception)
#BuildRequires: perl(Test::More) >= 0.88
BuildRequires: perl(Test::More)
BuildRequires: perl(Text::Balanced)
BuildRequires: perl(Text::SimpleTable) >= 0.03
BuildRequires: perl(Time::HiRes)
BuildRequires: perl(Tree::Simple) >= 1.15
BuildRequires: perl(Tree::Simple::Visitor::FindByPath)
BuildRequires: perl(URI) >= 1.35
BuildRequires: perl(namespace::autoclean)
BuildRequires: perl(namespace::clean)
BuildRequires: perl >= 5.8.4
Requires: perl(B::Hooks::EndOfScope) >= 0.08
Requires: perl(CGI::Simple::Cookie)
Requires: perl(Carp)
Requires: perl(Class::C3::Adopt::NEXT) >= 0.07
Requires: perl(Class::MOP) >= 0.95
Requires: perl(Data::Dump)
Requires: perl(HTML::Entities)
Requires: perl(HTTP::Body) >= 1.04
Requires: perl(HTTP::Headers) >= 1.64
Requires: perl(HTTP::Request) >= 5.814
Requires: perl(HTTP::Request::AsCGI) >= 1.0
Requires: perl(HTTP::Response) >= 5.813
Requires: perl(LWP::UserAgent)
Requires: perl(List::MoreUtils)
Requires: perl(MRO::Compat)
Requires: perl(Module::Pluggable) >= 3.9
Requires: perl(Moose) >= 0.93
Requires: perl(MooseX::Emulate::Class::Accessor::Fast) >= 0.00903
Requires: perl(MooseX::Getopt) >= 0.25
Requires: perl(MooseX::MethodAttributes::Inheritable) >= 0.17
Requires: perl(MooseX::Role::WithOverloading) >= 0.03
Requires: perl(MooseX::Types)
Requires: perl(MooseX::Types::Common::Numeric)
Requires: perl(Path::Class) >= 0.09
Requires: perl(Scalar::Util)
Requires: perl(String::RewritePrefix) >= 0.004
Requires: perl(Sub::Exporter)
Requires: perl(Task::Weaken)
Requires: perl(Text::Balanced)
Requires: perl(Text::SimpleTable) >= 0.03
Requires: perl(Time::HiRes)
Requires: perl(Tree::Simple) >= 1.15
Requires: perl(Tree::Simple::Visitor::FindByPath)
Requires: perl(URI) >= 1.35
Requires: perl(namespace::autoclean)
Requires: perl(namespace::clean)
Requires: perl >= 5.8.4

%filter_from_requires /^perl*/d
%filter_setup



%description
Catalyst Runtime version.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}" --skipdeps
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
%doc Changes MANIFEST META.yml
%doc %{_mandir}/man1/catalyst.pl.1*
%doc %{_mandir}/man3/Catalyst.3pm*
%doc %{_mandir}/man3/Catalyst::*.3pm*
%{_bindir}/catalyst.pl
%{perl_vendorlib}/Catalyst/
%{perl_vendorlib}/Catalyst.pm

%changelog
* Fri Jan  8 2010 Christoph Maser <cmr@financial.com> - 5.80016-1
- Updated to version 5.80016.

* Sat Aug 22 2009 Christoph Maser <cmr@financial.com> - 5.80010-1
- Updated to version 5.80010.

* Thu Dec 18 2008 Dag Wieers <dag@wieers.com> - 5.7015-1
- Updated to release 5.7015.

* Sun Jun 22 2008 Dag Wieers <dag@wieers.com> - 5.7014-1
- Updated to release 5.7014.

* Thu Dec 27 2007 Dag Wieers <dag@wieers.com> - 5.7012-1
- Updated to release 5.7012.

* Tue Nov 06 2007 Dag Wieers <dag@wieers.com> - 5.7011-1
- Updated to release 5.7011.

* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 5.7007-1
- Initial package. (using DAR)
