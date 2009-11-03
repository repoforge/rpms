# $Id$
# Authority: dries
# Upstream: Ken Fox <kfox$vulpes,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Math-Units

Summary: Unit conversion
Name: perl-Math-Units
Version: 1.3
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Math-Units/

Source: http://www.cpan.org/modules/by-module/Math/Math-Units-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This is Math::Units, the first official release of a powerful
unit conversion system written completely in Perl.  This module
has been tested fairly well using the GNU units program as a
baseline.

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
%doc %{_mandir}/man3/Math::Units.3pm*
%dir %{perl_vendorlib}/Math/
#%{perl_vendorlib}/Math/Units/
%{perl_vendorlib}/Math/Units.pm

%changelog
* Mon Oct 13 2008 Dag Wieers <dag@wieers.com> - 1.3-1
- Updated to release 1.3.

* Tue Apr 05 2005 Dries Verachtert <dries@ulyssis.org> - 1.2-1
- Initial package.
