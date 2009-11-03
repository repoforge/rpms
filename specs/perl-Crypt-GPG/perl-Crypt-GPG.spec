# $Id$
# Authority: dries
# Upstream: Ashish Gulhati <ashish$neomailbox,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Crypt-GPG

Summary: Object Oriented Interface to GnuPG
Name: perl-Crypt-GPG
Version: 1.63
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Crypt-GPG/

Source: http://www.cpan.org/modules/by-module/Crypt/Crypt-GPG-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
The Crypt::GPG module provides access to the functionality of the GnuPG
(www.gnupg.org) encryption tool through an object oriented interface.

It provides methods for encryption, decryption, signing, signature
verification, key generation, key certification, export and import.

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

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Crypt/GPG.pm

%changelog
* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 1.63-1
- Updated to release 1.63.

* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 1.61-1
- Updated to release 1.61.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.52-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.52-1
- Initial package.

