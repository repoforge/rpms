# $Id: $

# Authority: dries
# Upstream:

%define real_name Authen-SASL

Summary: Interface to SASL
Name: perl-Authen-SASL
Version: 2.08
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Authen-SASL/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/G/GB/GBARR/Authen-SASL-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
This module permits authentication with SASL.

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
%doc api.txt example_pl Changes
%{_mandir}/man3/*
%{_libdir}/perl5/vendor_perl/*/Authen/SASL.pm
%{_libdir}/perl5/vendor_perl/*/Authen/SASL.pod
%{_libdir}/perl5/vendor_perl/*/Authen/SASL/*
%exclude %{_libdir}/perl5/*/i386-linux-thread-multi/perllocal.pod
%exclude %{_libdir}/perl5/vendor_perl/*/i386-linux-thread-multi/auto/*/*/.packlist

%changelog
* Wed Jun 16 2004 Dries Verachtert <dries@ulyssis.org> - 2.08-1
- Initial package.
