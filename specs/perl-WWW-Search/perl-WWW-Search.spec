# $Id$

# Authority: dries
# Upstream: Martin 'Kingpin' Thurn <mthurn$verizon,net>

%define real_name WWW-Search
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Perl module for WWW searches.
Name: perl-WWW-Search
Version: 2.476
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/WWW-Search/

Source: http://search.cpan.org/CPAN/authors/id/M/MT/MTHURN/WWW-Search-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This module contains functions for WWW searches.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} -pi -e 's|/usr/local/bin/perl|%{_bindir}/perl|g;' lib/WWW/Search/*.pm
%{__perl} Makefile.PL INSTALLDIRS="vendor" destdir=%{buildroot}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README ChangeLog
%doc %{_mandir}/man3/*
%doc %{_mandir}/man1/*
%{_bindir}/AutoSearch
%{_bindir}/WebSearch
%{perl_vendorlib}/WWW/Search.pm
%{perl_vendorlib}/WWW/SearchResult.pm
%{perl_vendorlib}/WWW/Search/*
%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/.packlist

# perl_vendorlib: /usr/lib/perl5/vendor_perl/5.8.0
# perl_vendorarch: /usr/lib/perl5/vendor_perl/5.8.0/i386-linux-thread-multi
# perl_archlib: /usr/lib/perl5/5.8.0/i386-linux-thread-multi
# perl_privlib: /usr/lib/perl5/5.8.0

%changelog
* Fri Mar  4 2005 Dries Verachtert <dries@ulyssis.org> - 2.476-1
- Updated to release 2.476.

* Tue Dec 07 2004 Dries Verachtert <dries@ulyssis.org> - 2.475
- Initial package.
