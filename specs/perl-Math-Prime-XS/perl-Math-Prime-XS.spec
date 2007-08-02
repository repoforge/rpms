# $Id$
# Authority: dries
# Upstream: Steven Schubiger <schubiger$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Math-Prime-XS

Summary: Calculate/detect prime numbers with deterministic tests
Name: perl-Math-Prime-XS
Version: 0.17
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Math-Prime-XS/

Source: http://search.cpan.org/CPAN/authors/id/S/SC/SCHUBIGER/Math-Prime-XS-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, perl(Module::Build)

%description
Math::Prime::XS calculates/detects prime numbers by either applying
Modulo operator division, the Sieve of Eratosthenes, Trial division or a
Summing calculation.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorarch}/Math/Prime/XS.pm
%{perl_vendorarch}/auto/Math/Prime/XS/

%changelog
* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 0.17-1
- Updated to release 0.17.

* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.16-1
- Initial package.
