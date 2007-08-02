# $Id$
# Authority: dries
# Upstream: Lincoln D. Stein <lstein$cshl,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Crypt-CBC

Summary: Encrypt Data with Cipher Block Chaining Mode
Name: perl-Crypt-CBC
Version: 2.22
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Crypt-CBC/

Source: http://search.cpan.org/CPAN/authors/id/L/LD/LDS/Crypt-CBC-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This is Crypt::CBC, a Perl-only implementation of the cryptographic
cipher block chaining mode (CBC).  In combination with a block cipher
such as Crypt::DES or Crypt::IDEA, you can encrypt and decrypt
messages of arbitrarily long length.  The encrypted messages are
compatible with the encryption format used by B<SSLeay>.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Crypt/CBC.pm

%changelog
* Tue Nov 14 2006 Dries Verachtert <dries@ulyssis.org> - 2.22-1
- Updated to release 2.22.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 2.19-1
- Updated to release 2.19.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 2.17-1
- Updated to release 2.17.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 2.15-1.2
- Rebuild for Fedora Core 5.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 2.15-1
- Updated to release 2.15.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 2.14-1
- Updated to release 2.14.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 2.12-1
- Initial package.
