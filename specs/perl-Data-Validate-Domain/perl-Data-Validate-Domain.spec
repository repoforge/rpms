# $Id$
# Authority: dag
# Upstream: Neil A. Neely <neil$neely,cx>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Data-Validate-Domain

Summary: Domain validation methods
Name: perl-Data-Validate-Domain
Version: 0.09
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Data-Validate-Domain/

Source: http://www.cpan.org/modules/by-module/Data/Data-Validate-Domain-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Domain validation methods.

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
%doc %{_mandir}/man3/Data::Validate::Domain.3pm*
%dir %{perl_vendorlib}/Data/
%dir %{perl_vendorlib}/Data/Validate/
#%{perl_vendorlib}/Data/Validate/Domain/
%{perl_vendorlib}/Data/Validate/Domain.pm

%changelog
* Sat Mar 08 2008 Dag Wieers <dag@wieers.com> - 0.09-1
- Initial package. (using DAR)
