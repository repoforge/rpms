# $Id$
# Authority: dries
# Upstream: Lincoln D. Stein <lstein$cshl,edu>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Crypt-CBC

Summary: Encrypt Data with Cipher Block Chaining Mode
Name: perl-Crypt-CBC
Version: 2.30
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Crypt-CBC/

Source: http://www.cpan.org/authors/id/L/LD/LDS/Crypt-CBC-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

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
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

### Clean up docs
find eg/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST README eg/
%doc %{_mandir}/man3/Crypt::CBC.3pm*
%dir %{perl_vendorlib}/Crypt/
#%{perl_vendorlib}/Crypt/CBC/
%{perl_vendorlib}/Crypt/CBC.pm

%changelog
* Thu Jul  9 2009 Christoph Maser <cmr@financial.com> - 2.30-1
- Updated to version 2.30.

* Mon Nov 19 2007 Dag Wieers <dag@wieers.com> - 2.24-1
- Updated to release

* Tue Nov 14 2006 Dries Verachtert <dries@ulyssis.org> - 2.22-1
- Updated to release 2.22.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 2.19-1
- Updated to release 2.19.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 2.17-1
- Updated to release 2.17.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 2.15-1
- Updated to release 2.15.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 2.14-1
- Updated to release 2.14.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 2.12-1
- Initial package.
