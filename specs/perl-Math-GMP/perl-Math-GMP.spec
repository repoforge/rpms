# $Id$
# Authority: dries
# Upstream: Chip Turner <cturner$pattern,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Math-GMP

Summary: High speed arbitrary size integer math
Name: perl-Math-GMP
Version: 2.04
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Math-GMP/

Source: http://search.cpan.org/CPAN/authors/id/C/CH/CHIPT/Math-GMP-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, perl(ExtUtils::MakeMaker), gmp-devel

%description
Math::GMP gives you access to the fast GMP library for fast
big integer math.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorarch}/Math/
%{perl_vendorarch}/Math/GMP.pm
%dir %{perl_vendorarch}/auto/Math/
%{perl_vendorarch}/auto/Math/GMP/

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 2.04-1
- Initial package.
