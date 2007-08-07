# $Id: perl-Crypt-OpenSSL-RSA.spec 4890 2006-11-17 22:09:23Z dries $
# Authority: dries
# Upstream: Ian Robertson <iroberts+perl$red-bean,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Crypt-OpenSSL-RSA

Summary: RSA encoding and decoding
Name: perl-Crypt-OpenSSL-RSA
Version: 0.24
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Crypt-OpenSSL-RSA/

Source: http://search.cpan.org/CPAN/authors/id/I/IR/IROBERTS/Crypt-OpenSSL-RSA-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, openssl-devel, krb5-devel
Requires: openssl

%description
Crypt::OpenSSL::RSA is an XS perl module designed to provide basic RSA
functionality.  It does this by providing a glue to the RSA functions
in the OpenSSL library.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}" INC="-I/usr/kerberos/include"

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/Crypt/OpenSSL/RSA/.packlist
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%{_mandir}/man3/*.3pm*
%dir %{perl_vendorarch}/Crypt/
%dir %{perl_vendorarch}/Crypt/OpenSSL/
%{perl_vendorarch}/Crypt/OpenSSL/RSA.pm
%dir %{perl_vendorarch}/auto/Crypt/
%dir %{perl_vendorarch}/auto/Crypt/OpenSSL/
%{perl_vendorarch}/auto/Crypt/OpenSSL/RSA/

%changelog
* Tue Nov 14 2006 Dries Verachtert <dries@ulyssis.org> - 0.24-1
- Updated to release 0.24.

* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 0.23-1
- Updated to release 0.23.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.22-1.2
- Rebuild for Fedora Core 5.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 0.22-1
- Updated to release 0.22.

* Wed Jun 16 2004 Dries Verachtert <dries@ulyssis.org> - 0.21-1
- Initial package.
