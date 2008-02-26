# $Id$
# Authority: dries
# Upstream: Steven Schubiger <schubiger$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Math-Prime-XS

Summary: Calculate/detect prime numbers with deterministic tests
Name: perl-Math-Prime-XS
Version: 0.19
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Math-Prime-XS/

Source: http://www.cpan.org/modules/by-module/Math/Math-Prime-XS-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(Module::Build)
BuildRequires: perl(Test::More)

%description
Math::Prime::XS calculates/detects prime numbers by either applying
Modulo operator division, the Sieve of Eratosthenes, Trial division or a
Summing calculation.

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
%doc %{_mandir}/man3/Math::Prime::XS.3pm*
%dir %{perl_vendorarch}/auto/Math/
%dir %{perl_vendorarch}/auto/Math/Prime/
%{perl_vendorarch}/auto/Math/Prime/XS/
%dir %{perl_vendorarch}/Math/
%dir %{perl_vendorarch}/Math/Prime/
%{perl_vendorarch}/Math/Prime/XS.pm

%changelog
* Mon Feb 25 2008 Dag Wieers <dag@wieers.com> - 0.19-1 
- Updated to release 0.19.

* Wed Feb 20 2008 Dag Wieers <dag@wieers.com> - 0.18-1
- Updated to release 0.18.

* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 0.17-1
- Updated to release 0.17.

* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.16-1
- Initial package.
