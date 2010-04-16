# $Id$
# Authority: dries
# Upstream: Lincoln D. Stein <lstein$cshl,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Tie-DBI

Summary: Tie hashes to DBI relational databases
Name: perl-Tie-DBI
Version: 1.05
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Tie-DBI/

Source: http://search.cpan.org/CPAN/authors/id/T/TO/TODDR/Tie-DBI-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(DBD::SQLite)
BuildRequires: perl(DBI)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More)
Requires: perl(DBI)
Requires: perl(Test::More)

%filter_from_requires /^perl*/d
%filter_setup


%description
This distribution contains Tie::DBI and Tie::RDBM, two modules that
allow you to tie associative arrays to relational databases using the
DBI library.  The hash is tied to a table in a local or networked
database.  Reading from the hash retrieves values from the datavbase.
Storing into the hash updates the database (if you have sufficient
privileges).

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}
%{__make} test

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
%{perl_vendorlib}/Tie/DBI.pm
%{perl_vendorlib}/Tie/RDBM.pm

%changelog
* Fri Apr 16 2010 Christoph Maser <cmr@financial.com> - 1.05-1
- Updated to version 1.05.

* Wed Apr  7 2010 Christoph Maser <cmr@financial.com> - 1.04-1
- Updated to version 1.04.

* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 1.02-1
- Updated to release 1.02.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.01-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.01-1
- Initial package.
