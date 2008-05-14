# $Id$
# Authority: dries
# Upstream: Kim Ryan <kimryan$cpan org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Locale-SubCountry

Summary: Convert state, province, county ... names to/from ISO 3166-2 code
Name: perl-Locale-SubCountry
Version: 1.41
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Locale-SubCountry/

Source: http://www.cpan.org/modules/by-module/Locale/Locale-SubCountry-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 2:5.8.4
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl >= 2:5.8.4

%description
This module allows you to convert the full name for a countries administrative
region to the code commonly used for postal addressing. The reverse lookup
can also be done.  Sub country codes are defined in "ISO 3166-2:1998,
Codes for the representation of names of countries and their subdivisions".

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
%doc %{_mandir}/man3/Locale::SubCountry.3pm*
%dir %{perl_vendorlib}/Locale/
#%{perl_vendorlib}/Locale/SubCountry/
%{perl_vendorlib}/Locale/SubCountry.pm

%changelog
* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 1.41-1
- Updated to release 1.41.

* Wed Jan 23 2008 Dag Wieers <dag@wieers.com> - 1.40-1
- Updated to release 1.40.

* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 1.38-1
- Updated to release 1.38.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 1.37-1
- Updated to release 1.37.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 1.36-1
- Updated to release 1.36.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.34-1
- Initial package.
