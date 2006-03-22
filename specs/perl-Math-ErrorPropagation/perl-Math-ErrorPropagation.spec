# $Id$
# Authority: dries
# Upstream: Zbigniew Sroczynski <zs$elsewhere,de>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Math-ErrorPropagation

Summary: Computes the error of a function of statistical data
Name: perl-Math-ErrorPropagation
Version: 0.01
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Math-ErrorPropagation/

Source: http://search.cpan.org/CPAN/authors/id/Z/ZB/ZBYS/Math-ErrorPropagation-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

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
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

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
