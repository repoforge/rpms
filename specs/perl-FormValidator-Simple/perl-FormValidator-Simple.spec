# $Id$
# Authority: dag
# Upstream: Lyo Kato <lyo.kato$gmail,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name FormValidator-Simple

Summary: Validation with simple chains of constraints
Name: perl-FormValidator-Simple
Version: 0.28
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/FormValidator-Simple/

Source: http://www.cpan.org/modules/by-module/FormValidator/FormValidator-Simple-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Class::Accessor) >= 0.22
BuildRequires: perl(Class::Inspector) >= 1.13
BuildRequires: perl(Class::Data::Accessor) >= 0.03
BuildRequires: perl(Class::Data::Inheritable) >= 0.04
### Needed to work around problem on EL4
#BuildRequires: perl(Date::Calc) >= 5.4
BuildRequires: perl-Date-Calc >= 5.4
BuildRequires: perl(DateTime::Format::Strptime) >= 1.07
BuildRequires: perl(Email::Valid) >= 0.15
BuildRequires: perl(Email::Valid::Loose) >= 0.04
BuildRequires: perl(List::MoreUtils) >= 0.16
BuildRequires: perl(Mail::Address)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Tie::IxHash) >= 1.21
BuildRequires: perl(UNIVERSAL::require) >= 0.1
BuildRequires: perl(YAML) >= 0.39

%description
Validation with simple chains of constraints.

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
%doc Changes MANIFEST MANIFEST.SKIP META.yml README
%doc %{_mandir}/man3/FormValidator::Simple.3pm*
%doc %{_mandir}/man3/FormValidator::Simple::Results.3pm*
%dir %{perl_vendorlib}/FormValidator/
%{perl_vendorlib}/FormValidator/Simple/
%{perl_vendorlib}/FormValidator/Simple.pm

%changelog
* Sun Jul  5 2009 Christoph Maser <cmr@financial.com> - 0.28-1
- Updated to version 0.28.

* Mon May 05 2008 Dag Wieers <dag@wieers.com> - 0.23-1
- Updated to release 0.23.

* Fri Nov 23 2007 Dag Wieers <dag@wieers.com> - 0.22-1
- Initial package. (using DAR)
