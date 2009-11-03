# $Id$
# Authority: dag
# Upstream: Daisuke Maki <dmaki$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Class-DBI-Pg

Summary: Perl module that extends Class::DBI for Postgres 
Name: perl-Class-DBI-Pg
Version: 0.08
Release: 1%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Class-DBI-Pg/

Source: http://www.cpan.org/modules/by-module/Class/Class-DBI-Pg-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl

%description
Class-DBI-Pg is a Perl module that extends Class::DBI for Postgres.

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
%doc %{_mandir}/man3/Class::DBI::Pg.3pm*
%dir %{perl_vendorlib}/Class/
%dir %{perl_vendorlib}/Class/DBI/
%{perl_vendorlib}/Class/DBI/Pg.pm

%changelog
* Mon Apr 30 2007 Dag Wieers <dag@wieers.com> - 0.08-1
- Initial package. (using DAR)
