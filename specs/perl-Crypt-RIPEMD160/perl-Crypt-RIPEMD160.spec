# $Id$
# Authority: dries
# Upstream: Christian H. Geuer-Pollmann <geuer-pollmann$nue,et-inf,uni-siegen,de>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Crypt-RIPEMD160

Summary: RIPEMD-160 HASH and MAC function
Name: perl-Crypt-RIPEMD160
Version: 0.04
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Crypt-RIPEMD160/

Source: http://search.cpan.org/CPAN/authors/id/C/CH/CHGEUER/Crypt-RIPEMD160-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

#BuildArch: noarch
BuildRequires: perl

%description
Perl extension for RIPEMD-160 HASH and MAC function.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%doc %{_mandir}/man3/*
%{perl_vendorarch}/Crypt/RIPEMD160.pm
%{perl_vendorarch}/Crypt/RIPEMD160
%{perl_vendorarch}/auto/Crypt/RIPEMD160

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.04-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.04-1
- Initial package.
