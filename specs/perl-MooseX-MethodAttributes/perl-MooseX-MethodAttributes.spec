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
Version: 0.15
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/MooseX-MethodAttributes/

Source: http://www.cpan.org/modules/by-module/MooseX/MooseX-MethodAttributes-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
# From yaml requires
BuildRequires: perl(MRO::Compat)
BuildRequires: perl(Moose) >= 0.79
BuildRequires: perl(MooseX::Types) >= 0.06
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::More)
BuildRequires: perl(namespace::clean)


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
%doc %{_mandir}/man3/MooseX::MethodAttributes::Role::AttrContainer.3pm.gz
%doc %{_mandir}/man3/MooseX::MethodAttributes::Role::AttrContainer::Inheritable.3pm.gz
%doc %{_mandir}/man3/MooseX::MethodAttributes::Role::Meta::Class.3pm.gz
%doc %{_mandir}/man3/MooseX::MethodAttributes::Role::Meta::Map.3pm.gz
%doc %{_mandir}/man3/MooseX::MethodAttributes::Role::Meta::Method.3pm.gz
%doc %{_mandir}/man3/MooseX::MethodAttributes::Role::Meta::Method::MaybeWrapped.3pm.gz
%doc %{_mandir}/man3/MooseX::MethodAttributes::Role::Meta::Method::Wrapped.3pm.gz
%doc %{_mandir}/man3/MooseX::MethodAttributes::Role::Meta::Role.3pm.gz
%dir %{perl_vendorlib}/MooseX/
%{perl_vendorlib}/MooseX/MethodAttributes.pm
%{perl_vendorlib}/MooseX/MethodAttributes/Inheritable.pm
%{perl_vendorlib}/MooseX/MethodAttributes/Role/AttrContainer.pm
%{perl_vendorlib}/MooseX/MethodAttributes/Role/AttrContainer/Inheritable.pm
%{perl_vendorlib}/MooseX/MethodAttributes/Role/Meta/Class.pm
%{perl_vendorlib}/MooseX/MethodAttributes/Role/Meta/Map.pm
%{perl_vendorlib}/MooseX/MethodAttributes/Role/Meta/Method.pm
%{perl_vendorlib}/MooseX/MethodAttributes/Role/Meta/Method/MaybeWrapped.pm
%{perl_vendorlib}/MooseX/MethodAttributes/Role/Meta/Method/Wrapped.pm
%{perl_vendorlib}/MooseX/MethodAttributes/Role/Meta/Role.pm


%changelog
* Sat Aug 22 2009 Christoph Maser <cmr@financial.com> - 0.15-1
- Initial package. (using DAR)
