# $Id$
# Authority: dries
# Upstream: Ed Callahan <cpan$edcallahan,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Math-CDF

Summary: Generate probabilities and quantiles from probability functions
Name: perl-Math-CDF
Version: 0.1
Release: 1.2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Math-CDF/

Source: http://www.cpan.org/modules/by-module/Math/Math-CDF-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This package provides a perl interface to DCDFLIB, a set of C functions
written by Barry W. Brown, James Lovato and Kathy Russell of the
Department of Biomathematics at The University of Texas M.D. Anderson
Cancer Center in Houston, Texas. DCDFLIB code is included in this module
distribution with permission of its authors.

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
%dir %{perl_vendorarch}/Math/
%{perl_vendorarch}/Math/CDF.pm
%dir %{perl_vendorarch}/auto/Math/
%{perl_vendorarch}/auto/Math/CDF/

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.1-1
- Initial package.
