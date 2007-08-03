# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name DBIx-SearchBuilder

summary: Encapsulate SQL queries and rows in simple perl objects
Name: perl-DBIx-SearchBuilder
Version: 1.43
Release: 1
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DBIx-SearchBuilder/

Source: http://www.cpan.org/modules/by-module/DBIx/DBIx-SearchBuilder-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(DBD::SQLite), perl(DBI), perl(Want), perl(Encode)
BuildRequires: perl(Class::ReturnValue) >= 0.4, perl-capitalization >= 0.03
BuildRequires: perl(Cache::Simple::TimedExpiry) >= 0.21, perl(Clone)
BuildRequires: perl(capitalization) >= 0.03, perl(DBIx::DBSchema)
BuildRequires: perl(Class::Accessor)

Requires: perl

%description
Encapsulate SQL queries and rows in simple perl objects

%prep
%setup -n %{real_name}-%{version}

### Disable perl-Test-More (part of perl package)
%{__perl} -pi.orig -e "s|^(build_requires\('Test::More'.+$)|#$1|" Makefile.PL

%build
%{__perl} Makefile.PL PREFIX="%{buildroot}%{_prefix}" INSTALLDIRS="vendor"
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
%doc Changes MANIFEST README ROADMAP SIGNATURE
%doc %{_mandir}/man3/*.3*
%dir %{perl_vendorlib}/DBIx/
%{perl_vendorlib}/DBIx/SearchBuilder/
%{perl_vendorlib}/DBIx/SearchBuilder.pm

%changelog
* Mon Jun 05 2006 Dag Wieers <dag@wieers.com> - 1.43-1
- Initial package. (using DAR)
