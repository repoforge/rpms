# $Id$
# Authority: dag
# Upstream: Rafael Kitover <rkitover@io.com>
# ExcludeDist: el4

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Catalyst-Plugin-Authorization-ACL

Summary: ACL support for Catalyst applications
Name: perl-Catalyst-Plugin-Authorization-ACL
Version: 0.15
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Catalyst-Plugin-Authorization-ACL/

Source: http://search.cpan.org/CPAN/authors/id/R/RK/RKITOVER/Catalyst-Plugin-Authorization-ACL-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Catalyst::Plugin::Authentication)
BuildRequires: perl(Catalyst::Plugin::Authorization::Roles)
BuildRequires: perl(Catalyst::Plugin::Session)
BuildRequires: perl(Catalyst::Plugin::Session::State::Cookie)
BuildRequires: perl(Catalyst::Runtime) >= 5.80013
BuildRequires: perl(Class::Data::Inheritable)
BuildRequires: perl(Class::Throwable)
#BuildRequires: perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(MRO::Compat)
BuildRequires: perl(Moose)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::WWW::Mechanize::Catalyst)
BuildRequires: perl(Tree::Simple)
BuildRequires: perl(Tree::Simple::Visitor::FindByPath)
BuildRequires: perl(Tree::Simple::Visitor::GetAllDescendents)
BuildRequires: perl(namespace::autoclean)
BuildRequires: perl >= 5.8.0
Requires: perl(Catalyst::Plugin::Authentication)
Requires: perl(Catalyst::Plugin::Authorization::Roles)
Requires: perl(Catalyst::Runtime) >= 5.80013
Requires: perl(Class::Data::Inheritable)
Requires: perl(Class::Throwable)
Requires: perl(MRO::Compat)
Requires: perl(Moose)
Requires: perl(Tree::Simple)
Requires: perl(Tree::Simple::Visitor::FindByPath)
Requires: perl(Tree::Simple::Visitor::GetAllDescendents)
Requires: perl(namespace::autoclean)
Requires: perl >= 5.8.0

%filter_from_requires /^perl*/d
%filter_setup


%description
ACL support for Catalyst applications.

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
%doc %{_mandir}/man3/Catalyst::Plugin::Authorization::ACL.3pm*
%doc %{_mandir}/man3/Catalyst::Plugin::Authorization::ACL::Engine.3pm*
%dir %{perl_vendorlib}/Catalyst/
%dir %{perl_vendorlib}/Catalyst/Plugin/
%dir %{perl_vendorlib}/Catalyst/Plugin/Authorization/
%{perl_vendorlib}/Catalyst/Plugin/Authorization/ACL/
%{perl_vendorlib}/Catalyst/Plugin/Authorization/ACL.pm

%changelog
* Thu Jan 14 2010 Christoph Maser <cmr@financial.com> - 0.15-1
- Updated to version 0.15.

* Wed Oct 15 2008 Dag Wieers <dag@wieers.com> - 0.10-1
- Updated to release 0.10.

* Tue Oct 07 2008 Dag Wieers <dag@wieers.com> - 0.09-1
- Updated to release 0.09.

* Sun Dec 30 2007 Dag Wieers <dag@wieers.com> - 0.08-1
- Initial package. (using DAR)
