# $Id$
# Authority: dries
# Upstream: Benjamin Trott <cpan$stupidfool,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Crypt-DH

Summary: Diffie-Hellman key exchange system
Name: perl-Crypt-DH
Version: 0.06
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Crypt-DH/

Source: http://search.cpan.org/CPAN/authors/id/B/BT/BTROTT/Crypt-DH-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(Math::BigInt) >= 1.60

%description
This module implements the Diffie-Hellman key exchange system.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Cleaning up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/Crypt/
%{perl_vendorlib}/Crypt/DH.pm

%changelog
* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.06-1
- Initial package.
