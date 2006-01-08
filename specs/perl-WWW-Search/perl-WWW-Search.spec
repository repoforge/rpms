# $Id$
# Authority: dries
# Upstream: Martin 'Kingpin' Thurn <mthurn$verizon,net>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name WWW-Search

Summary: Perl module for WWW searches.
Name: perl-WWW-Search
Version: 2.484
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/WWW-Search/

Source: http://www.cpan.org/modules/by-module/WWW/WWW-Search-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This module contains functions for WWW searches.

%prep
%setup -n %{real_name}-%{version}

%{__perl} -pi -e 's|/usr/local/bin/perl|%{_bindir}/perl|g;' lib/WWW/Search/*.pm

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} \
		%{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog README
%doc %{_mandir}/man3/*
%doc %{_mandir}/man1/*
%{_bindir}/AutoSearch
%{_bindir}/WebSearch
%dir %{perl_vendorlib}/WWW/
%{perl_vendorlib}/WWW/Search.pm
%{perl_vendorlib}/WWW/SearchResult.pm
%{perl_vendorlib}/WWW/Search/

%changelog
* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 2.484-1
- Updated to release 2.484.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 2.479-1
- Updated to release 2.479.

* Fri Mar  4 2005 Dries Verachtert <dries@ulyssis.org> - 2.476-1
- Updated to release 2.476.

* Tue Dec 07 2004 Dries Verachtert <dries@ulyssis.org> - 2.475
- Initial package.
