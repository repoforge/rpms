# $Id$
# Authority: dries
# Upstream: Flávio Soibelmann Glock <fglock$pucrs,br>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Set-Infinite

Summary: Sets of intervals
Name: perl-Set-Infinite
Version: 0.63
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Set-Infinite/

Source: http://www.cpan.org/modules/by-module/Set/Set-Infinite-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Buildarch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This module contains functions for sets of intervals.

%prep
%setup -n %{real_name}-%{version}

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
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/Set/
%{perl_vendorlib}/Set/Infinite.pm
%{perl_vendorlib}/Set/Infinite/*.pm

%changelog
* Fri Jun 19 2009 Christoph Maser <cmr@financial.com> - 0.63-1
- Updated to version 0.63.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.61-1.2
- Rebuild for Fedora Core 5.

* Mon Dec 06 2004 Dries Verachtert <dries@ulyssis.org> - 0.61-1
- Initial package.
