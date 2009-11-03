# $Id$
# Authority: dries
# Upstream: Eric Boesch <ericboesch$hotmail,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Math-Integral-Romberg

Summary: Scalar numerical integration
Name: perl-Math-Integral-Romberg
Version: 0.04
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Math-Integral-Romberg/

Source: http://www.cpan.org/modules/by-module/Math/Math-Integral-Romberg-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Module::Build)

%description
Romberg integration is used for estimating the integral of a scalar
function over a finite closed interval.  It is a better alternative to
Simpson's method and the trapezoid method.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Build.PL --installdirs vendor --destdir %{buildroot}
./Build

%install
%{__rm} -rf %{buildroot}
./Build pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Math/Integral/Romberg.pm

%changelog
* Thu Jul 16 2009 Christoph Maser <cmr@financial.com> - 0.04-1
- Updated to version 0.04.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.02-1.2
- Rebuild for Fedora Core 5.

* Tue Apr 05 2005 Dries Verachtert <dries@ulyssis.org> - 0_02-1
- Initial package.
