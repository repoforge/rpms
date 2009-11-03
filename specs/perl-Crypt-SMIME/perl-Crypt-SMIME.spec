# $Id$
# Authority: dag
# Upstream: <mikage$ymir,co,jp>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Crypt-SMIME

Summary: S/MIME message signing, verification, encryption and decryption
Name: perl-Crypt-SMIME
Version: 0.09
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Crypt-SMIME/

Source: http://www.cpan.org/modules/by-module/Crypt/Crypt-SMIME-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
S/MIME message signing, verification, encryption and decryption.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST MANIFEST.SKIP META.yml README
%doc %{_mandir}/man3/SMIME.3pm*
%doc %{_mandir}/man3/SMIME::JA.3pm*
%dir %{perl_vendorarch}/auto/Crypt/
%{perl_vendorarch}/auto/Crypt/SMIME/
%dir %{perl_vendorarch}/Crypt/
%{perl_vendorarch}/Crypt/SMIME/
%{perl_vendorarch}/Crypt/SMIME.pm

%changelog
* Tue Oct 07 2008 Dag Wieers <dag@wieers.com> - 0.09-1
- Updated to release 0.09.

* Tue Aug 19 2008 Dag Wieers <dag@wieers.com> - 0.08-1
- Initial package. (using DAR)
