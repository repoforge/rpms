# $Id$
# Authority: dag
# Upstream: Tatsuhiko Miyagawa <miyagawa$gmail,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Class-DBI-SQLite

Summary: Perl module that extends Class::DBI for sqlite 
Name: perl-Class-DBI-SQLite
Version: 0.11
Release: 1%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Class-DBI-SQLite/

Source: http://www.cpan.org/modules/by-module/Class/Class-DBI-SQLite-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl

%description
Class-DBI-SQLite is a Perl module that extends Class::DBI for sqlite.

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
%doc Changes MANIFEST META.yml
%doc %{_mandir}/man3/Class::DBI::SQLite.3pm*
%dir %{perl_vendorlib}/Class/
%dir %{perl_vendorlib}/Class/DBI/
%{perl_vendorlib}/Class/DBI/SQLite.pm

%changelog
* Mon Apr 30 2007 Dag Wieers <dag@wieers.com> - 0.11-1
- Initial package. (using DAR)
