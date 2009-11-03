# $Id$
# Authority: dag
# Upstream: Gisle Aas <gisle$ActiveState,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Unicode-String

Summary: Unicode-String (String of Unicode characters (UCS2/UTF16)) module for perl
Name: perl-Unicode-String
Version: 2.09
Release: 1.2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Unicode-String/

Source: http://www.cpan.org/modules/by-module/Unicode/Unicode-String-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl

%description
Unicode-String (String of Unicode characters (UCS2/UTF16)) module for perl.

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
%doc %{_mandir}/man3/Unicode::CharName.3pm*
%doc %{_mandir}/man3/Unicode::String.3pm*
%dir %{perl_vendorarch}/Unicode/
%{perl_vendorarch}/Unicode/CharName.pm
%{perl_vendorarch}/Unicode/String.pm
%dir %{perl_vendorarch}/auto/Unicode/
%{perl_vendorarch}/auto/Unicode/String/

%changelog
* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 2.09-1
- Updated to release 2.09.

* Wed Jan 21 2004 Dag Wieers <dag@wieers.com> - 2.07-0
- Initial package. (using DAR)
