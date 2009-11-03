# $Id$
# Authority: dries
# Upstream: Anthony Thyssen <anthony$cit,gu,edu,au>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Math-VectorReal

Summary: Module to handle 3D Vector Mathematics
Name: perl-Math-VectorReal
Version: 1.02
Release: 1.2%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Math-VectorReal/

Source: http://www.cpan.org/modules/by-module/Math/Math-VectorReal-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
The Math::VectorReal' package defines a 3D mathematical "vector", in a way
that is compatible with the previous CPAN module ath::MatrixReal'.  However
it provides a more vector oriented set of mathematical functions and
overload operators, to the atrixReal' package. For example the normal perl string
functions "x" and "." have been overloaded to allow vector cross and dot
product operations. Vector math formula thus looks like vector math formula
in perl programs using this package.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

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
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/Math/
%{perl_vendorlib}/Math/VectorReal.pm
%{perl_vendorlib}/Math/*.pl

%changelog
* Mon Dec 06 2004 Dries Verachtert <dries@ulyssis.org> - 1.02-1
- Initial package.
