# $Id$
# Authority: cmr
# Upstream: Rafael Kitover <rkitover$cpan,org>
# ExcludeDist: el4

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name CatalystX-Component-Traits

Summary: Automatic Trait Loading and Resolution for
Name: perl-CatalystX-Component-Traits
Version: 0.14
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/CatalystX-Component-Traits/

Source: http://www.cpan.org/authors/id/R/RK/RKITOVER/CatalystX-Component-Traits-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Catalyst::Runtime) >= 5.80005
#BuildRequires: perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(List::MoreUtils)
BuildRequires: perl(Module::Pluggable) >= 3.9
BuildRequires: perl(MooseX::Traits::Pluggable) >= 0.08
BuildRequires: perl(Scalar::Util)
#BuildRequires: perl(Test::More) >= 0.88
BuildRequires: perl(Test::More)
BuildRequires: perl(namespace::autoclean)
Requires: perl(Catalyst::Runtime) >= 5.80005
Requires: perl(List::MoreUtils)
Requires: perl(MooseX::Traits::Pluggable) >= 0.08
Requires: perl(Scalar::Util)
Requires: perl(namespace::autoclean)

%filter_from_requires /^perl*/d
%filter_setup


%description
Automatic Trait Loading and Resolution for.

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
%doc %{_mandir}/man3/CatalystX::Component::Traits.3pm*
%dir %{perl_vendorlib}/CatalystX/
%dir %{perl_vendorlib}/CatalystX/Component/
#%{perl_vendorlib}/CatalystX/Component/Traits/
%{perl_vendorlib}/CatalystX/Component/Traits.pm

%changelog
* Thu Jan 14 2010 Christoph Maser <cmr@financial.com> - 0.14-1
- Initial package. (using DAR)
