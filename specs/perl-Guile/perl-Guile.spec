# $Id$
# Authority: dries
# Upstream: Matt S Trout <perl-stuff$trout,me,uk>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Guile

Summary: Interface to the Guile Scheme interpreter
Name: perl-Guile
Version: 0.002
Release: 1.2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Guile/

Source: http://www.cpan.org/modules/by-module/Guile/Guile-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: guile-devel
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This module provides an interface to the Gnu Guile system.

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
%{perl_vendorarch}/Guile.pm
%{perl_vendorarch}/Guile/
%{perl_vendorarch}/auto/Guile/

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.002-1
- Initial package.
