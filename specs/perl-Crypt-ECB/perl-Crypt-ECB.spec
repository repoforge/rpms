# $Id$
# Authority: dries
# Upstream: Christoph Appel <cappel$web,de>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Crypt-ECB

Summary: Encrypt Data using ECB Mode
Name: perl-Crypt-ECB
Version: 1.45
Release: 1%{?dist}
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Crypt-ECB/

Source: http://www.cpan.org/modules/by-module/Crypt/Crypt-ECB-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This module is a Perl-only implementation of the ECB mode. In
combination with a block cipher such as DES, IDEA or Blowfish, you can
encrypt and decrypt messages of arbitrarily long length. Though for
security reasons other modes than ECB such as CBC should be preferred.
See textbooks on cryptography if you want to know why.

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
%doc CHANGES COPYING MANIFEST META.yml README
%doc %{_mandir}/man3/Crypt::ECB.3pm*
%dir %{perl_vendorlib}/Crypt/
#%{perl_vendorlib}/Crypt/ECB/
%{perl_vendorlib}/Crypt/ECB.pm

%changelog
* Tue Oct 07 2008 Dag Wieers <dag@wieers.com> - 1.45-1
- Updated to release 1.45.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.40-1
- Initial package.
