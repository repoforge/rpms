# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Class-DBI-AbstractSearch

Summary: The Perl DB Abstract Search
Name: perl-Class-DBI-AbstractSearch
Version: 0.07
Release: 1.2
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Class-DBI-AbstractSearch/

Source: http://www.cpan.org/modules/by-module/Class/Class-DBI-AbstractSearch-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl

%description
The Perl Database Interface (DBI) is a database access Application Programming
Interface (API) for the Perl Language. The Perl DBI API specification defines a
set of functions, variables and conventions that provide a consistent database
interface independent of the actual database being used.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/Class/
%dir %{perl_vendorlib}/Class/DBI/
%{perl_vendorlib}/Class/DBI/AbstractSearch.pm

%changelog
* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 0.07-1
- Updated to release 0.07.

* Thu Mar 31 2005 Dag Wieers <dag@wieers.com> - 0.05-1
- Initial package. (using DAR)
