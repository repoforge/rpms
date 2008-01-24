# $Id$
# Authority: dries
# Upstream: Martin 'Kingpin' Thurn <mthurn$verizon,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name WWW-Search

Summary: Perl module for WWW searches.
Name: perl-WWW-Search
Version: 2.497
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/WWW-Search/

Source: http://www.cpan.org/modules/by-module/WWW/WWW-Search-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

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
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man1/AutoSearch.1*
%doc %{_mandir}/man1/WebSearch.1*
%doc %{_mandir}/man3/WWW::Search.3pm*
%doc %{_mandir}/man3/WWW::SearchResult.3pm*
%doc %{_mandir}/man3/WWW::Search::*.3pm*
%{_bindir}/AutoSearch
%{_bindir}/WebSearch
%dir %{perl_vendorlib}/WWW/
%{perl_vendorlib}/WWW/Search/
%{perl_vendorlib}/WWW/Search.pm
%{perl_vendorlib}/WWW/SearchResult.pm

%changelog
* Wed Jan 23 2008 Dag Wieers <dag@wieers.com> - 2.497-1
- Updated to release 2.497.

* Mon Nov 19 2007 Dag Wieers <dag@wieers.com> - 2.496-1
- Updated to release 2.496.

* Mon Jun 18 2007 Dries Verachtert <dries@ulyssis.org> - 2.494-1
- Updated to release 2.494.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 2.491-1
- Updated to release 2.491.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 2.489-1
- Updated to release 2.489.

* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 2.488-1
- Updated to release 2.488.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 2.487-1
- Updated to release 2.487.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 2.484-1.2
- Rebuild for Fedora Core 5.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 2.484-1
- Updated to release 2.484.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 2.479-1
- Updated to release 2.479.

* Fri Mar  4 2005 Dries Verachtert <dries@ulyssis.org> - 2.476-1
- Updated to release 2.476.

* Tue Dec 07 2004 Dries Verachtert <dries@ulyssis.org> - 2.475
- Initial package.
