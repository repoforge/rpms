# $Id: $

# Authority: dries
# Upstream:

%define real_name Digest-Nilsimsa

Summary: Nilsimsa algorithm
Name: perl-Digest-Nilsimsa
Version: 0.06
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Digest-Nilsimsa/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/V/VI/VIPUL/Digest-Nilsimsa-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
This module contains a perl version of the Nilsimsa code.

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
%doc README COPYING
%{_mandir}/man3/*
%{_libdir}/perl5/vendor_perl/*/i386-linux-thread-multi/Digest/Nilsimsa.pm
%{_libdir}/perl5/vendor_perl/*/i386-linux-thread-multi/auto/Digest/Nilsimsa/Nilsimsa.bs
%{_libdir}/perl5/vendor_perl/*/i386-linux-thread-multi/auto/Digest/Nilsimsa/Nilsimsa.so
%exclude %{_libdir}/perl5/*/i386-linux-thread-multi/perllocal.pod
%exclude %{_libdir}/perl5/vendor_perl/*/i386-linux-thread-multi/auto/*/*/.packlist

%changelog
* Wed Jun 16 2004 Dries Verachtert <dries@ulyssis.org> - 0.06-1
- Initial package.
