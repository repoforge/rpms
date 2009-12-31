# $Id$
# Upstream: Florian Ragwitz <rafl@debian.org>
# ExcludeDist: el4

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)
%define real_name MooseX-Role-WithOverloading

Summary: MooseX roles which support overloading
Name: perl-MooseX-Role-WithOverloading
Version: 0.03
Release: 1%{?dist}
License: perl
Group: Applications/CPAN
URL: http://search.cpan.org/dist/MooseX-Role-WithOverloading

Source: http://search.cpan.org/CPAN/authors/id/F/FL/FLORA/MooseX-Role-WithOverloading-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl(Moose) >= 0.90
BuildRequires: perl(MooseX::Types)
BuildRequires: perl(XSLoader)
BuildRequires: perl(aliased)
BuildRequires: perl(namespace::autoclean) >= 0.09
BuildRequires: perl(namespace::clean)
Requires: perl(Moose) >= 0.90
Requires: perl(MooseX::Types)
Requires: perl(XSLoader)
Requires: perl(aliased)
Requires: perl(namespace::autoclean) >= 0.09
Requires: perl(namespace::clean)

%filter_from_requires /^perl*/d
%filter_setup

%description
MooseX::Role::WithOverloading allows you to write a Moose::Role which defines overloaded operators and allows those operator overloadings to be composed into the classes/roles/instances it's compiled to, while plain Moose::Roles would lose the overloading.

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
%doc Changes LICENSE MANIFEST README
%doc %{_mandir}/man3/MooseX::Role::WithOverloading*.3pm*
%{perl_vendorarch}/MooseX/Role/WithOverloading
%{perl_vendorarch}/MooseX/Role/WithOverloading.pm
%{perl_vendorarch}/auto/MooseX/Role/WithOverloading/WithOverloading.bs
%{perl_vendorarch}/auto/MooseX/Role/WithOverloading/WithOverloading.so

%changelog
* Thu Dec 31 2009 Christoph Maser <cmr@financial.com> - 0.001000-1
- Initial package (using mcsfb)

