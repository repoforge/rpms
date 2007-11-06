# $Id$
# Authority: dries
# Upstream: G&#225;bor Szab&#243; <gabor$pti,co,il>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Array-Unique

Summary: Tie-able array that allows only unique values
Name: perl-Array-Unique
Version: 0.07
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Array-Unique/

Source: http://search.cpan.org/CPAN/authors/id/S/SZ/SZABGAB/Array-Unique-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker), perl

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
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Array/Unique.pm

%changelog
* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.07-1
- Updated to release 0.07.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.06-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.06-1
- Initial package.
