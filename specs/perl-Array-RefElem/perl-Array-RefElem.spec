# $Id: $

# Authority: dries
# Upstream:

%define real_name Array-RefElem

Summary: Use references as elements in hashes and arrays
Name: perl-Array-RefElem
Version: 1.00
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Array-RefElem/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/G/GA/GAAS/Array-RefElem-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
This module give direct access to the internal perl routines that let
you store reference to things in arrays and hashes.

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
%{_libdir}/perl5/vendor_perl/*/i386-linux-thread-multi/Array/RefElem.pm
%{_libdir}/perl5/vendor_perl/*/i386-linux-thread-multi/auto/Array/RefElem/RefElem.*
%exclude %{_libdir}/perl5/*/i386-linux-thread-multi/perllocal.pod
%exclude %{_libdir}/perl5/vendor_perl/*/i386-linux-thread-multi/auto/Array/RefElem/.packlist

%changelog
* Sat Jun 15 2004 Dries Verachtert <dries@ulyssis.org> - 1.00-1
- Initial package.
