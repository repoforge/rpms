# $Id$
# Authority: dries
# Upstream: Gabor Szabo <gabor$pti,co,il>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Array-Unique

Summary: Tie-able array that allows only unique values
Name: perl-Array-Unique
Version: 0.08
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Array-Unique/

Source: http://www.cpan.org/modules/by-module/Array/Array-Unique-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.006
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Module::Build)
BuildRequires: perl(Test::More) >= 0.47
Requires: perl >= 0:5.006

%description
This package lets you create an array which will allow only one
occurrence of any value.

In other words no matter how many times you put in 42 it will keep only
the first occurrence and the rest will be dropped.

You use the module via tie and once you tied your array to this module
it will behave correctly.

Uniqueness is checked with the 'eq' operator so among other things it is
case sensitive.

As a side effect the module does not allow undef as a value in the
array.

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

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Array::Unique.3pm*
%dir %{perl_vendorlib}/Array/
%{perl_vendorlib}/Array/Unique.pm

%changelog
* Sun Jun 22 2008 Dag Wieers <dag@wieers.com> - 0.08-1
- Updated to release 0.08.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.07-1
- Updated to release 0.07.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.06-1
- Initial package.
