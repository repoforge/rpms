# $Id$
# Authority: dries
# Upstream: Sanford Morton <smorton$pobox,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Statistics-OLS

Summary: Perform ordinary least squares and associated statistics
Name: perl-Statistics-OLS
Version: 0.07
Release: 1.2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Statistics-OLS/

Source: http://www.cpan.org/modules/by-module/Statistics/Statistics-OLS-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
I wrote Statistics::OLS to perform Ordinary Least Squares (linear curve
fitting) on two dimensional data: y = a + bx. The other simple
statistical module I found on CPAN (Statistics::Descriptive) is
designed for univariate analysis. It accomodates OLS, but somewhat
inflexibly and without rich bivariate statistics. Nevertheless, it
might make sense to fold OLS into that module or a supermodule someday.

Statistics::OLS computes the estimated slope and intercept of the
regression line, their T-statistics, R squared, standard error of the
regression and the Durbin-Watson statistic. It can also return the
residuals.

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
%{perl_vendorlib}/Statistics/OLS.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.07-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.07-1
- Initial package.
