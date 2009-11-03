# $Id$
# Authority: dag
# Upstream: Jerry D, Hedden <jdhedden AT cpan DOT org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Math-Random-MT-Auto

Summary: Auto-seeded Mersenne Twister PRNGs
Name: perl-Math-Random-MT-Auto
Version: 6.14
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Math-Random-MT-Auto/

Source: http://www.cpan.org/modules/by-module/Math/Math-Random-MT-Auto-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Auto-seeded Mersenne Twister PRNGs.

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

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README examples/
%doc %{_mandir}/man3/Math::Random::MT::Auto.3pm*
%doc %{_mandir}/man3/Math::Random::MT::Auto::Range.3pm*
%dir %{perl_vendorarch}/auto/Math/
%dir %{perl_vendorarch}/auto/Math/Random/
%dir %{perl_vendorarch}/auto/Math/Random/MT/
%{perl_vendorarch}/auto/Math/Random/MT/Auto/
%dir %{perl_vendorarch}/Math/
%dir %{perl_vendorarch}/Math/Random/
%dir %{perl_vendorarch}/Math/Random/MT/
%{perl_vendorarch}/Math/Random/MT/Auto/
%{perl_vendorarch}/Math/Random/MT/Auto.pm

%changelog
* Tue Jun 24 2008 Dag Wieers <dag@wieers.com> - 6.14-1
- Updated to release 6.14.

* Thu Feb 28 2008 Dag Wieers <dag@wieers.com> - 6.12-1
- Updated to release 6.12.

* Mon Feb 25 2008 Dag Wieers <dag@wieers.com> - 6.11-1
- Updated to release 6.11.

* Wed Nov 14 2007 Dag Wieers <dag@wieers.com> - 6.09-1
- Updated to release 6.09.

* Sun May 27 2007 Dag Wieers <dag@wieers.com> - 6.02-1
- Initial package. (using DAR)
