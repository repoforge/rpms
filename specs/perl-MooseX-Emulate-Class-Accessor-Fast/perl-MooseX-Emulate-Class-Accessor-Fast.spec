# $Id$
# Authority: cmr
# Upstream: Guillermo Roditi (groditi) <groditi$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name MooseX-Emulate-Class-Accessor-Fast

Summary: Emulate Class::Accessor::Fast behavior using Moose attributes
Name: perl-MooseX-Emulate-Class-Accessor-Fast
Version: 0.00903
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/MooseX-Emulate-Class-Accessor-Fast/

Source: http://www.cpan.org/modules/by-module/MooseX/MooseX-Emulate-Class-Accessor-Fast-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
# From yaml build_requires
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::More)
# From yaml requires
BuildRequires: perl(Moose) >= 0.84
BuildRequires: perl(namespace::clean)


%description
Emulate Class::Accessor::Fast behavior using Moose attributes.

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
%doc %{_mandir}/man3/MooseX::Adopt::Class::Accessor::Fast.3pm*
%doc %{_mandir}/man3/MooseX::Emulate::Class::Accessor::Fast.3pm*
%dir %{perl_vendorlib}/MooseX/
%dir %{perl_vendorlib}/MooseX/Emulate/
%dir %{perl_vendorlib}/MooseX/Emulate/Class/
%dir %{perl_vendorlib}/MooseX/Emulate/Class/Accessor/
#%{perl_vendorlib}/MooseX/Emulate/Class/Accessor/Fast/
%{perl_vendorlib}/MooseX/Emulate/Class/Accessor/Fast.pm
%{perl_vendorlib}/MooseX/Adopt/Class/Accessor/Fast.pm
%{perl_vendorlib}/MooseX/Emulate/Class/Accessor/Fast/Meta/Accessor.pm
%{perl_vendorlib}/MooseX/Emulate/Class/Accessor/Fast/Meta/Role/Attribute.pm

%changelog
* Thu Sep 17 2009 Christoph Maser <cmr@financial.com> - 0.00903-1
- Updated to version 0.00903.

* Sat Aug 22 2009 Christoph Maser <cmr@financial.com> - 0.00902-1
- Initial package. (using DAR)
