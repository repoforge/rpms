# $Id$
# Authority: dries
# Upstream: Rafael R. Sevilla <sevillar$team,ph,inter,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name SHA256

Summary: Implements the SHA-256/384/512 hash algorithm
Name: perl-SHA256
Version: 0.01b
Release: 1.2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/SHA256/

Source: http://www.cpan.org/authors/id/D/DI/DIDO/SHA256-%{version}b.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This module implements the SHA-256/384/512 hash algorithm developed by
NIST.

%prep
%setup -n %{real_name}-0.01

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
%doc README
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorarch}/auto/Digest/
%{perl_vendorarch}/auto/Digest/SHA256/
%dir %{perl_vendorarch}/Digest/
#%{perl_vendorarch}/Digest/SHA256/
%{perl_vendorarch}/Digest/SHA256.pm
%{perl_vendorarch}/Digest/SHA256.pod
%{perl_vendorarch}/Digest/sha256.pod

%changelog
* Wed Dec 21 2005 Dries Verachtert <dries@ulyssis.org> - 0.01b-1
- Initial package.
