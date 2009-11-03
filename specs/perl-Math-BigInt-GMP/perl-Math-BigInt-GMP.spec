# $Id$
# Authority: dries
# Upstream: Tels <perl_dummy$bloodgate,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Math-BigInt-GMP

Summary: Use the GMP library for Math::BigInt routines
Name: perl-Math-BigInt-GMP
Version: 1.24
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Math-BigInt-GMP/

Source: http://www.cpan.org/modules/by-module/Math/Math-BigInt-GMP-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: gmp-devel

%description
This package contains a replacement (drop-in) module for Math::BigInt's
core, Math::BigInt::Calc.pm.

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
%doc BUGS CHANGES CREDITS INSTALL LICENSE MANIFEST MANIFEST.SKIP META.yml README SIGNATURE TODO
%doc %{_mandir}/man3/Math::BigInt::GMP.3pm*
%dir %{perl_vendorarch}/auto/Math/
%dir %{perl_vendorarch}/auto/Math/BigInt/
%{perl_vendorarch}/auto/Math/BigInt/GMP/
%dir %{perl_vendorarch}/Math/
%dir %{perl_vendorarch}/Math/BigInt/
%{perl_vendorarch}/Math/BigInt/GMP.pm
%{perl_vendorarch}/Math/BigInt/

%changelog
* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 1.24-1
- Updated to release 1.24.

* Thu Jul 5 2007 Quien Sabe (aka Jim) <quien-sabe@metaorg.com> - 1.22-1
- Updated to latest upstream version { old source not available }

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 1.18-1
- Updated to release 1.18.

* Fri Mar  4 2005 Dries Verachtert <dries@ulyssis.org> - 1.17-1
- Updated to release 1.17.

* Wed Dec 29 2004 Dries Verachtert <dries@ulyssis.org> - 1.16-1
- Updated to release 1.16.

* Mon Dec 06 2004 Dries Verachtert <dries@ulyssis.org> - 1.15-1
- Initial package.
