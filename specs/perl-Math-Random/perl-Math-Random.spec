# $Id$
# Authority: dries
# Upstream: Geoffrey Rommel <grommel$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Math-Random

Summary: Random number generators
Name: perl-Math-Random
Version: 0.71
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Math-Random/

Source: http://www.cpan.org/modules/by-module/Math/Math-Random-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This module generates a variety of random numbers.  Capabilities
of wide interest include the generation of:
    uniform numbers between 0 and 1 (or user chosen boundaries)
    random integers between user specified bounds
    random permutations of a list (shuffle a deck of cards)

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

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
%doc %{_mandir}/man3/Math::Random.3pm*
%dir %{perl_vendorarch}/auto/Math/
%{perl_vendorarch}/auto/Math/Random/
%dir %{perl_vendorarch}/Math/
%{perl_vendorarch}/Math/Random.pm
%{perl_vendorarch}/Math/example.pl
%exclude %{perl_vendorarch}/Math/test1.pl
%exclude %{perl_vendorarch}/Math/test2.pl

%changelog
* Mon Oct 13 2008 Dag Wieers <dag@wieers.com> - 0.71-1
- Updated to release 0.71.

* Wed Nov 14 2007 Dag Wieers <dag@wieers.com> - 0.70-1
- Updated to release 0.70.

* Wed Dec 21 2005 Dries Verachtert <dries@ulyssis.org> - 0.67-1
- Initial package.
