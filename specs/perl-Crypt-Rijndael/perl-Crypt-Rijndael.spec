# $Id$
# Authority: dries
# Upstream: Rafael R. Sevilla <sevillar$team,ph,inter,net>
# Upstream: Brian D Foy <bdfoy$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Crypt-Rijndael

Summary: Crypt::CBC compliant Rijndael encryption module
Name: perl-Crypt-Rijndael
Version: 1.07
Release: 1
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Crypt-Rijndael/

Source: http://www.cpan.org/modules/by-module/Crypt/Crypt-Rijndael-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This is Crypt::Rijndael, an XS-based implementation of the newly-selected
Advanced Encryption Standard algorithm Rijndael, designed by Joan Daemen
and Vincent Rijmen.

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

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING Changes LICENSE MANIFEST META.yml NEWS README examples/
%doc %{_mandir}/man3/Crypt::Rijndael.3*
%dir %{perl_vendorarch}/auto/Crypt/
%{perl_vendorarch}/auto/Crypt/Rijndael/
%dir %{perl_vendorarch}/Crypt/
%{perl_vendorarch}/Crypt/Rijndael.pm

%changelog
* Tue Oct 07 2008 Dag Wieers <dag@wieers.com> - 1.07-1
- Updated to release 1.07.

* Sun May 04 2008 Dag Wieers <dag@wieers.com> - 1.06-1
- Updated to release 1.06.

* Tue Nov 13 2007 Dag Wieers <dag@wieers.com> - 1.05-1
- Updated to release 1.05.

* Fri Jul 06 2007 Dag Wieers <dag@wieers.com> - 1.04-1
- Updated to release 1.04.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 0.05-1
- Initial package.
