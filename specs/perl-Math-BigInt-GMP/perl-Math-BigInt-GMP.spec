# $Id$
# Authority: dries
# Upstream: Tels <perl_dummy$bloodgate,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Math-BigInt-GMP

Summary: Use the GMP library for Math::BigInt routines
Name: perl-Math-BigInt-GMP
Version: 1.18
Release: 1.2
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Math-BigInt-GMP/

Source: http://www.cpan.org/modules/by-module/Math/Math-BigInt-GMP-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, perl(ExtUtils::MakeMaker), gmp-devel

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
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} \
                %{buildroot}%{perl_vendorarch}/auto/*{,/*{,/*}}/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES CREDITS README
%doc %{_mandir}/man3/*
%dir %{perl_vendorarch}/Math/
%{perl_vendorarch}/Math/BigInt/
%dir %{perl_vendorarch}/auto/Math/BigInt/
%{perl_vendorarch}/auto/Math/BigInt/GMP/

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.18-1.2
- Rebuild for Fedora Core 5.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 1.18-1
- Updated to release 1.18.

* Fri Mar  4 2005 Dries Verachtert <dries@ulyssis.org> - 1.17-1
- Updated to release 1.17.

* Wed Dec 29 2004 Dries Verachtert <dries@ulyssis.org> - 1.16-1
- Updated to release 1.16.

* Mon Dec 06 2004 Dries Verachtert <dries@ulyssis.org> - 1.15-1
- Initial package.
