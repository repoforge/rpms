# $Id$
# Authority: dries
# Upstream: David Wheeler <david$kineticode,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Exception-Class-DBI

Summary: DBI Exception objects
Name: perl-Exception-Class-DBI
Version: 1.00
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Exception-Class-DBI/

Source: http://www.cpan.org/modules/by-module/Exception/Exception-Class-DBI-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Exception::Class)
BuildRequires: perl(Module::Build) >= 0.2701
BuildRequires: perl(Test::Harness) >= 2.03
BuildRequires: perl(Test::More) >= 0.17

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
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Exception::Class::DBI.3pm*
%dir %{perl_vendorlib}/Exception/
%dir %{perl_vendorlib}/Exception/Class/
#%{perl_vendorlib}/Exception/Class/DBI/
%{perl_vendorlib}/Exception/Class/DBI.pm

%changelog
* Mon Jun 23 2008 Dag Wieers <dag@wieers.com> - 1.00-1
- Updated to release 1.00.

* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 0.98-1
- Updated to release 0.98.

* Fri Nov 09 2007 Dag Wieers <dag@wieers.com> - 0.96-1
- Updated to release 0.96.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.95-1
- Updated to release 0.95.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.92-1
- Initial package.
