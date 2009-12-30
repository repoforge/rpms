# $Id$
# Authority: dries
# Upstream: H.Merijn Brand <h.m.brand$xs4all.nl>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name DBD-CSV

Summary: DBI driver for CSV files
Name: perl-DBD-CSV
Version: 0.26
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DBD-CSV/

Source: http://search.cpan.org/CPAN/authors/id/H/HM/HMBRAND/DBD-CSV-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Config)
BuildRequires: perl(DBD::File) >= 0.37
BuildRequires: perl(DBI) >= 1.00
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(SQL::Statement) >= 1.23
BuildRequires: perl(Test::Harness)
BuildRequires: perl(Test::More)
BuildRequires: perl(Text::CSV_XS) >= 0.64
BuildRequires: perl >= 5.005003
Requires: perl(DBD::File) >= 0.37
Requires: perl(DBI) >= 1.00
Requires: perl(SQL::Statement) >= 1.23
Requires: perl(Text::CSV_XS) >= 0.64
Requires: perl >= 5.005003

%filter_from_requires /^perl*/d
%filter_from_requires /\/pro\/bin\/perl/d
%filter_setup


%description
The DBD::CSV module is yet another driver for the DBI (Database
independent interface for Perl). This one is based on the SQL
"engine" SQL::Statement and the abstract DBI driver DBD::File
and implements access to so-called CSV files (Comma separated
values). Such files are mostly used for exporting MS Access and
MS Excel data.

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
%doc ChangeLog README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/DBD/CSV.pm
%{perl_vendorlib}/Bundle/DBD/CSV.pm

%changelog
* Wed Dec 30 2009 Christoph Maser <cmr@financial.com> - 0.26-1
- Updated to version 0.26.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 0.22-1
- Updated to release 0.22.

* Tue Mar  1 2005 Dries Verachtert <dries@ulyssis.org> - 0.21-1
- Initial package.
