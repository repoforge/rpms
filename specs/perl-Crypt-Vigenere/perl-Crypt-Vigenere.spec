# $Id$

# Authority: dries
# Upstream: Alistair Francis <alizta$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Crypt-Vigenere

Summary: Implementation of the Vigenere cipher
Name: perl-Crypt-Vigenere
Version: 0.07
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Crypt-Vigenere/

Source: http://www.cpan.org/modules/by-module/Crypt/Crypt-Vigenere-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This modules allows you to recreate the workings of the cryptographic
cipher invented several hundred years ago by a French cryptographer,
Blaise de Vigenère. 

The Crypt::Vigenere module accepts only alpha characters in the keyword
and will return an undefined object if any other characters are entered.
The module also only encrypts/decrypts alpha characters, any other 
characters will be stripped out of the resulting encrption/decryption.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README Changes
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Crypt/Vigenere.pm

%changelog
* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 0.07-1
- Initial package.
