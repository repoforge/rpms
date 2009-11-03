# $Id$
# Authority: dries
# Upstream: Franck Cuny <franck,cuny$gmail,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Games-WoW-Armory
%define real_version 0.000007

Summary: Access to the WoW Armory
Name: perl-Games-WoW-Armory
Version: 0.0.7
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Games-WoW-Armory/

Source: http://www.cpan.org/modules/by-module/Games/Games-WoW-Armory-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Access to the WoW Armory.

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

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README examples/
%doc %{_mandir}/man3/Games::WoW::Armory.3pm*
%dir %{perl_vendorlib}/Games/
%dir %{perl_vendorlib}/Games/WoW/
#%{perl_vendorlib}/Games/WoW/Armory/
%{perl_vendorlib}/Games/WoW/Armory.pm

%changelog
* Fri Nov 09 2007 Dag Wieers <dag@wieers.com> - 0.0.7-1
- Updated to release 0.0.7.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.0.3-1
- Initial package.
