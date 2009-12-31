# $Id$

# Authority: dries
# Upstream: Alistair Francis <alizta$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Crypt-Vigenere

Summary: Implementation of the Vigenere cipher
Name: perl-Crypt-Vigenere
Version: 0.08
Release: 1%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Crypt-Vigenere/

Source: http://search.cpan.org/CPAN/authors/id/F/FR/FRIFFIN/Crypt-Vigenere-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

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
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Crypt/Vigenere.pm

%changelog
* Thu Dec 31 2009 Christoph Maser <cmr@financial.com> - 0.08-1
- Updated to version 0.08.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.07-1.2
- Rebuild for Fedora Core 5.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 0.07-1
- Initial package.
