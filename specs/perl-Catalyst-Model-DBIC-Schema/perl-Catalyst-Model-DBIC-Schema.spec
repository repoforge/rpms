# $Id$
# Authority: dag
# Upstream: Rafael Kitover <rkitover@io.com>
# ExcludeDist: el4

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Catalyst-Model-DBIC-Schema

Summary: DBIx::Class::Schema Model Class
Name: perl-Catalyst-Model-DBIC-Schema
Version: 0.40
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Catalyst-Model-DBIC-Schema/

Source: http://search.cpan.org/CPAN/authors/id/R/RK/RKITOVER/Catalyst-Model-DBIC-Schema-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Carp::Clan)
BuildRequires: perl(Catalyst::Runtime) >= 5.80005
BuildRequires: perl(CatalystX::Component::Traits) >= 0.14
BuildRequires: perl(DBIx::Class) >= 0.08114
#BuildRequires: perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(List::MoreUtils)
BuildRequires: perl(Moose) >= 0.90
BuildRequires: perl(MooseX::Types)
BuildRequires: perl(Test::Exception)
#BuildRequires: perl(Test::More) >= 0.92
BuildRequires: perl(Test::More)
BuildRequires: perl(Tie::IxHash)
BuildRequires: perl(namespace::autoclean)
BuildRequires: perl >= 5.8.1
Requires: perl(Carp::Clan)
Requires: perl(Catalyst::Runtime) >= 5.80005
Requires: perl(CatalystX::Component::Traits) >= 0.14
Requires: perl(DBIx::Class) >= 0.08114
Requires: perl(List::MoreUtils)
Requires: perl(Moose) >= 0.90
Requires: perl(MooseX::Types)
Requires: perl(Tie::IxHash)
Requires: perl(namespace::autoclean)
Requires: perl >= 5.8.1

# Catalyst::Helper support
BuildRequires: perl(Catalyst::Devel) >= 1.0
BuildRequires: perl(DBIx::Class::Schema::Loader) >= 0.04005
Requires: perl(Catalyst::Devel) >= 1.0
Requires: perl(DBIx::Class::Schema::Loader) >= 0.04005
# Caching support
#BuildRequires: perl(DBIx::Class::Cursor::Cached)
#Requires: perl(DBIx::Class::Cursor::Cached)
# Replication support
BuildRequires: perl(MooseX::AttributeHelpers)
BuildRequires: perl(Hash::Merge)
Requires: perl(MooseX::AttributeHelpers)
Requires: perl(Hash::Merge)

%filter_from_requires /^perl*/d
%filter_setup


%description
DBIx::Class::Schema Model Class.

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Catalyst::Helper::Model::DBIC::Schema.3pm*
%doc %{_mandir}/man3/Catalyst::Model::DBIC::Schema.3pm*
%doc %{_mandir}/man3/Catalyst::TraitFor::Model::DBIC::Schema::Caching.3pm.*
%doc %{_mandir}/man3/Catalyst::TraitFor::Model::DBIC::Schema::Replicated.3pm*
%doc %{_mandir}/man3/Catalyst::TraitFor::Model::DBIC::Schema::SchemaProxy.3pm*
%dir %{perl_vendorlib}/Catalyst/
%dir %{perl_vendorlib}/Catalyst/Helper/Model/DBIC/Schema.pm
%dir %{perl_vendorlib}/Catalyst/Model/
%dir %{perl_vendorlib}/Catalyst/Model/DBIC/
%dir %{perl_vendorlib}/Catalyst/Model/DBIC/Schema/Types.pm
%{perl_vendorlib}/Catalyst/Model/DBIC/Schema.pm
%{perl_vendorlib}/Catalyst/TraitFor/Model/DBIC/Schema/Caching.pm
%{perl_vendorlib}/Catalyst/TraitFor/Model/DBIC/Schema/Replicated.pm
%{perl_vendorlib}/Catalyst/TraitFor/Model/DBIC/Schema/SchemaProxy.pm


%changelog
* Sat Feb  6 2010 Christoph Maser <cmr@financial.com> - 0.40-1
- Updated to version 0.40.

* Thu Jan 14 2010 Christoph Maser <cmr@financial.com> - 0.35-1
- Updated to version 0.35.

* Tue Oct 07 2008 Dag Wieers <dag@wieers.com> - 0.21-1
- Updated to release 0.21.

* Sun Dec 30 2007 Dag Wieers <dag@wieers.com> - 0.20-1
- Initial package. (using DAR)
