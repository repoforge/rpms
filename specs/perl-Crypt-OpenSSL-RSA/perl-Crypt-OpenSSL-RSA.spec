# $Id: $

# Authority: dries
# Upstream:

%define real_name Crypt-OpenSSL-RSA

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

BuildRequires: perl
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
%{_libdir}/perl5/vendor_perl/*/i386-linux-thread-multi/Crypt/OpenSSL/RSA.pm
%exclude %{_libdir}/perl5/vendor_perl/*/i386-linux-thread-multi/auto/Crypt/OpenSSL/RSA/.packlist
/usr/lib/perl5/vendor_perl/*/i386-linux-thread-multi/auto/Crypt/OpenSSL/RSA/*
%exclude %{_libdir}/perl5/*/i386-linux-thread-multi/perllocal.pod

%changelog
* Wed Jun 16 2004 Dries Verachtert <dries@ulyssis.org> - 0.21-1
- Initial package.
