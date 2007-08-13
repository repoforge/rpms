# $Id$
# Authority: dries
# Upstream: Robin Houston <robin-cpan$kitsite,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Want

Summary: Implement the 'want' command
Name: perl-Want
Version: 0.14
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Want/

Source: http://search.cpan.org/CPAN/authors/id/R/RO/ROBIN/Want-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
This module generalises the mechanism of the wantarray
function, allowing a function to determine in some detail
how its return value is going to be immediately used.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/Want*.3pm*
%{perl_vendorarch}/Want.pm
%{perl_vendorarch}/auto/Want/

%changelog
* Wed May 09 2007 Dries Verachtert <dries@ulyssis.org> - 0.14-1
- Updated to release 0.14.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.12-1
- Updated to release 0.12.

* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 0.10-1
- Updated to release 0.10.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 0.09-1
- Updated to release 0.09.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.08-1
- Initial package.
