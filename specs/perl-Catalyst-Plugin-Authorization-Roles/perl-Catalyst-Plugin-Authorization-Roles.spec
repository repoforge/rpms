# $Id$
# Authority: dag
# Upstream: Brian Cassidy <bricas@cpan.org>
# ExcludeDist: el4

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Catalyst-Plugin-Authorization-Roles

Summary: Role based authorization for Catalyst based on Catalyst::Plugin::Authentication
Name: perl-Catalyst-Plugin-Authorization-Roles
Version: 0.08
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Catalyst-Plugin-Authorization-Roles/

Source: http://search.cpan.org/CPAN/authors/id/B/BR/BRICAS/Catalyst-Plugin-Authorization-Roles-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Catalyst::Plugin::Authentication) >= 0.10003
BuildRequires: perl(Catalyst::Runtime) >= 5.7
#BuildRequires: perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Set::Object) >= 1.14
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::More)
BuildRequires: perl(UNIVERSAL::isa) >= 0.05
BuildRequires: perl >= 5.8.0
Requires: perl(Catalyst::Plugin::Authentication) >= 0.10003
Requires: perl(Catalyst::Runtime) >= 5.7
Requires: perl(Set::Object) >= 1.14
Requires: perl(UNIVERSAL::isa) >= 0.05
Requires: perl >= 5.8.0

%filter_from_requires /^perl*/d
%filter_setup


%description
Role based authorization for Catalyst based on Catalyst::Plugin::Authentication.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
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
%doc %{_mandir}/man3/Catalyst::Plugin::Authorization::Roles.3pm*
%dir %{perl_vendorlib}/Catalyst/
%dir %{perl_vendorlib}/Catalyst/Plugin/
%dir %{perl_vendorlib}/Catalyst/Plugin/Authorization/
#%{perl_vendorlib}/Catalyst/Plugin/Authorization/Roles/
%{perl_vendorlib}/Catalyst/Plugin/Authorization/Roles.pm

%changelog
* Thu Jan 14 2010 Christoph Maser <cmr@financial.com> - 0.08-1
- Updated to version 0.08.

* Tue Oct 07 2008 Dag Wieers <dag@wieers.com> - 0.07-1
- Updated to release 0.07.

* Sun Dec 30 2007 Dag Wieers <dag@wieers.com> - 0.05-1
- Initial package. (using DAR)
