# $Id$
# Authority: dries
# Upstream: Abhijit Menon-Sen <ams$wiw,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Crypt-Twofish

Summary: Twofish Encryption Algorithm
Name: perl-Crypt-Twofish
Version: 2.13
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Crypt-Twofish/

Source: http://www.cpan.org/modules/by-module/Crypt/Crypt-Twofish-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Twofish is a 128-bit symmetric block cipher with a variable
length (128, 192, or 256-bit) key, developed by Counterpane
Labs. It is unpatented and free for all uses, as described at
URL:http://www.counterpane.com/twofish.html.

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
%{perl_vendorarch}/Crypt/Twofish.pm
%dir %{perl_vendorarch}/auto/Crypt/
%{perl_vendorarch}/auto/Crypt/Twofish/

%changelog
* Thu Jul  9 2009 Christoph Maser <cmr@financial.com> - 2.13-1
- Updated to version 2.13.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 2.12-1
- Initial package.
