# $Id$
# Authority: dag
# Upstream: GomoR <perl$gomor,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name DBIx-SQLite-Simple

Summary: easy access to SQLite databases using objects
Name: perl-DBIx-SQLite-Simple
Version: 0.34
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DBIx-SQLite-Simple/

Source: http://www.cpan.org/modules/by-module/DBIx/DBIx-SQLite-Simple-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
easy access to SQLite databases using objects.

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

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes LICENSE LICENSE.Artistic MANIFEST META.yml README examples/
%doc %{_mandir}/man3/DBIx::SQLite::Simple.3pm*
%doc %{_mandir}/man3/DBIx::SQLite::Simple::Table.3pm*
%dir %{perl_vendorlib}/DBIx/
%dir %{perl_vendorlib}/DBIx/SQLite/
%{perl_vendorlib}/DBIx/SQLite/Simple/
%{perl_vendorlib}/DBIx/SQLite/Simple.pm

%changelog
* Sat Aug 04 2007 Dag Wieers <dag@wieers.com> - 0.34-1
- Initial package. (using DAR)
