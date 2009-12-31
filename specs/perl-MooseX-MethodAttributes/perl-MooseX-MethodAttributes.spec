# $Id$
# Authority: cmr
# Upstream: Florian Ragwitz <rafl$debian,org>
# Upstream: Tomas Doran <bobtfish$bobtfish,net>
# Need MooseX::Types
# ExcludeDist: el4

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name MooseX-MethodAttributes

Summary: code attribute introspection
Name: perl-MooseX-MethodAttributes
Version: 0.18
Release: 2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/MooseX-MethodAttributes/

Source: http://www.cpan.org/modules/by-module/MooseX/MooseX-MethodAttributes-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Moose) >= 0.90
BuildRequires: perl(MooseX::Types) >= 0.20
BuildRequires: perl(Test::Exception)
#BuildRequires: perl(Test::More) >= 0.88
BuildRequires: perl(Test::More)
BuildRequires: perl(namespace::autoclean)
BuildRequires: perl(namespace::clean) >= 0.10
Requires: perl(Moose) >= 0.90
Requires: perl(MooseX::Types) >= 0.20
Requires: perl(Test::Exception)
#Requires: perl(Test::More) >= 0.88
Requires: perl(Test::More)
Requires: perl(namespace::autoclean)
Requires: perl(namespace::clean) >= 0.10

%filter_from_requires /^perl*/d
%filter_setup


%description
code attribute introspection.

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
%doc Changes LICENSE MANIFEST META.yml README TODO
%doc %{_mandir}/man3/MooseX::MethodAttributes.3pm*
%doc %{_mandir}/man3/MooseX::MethodAttributes::Inheritable.3pm.gz
%doc %{_mandir}/man3/MooseX::MethodAttributes::Role.3pm.gz
%doc %{_mandir}/man3/MooseX::MethodAttributes::Role::AttrContainer.3pm.gz
%doc %{_mandir}/man3/MooseX::MethodAttributes::Role::AttrContainer::Inheritable.3pm.gz
%doc %{_mandir}/man3/MooseX::MethodAttributes::Role::Meta::Class.3pm.gz
%doc %{_mandir}/man3/MooseX::MethodAttributes::Role::Meta::Map.3pm.gz
%doc %{_mandir}/man3/MooseX::MethodAttributes::Role::Meta::Method.3pm.gz
%doc %{_mandir}/man3/MooseX::MethodAttributes::Role::Meta::Method::MaybeWrapped.3pm.gz
%doc %{_mandir}/man3/MooseX::MethodAttributes::Role::Meta::Method::Wrapped.3pm.gz
%doc %{_mandir}/man3/MooseX::MethodAttributes::Role::Meta::Role.3pm.gz
%doc %{_mandir}/man3/MooseX::MethodAttributes::Role::Meta::Role::Application.3pm.gz
%doc %{_mandir}/man3/MooseX::MethodAttributes::Role::Meta::Role::Application::Summation.3pm.gz
%dir %{perl_vendorlib}/MooseX/
%{perl_vendorlib}/MooseX/MethodAttributes.pm
%{perl_vendorlib}/MooseX/MethodAttributes/Inheritable.pm
%{perl_vendorlib}/MooseX/MethodAttributes/Role.pm
%{perl_vendorlib}/MooseX/MethodAttributes/Role/AttrContainer.pm
%{perl_vendorlib}/MooseX/MethodAttributes/Role/AttrContainer/Inheritable.pm
%{perl_vendorlib}/MooseX/MethodAttributes/Role/Meta/Class.pm
%{perl_vendorlib}/MooseX/MethodAttributes/Role/Meta/Map.pm
%{perl_vendorlib}/MooseX/MethodAttributes/Role/Meta/Method.pm
%{perl_vendorlib}/MooseX/MethodAttributes/Role/Meta/Method/MaybeWrapped.pm
%{perl_vendorlib}/MooseX/MethodAttributes/Role/Meta/Method/Wrapped.pm
%{perl_vendorlib}/MooseX/MethodAttributes/Role/Meta/Role.pm
%{perl_vendorlib}/MooseX/MethodAttributes/Role/Meta/Role/Application.pm
%{perl_vendorlib}/MooseX/MethodAttributes/Role/Meta/Role/Application/Summation.pm


%changelog
* Thu Dec 31 2009 Christoph Maser <cmr@financial.com> - 0.18-2
- remove version from Test::More requirement

* Thu Dec 10 2009 Christoph Maser <cmr@financial.com> - 0.18-1
- Updated to version 0.18.

* Thu Sep 17 2009 Christoph Maser <cmr@financial.com> - 0.16-1
- Updated to version 0.16.

* Sat Aug 22 2009 Christoph Maser <cmr@financial.com> - 0.15-1
- Initial package. (using DAR)
