# $Id$
# Authority: cmr
# Upstream: Chris Prather  C<< <chris$prather,org> >>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name MooseX-POE

Summary: The Illicit Love Child of Moose and POE
Name: perl-MooseX-POE
Version: 0.205
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/MooseX-POE/

Source: http://www.cpan.org/modules/by-module/MooseX/MooseX-POE-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker) 
BuildRequires: perl(Test::More) >= 0.42

%description
The Illicit Love Child of Moose and POE.

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
%doc Changes MANIFEST META.yml
%doc %{_mandir}/man3/MooseX::POE.3pm*
%doc %{_mandir}/man3/MooseX::POE::Aliased.3pm*
%doc %{_mandir}/man3/MooseX::POE::Meta::Trait::Class.3pm*
%doc %{_mandir}/man3/MooseX::POE::Meta::Trait::Constructor.3pm*
%doc %{_mandir}/man3/MooseX::POE::Meta::Trait::Instance.3pm*
%doc %{_mandir}/man3/MooseX::POE::Meta::Trait::Object.3pm*
%doc %{_mandir}/man3/MooseX::POE::Meta::Trait::SweetArgs.3pm*
%doc %{_mandir}/man3/MooseX::POE::Role.3pm*
%doc %{_mandir}/man3/MooseX::POE::SweetArgs.3pm*
%dir %{perl_vendorlib}/MooseX/
%{perl_vendorlib}/MooseX/POE.pm
%{perl_vendorlib}/MooseX/POE/Aliased.pm
%{perl_vendorlib}/MooseX/POE/Meta/Role.pm
%{perl_vendorlib}/MooseX/POE/Meta/Trait/Class.pm
%{perl_vendorlib}/MooseX/POE/Meta/Trait/Constructor.pm
%{perl_vendorlib}/MooseX/POE/Meta/Trait/Instance.pm
%{perl_vendorlib}/MooseX/POE/Meta/Trait/Object.pm
%{perl_vendorlib}/MooseX/POE/Meta/Trait/SweetArgs.pm
%{perl_vendorlib}/MooseX/POE/Role.pm
%{perl_vendorlib}/MooseX/POE/SweetArgs.pm


%changelog
* Fri Sep 04 2009 Christoph Maser <cmr@financial.com> - 0.205-1
- Initial package. (using DAR)
