# $Id: $

# Authority: dries
# Upstream:

%define real_name Digest-MD2

Summary: Interface to the MD2 algorithm
Name: perl-Digest-MD2
Version: 2.03
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Digest-MD2/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/G/GA/GAAS/Digest-MD2-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
The Digest::MD2 module allows you to use the RSA Data Security
Inc. MD2 Message Digest algorithm from within Perl programs.  The
algorithm takes as input a message of arbitrary length and produces as
output a 128-bit "fingerprint" or "message digest" of the input.

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
%{_libdir}/perl5/vendor_perl/*/i386-linux-thread-multi/Digest/MD2.pm
%{_libdir}/perl5/vendor_perl/*/i386-linux-thread-multi/auto/Digest/MD2/MD2.bs
%{_libdir}/perl5/vendor_perl/*/i386-linux-thread-multi/auto/Digest/MD2/MD2.so
%exclude %{_libdir}/perl5/*/i386-linux-thread-multi/perllocal.pod
%exclude %{_libdir}/perl5/vendor_perl/*/i386-linux-thread-multi/auto/*/*/.packlist

%changelog
* Wed Jun 16 2004 Dries Verachtert <dries@ulyssis.org> - 2.03-1
- Initial package.
