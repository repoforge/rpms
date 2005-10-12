# $Id$
# Authority: dries
# Upstream: Michael Robinton <michael$bizsystems,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Crypt-CapnMidNite

Summary: Perl interface to MD5, RC4, encrypt/decrypt
Name: perl-Crypt-CapnMidNite
Version: 1.00
Release: 2
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Crypt-CapnMidNite/

Source: http://search.cpan.org/CPAN/authors/id/M/MI/MIKER/Crypt-CapnMidNite-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
Perl interface to MD5, RC4, and modified asymetric RC4 
encryption/decryption methods. The module is named for its 
functionality as a swiss army knife of encode/decode, hash 
methods or... in the old days, the Captain Midnight Decoder Ring.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%{__mv} Makefile Makefile.CapnMidNite
%{__perl} -pi -e 's|= \(1\)|= \(0\)|g;' Makefile.PL

CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall -f Makefile.CapnMidNite
%makeinstall

### Clean up buildroot  
%{__rm} -rf %{buildroot}%{perl_archlib} \
		%{buildroot}%{perl_vendorarch}/auto/*{,/*{,/*}}/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%dir %{perl_vendorarch}/Crypt/
%{perl_vendorarch}/Crypt/CapnMidNite.pm
%{perl_vendorarch}/Crypt/C_LockTite.pm
%dir %{perl_vendorarch}/auto/Crypt/
%{perl_vendorarch}/auto/Crypt/CapnMidNite/
%{perl_vendorarch}/auto/Crypt/C_LockTite/

%changelog
* Sat Dec 11 2004 Dries Verachtert <dries@ulyssis.org> - 1.00-2
- Figured out how to build the Crypt::C_LockTite module

* Tue Dec 07 2004 Dries Verachtert <dries@ulyssis.org> - 1.00-1
- Initial package.
