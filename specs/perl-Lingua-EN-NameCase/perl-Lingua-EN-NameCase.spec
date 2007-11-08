# $Id$
# Authority: dries
# Upstream: Mark Summerfield <summer$qtrac,eu>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Lingua-EN-NameCase

Summary: Perl module to fix the case of people's names
Name: perl-Lingua-EN-NameCase
Version: 1.14
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Lingua-EN-NameCase/

Source: http://search.cpan.org//CPAN/authors/id/S/SU/SUMMER/Lingua-EN-NameCase-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Perl module to fix the case of people's names.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
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
%doc README
%doc %{_mandir}/man3/Lingua::EN::NameCase*
%{perl_vendorlib}/Lingua/EN/NameCase.pm
%dir %{perl_vendorlib}/Lingua/EN/

%changelog
* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 1.14-1
- Initial package.
