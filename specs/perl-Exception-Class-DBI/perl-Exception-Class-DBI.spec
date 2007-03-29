# $Id$
# Authority: dries
# Upstream: David Wheeler <david$justatheory,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Exception-Class-DBI

Summary: DBI Exception objects
Name: perl-Exception-Class-DBI
Version: 0.95
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Exception-Class-DBI/

Source: http://search.cpan.org/CPAN/authors/id/D/DW/DWHEELER/Exception-Class-DBI-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl-Module-Build, perl(Exception::Class)

%description
This module offers a set of DBI-specific exception classes. They inherit from
Exception::Class::Base, the base class for all exception objects created by
the Exception::Class module from the CPAN.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Exception/Class/DBI.pm

%changelog
* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.95-1
- Updated to release 0.95.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.92-1
- Initial package.
