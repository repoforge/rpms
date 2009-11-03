# $Id$
# Authority: dries
# Upstream: Dave Paris <a-mused$pobox,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Crypt-Blowfish

Summary: Perl Blowfish encryption module
Name: perl-Crypt-Blowfish
Version: 2.10
Release: 1.2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Crypt-Blowfish/

Source: http://www.cpan.org/modules/by-module/Crypt/Crypt-Blowfish-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This is Crypt::Blowfish version, an XS-based implementation of the
Blowfish cryptography algorithm designed by Bruce Schneier.  It's designed
to take full advantage of Crypt::CBC when desired.  Blowfish keys may be
up to 448 bits (56 bytes) long.

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
%dir %{perl_vendorarch}/Crypt/
%{perl_vendorarch}/Crypt/Blowfish.pm
%dir %{perl_vendorarch}/auto/Crypt/
%{perl_vendorarch}/auto/Crypt/Blowfish/

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 2.10-1.2
- Rebuild for Fedora Core 5.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 2.10-1
- Updated to release 2.10.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 2.09-1
- Initial package.
