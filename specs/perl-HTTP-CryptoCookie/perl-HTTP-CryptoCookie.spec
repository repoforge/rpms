# $Id$
# Authority: dries
# Upstream: Dave Paris <a-mused$pobox,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name HTTP-CryptoCookie

Summary: Encrypted cookies
Name: perl-HTTP-CryptoCookie
Version: 1.14
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/HTTP-CryptoCookie/

Source: http://www.cpan.org/modules/by-module/HTTP/HTTP-CryptoCookie-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Convert::ASCII::Armour)
BuildRequires: perl(Crypt::CBC)
BuildRequires: perl(Digest::SHA256)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(FreezeThaw)

%description
HTTP::CryptoCookie provides a method for the secure storage and
transmitting of any perl data structure (except coderefs or other
objects, as are the normal restrictions for FreezeThaw).

The structure is frozen, compressed, encrypted, then ASCII-armoured
and finally sent to the browser.  The order reverses itself when
a cookie is read.

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/HTTP::CryptoCookie.3pm*
%dir %{perl_vendorlib}/HTTP/
#%{perl_vendorlib}/HTTP/CryptoCookie/
%{perl_vendorlib}/HTTP/CryptoCookie.pm

%changelog
* Thu Feb 28 2008 Dag Wieers <dag@wieers.com> - 1.14-1
- Updated to release 1.14.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 1.13-1
- Updated to release 1.13.

* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 1.12-1
- Updated to release 1.12.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 1.11-1
- Updated to release 1.11.

* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.10-1
- Initial package.
