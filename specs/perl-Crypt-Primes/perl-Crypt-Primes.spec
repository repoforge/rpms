# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define rname Crypt-Primes

Summary: Crypt-Primes module for perl
Name: perl-Crypt-Primes
Version: 0.50
Release: 1.2%{?dist}
License: distributable
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Crypt-Primes/

Source: http://www.cpan.org/modules/by-module/Crypt/Crypt-Primes-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl >= 0:5.00503
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl >= 0:5.00503

%description
Crypt-Primes module for perl

%prep
%setup -n %{rname}-%{version}

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
%doc README
%doc %{_mandir}/man1/largeprimes.1*
%doc %{_mandir}/man3/*
%{_bindir}/largeprimes
%{perl_vendorlib}/Crypt/Primes.pm
%dir %{perl_vendorarch}/auto/Crypt/
%{perl_vendorarch}/auto/Crypt/Primes/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.50-1.2
- Rebuild for Fedora Core 5.

* Thu Jan 12 2006 Dag Wieers <dag@wieers.com> - 0.50-1
- Initial package. (using DAR)
