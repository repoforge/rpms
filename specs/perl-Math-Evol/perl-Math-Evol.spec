# $Id$
# Authority: dries
# Upstream: Peter Billam <contact,html$pjb,com,au>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Math-Evol

Summary: Evolution search optimisation
Name: perl-Math-Evol
Version: 1.06
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Math-Evol/

Source: http://search.cpan.org/CPAN/authors/id/P/PJ/PJB/Math-Evol-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

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
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man?/*
%{_bindir}/ps_evol
%{perl_vendorlib}/Math/Evol.pm

%changelog
* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 1.06-1
- Updated to release 1.06.

* Mon Apr 04 2005 Dries Verachtert <dries@ulyssis.org> - 1.05-1
- Initial package.
