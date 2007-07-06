# $Id$
# Authority: dries
# Upstream: Jonathan Leto <jonathan$leto,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Math-Gsl

Summary: Interface to The GNU Scientific Library
Name: perl-Math-Gsl
Version: 0.08
Release: 1.2
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Math-Gsl/

Source: http://search.cpan.org/CPAN/authors/id/L/LE/LETO/Math-Gsl-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

#BuildArch: noarch
Requires: gsl >= 0.94
BuildRequires: perl, perl(ExtUtils::MakeMaker)
BuildRequires: gsl-devel >= 0.94

%description
Currently this module implements the GSL Special function library and the
single GSL function poly_complex_solve.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
#so strip doesn't fail
find %{buildroot}%{perl_vendorarch} -name '*.so' -exec chmod u+w {} \;
### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib}/*.pod
%{__rm} %{buildroot}%{perl_vendorarch}/auto/Math/Gsl/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST README THANKS doc contrib
%doc %{_mandir}/man3/Math::Gsl.3pm*
%doc %{_mandir}/man3/Math::Gsl::*.3pm*
%{perl_vendorarch}/Math/Gsl.pm
%{perl_vendorarch}/Math/Gsl/Sf.pm
%{perl_vendorarch}/Math/Gsl/Polynomial.pm
%{perl_vendorarch}/auto/Math/Gsl/Gsl.bs
%{perl_vendorarch}/auto/Math/Gsl/Gsl.so
%{perl_vendorarch}/auto/Math/Gsl/Sf/Sf.bs
%{perl_vendorarch}/auto/Math/Gsl/Sf/Sf.so
%{perl_vendorarch}/auto/Math/Gsl/Polynomial/Polynomial.bs
%{perl_vendorarch}/auto/Math/Gsl/Polynomial/Polynomial.so

%changelog
* Thu Jul 5 2007 Quien Sabe (aka Jim) <quien-sabe@metaorg.com> - 0.08-1.3
- Added Requires/BuildRequires to build for Fedora 7

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.08-1.2
- Rebuild for Fedora Core 5.

* Tue Apr 05 2005 Dries Verachtert <dries@ulyssis.org> - 0.08-1
- Initial package.
