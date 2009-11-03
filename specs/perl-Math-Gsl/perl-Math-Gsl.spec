# $Id$
# Authority: dries
# Upstream: Jonathan Leto <jonathan$leto,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Math-Gsl

Summary: Interface to The GNU Scientific Library
Name: perl-Math-Gsl
Version: 0.08
Release: 2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Math-Gsl/

Source: http://www.cpan.org/modules/by-module/Math/Math-Gsl-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

#BuildArch: noarch
Requires: gsl >= 0.94
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: gsl-devel >= 0.94

%description
Currently this module implements the GSL Special function library and the
single GSL function poly_complex_solve.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

#so strip doesn't fail
find %{buildroot}%{perl_vendorarch} -name '*.so' -exec chmod u+w {} \;

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

### Clean up docs
find contrib/ doc/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST README THANKS contrib/ doc/
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorarch}/Math/
%{perl_vendorarch}/Math/Gsl.pm
%{perl_vendorarch}/Math/Gsl/
%dir %{perl_vendorarch}/auto/Math/
%{perl_vendorarch}/auto/Math/Gsl/

%changelog
* Thu Jul 5 2007 Quien Sabe (aka Jim) <quien-sabe@metaorg.com> - 0.08-2
- Added Requires/BuildRequires to build for Fedora 7

* Tue Apr 05 2005 Dries Verachtert <dries@ulyssis.org> - 0.08-1
- Initial package.
