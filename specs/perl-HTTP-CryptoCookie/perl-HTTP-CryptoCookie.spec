# $Id$
# Authority: dries
# Upstream: Dave Paris <a-mused$pobox,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name HTTP-CryptoCookie

Summary: Encrypted cookies
Name: perl-HTTP-CryptoCookie
Version: 1.13
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/HTTP-CryptoCookie/

Source: http://www.cpan.org/modules/by-module/HTTP/HTTP-CryptoCookie-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)
BuildRequires: perl-SHA256
BuildRequires: perl-Crypt-CBC
BuildRequires: perl-Convert-ASCII-Armour
BuildRequires: perl-FreezeThaw

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
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/HTTP/CryptoCookie.pm

%changelog
* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 1.13-1
- Updated to release 1.13.

* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 1.12-1
- Updated to release 1.12.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 1.11-1
- Updated to release 1.11.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.10-1.2
- Rebuild for Fedora Core 5.

* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.10-1
- Initial package.
