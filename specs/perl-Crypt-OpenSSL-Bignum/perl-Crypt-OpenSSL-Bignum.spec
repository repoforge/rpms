# $Id$
# Authority: dries
# Upstream: Ian Robertson <iroberts+perl$red-bean,com>

### EL6 ships with perl-Crypt-OpenSSL-Bignum-0.04-8.1.el6
%{?el6:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Crypt-OpenSSL-Bignum

Summary: OpenSSL's multiprecision integer arithmetic
Name: perl-Crypt-OpenSSL-Bignum
Version: 0.04
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Crypt-OpenSSL-Bignum/

Source: http://www.cpan.org/modules/by-module/Crypt/Crypt-OpenSSL-Bignum-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: openssl-devel
BuildRequires: krb5-devel

%description
Crypt::OpenSSL::Bignum is an XS perl module designed to provide basic
access to the OpenSSL multiprecision integer arithmetic libraries.
Presently, many though not all of the arithmetic operations that
OpenSSL provides are exposed to perl.  In addition, this module can be
used to provide access to bignum values produced by other OpenSSL
modules, such as key parameters from Crypt::OpenSSL::RSA.  This module
requires that the OpenSSL libraries and header files be installed.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}" INC="-I/usr/kerberos/include"
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
%doc Changes LICENSE MANIFEST META.yml README
%doc %{_mandir}/man3/Crypt::OpenSSL::Bignum.3pm*
%doc %{_mandir}/man3/Crypt::OpenSSL::Bignum::CTX.3pm*
%dir %{perl_vendorarch}/Crypt/
%dir %{perl_vendorarch}/Crypt/OpenSSL/
%{perl_vendorarch}/Crypt/OpenSSL/Bignum/
%{perl_vendorarch}/Crypt/OpenSSL/Bignum.pm
%dir %{perl_vendorarch}/auto/Crypt/
%dir %{perl_vendorarch}/auto/Crypt/OpenSSL/
%{perl_vendorarch}/auto/Crypt/OpenSSL/Bignum/

%changelog
* Thu Nov 08 2007 Dag Wieers <dag@wieers.com> - 0.04-1
- Updated to release 0.04.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 0.03-1
- Initial package.
