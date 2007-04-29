# $Id$
# Authority: dries
# Upstream: Andy Lester <andy$petdance,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name WWW-Mechanize

Summary: Web browsing in a Perl object
Name: perl-WWW-Mechanize
Version: 1.22
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/WWW-Mechanize/

Source: http://www.cpan.org/modules/by-module/WWW/WWW-Mechanize-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This module provides perl objects for web browsing.

%prep
%setup -n %{real_name}-%{version}

%build
echo y | %{__perl} Makefile.PL --nolive INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
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
%doc Changes
%doc %{_mandir}/man1/*
%doc %{_mandir}/man3/*
%{_bindir}/mech-dump
%dir %{perl_vendorlib}/WWW/
%{perl_vendorlib}/WWW/Mechanize.pm
%{perl_vendorlib}/WWW/Mechanize/

%changelog
* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 1.22-1
- Updated to release 1.22.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 1.20-1
- Updated to release 1.20.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 1.18-1
- Updated to release 1.18.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.16-1.2
- Rebuild for Fedora Core 5.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 1.16-1
- Updated to release 1.16.

* Fri Mar  4 2005 Dries Verachtert <dries@ulyssis.org> - 1.12-1
- Updated to release 1.12.

* Mon Dec 27 2004 Dries Verachtert <dries@ulyssis.org> - 1.08-1
- Initial package.

