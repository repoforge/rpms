# $Id: perl-Crypt-OpenSSL-X509.spec 5976 2007-11-09 20:21:26Z dag $
# Authority: dries
# Upstream: Dan Sully <daniel$cpan,org>
# Tests fail on el4 but not on el5
# ExcludeDist: el4 

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Crypt-OpenSSL-X509

Summary: Crypt::OpenSSL::X509 module
Name: perl-Crypt-OpenSSL-X509
Version: 1.0
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Crypt-OpenSSL-X509/

Source: http://search.cpan.org/CPAN/authors/id/D/DA/DANIEL/Crypt-OpenSSL-X509-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: openssl-devel

%description
This package contains the Crypt::OpenSSL::X509 module.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"
%{__make} test

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
%doc %{_mandir}/man3/Crypt::OpenSSL::X509.3pm*
%dir %{perl_vendorarch}/Crypt/
%dir %{perl_vendorarch}/Crypt/OpenSSL/
%{perl_vendorarch}/Crypt/OpenSSL/X509.pm
%dir %{perl_vendorarch}/auto/Crypt/
%dir %{perl_vendorarch}/auto/Crypt/OpenSSL/
%{perl_vendorarch}/auto/Crypt/OpenSSL/X509/

%changelog
* Sat Feb  6 2010 Christoph Maser <cmr@financial.com> - 1.0-1
- Updated to version 1.0.

* Thu Aug 21 2008 Dries Verachtert <dries@ulyssis.org> - 0.7-1
- Initial package.
