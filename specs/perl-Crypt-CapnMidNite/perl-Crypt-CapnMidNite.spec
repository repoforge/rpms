# $Id$

# Authority: dries
# Upstream: Michael Robinton <michael$bizsystems,com>

%define real_name Crypt-CapnMidNite
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Perl interface to MD5, RC4, encrypt/decrypt
Name: perl-Crypt-CapnMidNite
Version: 1.00
Release: 2
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Crypt-CapnMidNite/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

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
%{__perl} Makefile.PL INSTALLDIRS="vendor" destdir=%{buildroot}
%{__make} %{?_smp_mflags}
%{__mv} Makefile Makefile.CapnMidNite
%{__perl} -pi -e 's|= \(1\)|= \(0\)|g;' Makefile.PL
%{__perl} Makefile.PL INSTALLDIRS="vendor" destdir=%{buildroot}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall -f Makefile.CapnMidNite
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README Changes
%doc %{_mandir}/man3/*
%{perl_vendorarch}/Crypt/CapnMidNite.pm
%{perl_vendorarch}/Crypt/C_LockTite.pm
%{perl_vendorarch}/auto/Crypt/CapnMidNite
%{perl_vendorarch}/auto/Crypt/C_LockTite
%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/.packlist

%changelog
* Sat Dec 11 2004 Dries Verachtert <dries@ulyssis.org> - 1.00-2
- Figured out how to build the Crypt::C_LockTite module

* Tue Dec 07 2004 Dries Verachtert <dries@ulyssis.org> - 1.00-1
- Initial package.
