# $Id$
# Authority: dries
# Upstream: Wim Verhaegen <wimv$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Math-LinearCombination

Summary: Sum of variables with a numerical coefficient
Name: perl-Math-LinearCombination
Version: 0.03
Release: 1.2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Math-LinearCombination/

Source: http://www.cpan.org/modules/by-module/Math/Math-LinearCombination-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Math::LinearCombination is a module for representing mathematical linear
combinations of variables, i.e. expressions of the format

a1 * x1 + a2 * x2 + ... + an * xn

with x1, x2, ..., xn variables, and a1, a2, ..., an numerical
coefficients. Evaluation and manipulation of linear combinations is also
supported. The numerical coefficients a_i and variables x_i are stored
as pairs in an internal data structure and should not be manipulated
directly. All access and manipulation should be performed through the
methods.

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
%{perl_vendorlib}/Math/LinearCombination.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.03-1.2
- Rebuild for Fedora Core 5.

* Mon Apr 04 2005 Dries Verachtert <dries@ulyssis.org> - 0.03-1
- Initial package.
