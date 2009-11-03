# $Id$
# Authority: dag
# Upstream: Richard Sonnen <sonnen$richardsonnen,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Data-Validate-Email

Summary: Common email validation methods
Name: perl-Data-Validate-Email
Version: 0.04
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Data-Validate-Email/

Source: http://www.cpan.org/modules/by-module/Data/Data-Validate-Email-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Data::Validate::Domain)
BuildRequires: perl(Email::Address)

%description
Common email validation methods.

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
%doc Changes INSTALL MANIFEST META.yml README
%doc %{_mandir}/man3/Data::Validate::Email.3pm*
%dir %{perl_vendorlib}/Data/
%dir %{perl_vendorlib}/Data/Validate/
%{perl_vendorlib}/auto/Data/Validate/Email/
%{perl_vendorlib}/Data/Validate/Email.pm

%changelog
* Sat Mar 08 2008 Dag Wieers <dag@wieers.com> - 0.04-1
- Initial package. (using DAR)
