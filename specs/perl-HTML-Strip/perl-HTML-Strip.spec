# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name HTML-Strip

Summary: Perl module to strip HTML-like markup from text.
Name: perl-HTML-Strip
Version: 1.06
Release: 1%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/HTML-Strip/

Source: http://www.cpan.org/modules/by-module/HTML/HTML-Strip-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl >= 0:5.006
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl >= 0:5.006

%description
This module strips HTML-like markup from text.  It is written in XS,
and thus about five times quicker than using regular expressions for
the same task.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST README
%doc %{_mandir}/man3/*.3pm*
%{perl_vendorarch}/auto/HTML/
%{perl_vendorarch}/HTML/

%changelog
* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 1.06-1
- Updated to release 1.06.

* Sat Feb 12 2005 Dag Wieers <dag@wieers.com> - 1.04-1
- Initial package. (using DAR)
