# $Id$
# Authority: dries
# Upstream: Daisuke Maki <daisuke$endeworks,jp>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name DateTime-Event-Chinese

Summary: DateTime Extension for Calculating Important Chinese Dates
Name: perl-DateTime-Event-Chinese
Version: 0.05
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DateTime-Event-Chinese/

Source: http://www.cpan.org/modules/by-module/DateTime/DateTime-Event-Chinese-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(DateTime)
BuildRequires: perl(DateTime::Event::Lunar) >= 0.06
BuildRequires: perl(DateTime::Event::SolarTerm) >= 0.05
BuildRequires: perl(DateTime::Util::Astro) >= 0.11
BuildRequires: perl(Module::Build)

%description
DateTime Extension for Calculating Important Chinese Dates.

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
%doc %{_mandir}/man3/DateTime::Event::Chinese.3pm*
%dir %{perl_vendorlib}/DateTime/
%dir %{perl_vendorlib}/DateTime/Event/
#%{perl_vendorlib}/DateTime/Event/Chinese/
%{perl_vendorlib}/DateTime/Event/Chinese.pm

%changelog
* Thu Nov 08 2007 Dag Wieers <dag@wieers.com> - 0.05-1
- Updated to release 0.05.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 0.04-1
- Updated to release 0.04.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 0.03-1
- Initial package.
