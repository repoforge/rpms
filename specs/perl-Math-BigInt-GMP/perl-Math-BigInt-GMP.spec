# $Id$

# Authority: dries
# Upstream: Tels <perl_dummy$bloodgate,com>

%define real_name Math-BigInt-GMP
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Use the GMP library for Math::BigInt routines
Name: perl-Math-BigInt-GMP
Version: 1.17
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Math-BigInt-GMP/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/T/TE/TELS/math/Math-BigInt-GMP-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, gmp-devel

%description
This package contains a replacement (drop-in) module for Math::BigInt's
core, Math::BigInt::Calc.pm.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" destdir=%{buildroot}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README CHANGES CREDITS
%doc %{_mandir}/man3/*
%{perl_vendorarch}/Math/BigInt/GMP.pm
%{perl_vendorarch}/auto/Math/BigInt/GMP/GMP.*
%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/*/.packlist

%changelog
* Fri Mar  4 2005 Dries Verachtert <dries@ulyssis.org> - 1.17-1
- Updated to release 1.17.

* Wed Dec 29 2004 Dries Verachtert <dries@ulyssis.org> - 1.16-1
- Updated to release 1.16.

* Mon Dec 06 2004 Dries Verachtert <dries@ulyssis.org> - 1.15-1
- Initial package.
