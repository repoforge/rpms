# $Id$
# Authority: dries
# Upstream: Nikolay Pelov <pelov$cs,kuleuven,ac,be>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Authen-PAM

Summary: Interface to the PAM library
Name: perl-Authen-PAM
Version: 0.16
Release: 1.2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Authen-PAM/

Source: http://www.cpan.org/modules/by-module/Authen/Authen-PAM-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: pam-devel

%description
This module provides a Perl interface to the PAM library.

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorarch}/Authen/
%{perl_vendorarch}/Authen/PAM/
%{perl_vendorarch}/Authen/PAM.pm
%dir %{perl_vendorarch}/auto/Authen/
%{perl_vendorarch}/auto/Authen/PAM/

%changelog
* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 0.16-1
- Updated to release 0.16.

* Wed Dec 29 2004 Dries Verachtert <dries@ulyssis.org> - 0.15-1
- Updated to release 0.15.

* Wed Jun 16 2004 Dries Verachtert <dries@ulyssis.org> - 0.14-1
- Initial package.

