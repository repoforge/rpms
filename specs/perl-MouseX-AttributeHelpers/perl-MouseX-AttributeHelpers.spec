# $Id$
# Authority: cmr
# Upstream: NAKAGAWA Masaki <masaki$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name MouseX-AttributeHelpers

Summary: Extend your attribute interfaces
Name: perl-MouseX-AttributeHelpers
Version: 0.06
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/MouseX-AttributeHelpers/

Source: http://www.cpan.org/authors/id/M/MA/MASAKI/MouseX-AttributeHelpers-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Any::Moose) >= 0.10
#BuildRequires: perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Mouse) >= 0.40
BuildRequires: perl(Mouse::Meta::Attribute)
BuildRequires: perl(Mouse::Util::TypeConstraints)
BuildRequires: perl(Test::Data::Scalar)
BuildRequires: perl(Test::Deep)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::UseAllModules)
BuildRequires: perl >= 5.6.2
Requires: perl(Mouse) >= 0.40
Requires: perl(Mouse::Meta::Attribute)
Requires: perl(Mouse::Util::TypeConstraints)
Requires: perl >= 5.6.2

%filter_from_requires /^perl*/d
%filter_setup

%description
Extend your attribute interfaces.

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
%doc Changes MANIFEST META.yml README README.mkdn
%doc %{_mandir}/man3/MouseX::AttributeHelpers*.3pm*
%dir %{perl_vendorlib}/MouseX/
%{perl_vendorlib}/MouseX/AttributeHelpers/
%{perl_vendorlib}/MouseX/AttributeHelpers.pm

%changelog
* Tue Dec 22 2009 Christoph Maser <cmr@financial.com> - 0.06-1
- Initial package. (using DAR)
