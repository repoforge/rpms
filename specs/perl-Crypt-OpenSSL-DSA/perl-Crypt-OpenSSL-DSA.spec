# $Id$

# Authority: dries
# Upstream:

%define real_name Crypt-OpenSSL-DSA
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: DSA encryption
Name: perl-Crypt-OpenSSL-DSA
Version: 0.11
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Crypt-OpenSSL-DSA/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/T/TJ/TJMATHER/Crypt-OpenSSL-DSA-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, openssl-devel

%description
Crypt::OpenSSL::DSA implements the DSA (Digital Signature Algorithm) 
signature verification system.

It is a thin XS wrapper to the DSA functions contained in the 
OpenSSL crypto library, located at http://www.openssl.org.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" destdir=%{buildroot}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README Changes
%{_mandir}/man3/*
%{perl_vendorarch}/Crypt/OpenSSL/DSA.pm
%{perl_vendorarch}/Crypt/OpenSSL/DSA/Signature.pod
%exclude %{perl_vendorarch}/auto/Crypt/OpenSSL/DSA/.packlist
%{perl_vendorarch}/auto/Crypt/OpenSSL/DSA/DSA.bs
%{perl_vendorarch}/auto/Crypt/OpenSSL/DSA/DSA.so
%exclude %{perl_archlib}/perllocal.pod

%changelog
* Wed Jun 16 2004 Dries Verachtert <dries@ulyssis.org> - 0.11-1
- Initial package.
