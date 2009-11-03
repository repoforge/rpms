# $Id$
# Authority: dries
# Upstream: Zbigniew Sroczynski <zs$elsewhere,de>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Math-ErrorPropagation

Summary: Computes the error of a function of statistical data
Name: perl-Math-ErrorPropagation
Version: 0.01
Release: 1.2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Math-ErrorPropagation/

Source: http://www.cpan.org/modules/by-module/Math/Math-ErrorPropagation-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This package allows the propagation of errors on the variables through
various simple mathematical operations to automatically compute the error of
the function. Use it to define  data each with a central (mean) value and
either the variance or standard deviation (square root of the variance),
then apply perl's mathematical operators to them to calculate your function
f. These operators are overloaded so that f automatically has the correct
variance.

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
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Math/ErrorPropagation.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.01-1.2
- Rebuild for Fedora Core 5.

* Mon Apr 04 2005 Dries Verachtert <dries@ulyssis.org> - 0.01-1
- Initial package.
