# $Id$
# Authority: dries
# Upstream: Christophe Wolfhugel <wolf$oleane,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Msgcat

Summary: Support for XPG4 message catalog functions
Name: perl-Msgcat
Version: 1.03
Release: 1.2%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Msgcat/

Source: http://www.cpan.org/authors/id/C/CH/CHRWOLF/Msgcat-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This module contains support for XPG4 message catalog functions  : catopen(3), catgets(3) and catclose(4).

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist


%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%{_mandir}/man3/*.3pm*
%dir %{perl_vendorarch}/Locale/
%{perl_vendorarch}/Locale/Msgcat.pm
%dir %{perl_vendorarch}/auto/Locale/
%{perl_vendorarch}/auto/Locale/Msgcat/

%changelog
* Wed Jun 16 2004 Dries Verachtert <dries@ulyssis.org> - 1.03-1
- Initial package.
