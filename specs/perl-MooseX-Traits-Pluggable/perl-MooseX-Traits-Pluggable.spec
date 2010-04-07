# $Id$
# Authority: cmr
# Upstream: Tomas Doran <bobtfish@bobtfish.net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name MooseX-Traits-Pluggable

Summary: an extension to MooseX::Traits
Name: perl-MooseX-Traits-Pluggable
Version: 0.08
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/MooseX-Traits-Pluggable/

Source: http://search.cpan.org/CPAN/authors/id/B/BO/BOBTFISH/MooseX-Traits-Pluggable-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Class::MOP) >= 0.84
#BuildRequires: perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(List::MoreUtils)
BuildRequires: perl(Moose)
BuildRequires: perl(Moose::Role)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::More)
BuildRequires: perl(namespace::autoclean)
Requires: perl(Class::MOP) >= 0.84
Requires: perl(List::MoreUtils)
Requires: perl(Moose)
Requires: perl(Moose::Role)
Requires: perl(Scalar::Util)
Requires: perl(namespace::autoclean)

%filter_from_requires /^perl*/d
%filter_setup

%description
an extension to MooseX::Traits.

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
%doc %{_mandir}/man3/MooseX::Traits::Pluggable.3pm*
%dir %{perl_vendorlib}/MooseX/
%dir %{perl_vendorlib}/MooseX/Traits/
#%{perl_vendorlib}/MooseX/Traits/Pluggable/
%{perl_vendorlib}/MooseX/Traits/Pluggable.pm

%changelog
* Thu Jan 14 2010 Christoph Maser <cmr@financial.com> - 0.08-1
- Initial package. (using DAR)
