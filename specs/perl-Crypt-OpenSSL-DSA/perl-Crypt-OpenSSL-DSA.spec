# $Id: $

# Authority: dries
# Upstream:

%define real_name Crypt-OpenSSL-DSA

Summary: DSA encryption
Name: perl-Crypt-OpenSSL-DSA
Version: 0.11
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Crypt-OpenSSL-DSA/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/T/TJ/TJMATHER/Crypt-OpenSSL-DSA-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
Crypt::OpenSSL::DSA implements the DSA (Digital Signature Algorithm) 
signature verification system.

It is a thin XS wrapper to the DSA functions contained in the 
OpenSSL crypto library, located at http://www.openssl.org.

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
%{_libdir}/perl5/vendor_perl/*/i386-linux-thread-multi/Crypt/OpenSSL/DSA.pm
%{_libdir}/perl5/vendor_perl/*/i386-linux-thread-multi/Crypt/OpenSSL/DSA/Signature.pod
%exclude %{_libdir}/perl5/vendor_perl/*/i386-linux-thread-multi/auto/Crypt/OpenSSL/DSA/.packlist
%{_libdir}/perl5/vendor_perl/*/i386-linux-thread-multi/auto/Crypt/OpenSSL/DSA/DSA.bs
%{_libdir}/perl5/vendor_perl/*/i386-linux-thread-multi/auto/Crypt/OpenSSL/DSA/DSA.so
%exclude %{_libdir}/perl5/*/i386-linux-thread-multi/perllocal.pod

%changelog
* Wed Jun 16 2004 Dries Verachtert <dries@ulyssis.org> - 0.11-1
- Initial package.
