# $Id$

# Authority: dries
# Upstream: T,J, Mather <tjmather$maxmind,com>


%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Crypt-OpenSSL-DSA

Summary: DSA encryption
Name: perl-Crypt-OpenSSL-DSA
Version: 0.11
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Crypt-OpenSSL-DSA/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://www.cpan.org/modules/by-module/Crypt/Crypt-OpenSSL-DSA-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, openssl-devel, krb5-devel

%description
Crypt::OpenSSL::DSA implements the DSA (Digital Signature Algorithm) 
signature verification system.

It is a thin XS wrapper to the DSA functions contained in the 
OpenSSL crypto library, located at http://www.openssl.org.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/Crypt/OpenSSL/DSA/.packlist
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod


%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README Changes
%{_mandir}/man3/*
%{perl_vendorarch}/Crypt/OpenSSL/DSA.pm
%{perl_vendorarch}/Crypt/OpenSSL/DSA/Signature.pod
%{perl_vendorarch}/auto/Crypt/OpenSSL/DSA/DSA.bs
%{perl_vendorarch}/auto/Crypt/OpenSSL/DSA/DSA.so

%changelog
* Wed Jun 16 2004 Dries Verachtert <dries@ulyssis.org> - 0.11-1
- Initial package.
