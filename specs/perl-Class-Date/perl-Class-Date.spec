# $Id$
# Authority: dries
# Upstream: Szab&#243;, Bal&#225;zs <dlux$kapu,hu>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Class-Date

Summary: Class for easy date and time manipulation
Name: perl-Class-Date
Version: 1.1.9
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Class-Date/

Source: http://www.cpan.org/modules/by-module/Class/Class-Date-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This module is intended to provide a general-purpose date and datetime
type for perl. You have a Class::Date class for absolute date and
datetime, and have a Class::Date::Rel class for relative dates.

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
%dir %{perl_vendorarch}/Class/
%{perl_vendorarch}/Class/Date/
%{perl_vendorarch}/Class/Date.pm
%{perl_vendorarch}/Class/Date.pod
%dir %{perl_vendorarch}/auto/Class/
%{perl_vendorarch}/auto/Class/Date/

%changelog
* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 1.1.9-1
- Updated to release 1.1.9.

* Mon Nov  7 2005 Dries Verachtert <dries@ulyssis.org> - 1.1.8-1
- Updated to release 1.1.8.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.1.7-1
- Initial package.
