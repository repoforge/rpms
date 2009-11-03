# $Id$
# Authority: dries
# Upstream: Daisuke Maki <daisuke$endeworks,jp>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name DateTime-Event-SolarTerm

Summary: DateTime Extension to Calculate Solar Terms
Name: perl-DateTime-Event-SolarTerm
Version: 0.05
Release: 1%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DateTime-Event-SolarTerm/

Source: http://www.cpan.org/modules/by-module/DateTime/DateTime-Event-SolarTerm-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(DateTime)
BuildRequires: perl(DateTime::Set)
BuildRequires: perl(DateTime::Util::Astro::Sun) >= 0.11
BuildRequires: perl(DateTime::Util::Calc) >= 0.12
BuildRequires: perl(Module::Build)

%description
DateTime Extension to Calculate Solar Terms.

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
%doc CHANGES LICENSE MANIFEST META.yml
%doc %{_mandir}/man3/DateTime::Event::SolarTerm.3pm*
%dir %{perl_vendorlib}/DateTime/
%dir %{perl_vendorlib}/DateTime/Event/
#%{perl_vendorlib}/DateTime/Event/SolarTerm/
%{perl_vendorlib}/DateTime/Event/SolarTerm.pm

%changelog
* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 0.04-1
- Initial package.
