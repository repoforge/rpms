# $Id$
# Authority: dries
# Upstream: Steven Schubiger <schubiger$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Math-Factor-XS

Summary: Factorise numbers and calculate matching multiplications
Name: perl-Math-Factor-XS
Version: 0.33
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Math-Factor-XS/

Source: http://search.cpan.org/CPAN/authors/id/S/SC/SCHUBIGER/Math-Factor-XS-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(Module::Build)

%description
Math::Factor::XS factorises numbers by applying modulo operator divisons.

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
%dir %{perl_vendorarch}/Math/Factor/
%{perl_vendorarch}/Math/Factor/XS.pm
%dir %{perl_vendorarch}/auto/Math/
%dir %{perl_vendorarch}/auto/Math/Factor/
%{perl_vendorarch}/auto/Math/Factor/XS/

%changelog
* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 0.33-1
- Updated to release 0.33.

* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.32-1
- Initial package.
