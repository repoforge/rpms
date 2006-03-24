# $Id$

# Authority: dries
# Upstream: Ian Robertson <iroberts+perl$red-bean,com>


%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Crypt-OpenSSL-RSA

Summary: RSA encoding and decoding
Name: perl-Crypt-OpenSSL-RSA
Version: 0.22
Release: 1.2
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Crypt-OpenSSL-RSA/

Source: http://search.cpan.org/CPAN/authors/id/C/CD/CDRAKE/Crypt-OpenSSL-RSA-%{version}.tar.gz
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
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}" INC=-I/usr/kerberos/include

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
%{_mandir}/man3/*
%{perl_vendorarch}/Crypt/OpenSSL/RSA.pm
%{perl_vendorarch}/auto/Crypt/OpenSSL/RSA/*

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.22-1.2
- Rebuild for Fedora Core 5.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 0.22-1
- Updated to release 0.22.

* Wed Jun 16 2004 Dries Verachtert <dries@ulyssis.org> - 0.21-1
- Initial package.
