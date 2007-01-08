# $Id$
# Authority: dries
# Upstream: Chris Williams <chris$bingosnet,co,uk>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name POE-Component-Client-Whois

Summary: Non-blocking RFC812 Whois query
Name: perl-POE-Component-Client-Whois
Version: 1.08
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/POE-Component-Client-Whois/

Source: http://search.cpan.org/CPAN/authors/id/B/BI/BINGOS/POE-Component-Client-Whois-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This module implements a non-blocking RFC812 whois query.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/POE/Component/Client/Whois.pm
%{perl_vendorlib}/POE/Component/Client/Whois/

%changelog
* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 1.08-1
- Updated to release 1.08.

* Tue Sep 26 2006 Dries Verachtert <dries@ulyssis.org> - 1.07-1
- Updated to release 1.07.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 1.06-1
- Updated to release 1.06.

* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 1.04-1
- Updated to release 1.04.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.02-1.2
- Rebuild for Fedora Core 5.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 1.02-1
- Updated to release 1.02.

* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.00-1
- Initial package.

