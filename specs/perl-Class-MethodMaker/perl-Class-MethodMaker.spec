# $Id$
# Authority: dries
# Upstream: Steffen Schwigon <schwigon$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Class-MethodMaker

Summary: Module for creating generic methods
Name: perl-Class-MethodMaker
Version: 2.12
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Class-MethodMaker/

Source: http://www.cpan.org/modules/by-module/Class/Class-MethodMaker-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(Module::Build)

%description
This package allows you to create generic methods for OO Perl.

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
%doc Changes INSTALL MANIFEST MANIFEST.SKIP META.yml README SIGNATURE TODO examples/
%doc %{_mandir}/man3/Class::MethodMaker.3pm*
%doc %{_mandir}/man3/Class::MethodMaker::*.3pm*
%dir %{perl_vendorarch}/auto/Class/
%{perl_vendorarch}/auto/Class/MethodMaker/
%dir %{perl_vendorarch}/Class/
%{perl_vendorarch}/Class/MethodMaker.pm
%{perl_vendorarch}/Class/MethodMaker/

%changelog
* Tue Oct 07 2008 Dag Wieers <dag@wieers.com> - 2.12-1
- Updated to release 2.12.

* Sat May 03 2008 Dag Wieers <dag@wieers.com> - 2.11-1
- Updated to release 2.11.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 2.08-1
- Updated to release 2.08.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 2.07-1
- Updated to release 2.07.

* Wed Feb  2 2005 Dries Verachtert <dries@ulyssis.org> - 2.05-1
- Initial package.
