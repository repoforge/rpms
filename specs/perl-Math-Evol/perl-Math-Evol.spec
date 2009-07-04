# $Id$
# Authority: dries
# Upstream: Peter Billam <contact,html$pjb,com,au>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Math-Evol

Summary: Evolution search optimisation
Name: perl-Math-Evol
Version: 1.10
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Math-Evol/

Source: http://www.cpan.org/modules/by-module/Math/Math-Evol-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This module implements the evolution search strategy.
Derivatives of the objective function are not required.
Constraints can be incorporated.  The caller must supply initial
values for the variables and for the initial step sizes.

This evolution search strategy is a random strategy, and as such is
particularly robust and will cope well with large numbers of variables
or rugged objective funtions.  It derives from the 'EVOL' Fortran routine
of Schwefel, which uses Rechenberg's work on step-size adjustment.

Evol.pm works either automatically with an objective function to be
minimised, or interactively with a (suitably patient) human who at
each step will choose the better of two (or several) possibilities.

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
%doc %{_mandir}/man?/*
%{_bindir}/ps_evol
%{perl_vendorlib}/Math/Evol.pm

%changelog
* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 1.10-1
- Updated to version 1.10.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.06-1.2
- Rebuild for Fedora Core 5.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 1.06-1
- Updated to release 1.06.

* Mon Apr 04 2005 Dries Verachtert <dries@ulyssis.org> - 1.05-1
- Initial package.
