# $Id$
# Authority: dag
# Upstream: Andy Armstrong <andy$hexten,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Acme-6502

Summary: Pure Perl 65C02 simulator
Name: perl-Acme-6502
Version: 0.75
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Acme-6502/

#Source: http://www.cpan.org/modules/by-module/Acme/Acme-6502-%{version}.tar.gz
Source: http://search.cpan.org/CPAN/authors/id/A/AN/ANDYA/Acme-6502-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Class::Std)
BuildRequires: perl(Class::Std::Slots)
BuildRequires: perl(Module::Build)
BuildRequires: perl(Term::ReadKey)
BuildRequires: perl(Test::More)
BuildRequires: perl(version)

%description
Pure Perl 65C02 simulator.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Build.PL --installdirs vendor --destdir %{buildroot}
./Build

%install
%{__rm} -rf %{buildroot}
./Build pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README SIGNATURE
%doc %{_mandir}/man3/Acme::6502.3pm*
%doc %{_mandir}/man3/Acme::6502::Tube.3pm*
%dir %{perl_vendorlib}/Acme/
%{perl_vendorlib}/Acme/6502/
%{perl_vendorlib}/Acme/6502.pm

%changelog
* Mon Sep 28 2009 Christoph Maser <cmr@financial.com> - 0.75-1
- Updated to version 0.75.

* Mon Oct 06 2008 Dag Wieers <dag@wieers.com> - 0.73-1
- Updated to release 0.73.

* Tue Nov 13 2007 Dag Wieers <dag@wieers.com> - 0.71-1
- Updated to release 0.71.

* Thu Oct 11 2007 Dag Wieers <dag@wieers.com> - 0.0.6-1
- Initial package. (using DAR)
