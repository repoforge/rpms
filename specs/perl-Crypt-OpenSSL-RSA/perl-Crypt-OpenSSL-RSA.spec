# $Id$

# Authority: dries
# Upstream:

%define real_name Crypt-OpenSSL-RSA
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: RSA encoding and decoding
Name: perl-Crypt-OpenSSL-RSA
Version: 0.21
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Crypt-OpenSSL-RSA/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/I/IR/IROBERTS/Crypt-OpenSSL-RSA-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, openssl-devel
Requires: openssl

%description
Crypt::OpenSSL::RSA is an XS perl module designed to provide basic RSA
functionality.  It does this by providing a glue to the RSA functions
in the OpenSSL library.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" destdir=%{buildroot}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README Changes
%{_mandir}/man3/*
%{perl_vendorarch}/Crypt/OpenSSL/RSA.pm
%exclude %{perl_vendorarch}/auto/Crypt/OpenSSL/RSA/.packlist
%{perl_vendorarch}/auto/Crypt/OpenSSL/RSA/*
%exclude %{perl_archlib}/perllocal.pod

%changelog
* Wed Jun 16 2004 Dries Verachtert <dries@ulyssis.org> - 0.21-1
- Initial package.
