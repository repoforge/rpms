# $Id$
# Authority: dag
# Upstream: Damian Conway <damian$conway,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Module-Starter-PBP
%define real_version 0.000003

Summary: Perl module to create a module as recommended in "Perl Best Practices"
Name: perl-Module-Starter-PBP
Version: 0.0.3
Release: 1%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Module-Starter-PBP/

Source: http://www.cpan.org/modules/by-module/Module/Module-Starter-PBP-v%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Module::Starter)

%description
Module-Starter-PBP is a Perl module to create a module
as recommended in "Perl Best Practices".

%prep
%setup -n %{real_name}-v%{version}

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
%doc %{_mandir}/man3/Module::Starter::PBP.3pm*
%dir %{perl_vendorlib}/Module/
%dir %{perl_vendorlib}/Module/Starter/
%{perl_vendorlib}/Module/Starter/PBP.pm

%changelog
* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 0.0.3-1
- Initial package. (using DAR)
