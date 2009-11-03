# $Id$
# Authority: dries
# Upstream: John Hughes <jhughes$frostburg,edu>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Crypt-Serpent

Summary: Crypt::CBC compliant Serpent block cipher encryption module
Name: perl-Crypt-Serpent
Version: 1.01
Release: 1.2%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Crypt-Serpent/

Source: http://www.cpan.org/modules/by-module/Crypt/Crypt-Serpent-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
"Serpent was designed by Ross Anderson, Eli Biham and Lars Knudsen
as a candidate for the Advanced Encryption Standard. It has been
selected as one of the five finalists in the AES competition.
Serpent is faster than DES and more secure than Triple DES. It
provides users with a very high level of assurance that no shortcut
attack will be found. To achieve this, the algorithm's designers
limited themselves to well understood cryptography mechanisms, so
that they could rely on the wide experience and proven techniques
of block cipher cryptanalysis. The algorithm uses twice as many
rounds as are necessary to block all currently known shortcut
attacks. This means that Serpent should be safe against as yet
unknown attacks that may be capable of breaking the standard 16
rounds used in many types of encryption today. However, the fact
that Serpent uses so many rounds means that it is the slowest of
the five AES finalists. But this shouldn't be an issue because it
still outperforms Triple DES. The algorithm's designers maintain
that Serpent has a service life of at least a century."

"Serpent is a 128-bit block cipher, meaning that data is encrypted
and decrypted in 128-bit chunks. The key length can vary, but for
the purposes of the AES it is defined to be either 128, 192, or 256
bits. This block size and variable key length is standard among all
AES candidates and was one of the major design requirements specified
by NIST. The Serpent algorithm uses 32 rounds, or iterations of the
main algorithm."

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES README
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorarch}/Crypt/
%{perl_vendorarch}/Crypt/Serpent.pm
%dir %{perl_vendorarch}/auto/Crypt/
%{perl_vendorarch}/auto/Crypt/Serpent/

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.01-1.2
- Rebuild for Fedora Core 5.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 1.01-1
- Initial package.
