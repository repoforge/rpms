# $Id$
# Authority: dries
# Upstream: John A.R. Williams <J,A,R,Williams$aston,ac,uk>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Math-Fortran

Summary: Perl implimentations of Fortrans sign and log10
Name: perl-Math-Fortran
Version: 0.01
Release: 1.2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Math-Fortran/

Source: http://www.cpan.org/modules/by-module/Math/Math-Fortran-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This module provides and exports some mathematical functions which are built
in in Fortran but not in Perl. Currently there are only 2 included.
log10 log to the base of 10 =item sign with 1 parameter, +1 if $y>=0, -1
otherwise, with 2 parameters +abs($x) if $y>=0, -abs($x) otherwise.

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
%doc README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Math/Fortran.pm

%changelog
* Sun Apr  3 2005 Dries Verachtert <dries@ulyssis.org> - 0.01-1
- Initial package.
