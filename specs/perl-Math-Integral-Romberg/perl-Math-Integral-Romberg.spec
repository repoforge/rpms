# $Id$
# Authority: dries
# Upstream: Eric Boesch <ericboesch$hotmail,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Math-Integral-Romberg
%define real_version 0_02

Summary: Scalar numerical integration
Name: perl-Math-Integral-Romberg
Version: 0.02
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Math-Integral-Romberg/

Source: http://search.cpan.org/CPAN/authors/id/B/BO/BOESCH/Math-Integral-Romberg-%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Romberg integration is used for estimating the integral of a scalar
function over a finite closed interval.  It is a better alternative to
Simpson's method and the trapezoid method.

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
%doc README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Math/Integral/Romberg.pm

%changelog
* Tue Apr 05 2005 Dries Verachtert <dries@ulyssis.org> - 0_02-1
- Initial package.
